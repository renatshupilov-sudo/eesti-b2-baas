# -*- coding: utf-8 -*-
"""Озвучивает недостающие аудиофайлы базы. Запускается в GitHub Actions (там есть интернет и ffmpeg).
Синтезатор: TartuNLP Neurokõne, https://neurokone.ee (API https://api.tartunlp.ai/text-to-speech/v2)."""
import glob, json, os, subprocess, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
from audio_plan import plan, path

API = "https://api.tartunlp.ai/text-to-speech/v2"
ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
C = os.path.join(ROOT, "content")

def tts(text, speaker):
    body = json.dumps({"text": text, "speaker": speaker, "speed": 0.95}).encode()
    for attempt in range(4):
        try:
            req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "eesti-b2-baas"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:
            print("  retry", attempt + 1, e)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"TTS failed: {speaker}: {text[:60]}")

RATE = 22050

def to_pcm(data):
    """Любой WAV от синтезатора (в т.ч. float32) → сырой PCM s16le, моно, 22050 Гц."""
    return subprocess.run(["ffmpeg", "-loglevel", "error", "-i", "pipe:0", "-f", "s16le", "-ac", "1", "-ar", str(RATE), "pipe:1"],
                          input=data, capture_output=True, check=True).stdout

def join_pcm(chunks, pause=0.6):
    silence = b"\x00\x00" * int(RATE * pause)
    return silence.join(to_pcm(c) for c in chunks)

needed = {}
for f in sorted(glob.glob(os.path.join(C, "lessons", "*.json"))):
    for _, _, segs in plan(json.load(open(f, encoding="utf-8"))):
        needed[path(segs)] = segs

made = 0
for rel, segs in needed.items():
    dst = os.path.join(C, rel)
    if os.path.exists(dst):
        continue
    print("TTS", rel, segs[0][1][:50])
    pcm = join_pcm([tts(t, s) for s, t in segs])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "s16le", "-ar", str(RATE), "-ac", "1", "-i", "pipe:0", "-b:a", "64k", dst], input=pcm, check=True)
    made += 1
    time.sleep(0.3)

# Удалить файлы, на которые больше нет ссылок
for f in glob.glob(os.path.join(C, "audio", "*.mp3")):
    if os.path.relpath(f, C).replace(os.sep, "/") not in needed:
        os.remove(f); print("removed", f)
print(f"audio: {len(needed)} needed, {made} generated")
