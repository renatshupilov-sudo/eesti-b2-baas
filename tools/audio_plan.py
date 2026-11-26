# -*- coding: utf-8 -*-
"""Какие аудиофайлы нужны базе. Общий модуль для build.py (ставит ссылки в уроки)
и make_audio.py (озвучивает недостающие файлы через синтезатор TartuNLP/Neurokõne).

Реплики с ролью озвучиваются голосом роли. Текст без ролей (диктор, слова) озвучивается
в двух вариантах: женский голос -> audio_file, мужской -> audio_file_m."""
import hashlib, json, re

VOICES = {"Saatejuht": "tambet", "Mari": "mari", "Ajakirjanik": "liivika", "Andres": "kalev", "Olga": "vesta",
          "Mees": "kalev", "Naine": "liivika", "Õpetaja": "albert", "Õpilane": "vesta"}
NARRATOR = {"audio_file": "mari", "audio_file_m": "albert"}

def key(segments):
    return hashlib.sha1(json.dumps(segments, ensure_ascii=False).encode()).hexdigest()[:16]

def path(segments):
    return f"audio/{key(segments)}.mp3"

def clean_word(et):
    return re.sub(r"\s*\(.*?\)", "", et).strip()

def transcript_segments(transcript):
    segs = []
    for line in transcript.split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-ZÕÄÖÜŠŽ][\wõäöüšž]+):\s*(.+)$", line)
        segs.append([VOICES[m.group(1)], m.group(2)] if m and m.group(1) in VOICES else [None, line])
    return segs

def variants(segs):
    """{поле: сегменты с голосами}. None = диктор."""
    if any(v is None for v, _ in segs):
        return {f: [[v or nv, t] for v, t in segs] for f, nv in NARRATOR.items()}
    return {"audio_file": segs}

def plan(lesson):
    """Список (объект, поле, сегменты) для всего, что нужно озвучить."""
    out = []
    for b in lesson["blocks"]:
        if b["type"] == "listening":
            out += [(b, f, s) for f, s in variants(transcript_segments(b["transcript"])).items()]
        elif b["type"] == "dictation":
            for it in b["items"]:
                out += [(it, f, s) for f, s in variants([[None, it["audio"]]]).items()]
        elif b["type"] == "vocab":
            for it in b["items"]:
                out += [(it, f, s) for f, s in variants([[None, clean_word(it["et"])]]).items()]
    return out

def attach(lesson):
    for obj, field, segs in plan(lesson):
        obj[field] = path(segs)
