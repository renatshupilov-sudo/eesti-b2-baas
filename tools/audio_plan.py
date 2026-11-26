# -*- coding: utf-8 -*-
"""Какие аудиофайлы нужны базе. Общий модуль для build.py (ставит ссылки в уроки)
и make_audio.py (озвучивает недостающие файлы через синтезатор TartuNLP/Neurokõne)."""
import hashlib, json, re

# Голоса синтезатора TartuNLP. Роли в диалогах получают разные голоса.
VOICES = {"Saatejuht": "tambet", "Mari": "mari", "Ajakirjanik": "liivika", "Andres": "kalev", "Olga": "vesta"}
NARRATOR = "mari"
LESSON_NARRATOR = {"d012": "meelis", "d014": "külli"}

def key(segments):
    return hashlib.sha1(json.dumps(segments, ensure_ascii=False).encode()).hexdigest()[:16]

def path(segments):
    return f"audio/{key(segments)}.mp3"

def clean_word(et):
    return re.sub(r"\s*\(.*?\)", "", et).strip()

def transcript_segments(lesson_id, transcript):
    segs = []
    for line in transcript.split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-ZÕÄÖÜŠŽ][\wõäöüšž]+):\s*(.+)$", line)
        if m and m.group(1) in VOICES:
            segs.append([VOICES[m.group(1)], m.group(2)])
        else:
            segs.append([LESSON_NARRATOR.get(lesson_id, NARRATOR), line])
    return segs

def plan(lesson):
    """Возвращает список (block, item_or_None, segments) для всего, что нужно озвучить."""
    out = []
    for b in lesson["blocks"]:
        if b["type"] == "listening":
            out.append((b, None, transcript_segments(lesson["id"], b["transcript"])))
        elif b["type"] == "dictation":
            for it in b["items"]:
                out.append((b, it, [[NARRATOR, it["audio"]]]))
        elif b["type"] == "vocab":
            for it in b["items"]:
                out.append((b, it, [[NARRATOR, clean_word(it["et"])]]))
    return out

def attach(lesson):
    """Пишет в урок относительные пути к аудио (относительно папки content/)."""
    for b, it, segs in plan(lesson):
        (it if it is not None else b)["audio_file"] = path(segs)
