# -*- coding: utf-8 -*-
# Уроки 1–7. Все тексты учебные (составлены для тренировки), цифры и имена вымышлены.

def mc(q, options, answer, explain=None):
    d = {"kind": "mc", "q": q, "options": options, "answer": answer}
    if explain: d["explain_ru"] = explain
    return d

def tf(q, answer, explain=None):
    d = {"kind": "tf", "q": q, "answer": answer}
    if explain: d["explain_ru"] = explain
    return d

def gap(q, answer, hint=None, explain=None):
    d = {"kind": "gap", "q": q, "answer": answer if isinstance(answer, list) else [answer]}
    if hint: d["hint"] = hint
    if explain: d["explain_ru"] = explain
    return d

def vocab(items, minutes=5, title="Sõnavara"):
    return {"type": "vocab", "minutes": minutes, "title": title,
            "instruction_ru": "Прочитайте слова вслух, закройте перевод и проверьте себя. Нажмите на слово, чтобы услышать его.",
            "items": [{"et": a, "ru": b, **({"example": c} if c else {})} for a, b, c in items]}

ABC = ["A", "B", "C", "D", "E"]

L = []

# ---------------------------------------------------------------- 1
L.append({
 "id": "d001", "day": 1, "version": 1, "skill": "lugemine",
 "title": "Kaugtöö: vabadus või üksindus?", "title_ru": "Удалённая работа: свобода или одиночество?",
 "topic": "töö", "minutes": 35,
 "goal_ru": "Тренируем задание экзамена «найти абзац, к которому относится утверждение» и лексику о работе.",
 "blocks": [
  vocab([
   ("kaugtöö", "удалённая работа", "Ta teeb kaks päeva nädalas kaugtööd."),
   ("tööandja", "работодатель", "Tööandja lubab kodus töötada."),
   ("pooldaja", "сторонник", "Kaugtöö pooldajad rõhutavad aja kokkuhoidu."),
   ("keskenduma (millele?)", "сосредоточиться", "Kodus on lihtsam tööle keskenduda."),
   ("varjukülg", "обратная (теневая) сторона", "Igal asjal on oma varjuküljed."),
   ("üksildane", "одинокий", "Ta tundis end kodus üksildasena."),
   ("tootlik", "продуктивный", "Inimesed on kodus sama tootlikud."),
   ("kohanema (millega?)", "адаптироваться", "Uuel töötajal on raske kohaneda."),
   ("kokku leppima", "договориться", "Reeglid lepitakse kokku ühiselt."),
  ]),
  {"type": "reading", "minutes": 20, "title": "Lugemine",
   "instruction_et": "Lugege teksti ja vastake küsimustele.",
   "instruction_ru": "На экзамене на чтение даётся 70 минут на 4 задания, то есть около 15–17 минут на текст. Засеките время.",
   "text": "Kaugtöö: vabadus või üksindus?\n\nA. Veel mõni aasta tagasi tähendas tööpäev enamiku inimeste jaoks hommikust sõitu kontorisse ja õhtust ummikut. Pärast koroonapandeemiat on olukord muutunud: paljud ettevõtted lubavad töötajatel vähemalt osa nädalast kodus töötada. Kaugtöö on muutunud tavaliseks, kuid selle mõju inimestele ei ole sugugi ühene.\n\nB. Kaugtöö pooldajad rõhutavad eelkõige aja kokkuhoidu. Kui ei pea iga päev tund aega bussis või autos istuma, jääb rohkem aega perele, spordile ja puhkusele. Paljud töötajad ütlevad ka, et kodus on lihtsam keskenduda, sest keegi ei sega ega küsi pidevalt midagi.\n\nC. Teisalt on kaugtööl ka varjukülgi. Psühholoogide sõnul tunnevad paljud kodus töötavad inimesed end üksildasena. Kohvipausid ja juhuslikud vestlused koridoris ei ole ainult meelelahutus – just seal sünnivad sageli uued ideed ja tekib meeskonnatunne. Lisaks on kodus raskem tõmmata piiri töö ja eraelu vahele. Kui sülearvuti on alati käeulatuses, kipub tööpäev venima hilisõhtuni.\n\nD. Ka tööandjate arvamused on erinevad. Osa juhte usub, et inimesed on kodus sama tootlikud kui kontoris või isegi tootlikumad. Teised kardavad, et kontrolli kadumine vähendab vastutustunnet ning uutel töötajatel on keerulisem organisatsiooni kultuuriga kohaneda.\n\nE. Paljud eksperdid peavad parimaks lahenduseks hübriidtööd, mille puhul töötaja on osa nädalast kontoris ja osa kodus. Oluline on, et reeglid lepitakse kokku ühiselt ja et iga töötaja saaks valida endale sobiva rütmi. Kaugtöö ei ole iseenesest hea ega halb – kõik oleneb sellest, kuidas seda korraldada.",
   "tasks": [
    mc("Millise lõigu kohta käib väide? „Kodus töötades on keeruline tööpäeva õigel ajal lõpetada.“", ABC, 2, "C: «kipub tööpäev venima hilisõhtuni» — рабочий день затягивается до позднего вечера."),
    mc("Millise lõigu kohta käib väide? „Uutel töötajatel võib olla raske ettevõttega harjuda.“", ABC, 3, "D: «uutel töötajatel on keerulisem organisatsiooni kultuuriga kohaneda»."),
    mc("Millise lõigu kohta käib väide? „Kodus on vähem segajaid.“", ABC, 1, "B: «keegi ei sega». Обратите внимание: в утверждении другие слова, чем в тексте, — так и на экзамене."),
    mc("Millise lõigu kohta käib väide? „Töökorralduse reeglid tuleks kokku leppida koos töötajatega.“", ABC, 4),
    tf("Pärast pandeemiat lubavad paljud ettevõtted osaliselt kodus töötada.", True),
    tf("Kõik juhid usuvad, et kodus töötatakse vähem.", False, "Osa juhte usub vastupidist — часть руководителей считает, что дома работают так же или даже продуктивнее."),
    tf("Autori arvates on kaugtöö alati parem kui kontoritöö.", False, "«ei ole iseenesest hea ega halb»."),
    gap("Kohvipausidel ja vestlustel koridoris sünnivad sageli uued ___.", ["ideed"]),
    gap("Kui sülearvuti on alati käeulatuses, kipub tööpäev ___ hilisõhtuni.", ["venima"]),
   ]},
  {"type": "phrases", "minutes": 6, "title": "Arvamuse väljendamine",
   "instruction_ru": "Эти связки нужны и в письме, и в устной части. Прочитайте и скажите вслух 2–3 предложения о своей работе, используя минимум три связки.",
   "phrases": ["Ühelt poolt …, teiselt poolt …", "Pooldajad rõhutavad, et …", "Vastased kardavad, et …", "Minu arvates / Minu meelest …", "Kõik oleneb sellest, kuidas …", "Lisaks sellele …", "Kokkuvõttes võib öelda, et …"]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Отметьте: сколько вопросов вы угадали по ключевым словам, а сколько поняли по смыслу абзаца? На экзамене формулировки в вопросах почти всегда отличаются от текста — ищите синонимы (segama → segajad, harjuma → kohanema)."}
 ]})

# ---------------------------------------------------------------- 2
L.append({
 "id": "d002", "day": 2, "version": 1, "skill": "kuulamine",
 "title": "Bussid on hommikuti täis", "title_ru": "Утром автобусы переполнены",
 "topic": "linn ja transport", "minutes": 35,
 "goal_ru": "Аудирование: интервью по радио. Учимся улавливать числа, причины и рекомендации.",
 "blocks": [
  vocab([
   ("ühistransport", "общественный транспорт", None),
   ("kurtma (mille üle?)", "жаловаться", "Kuulajad kurdavad, et bussid on täis."),
   ("tipptund", "час пик", "Tipptunnil on bussid täis."),
   ("puuduma", "не хватать, отсутствовать", "Linnas puudub kuuskümmend bussijuhti."),
   ("koormus", "нагрузка", "Hommikune koormus on suur."),
   ("end õigustama", "оправдать себя", "Kas tasuta transport on end õigustanud?"),
   ("eakas", "пожилой", "Eakad sõidavad tasuta."),
   ("harjumus", "привычка", "Harjumusi on raske muuta."),
   ("usaldusväärne", "надёжный", "Sõiduplaan peab olema usaldusväärne."),
  ]),
  {"type": "listening", "minutes": 18, "title": "Raadiointervjuu", "plays": 2,
   "instruction_et": "Kuulake intervjuud kaks korda ja vastake küsimustele.",
   "instruction_ru": "Сначала прочитайте вопросы (30 секунд), потом слушайте. Текст расшифровки откройте только после проверки ответов. Если на телефоне нет эстонского голоса, приложение предупредит — тогда читайте текст один раз быстро, закрыв вопросы.",
   "transcript": "Saatejuht: Tere tulemast saatesse „Linnaelu“. Täna räägime ühistranspordist ja stuudios on liikluseekspert Mari Kask. Tere, Mari!\nMari: Tere!\nSaatejuht: Paljud kuulajad kurdavad, et bussid on hommikuti liiga täis. Miks see nii on?\nMari: Põhjus on lihtne. Kõige rohkem inimesi sõidab tööle ja kooli seitsmest üheksani. Just siis on vaja kõige rohkem busse, aga juhte ei jätku. Praegu puudub linnas umbes kuuskümmend bussijuhti.\nSaatejuht: Mida saaks teha?\nMari: Esiteks tuleb bussijuhi amet populaarsemaks muuta, näiteks palka tõsta. Teiseks soovitame ettevõtetel kaaluda paindlikku tööaega. Kui osa töötajaid alustaks tööd kell kümme, oleks hommikune koormus palju väiksem.\nSaatejuht: Kas tasuta ühistransport on end õigustanud?\nMari: Osaliselt. Linnasisene sõit on tõesti populaarsemaks muutunud, eriti eakate ja õpilaste seas. Samas ei ole autojuhid oma harjumusi kuigi palju muutnud. Inimesed valivad auto mugavuse pärast, mitte raha pärast.\nSaatejuht: Mis aitaks autojuhid bussi peale meelitada?\nMari: Kiirus. Kui buss sõidab oma rajal ja jõuab kohale kiiremini kui auto, hakkavad inimesed seda ise eelistama. Lisaks peavad peatused olema mugavad ja turvalised ning sõiduplaan usaldusväärne.\nSaatejuht: Aitäh, Mari!",
   "tasks": [
    mc("Millal on bussid kõige täiemad?", ["kell 7–9", "kell 9–10", "kell 16–18"], 0),
    mc("Mitu bussijuhti linnas puudub?", ["16", "60", "600"], 1, "kuuskümmend = 60; kuusteist = 16. Числа — частая ловушка в аудировании."),
    mc("Mida soovitab ekspert ettevõtetele?", ["maksta töötajate bussipilet kinni", "lubada paindlikku tööaega", "osta töötajatele jalgrattad"], 1),
    mc("Miks eelistavad inimesed autot?", ["see on odavam", "see on mugavam", "see on turvalisem"], 1),
    tf("Tasuta ühistransport on populaarne eakate ja õpilaste seas.", True),
    tf("Autojuhid on hakanud massiliselt bussiga sõitma.", False),
    tf("Eksperdi arvates on kõige olulisem bussi kiirus.", True),
    gap("Kui buss sõidab oma ___, jõuab ta kohale kiiremini kui auto.", ["rajal"]),
   ]},
  {"type": "dictation", "minutes": 7, "title": "Arvud kuulmise järgi",
   "instruction_ru": "Нажмите ▶, послушайте и запишите цифрами. Числа, время и даты встречаются почти в каждом задании на аудирование.",
   "items": [
    {"audio": "kuuskümmend kaks", "answer": ["62"]},
    {"audio": "kuusteist", "answer": ["16"]},
    {"audio": "kakssada viisteist", "answer": ["215"]},
    {"audio": "üheksateist", "answer": ["19"]},
    {"audio": "kolmsada üheksakümmend", "answer": ["390"]},
    {"audio": "tuhat kaheksasada", "answer": ["1800"]},
    {"audio": "seitsekümmend seitse", "answer": ["77"]},
    {"audio": "kaks tuhat kakskümmend kuus", "answer": ["2026"]},
   ]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Откройте расшифровку и найдите места, где вы ошиблись. Выпишите 3 новых слова. Совет: в аудировании ответ часто звучит после слов «esiteks / teiseks / põhjus on / samas»."}
 ]})

# ---------------------------------------------------------------- 3
L.append({
 "id": "d003", "day": 3, "version": 1, "skill": "kirjutamine",
 "title": "Kaebus e-poele", "title_ru": "Жалоба в интернет-магазин",
 "topic": "tarbimine", "minutes": 40,
 "goal_ru": "Письмо (полуофициальное, около 140 слов): жалоба. Учим структуру и вежливые формы.",
 "blocks": [
  vocab([
   ("tellimus", "заказ", "Tellimuse number on 45821."),
   ("tellima", "заказывать", "Tellisin e-poest tolmuimeja."),
   ("pakk", "посылка", "Pakk saabus kaks nädalat hiljem."),
   ("katki", "сломан(ный)", "Karp oli katki."),
   ("puuduma", "отсутствовать", "Üks osa puudus."),
   ("pettunud", "разочарован", "Olen väga pettunud."),
   ("vahetama (mille vastu?)", "обменять (на что)", "Palun vahetage toode uue vastu."),
   ("raha tagastama", "вернуть деньги", None),
   ("saatmiskulud", "расходы на пересылку", None),
  ]),
  {"type": "grammar", "minutes": 8, "title": "Viisakas palve: tingiv kõneviis",
   "rule_ru": "В официальных письмах просьбу смягчают условным наклонением (-ks-): ma sooviksin (я хотел бы), kas oleks võimalik (возможно ли было бы), võiksite (могли бы вы). Форма: основа da-инфинитива/ma-инфинитива + ks + личное окончание: soovi-ks-in, saa-ks-ite, oleks.",
   "examples": ["Sooviksin, et vahetaksite toote.", "Kas oleks võimalik raha tagastada?", "Võiksite mulle teada anda, millal …"],
   "tasks": [
    gap("Ma ___ (soovima) teada, millal pakk saabub.", ["sooviksin"]),
    gap("Kas ___ (olema) võimalik tellimus tühistada?", ["oleks"]),
    gap("___ (saama) te mulle arve uuesti saata?", ["Saaksite", "saaksite"]),
    gap("Oleksin tänulik, kui te ___ (vastama) lähipäevil.", ["vastaksite"]),
    gap("Me ___ (tahtma) broneerida laua neljale.", ["tahaksime"]),
   ]},
  {"type": "writing", "minutes": 22, "title": "Kirjutamine: kaebus",
   "prompt_et": "Te tellisite e-poest tolmuimeja. Pakk saabus hilinemisega ja toode ei tööta korralikult. Kirjutage e-poe klienditeenindusele kiri. Kirjutage:\n• mida ja millal te tellisite;\n• mis on probleem (vähemalt kaks probleemi);\n• mida te ootate e-poelt.",
   "prompt_ru": "На экзамене письмо — первое задание части «kirjutamine» (80 минут на два текста). Оставьте 20–25 минут на письмо и 3 минуты на проверку.",
   "words": {"min": 120, "max": 160},
   "checklist": ["Обращение: Lugupeetud klienditeenindus! / Tere!", "Все три пункта задания раскрыты", "Есть даты/номер заказа (конкретика)", "Вежливая просьба в условном наклонении (sooviksin, palun …)", "Заключение и подпись: Lugupidamisega / Parimate soovidega", "Абзацы, 120–160 слов"],
   "phrases": ["Pöördun teie poole seoses …", "Tellisin … (kuupäev) teie e-poest …", "Kahjuks selgus, et …", "Lisaks sellele …", "Sooviksin, et …", "Palun andke teada, …", "Ootan teie vastust.", "Lugupidamisega"],
   "model": "Lugupeetud klienditeenindus!\n\nTellisin 3. novembril teie e-poest tolmuimeja (tellimuse number 45821). Kodulehel oli kirjas, et kaup jõuab kohale kolme tööpäeva jooksul, kuid pakk saabus alles kaks nädalat hiljem.\n\nKahjuks selgus kohe pärast paki avamist, et tolmuimeja ei tööta korralikult: see lülitub sisse, kuid mõne sekundi pärast uuesti välja. Lisaks oli karp seest katki ja üks otsik puudus.\n\nOlen teie poest varem mitu korda ostnud ja olnud teenindusega rahul, seega olen praeguse olukorra pärast eriti pettunud. Sooviksin, et vahetaksite tolmuimeja uue vastu või tagastaksite mulle raha. Palun andke teada, kuidas saan toote teile tagasi saata ja kes maksab saatmiskulud.\n\nOotan teie vastust lähipäevil.\n\nLugupidamisega\nNimi Perekonnanimi"},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Сравните своё письмо с образцом по чек-листу. Проверьте 3 частые ошибки: падеж после «tellisin» (tolmuimeja — полный объект, родительный), порядок слов после «kahjuks» (глагол на втором месте: Kahjuks selgus …), запятая перед «et» и «kuid»."}
 ]})

# ---------------------------------------------------------------- 4
L.append({
 "id": "d004", "day": 4, "version": 1, "skill": "raakimine",
 "title": "Õppimine ei lõpe kunagi", "title_ru": "Учёба не заканчивается никогда",
 "topic": "haridus", "minutes": 35,
 "goal_ru": "Устная часть: знакомство, короткое выступление (около 1–2 минут) и обсуждение «за и против».",
 "blocks": [
  vocab([
   ("elukestev õpe", "обучение в течение всей жизни", None),
   ("täienduskoolitus", "курсы повышения квалификации", "Käisin eelmisel aastal täienduskoolitusel."),
   ("end täiendama", "повышать квалификацию", "Tahan end erialal täiendada."),
   ("oskus", "навык, умение", "Uued oskused aitavad tööl."),
   ("tunnistus", "свидетельство, сертификат", "Kursuse lõpus sain tunnistuse."),
   ("eneseareng", "саморазвитие", None),
   ("kulud", "расходы", "Kes peaks kulud kinni maksma?"),
   ("kasu", "польза", "Sellest on palju kasu."),
   ("veebikursus", "онлайн-курс", None),
  ]),
  {"type": "speaking", "minutes": 22, "title": "Rääkimine",
   "instruction_ru": "Говорите вслух, лучше записывая себя на диктофон телефона. Таймер покажет время подготовки и ответа. Не читайте с листа — только ключевые слова.",
   "parts": [
    {"label": "1. Tutvumine", "prompt_et": "Rääkige endast: kus te töötate või õpite? Miks te õpite eesti keelt? Kuidas te keelt praktiseerite?", "prompt_ru": "Разминка, как в начале экзамена.", "prep_sec": 0, "talk_sec": 60,
     "hints": ["Ma töötan … / Ma õpin …", "Eesti keelt on mul vaja, et …", "Praktiseerin keelt nii, et …"]},
    {"label": "2. Ettekanne", "prompt_et": "Rääkige, kuidas täiskasvanud inimene saab end täiendada. Nimetage vähemalt kolm võimalust ja rääkige oma kogemusest.", "prep_sec": 120, "talk_sec": 90,
     "hints": ["Esiteks … teiseks … kolmandaks …", "Näiteks mina käisin …", "Kõige rohkem kasu oli mulle …", "Kokkuvõtteks …"]},
    {"label": "3. Arutelu", "prompt_et": "Kas tööandja peaks maksma töötaja koolituse eest? Tooge argumente poolt ja vastu ning jõudke järeldusele.", "prompt_ru": "На экзамене обсуждение идёт с партнёром. Дома сыграйте обе роли: сначала «за», потом «против», в конце общий вывод.", "prep_sec": 60, "talk_sec": 120,
     "hints": ["Poolt: töötaja oskused on ettevõttele kasulikud.", "Vastu: töötaja võib pärast koolitust lahkuda.", "Kompromiss: leping, et töötaja jääb ettevõttesse kindlaks ajaks."]},
   ],
   "phrases": ["Olen sinuga nõus, aga …", "Ma näen seda pisut teisiti.", "Mis sa arvad, kas …?", "See on hea mõte, kuid …", "Kokkuvõttes jõudsime järeldusele, et …"]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Прослушайте запись. Оценивают: выполнение задания, связность, богатство словаря, грамматику и произношение. Отметьте: были ли длинные паузы? Использовали ли вы связки (esiteks, lisaks, samas)? Повторите часть 2 ещё раз — второй вариант почти всегда лучше."}
 ]})

# ---------------------------------------------------------------- 5
L.append({
 "id": "d005", "day": 5, "version": 1, "skill": "grammatika",
 "title": "Sihitis: terve või osa?", "title_ru": "Объект: полный или частичный?",
 "topic": "tervis", "minutes": 35,
 "goal_ru": "Самая частая ошибка русскоязычных на B2 — падеж объекта. Повторяем правило на теме «здоровье».",
 "blocks": [
  vocab([
   ("retsept", "рецепт", "Arst kirjutas retsepti."),
   ("perearst", "семейный врач", None),
   ("haigusleht", "больничный лист", "Võtsin kolmeks päevaks haiguslehe."),
   ("ravim", "лекарство", None),
   ("vastuvõtt", "приём (у врача)", "Panin end arsti vastuvõtule kirja."),
   ("valu", "боль", "Mul on seljavalu."),
   ("tervislik", "здоровый (полезный)", "tervislik toit"),
   ("liikuma", "двигаться", "Liigu iga päev vähemalt pool tundi."),
   ("ennetama", "предупреждать, предотвращать", "Haigusi on lihtsam ennetada kui ravida."),
  ]),
  {"type": "grammar", "minutes": 20, "title": "Täis- ja osasihitis",
   "rule_ru": "ЧАСТИЧНЫЙ объект (osasihitis, partitiiv: leiba, raamatut, vett) — если: 1) предложение отрицательное (Ma ei ostnud leiba); 2) действие не завершено, идёт процесс (Ma loen raamatut); 3) неопределённое количество (Ostsin piima); 4) после глаголов чувств и процесса: armastama, vihkama, ootama, kuulama, aitama, vajama, kartma.\nПОЛНЫЙ объект (täissihitis) — если действие завершено и результат целиком: ед. ч. — родительный (Ostsin uue jope), мн. ч. — именительный (Ostsin need raamatud). В повелительном наклонении и безличных конструкциях ед. ч. — именительный: Võta see raamat! Raamat loeti läbi.\nПодсказка: слова läbi, valmis, ära, kinni, lõpuni обычно сигнализируют о полном объекте.",
   "examples": ["Ma lugesin raamatu läbi. (полный: завершено)", "Ma loen raamatut. (частичный: процесс)", "Ma ei lugenud raamatut. (частичный: отрицание)", "Loe raamat läbi! (повелительное — именительный)"],
   "tasks": [
    gap("Ma lugesin ___ (see artikkel) eile lõpuni.", ["selle artikli"]),
    gap("Ma ei leidnud ___ (oma ravim) üles.", ["oma ravimit"]),
    gap("Arst kirjutas mulle ___ (uus retsept).", ["uue retsepti"]),
    gap("Ma armastan ___ (eesti muusika).", ["eesti muusikat"]),
    gap("Jooge päevas vähemalt kaks liitrit ___ (vesi).", ["vett"]),
    gap("Võtke ___ (need tabletid) pärast sööki!", ["need tabletid"]),
    gap("Ma ootan ___ (teie vastus).", ["teie vastust"]),
    gap("Praegu ehitame ___ (suvila).", ["suvilat"]),
    gap("Ostsin poest ___ (piim) ja ___ (leib).", ["piima ja leiba", "piima, leiba"], "Впишите оба слова через «ja»."),
    gap("Ta tegi ___ (kodutöö) valmis.", ["kodutöö"]),
    mc("Milline lause on õige?", ["Ma panin ennast arsti vastuvõtule kirja.", "Ma panin end arsti vastuvõttu kirja.", "Ma panin ennast arsti vastuvõtule kirjas."], 0),
    mc("Milline lause on õige?", ["Perearst aitas mind.", "Perearst aitas mina.", "Perearst aitas minu."], 0, "aitama требует частичного объекта: aitas mind."),
   ]},
  {"type": "reading", "minutes": 7, "title": "Lühitekst: tervis",
   "text": "Paljud inimesed mõtlevad oma tervisele alles siis, kui midagi valutab. Perearstid soovitavad aga haigusi ennetada. Lihtsaim viis on liikuda iga päev vähemalt pool tundi, magada piisavalt ja süüa rohkem köögivilju. Ka iga-aastane tervisekontroll aitab probleeme varakult märgata. Kui te tunnete end halvasti, ärge oodake mitu nädalat, vaid pange end arsti vastuvõtule kirja. Paljud küsimused saab perearstiga lahendada ka telefoni teel või e-kirja kaudu.",
   "tasks": [
    mc("Mida soovitavad perearstid?", ["minna arsti juurde ainult siis, kui midagi valutab", "haigusi ennetada", "võtta iga päev ravimeid"], 1),
    tf("Perearstiga saab mõnikord suhelda ka telefoni teel.", True),
    tf("Tekst soovitab oodata mitu nädalat, enne kui arsti juurde minna.", False),
   ]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Найдите в своём письме из дня 3 все объекты и проверьте их падеж по правилу. Это самый быстрый способ поднять баллы за грамматику."}
 ]})

# ---------------------------------------------------------------- 6
L.append({
 "id": "d006", "day": 6, "version": 1, "skill": "lugemine",
 "title": "Kas prügi sorteerimisel on mõtet?", "title_ru": "Есть ли смысл сортировать мусор?",
 "topic": "keskkond", "minutes": 35,
 "goal_ru": "Чтение: задание «вставьте пропущенное предложение» и вопросы с выбором ответа.",
 "blocks": [
  vocab([
   ("jäätmed", "отходы", "Olmejäätmed visatakse segaprügi konteinerisse."),
   ("sorteerima", "сортировать", None),
   ("pakend", "упаковка", "Pakendid pannakse kollasesse konteinerisse."),
   ("biojäätmed", "пищевые (био)отходы", None),
   ("taaskasutama", "повторно использовать", None),
   ("prügila", "свалка", None),
   ("ladestama", "захоранивать (отходы)", "Prügi ladestatakse prügilasse."),
   ("trahv", "штраф", None),
   ("kahtlema (milles?)", "сомневаться", "Paljud kahtlevad sorteerimise mõttekuses."),
  ]),
  {"type": "reading", "minutes": 22, "title": "Lugemine",
   "instruction_ru": "Сначала прочитайте весь текст, не глядя на варианты. Потом для каждого пропуска [1]–[4] выберите предложение. Смотрите на связь с предыдущим и следующим предложением.",
   "text": "Kas prügi sorteerimisel on mõtet?\n\nViimastel aastatel on jäätmete sorteerimine muutunud Eestis kohustuslikuks. Kodudes tuleb eraldi koguda pakendeid, paberit, biojäätmeid ja ohtlikke jäätmeid. [1] Paljud inimesed aga kahtlevad, kas sellel on üldse mõtet.\n\nLevinud on arvamus, et prügiauto viib kõik konteinerid lõpuks ikkagi samasse kohta. Jäätmekäitlejate sõnul ei vasta see tõele. [2] Näiteks pakenditest valmistatakse uusi tooteid ja biojäätmetest toodetakse komposti või biogaasi.\n\nSorteerimisel on ka rahaline pool. Segaolmejäätmete äravedu on kallim kui sorteeritud jäätmete oma. [3] Seega võib korrusmaja, mille elanikud prügi hoolikalt sorteerivad, maksta prügiveo eest märgatavalt vähem.\n\nSpetsialistide arvates on kõige suurem probleem siiski see, et me tekitame liiga palju jäätmeid. [4] Kõige keskkonnasõbralikum prügi on see, mida üldse ei teki. Seepärast tasub poes valida vähem pakendatud kaupu ning kanda kaasas oma kotti.",
   "tasks": [
    mc("Milline lause sobib lünka [1]?", ["Selle eest, kes reegleid ei järgi, võib määrata trahvi.", "Sorteeritud jäätmed veetakse eri ettevõtetesse.", "Kuid sorteerimine üksi probleemi ei lahenda."], 0),
    mc("Milline lause sobib lünka [2]?", ["Selle eest, kes reegleid ei järgi, võib määrata trahvi.", "Sorteeritud jäätmed veetakse eri ettevõtetesse.", "Mida rohkem prügi, seda suurem arve."], 1),
    mc("Milline lause sobib lünka [3]?", ["Kuid sorteerimine üksi probleemi ei lahenda.", "Sorteeritud jäätmed veetakse eri ettevõtetesse.", "Mida rohkem segaprügi, seda suurem arve."], 2),
    mc("Milline lause sobib lünka [4]?", ["Kuid sorteerimine üksi probleemi ei lahenda.", "Selle eest, kes reegleid ei järgi, võib määrata trahvi.", "Biojäätmed tuleb panna pruuni konteinerisse."], 0),
    mc("Mis on teksti peamine mõte?", ["Sorteerimine on mõttetu, sest kõik jäätmed jõuavad prügilasse.", "Sorteerimine on kasulik, kuid veel tähtsam on jäätmeid vähem tekitada.", "Sorteerimine on liiga kallis."], 1),
    tf("Sorteeritud jäätmete äravedu on odavam kui segaprügi oma.", True),
    tf("Biojäätmetest toodetakse uusi pakendeid.", False, "Из биоотходов — компост или биогаз."),
   ]},
  {"type": "phrases", "minutes": 6, "title": "Põhjus ja tagajärg",
   "instruction_ru": "Связки причины и следствия. Составьте по одному предложению о сортировке мусора с каждой из первых четырёх.",
   "phrases": ["sest / kuna (потому что / так как)", "seetõttu / seepärast (поэтому)", "seega (таким образом)", "mistõttu (из-за чего)", "tänu sellele (благодаря этому)", "selle tulemusena (в результате)"]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "В задании с пропусками помогают «сцепки»: местоимения (see, selle eest), противопоставления (kuid, samas) и повтор слов (arve ← äravedu on kallim). Отметьте, какая сцепка помогла вам в каждом пропуске."}
 ]})

# ---------------------------------------------------------------- 7
L.append({
 "id": "d007", "day": 7, "version": 1, "skill": "kuulamine",
 "title": "Vabatahtlik toidupangas", "title_ru": "Волонтёр в продовольственном банке",
 "topic": "ühiskond", "minutes": 35,
 "goal_ru": "Аудирование: интервью о волонтёрстве. Понимание мотивов и мнений говорящего.",
 "blocks": [
  vocab([
   ("vabatahtlik", "доброволец, волонтёр; добровольный", None),
   ("toidupank", "продовольственный банк", None),
   ("annetama", "жертвовать", "Inimesed annetavad toitu."),
   ("abivajaja", "нуждающийся", None),
   ("jagama", "раздавать, делить", "Me jagame toidupakke."),
   ("rahuldust pakkuma", "приносить удовлетворение", "See töö pakub mulle rahuldust."),
   ("kogemus", "опыт", None),
   ("kogukond", "сообщество, община", None),
   ("panustama (millesse?)", "вкладываться, вносить вклад", "Igaüks saab panustada."),
  ]),
  {"type": "listening", "minutes": 18, "title": "Intervjuu vabatahtlikuga", "plays": 2,
   "instruction_et": "Kuulake intervjuud kaks korda ja vastake küsimustele.",
   "transcript": "Ajakirjanik: Andres, sa oled juba kolm aastat toidupangas vabatahtlik. Kuidas sa sinna sattusid?\nAndres: Täiesti juhuslikult. Mu naaber töötas seal ja kutsus mind ühel laupäeval appi, sest neil oli inimestest puudus. Ma mõtlesin, et lähen ühe korra, aga jäingi.\nAjakirjanik: Mida sa seal täpsemalt teed?\nAndres: Põhiliselt sorteerin toitu, mida poed ja eraisikud annetavad, ning panen kokku toidupakke. Kord kuus käin ka poes, kus palume ostjatel midagi annetada.\nAjakirjanik: Kas see ei ole raske, kui sul on ka tavaline töö?\nAndres: Ausalt öeldes on mõnikord raske. Ma töötan nädala sees, nii et vabatahtlik töö jääb nädalavahetusse. Aga ma ei kahetse. See töö pakub mulle rahuldust, sest ma näen kohe, et minu abist on kasu.\nAjakirjanik: Kes on teie abivajajad?\nAndres: Väga erinevad inimesed. Paljud arvavad, et toidupanka tulevad ainult töötud, aga tegelikult on seal palju eakaid ja paljulapselisi peresid. Ka töötavatel inimestel ei pruugi raha alati jätkuda.\nAjakirjanik: Mida sa soovitaksid neile, kes tahaksid samuti panustada?\nAndres: Alustage väikselt. Ei pea kohe iga nädal käima. Ka üks kord kuus on suur abi. Ja vabatahtlik töö on hea võimalus harjutada eesti keelt — meil on mitu vabatahtlikku, kes on nii oma keeleoskust parandanud.",
   "tasks": [
    mc("Kuidas Andres toidupanka sattus?", ["Ta luges kuulutust ajalehest.", "Naaber kutsus ta appi.", "Ta tööandja saatis ta sinna."], 1),
    mc("Mida Andres toidupangas põhiliselt teeb?", ["juhib toidupanka", "sorteerib toitu ja paneb kokku pakke", "veab toitu autoga laiali"], 1),
    mc("Millal Andres vabatahtlikuna töötab?", ["tööpäeviti õhtuti", "nädalavahetustel", "ainult suvel"], 1),
    mc("Miks see töö Andresele rahuldust pakub?", ["Ta saab selle eest palka.", "Ta näeb kohe oma abi kasu.", "Ta leidis sealt uue töö."], 1),
    tf("Toidupanka pöörduvad ainult töötud.", False),
    tf("Andrese sõnul piisab ka sellest, kui aidata üks kord kuus.", True),
    tf("Mõned vabatahtlikud on toidupangas oma eesti keelt parandanud.", True),
   ]},
  {"type": "speaking", "minutes": 8, "title": "Räägi ise",
   "parts": [{"label": "Arvamus", "prompt_et": "Kas teie oleksite valmis vabatahtlikuks hakkama? Miks või miks mitte? Millist vabatahtlikku tööd te teha tahaksite?", "prep_sec": 60, "talk_sec": 90,
              "hints": ["Ma oleksin valmis …, sest …", "Mulle sobiks kõige paremini …", "Ainus probleem on see, et …"]}]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll",
   "text": "Неделя 1 пройдена: чтение ×2, аудирование ×2, письмо, речь, грамматика. Отметьте в приложении, какая часть далась тяжелее всего — завтра начинаем второй круг."}
 ]})
