import json, hashlib, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from jsonschema import Draft202012Validator
from lessons_01_07 import L as A
from lessons_08_14 import L as B
ROOT = sys.argv[1]
C = os.path.join(ROOT, "content")
lessons = A + B
from extras import EXPLAIN, GRAMMAR, ADVICE, REPLACE_MAIN, D014_INTRO
from extras2 import VOCAB, PHRASE_TASKS, D001_GRAMMAR, JUPITER
from extras3 import SHORT, D007
for l in lessons:
    if l["id"] == "d007":
        for k in ("title", "title_ru", "topic", "goal_ru"): l[k] = D007[k]
        for i, b in enumerate(l["blocks"]):
            if b["type"] == "listening": l["blocks"][i] = dict(D007["listening"], _new=True)
            if b["type"] == "vocab": b["items"] = [{"et": a, "ru": r, "example": e} for a, r, e in D007["vocab"]]
    if l["id"] in SHORT:
        di = next((i for i, b in enumerate(l["blocks"]) if b["type"] == "dictation"), None)
        if di is not None: l["blocks"][di] = dict(SHORT[l["id"]], _new=True)
        else:
            vi = next(i for i, b in enumerate(l["blocks"]) if b["type"] == "vocab")
            l["blocks"].insert(vi + 1, dict(SHORT[l["id"]], _new=True))
GRAMMAR["d001"] = D001_GRAMMAR
for l in lessons:
    for b in l["blocks"]:
        if b["type"] == "vocab" and l["id"] in VOCAB and l["id"] != "d007":
            b["items"] = [dict(x) for x in VOCAB[l["id"]]]
            b["instruction_ru"] = "Нажмите на слово, чтобы услышать его. Перевод скрыт: нажмите на него, чтобы открыть или снова скрыть."
        if b["type"] == "phrases" and l["id"] in PHRASE_TASKS:
            b["instruction_ru"], b["tasks"] = PHRASE_TASKS[l["id"]][0], PHRASE_TASKS[l["id"]][1]
    if any(b["type"] == "listening" for b in l["blocks"]) and l["skill"] == "kuulamine":
        ri = next((i for i, b in enumerate(l["blocks"]) if b["type"] == "review"), len(l["blocks"]))
        l["blocks"].insert(ri, dict(JUPITER))
SONAVEEB = "https://sonaveeb.ee/search/unif/dlall/dsall/{word}/1"
import re, urllib.parse
for l in lessons:
    if l["id"] in REPLACE_MAIN:
        r = REPLACE_MAIN[l["id"]]
        for k in ("skill","title","title_ru","goal_ru"): l[k] = r[k]
        l["version"] = 2
        i = next(i for i,b in enumerate(l["blocks"]) if b["type"]=="speaking")
        l["blocks"][i] = r["block"]
    elif any(b["type"]=="speaking" for b in l["blocks"]):
        l["blocks"] = [b for b in l["blocks"] if b["type"]!="speaking"]
        l["version"] = 2
    if l["id"]=="d014":
        l["blocks"][0]["text"] = D014_INTRO
        l["goal_ru"] = "Письмо, аудирование и чтение в сжатом виде, строго по таймеру. Итог двух недель."
    if l["id"]=="d001":
        for b in l["blocks"]:
            if b["type"]=="phrases": b["instruction_ru"] = "Эти связки нужны в письме. Напишите 2–3 предложения о своей работе, используя минимум три связки."
    l["version"] = 5  # 2026.11.26-2: ссылки на словарь во всех уроках
    for b in l["blocks"]:
        if b["type"]=="vocab":
            for it in b["items"]:
                w = re.sub(r"\s*\(.*?\)", "", it["et"]).strip()
                it["dict"] = SONAVEEB.format(word=urllib.parse.quote(w))
MODULE = {"vocab":"sonavara","phrases":"sonavara","listening":"kuulamine","dictation":"kuulamine","grammar":"grammatika","writing":"kirjutamine","reading":"lugemine","speaking":"raakimine"}
for l in lessons:
    types=[b["type"] for b in l["blocks"]]
    ri = types.index("review") if "review" in types else len(types)
    if "grammar" not in types:
        l["blocks"].insert(ri, GRAMMAR[l["id"]])
    if "listening" not in types and "dictation" not in types:
        vb = next(b for b in l["blocks"] if b["type"]=="vocab")
        sents=[i["example"] for i in vb["items"] if i.get("example") and len(i["example"].split())>=3][:3]
        l["blocks"].insert(types.index("vocab")+1, {"type":"dictation","minutes":4,"title":"Kuula ja kirjuta",
          "instruction_ru":"Аудио-диктант с новыми словами: нажмите ▶, послушайте предложение и запишите его. Знаки препинания не проверяются.",
          "items":[{"audio":x,"answer":[x]} for x in sents]})
    i=0
    for b in l["blocks"]:
        if b["type"] in MODULE: b["module"]=MODULE[b["type"]]
        if b["type"] in ADVICE: b["advice_ru"]=ADVICE[b["type"]]
        if b.get("title")=="Kuula ja kirjuta": b["advice_ru"]="Сравните свой вариант с правильным: чаще всего теряются долгие гласные и двойные согласные (kokkuhoid, lubab, töötada). Прослушайте ещё раз и перепишите предложение без ошибок."
        new = b.pop("_new", False)
        for t in b.get("tasks",[]):
            if new: continue
            k=f"{l['id']}:{i}"
            if "explain_ru" not in t: t["explain_ru"]=EXPLAIN[k]
            i+=1
    # уложиться в 40 минут: урезаем самый длинный блок
    while sum(b["minutes"] for b in l["blocks"] if not b.get("optional"))>40:
        max(l["blocks"], key=lambda b:b["minutes"])["minutes"]-=1
ls = json.load(open(os.path.join(C, "schema/lesson.schema.json")))
ms = json.load(open(os.path.join(C, "schema/manifest.schema.json")))
v = Draft202012Validator(ls)
errs = 0
for l in lessons:
    for b in l["blocks"]:
        if b["type"] in ("grammar",) and "instruction_ru" not in b:
            b["instruction_ru"] = "Короткое напоминание правила — сразу переходите к упражнениям."
        for t in b.get("tasks", []):
            if t["kind"] == "mc": assert 0 <= t["answer"] < len(t["options"]), (l["id"], t["q"])
    mins = sum(b["minutes"] for b in l["blocks"] if not b.get("optional"))
    l["minutes"] = mins; print(l["id"], mins) if not 30 <= mins <= 42 else None
    for e in v.iter_errors(l):
        errs += 1; print(l["id"], list(e.path), e.message)
from audio_plan import attach
for l in lessons:
    attach(l)
os.makedirs(os.path.join(C, "lessons"), exist_ok=True)
entries = []
for l in lessons:
    data = json.dumps(l, ensure_ascii=False, indent=1).encode()
    fn = f"lessons/{l['id']}.json"
    open(os.path.join(C, fn), "wb").write(data)
    entries.append({k: l[k] for k in ("id","day","version","skill","title","title_ru","topic","minutes")} | {"file": fn, "sha256": hashlib.sha256(data).hexdigest()})
manifest = {
 "schemaVersion": "1.0",
 "contentVersion": "2026.11.26-5",
 "updatedAt": "2026-11-26",
 "language": "et", "level": "B2", "cycleDays": len(lessons),
 "dictionary": {"name": "EKI Sõnaveeb", "urlTemplate": SONAVEEB},
 "changelog": [{"version": "2026.11.26-5", "date": "2026-11-26", "ru": "Вместо диктантов из отдельных предложений — короткие диалоги с вопросами. Урок 7: длинная лекция «Eesti mets» (около 5–6 минут). Выбор мужского или женского голоса, речь по умолчанию медленнее на 20%."},{"version": "2026.11.26-4", "date": "2026-11-26", "ru": "Слова заменены на лексику уровня B2. Связки и фразы проверяются автоматически. В уроке 1 вместо порядка слов — словообразование. Итог урока с советом. Ссылки на живое аудирование ERR Jupiter. План тем."},{"version": "2026.11.26-3", "date": "2026-11-26", "ru": "Настоящая эстонская озвучка (TartuNLP Neurokõne) для аудирования, диктантов и слов вместо голоса телефона."},{"version": "2026.11.26-2", "date": "2026-11-26", "ru": "Убрана устная часть. Уроки 4 и 9 заменены на аудирование и чтение. К словам добавлены ссылки на словарь EKI (Sõnaveeb)."},{"version": "2026.11.26-1", "date": "2026-11-26", "ru": "Первая версия: 14 уроков (2 недели), все 4 части экзамена + грамматика и мини-пробный экзамен."}],
 "exam": {
  "parts": [
   {"skill": "kirjutamine", "name": "Kirjutamine", "minutes": "80", "points": 25, "format_ru": "2 текста: письмо (около 140 слов) и рассуждение/мнение (около 180 слов)."},
   {"skill": "kuulamine", "name": "Kuulamine", "minutes": "35–40", "points": 25, "format_ru": "4 задания: выбор ответа, верно/неверно, заполнение пропусков. Первый текст звучит один раз, остальные — дважды."},
   {"skill": "lugemine", "name": "Lugemine", "minutes": "70", "points": 25, "format_ru": "4 задания: выбор ответа, соотнесение утверждений с абзацами, пропуски слов или предложений."},
   {"skill": "raakimine", "name": "Rääkimine", "minutes": "≈20", "points": 25, "format_ru": "После письменной части. Знакомство, выступление/монолог по теме и обсуждение с партнёром. Ответ записывается."}
  ],
  "passRule_ru": "Сдано, если набрано не меньше 60% от максимума (60 из 100) и ни одна часть не оценена в 0 баллов. При результате ниже 45% пересдача не раньше чем через 6 месяцев.",
  "rules_ru": ["Письменная часть: 3 ч 5 мин, порядок — письмо, аудирование, чтение.", "Устная часть начинается через 15–20 минут после письменной.", "Нельзя: словари, телефоны, смарт-часы. Пишут синей или чёрной ручкой.", "Документ: ID-карта, паспорт или вид на жительство (права не подходят)."],
  "sources": [
   {"title": "Harno: Teabeleht eesti keele tasemeeksami sooritajale 2024", "url": "https://harno.ee/sites/default/files/documents/2024-01/Teabeleht%20tasemeeksami%20sooritajale%202024_korras%20printimiseks.pdf"},
   {"title": "Harno EIS: avalikud ülesanded (официальные тренировочные задания)", "url": "https://eis.harno.ee/publicitems"},
   {"title": "Superprof: Eesti keele B2 eksam — ülesehitus ja hindamine", "url": "https://www.superprof.ee/blog/b2-keeleeksami-juhend/"}
  ]
 },
 "lessons": entries
}
mods=[("sonavara","Sõnavara","Новые слова и фразы"),("kuulamine","Kuulamine","Аудирование"),("grammatika","Grammatika","Грамматика"),("lugemine","Lugemine","Чтение"),("kirjutamine","Kirjutamine","Письмо")]
manifest["modules"]=[{"id":m,"name":n,"name_ru":r,"items":[{"lesson":l["id"],"block":bi,"title":b["title"],"topic":l["topic"],"minutes":b["minutes"]} for l in lessons for bi,b in enumerate(l["blocks"]) if b.get("module")==m]} for m,n,r in mods]
manifest["lessonPlan_ru"]="Каждый урок дня (30–40 мин) содержит: новые слова, аудирование или аудио-диктант, основное задание в формате экзамена, мини-грамматику и самопроверку. Те же упражнения доступны отдельно по модулям."
for e in Draft202012Validator(ms).iter_errors(manifest):
    errs += 1; print("manifest", list(e.path), e.message)
manifest["topicPlan"] = [
 {"topic": "loodus", "ru": "природа", "status": "partly", "lessons": ["d007"]},
 {"topic": "majandus", "ru": "экономика", "status": "planned"},
 {"topic": "keskkond ja kliima", "ru": "экология и климат", "status": "partly", "lessons": ["d006"]},
 {"topic": "poliitika ja riik", "ru": "политика и государство", "status": "planned"},
 {"topic": "ühiskond", "ru": "общество", "status": "planned"},
 {"topic": "teadus ja tehnoloogia", "ru": "наука и технологии", "status": "partly", "lessons": ["d011"]},
 {"topic": "töö ja karjäär", "ru": "работа и карьера", "status": "done", "lessons": ["d001"]},
 {"topic": "haridus", "ru": "образование", "status": "done", "lessons": ["d004", "d008"]},
 {"topic": "tervis", "ru": "здоровье", "status": "done", "lessons": ["d005"]},
 {"topic": "linn, transport, eluase", "ru": "город, транспорт, жильё", "status": "done", "lessons": ["d002", "d009", "d013"]},
 {"topic": "kultuur ja ajalugu", "ru": "культура и история", "status": "partly", "lessons": ["d010"]},
 {"topic": "tarbimine ja raha", "ru": "потребление и деньги", "status": "partly", "lessons": ["d003"]},
 {"topic": "meedia", "ru": "СМИ", "status": "planned"},
 {"topic": "turvalisus ja riigikaitse", "ru": "безопасность и оборона", "status": "planned"},
 {"topic": "perekond ja demograafia", "ru": "семья и демография", "status": "planned"},
 {"topic": "reisimine ja turism", "ru": "путешествия и туризм", "status": "planned"}
]
json.dump(manifest, open(os.path.join(C, "manifest.json"), "w"), ensure_ascii=False, indent=1)
print("lessons", len(lessons), "errors", errs)
from collections import Counter
print(Counter(l["skill"] for l in lessons), sum(len(b.get("tasks",[]))+len(b.get("items",[])) for l in lessons for b in l["blocks"]), "items/tasks")
