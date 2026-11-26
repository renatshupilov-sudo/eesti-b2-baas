# -*- coding: utf-8 -*-
# Уроки 8–14. Учебные тексты, имена и цифры вымышлены.
from lessons_01_07 import mc, tf, gap, vocab, ABC

L = []

# ---------------------------------------------------------------- 8
L.append({
 "id": "d008", "day": 8, "version": 1, "skill": "kirjutamine",
 "title": "Nutitelefonid koolis", "title_ru": "Смартфоны в школе",
 "topic": "haridus ja tehnoloogia", "minutes": 40,
 "goal_ru": "Второе задание письма: рассуждение-мнение (около 180 слов) с аргументами «за» и «против».",
 "blocks": [
  vocab([
   ("keelama", "запрещать", "Kool keelas telefonid tundides."),
   ("keeld", "запрет", None),
   ("tähelepanu hajuma", "внимание рассеивается", "Telefoni tõttu hajub tähelepanu."),
   ("kiusamine", "травля, буллинг", None),
   ("vahetund", "перемена", None),
   ("sõltuvus", "зависимость", None),
   ("vastutus", "ответственность", None),
   ("põhjendama", "обосновывать", "Põhjendage oma arvamust."),
   ("seisukoht", "точка зрения, позиция", "Minu seisukoht on selge."),
  ]),
  {"type": "grammar", "minutes": 8, "title": "Sidesõnad ja seostajad",
   "rule_ru": "Связность текста — отдельный критерий оценки. Противопоставление: kuid, aga, samas, seevastu. Уступка: kuigi (хотя), vaatamata sellele, et. Добавление: lisaks, peale selle, ka. Вывод: seega, seetõttu, kokkuvõttes. Порядок слов: после наречия-связки в начале предложения глагол стоит на втором месте (Seetõttu arvan …, Samas on …).",
   "examples": ["Kuigi telefon on kasulik, segab see tundides.", "Samas on telefon vajalik, et vanematega ühendust võtta.", "Seega pooldan osalist keeldu."],
   "tasks": [
    gap("___ telefon on kasulik õppevahend, segab see sageli tundi.", ["Kuigi"], "уступка"),
    gap("Paljud õpilased mängivad vahetundides telefonis. ___ liiguvad nad vähem.", ["Seetõttu", "Seepärast", "Seega"]),
    gap("Keeld vähendab kiusamist. ___ ei õpi lapsed nii telefoni vastutustundlikult kasutama.", ["Samas", "Teisalt", "Kuid"]),
    mc("Milline lause on õige sõnajärjega?", ["Seetõttu ma arvan, et keeld on vajalik.", "Seetõttu arvan ma, et keeld on vajalik.", "Seetõttu arvan, et keeld vajalik on."], 1, "После «seetõttu» в начале — глагол на второе место: Seetõttu arvan ma … (или: Seetõttu arvan, et …)."),
   ]},
  {"type": "writing", "minutes": 25, "title": "Kirjutamine: arvamuskirjutis",
   "prompt_et": "Mitmes Eesti koolis on nutitelefonide kasutamine tundides ja vahetundides keelatud. Kirjutage arvamuskirjutis teemal „Kas nutitelefonid tuleks koolis keelata?“. Tooge välja vähemalt kaks argumenti poolt ja üks vastu ning põhjendage oma seisukohta.",
   "prompt_ru": "Структура: вступление (тема + ваша позиция) → 2 аргумента с примерами → контраргумент и ответ на него → вывод. Около 180 слов, 4–5 абзацев.",
   "words": {"min": 160, "max": 210},
   "checklist": ["Есть заголовок", "Во вступлении ясна ваша позиция", "Минимум 2 аргумента «за» и 1 «против»", "Каждый аргумент подкреплён примером", "Связки: esiteks, lisaks, samas, seega, kokkuvõttes", "Вывод не повторяет вступление дословно", "160–210 слов"],
   "phrases": ["Viimasel ajal arutatakse palju selle üle, kas …", "Minu arvates …", "Esiteks …", "Teiseks / Lisaks sellele …", "Teisalt võib väita, et …", "Sellega võib osaliselt nõustuda, kuid …", "Kokkuvõttes leian, et …"],
   "model": "Kas nutitelefonid tuleks koolis keelata?\n\nViimasel ajal arutatakse palju selle üle, kas õpilased peaksid koolis nutitelefoni kasutama. Minu arvates oleks mõistlik telefonid tundides keelata, kuid täielik keeld ei ole vajalik.\n\nEsiteks hajub telefoni tõttu õpilaste tähelepanu. Kui laud on täis teavitusi, on raske õpetaja selgitusi kuulata ja ülesannetele keskenduda. Teiseks liiguvad lapsed vahetundides vähem ja suhtlevad omavahel harvem, sest paljud istuvad nurgas ja vaatavad ekraani. Lisaks aitab keeld vähendada küberkiusamist, mis sageli algab just koolipäeva jooksul.\n\nTeisalt võib väita, et telefon on tänapäeval oluline õppevahend ning vajalik ka selleks, et vanematega ühendust võtta. Sellega võib osaliselt nõustuda. Kui õpetaja palub telefoni mõne ülesande jaoks kasutada, peaks see olema lubatud.\n\nKokkuvõttes leian, et kõige parem lahendus on kokkulepe, mille järgi telefonid on tundides kotis ja neid võetakse välja ainult õpetaja loal. Nii õpivad lapsed tehnoloogiat vastutustundlikult kasutama."},
  {"type": "review", "minutes": 4, "title": "Enesekontroll",
   "text": "Посчитайте слова (приложение считает автоматически). Подчеркните все связки — их должно быть не меньше 6. Проверьте, что в каждом абзаце одна мысль."}
 ]})

# ---------------------------------------------------------------- 9
L.append({
 "id": "d009", "day": 9, "version": 1, "skill": "raakimine",
 "title": "Linnas või maal?", "title_ru": "В городе или в деревне?",
 "topic": "eluase ja elukeskkond", "minutes": 35,
 "goal_ru": "Устная часть: сравнение, описание ситуации и аргументированная дискуссия.",
 "blocks": [
  vocab([
   ("eluase", "жильё", None),
   ("üürima", "снимать (в аренду)", "Me üürime korterit kesklinnas."),
   ("kinnisvara", "недвижимость", None),
   ("laenu võtma", "брать кредит", "Kodu ostmiseks tuli võtta laenu."),
   ("maapiirkond", "сельская местность", None),
   ("teenused", "услуги", "Maal on vähem teenuseid."),
   ("rahulik", "спокойный", None),
   ("mürarikas", "шумный", None),
   ("eelis", "преимущество", "Linnaelu eelis on mugavus."),
   ("puudus", "недостаток", None),
  ]),
  {"type": "speaking", "minutes": 25, "title": "Rääkimine",
   "parts": [
    {"label": "1. Soojendus", "prompt_et": "Kirjeldage oma kodu ja kodukohta. Mis teile seal meeldib ja mis mitte?", "prep_sec": 0, "talk_sec": 60,
     "hints": ["Ma elan … (kus?)", "Mulle meeldib, et …", "Ainus puudus on …"]},
    {"label": "2. Võrdlus", "prompt_et": "Võrrelge elu linnas ja maal. Rääkige vähemalt kahest eelisest ja kahest puudusest.", "prep_sec": 120, "talk_sec": 120,
     "hints": ["Linnas on … rohkem / vähem …", "Võrreldes linnaga on maal …", "Seevastu …", "Kui maal elada, tuleb arvestada sellega, et …"]},
    {"label": "3. Olukord", "prompt_et": "Teie sõber saab tööpakkumise väikelinnas, mis asub pealinnast 150 km kaugusel. Ta kõhkleb. Andke talle nõu: mida ta peaks enne otsustamist kaaluma?", "prompt_ru": "Ролевое задание: используйте повелительное и условное наклонение — mõtle, kaalu, võiksid, ma soovitaksin.", "prep_sec": 60, "talk_sec": 90,
     "hints": ["Ma soovitaksin sul kõigepealt …", "Mõtle, kas …", "Sa võiksid ka …", "Kui ma oleksin sinu asemel, siis …"]},
    {"label": "4. Arutelu", "prompt_et": "Kas riik peaks toetama noori peresid, kes kolivad maale? Tooge argumente poolt ja vastu.", "prep_sec": 60, "talk_sec": 120,
     "hints": ["Poolt: maapiirkonnad tühjenevad.", "Vastu: toetus ei loo töökohti.", "Minu seisukoht on …"]},
   ],
   "phrases": ["Võrreldes …-ga", "Mida …, seda …", "Ühest küljest …, teisest küljest …", "Ma ei ole päris kindel, aga …", "See sõltub sellest, …"]},
  {"type": "review", "minutes": 4, "title": "Enesekontroll",
   "text": "Запишите ответ на часть 2. Посчитайте, сколько раз вы использовали сравнительную степень (suurem, rahulikum, kallim). Цель — минимум 4 раза за 2 минуты."}
 ]})

# ---------------------------------------------------------------- 10
L.append({
 "id": "d010", "day": 10, "version": 1, "skill": "grammatika",
 "title": "-ma, -da ja -des", "title_ru": "Инфинитивы на -ma, -da и деепричастие на -des",
 "topic": "kultuur ja vaba aeg", "minutes": 35,
 "goal_ru": "Глагольные формы, которые чаще всего путают: ma-инфинитив, da-инфинитив и des-форма.",
 "blocks": [
  vocab([
   ("etendus", "спектакль, представление", None),
   ("näitus", "выставка", None),
   ("pilet", "билет", None),
   ("muuseum", "музей", None),
   ("kontsert", "концерт", None),
   ("huviring", "кружок по интересам", None),
   ("lõõgastuma", "расслабляться", None),
   ("harrastus", "хобби, увлечение", "Minu harrastus on matkamine."),
   ("osalema (milles?)", "участвовать", "Ma osalen laulukooris."),
  ]),
  {"type": "grammar", "minutes": 22, "title": "Tegevusnimed ja des-vorm",
   "rule_ru": "-MA (lugema, vaatama) — после глаголов движения и начала: minema, tulema, hakkama, jääma, õppima, käima, kutsuma, aitama (Lähen kinno filmi vaatama. Hakkan õppima).\n-DA (lugeda, vaadata) — после глаголов желания, умения, возможности и оценок: tahtma, soovima, meeldima, võima, oskama, saama (= мочь), proovima, on vaja/tore/raske (Mulle meeldib lugeda. On raske otsustada).\n-DES (lugedes, vaadates) — «делая что-то» одновременно с основным действием, или способ действия (Ta kuulab muusikat süüa tehes. Keelt õpib kõige paremini rääkides). Образуется от da-инфинитива: lugeda → lugedes, teha → tehes, minna → minnes.",
   "examples": ["Läksime teatrisse etendust vaatama.", "Mulle meeldib nädalavahetusel muuseumides käia.", "Ta õppis eesti keelt raadiot kuulates."],
   "tasks": [
    gap("Me läheme laupäeval kinno uut filmi ___ (vaatama).", ["vaatama"]),
    gap("Mulle meeldib õhtuti raamatuid ___ (lugema).", ["lugeda"]),
    gap("Ta kuulab muusikat, ___ (sööki tegema) — kirjutage ainult verb.", ["tehes"], "teha → tehes"),
    gap("Kas te oskate ___ (ujuma)?", ["ujuda"]),
    gap("Lapsed hakkasid laulukooris ___ (käima).", ["käima"]),
    gap("Keelt õpib kõige paremini, emakeelsete inimestega ___ (rääkima).", ["rääkides"]),
    gap("Tal on raske nii varakult ___ (ärkama).", ["ärgata"], "ärkama → ärgata"),
    gap("Sõber kutsus mind kontserdile ___ (kaasa tulema) — kirjutage ainult verb.", ["tulema"]),
    gap("Ma tahaksin näitusele ___ (minema).", ["minna"]),
    gap("Koju ___ (minema) ostsin poest leiba.", ["minnes"]),
    mc("Milline lause on õige?", ["Ma unustasin pileteid osta.", "Ma unustasin piletid osta.", "Ma unustasin piletid ostma."], 1, "unustama + da-инфинитив; билеты куплены целиком (бы) — полный объект."),
   ]},
  {"type": "speaking", "minutes": 8, "title": "Räägi ise",
   "parts": [{"label": "Vaba aeg", "prompt_et": "Kuidas te oma vaba aega veedate? Mida te tahaksite proovida, aga pole veel jõudnud? Kasutage vähemalt kolme ma-, da- ja des-vormi.", "prep_sec": 30, "talk_sec": 90,
              "hints": ["Nädalavahetusel käin …", "Mulle meeldib …", "Ma tahaksin proovida …", "Lõõgastun kõige paremini …-des"]}]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll", "text": "Выпишите 5 глаголов, после которых вы ошиблись, и составьте с каждым своё предложение."}
 ]})

# ---------------------------------------------------------------- 11
L.append({
 "id": "d011", "day": 11, "version": 1, "skill": "lugemine",
 "title": "Tehisintellekt klassiruumis", "title_ru": "Искусственный интеллект в классе",
 "topic": "tehnoloogia", "minutes": 35,
 "goal_ru": "Чтение публицистического текста: позиция автора, значение слова из контекста, верно/неверно/нет в тексте.",
 "blocks": [
  vocab([
   ("tehisintellekt (TI)", "искусственный интеллект (ИИ)", None),
   ("õppevahend", "учебное средство", None),
   ("kodutöö", "домашнее задание", None),
   ("petma", "обманывать, списывать", None),
   ("hindama", "оценивать", None),
   ("kriitiline mõtlemine", "критическое мышление", None),
   ("allikas", "источник", "Kontrolli allikat."),
   ("asendama", "заменять", "TI ei asenda õpetajat."),
   ("ohustama", "угрожать", None),
  ]),
  {"type": "reading", "minutes": 22, "title": "Lugemine",
   "text": "Tehisintellekt klassiruumis\n\nKui mõni aasta tagasi said tehisintellekti vestlusrobotid laialdaselt kättesaadavaks, kartsid paljud õpetajad, et kodutööd kaotavad mõtte. Milleks õpilane peaks ise essee kirjutama, kui masin teeb selle mõne sekundiga? Esimene reaktsioon oli paljudes koolides keelata.\n\nPraeguseks on suhtumine muutunud. Õpetajad on mõistnud, et keelamine on sama vähe tulemuslik kui omal ajal taskuarvutite või Vikipeedia keelamine. Selle asemel otsitakse viise, kuidas uut tehnoloogiat targalt kasutada. Näiteks laseb ajalooõpetaja Kristi Ilves õpilastel kõigepealt tehisintellektiga essee koostada ja seejärel selle vead üles leida. „Õpilased avastavad üllatusega, et masin esitab enesekindlalt ka valeinfot,“ ütleb ta.\n\nSamas ei saa probleeme eitada. Kui õpilane laseb kõik ülesanded masinal ära teha, ei arene tema enda oskused. Seepärast on paljud koolid muutnud hindamist: rohkem tähtsust antakse klassis tehtavale tööle, suulistele esitlustele ja sellele, kuidas õpilane oma mõttekäiku selgitab.\n\nEksperdid rõhutavad, et kõige tähtsam oskus tehisintellekti ajastul on kriitiline mõtlemine. Õpilane peab oskama küsida, kust info pärineb, ja kontrollima allikaid. Tehisintellekt ei asenda õpetajat, kuid muudab tema rolli: õpetajast saab üha enam juhendaja, kes aitab õpilasel infotulvas orienteeruda.",
   "tasks": [
    mc("Mis oli paljude koolide esimene reaktsioon vestlusrobotitele?", ["Neid hakati kohe tundides kasutama.", "Nende kasutamine keelati.", "Kodutööd kaotati ära."], 1),
    mc("Miks võrdleb autor tehisintellekti keelamist taskuarvutite keelamisega?", ["Mõlemad olid kallid.", "Mõlemad keelud ei andnud tulemust.", "Mõlemaid kasutatakse matemaatikas."], 1),
    mc("Milleks kasutab Kristi Ilves tehisintellekti?", ["Õpilased kirjutavad TI abil essee ja otsivad sealt vigu.", "TI hindab õpilaste esseesid.", "TI koostab tema eest tunnikava."], 0),
    mc("Mida tähendab tekstis sõna „infotulv“?", ["infotund koolis", "väga suur hulk infot", "vale info"], 1, "tulv = поток, наводнение → поток информации."),
    mc("Milline on autori seisukoht?", ["TI ohustab haridust ja tuleks keelata.", "TI on kasulik, kui seda kasutatakse targalt ja kriitiliselt.", "TI asendab peagi õpetajad."], 1),
    tf("Paljud koolid annavad nüüd rohkem tähtsust suulistele esitlustele.", True),
    tf("Kristi Ilvese õpilased usaldavad masina vastuseid täielikult.", False),
    tf("Tekstis öeldakse, et Eestis on vestlusrobotid koolis seadusega keelatud.", False, "Такого в тексте нет. На экзамене бывают утверждения, которых нет в тексте, — их отмечают как неверные (или «ei selgu tekstist», если такой вариант дан)."),
   ]},
  {"type": "phrases", "minutes": 6, "title": "Sõnavara laiendamine",
   "instruction_ru": "Образуйте существительные от глаголов (на B2 за богатство словаря дают отдельные баллы): hindama → hindamine; kasutama → kasutamine / kasutaja; arenema → areng; keelama → keeld; muutuma → muutus; õpetama → õpetaja / õpetus.",
   "phrases": ["hindama → hindamine", "kasutama → kasutaja, kasutamine", "arenema → areng", "keelama → keeld", "muutuma → muutus", "esitama → esitlus", "mõtlema → mõte, mõtlemine"]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll", "text": "Определите, в каком абзаце позиция автора видна лучше всего (обычно — последний). На экзамене вопрос о мнении автора почти всегда решается по вступлению и выводу."}
 ]})

# ---------------------------------------------------------------- 12
L.append({
 "id": "d012", "day": 12, "version": 1, "skill": "kuulamine",
 "title": "Teadaanded ja uudised", "title_ru": "Объявления и новости",
 "topic": "igapäevaelu", "minutes": 35,
 "goal_ru": "Короткие аудиотексты: объявления на вокзале и в магазине, прогноз погоды, новость. Ловим время, место и изменения.",
 "blocks": [
  vocab([
   ("väljuma", "отправляться", "Rong väljub teiselt platvormilt."),
   ("hilinema", "опаздывать", None),
   ("ärajäämine", "отмена", None),
   ("asendusbuss", "автобус взамен (поезда)", None),
   ("allahindlus", "скидка", None),
   ("sademed", "осадки", None),
   ("tuul pöördub", "ветер меняется", None),
   ("teetööd", "дорожные работы", None),
   ("ümbersõit", "объезд", None),
  ]),
  {"type": "listening", "minutes": 15, "title": "Neli lühiteksti", "plays": 2,
   "instruction_ru": "Четыре коротких текста подряд. На каждый — один-два вопроса.",
   "transcript": "Tekst 1. Lugupeetud reisijad! Kell 17.45 Tartusse väljuv rong hilineb tehnilise rikke tõttu umbes kakskümmend minutit. Rong väljub tavapärase kolmanda platvormi asemel esimeselt platvormilt. Vabandame ebamugavuste pärast.\nTekst 2. Head kliendid! Täna kella kaheksateistkümnest kuni poest sulgemiseni on kõik talvejalanõud kolmkümmend protsenti soodsamad. Allahindlus ei kehti kinkekaartidega ostes. Kassad asuvad teisel korrusel.\nTekst 3. Homme on ilm pilvine. Hommikul sajab Lääne-Eestis lund, pärastlõunal läheb sadu üle lörtsiks. Puhub läänetuul, mis õhtul pöördub loodesse. Õhutemperatuur on miinus kahest pluss ühe kraadini. Teed võivad olla libedad.\nTekst 4. Alates esmaspäevast algavad Pärnu maanteel teetööd, mis kestavad eeldatavalt mai lõpuni. Liiklus on piiratud ühele sõidurajale. Autojuhtidel soovitatakse kasutada ümbersõitu läbi Hiiu tänava. Bussiliiklust muudatused ei mõjuta.",
   "tasks": [
    mc("Tekst 1. Mitu minutit rong hilineb?", ["umbes 12", "umbes 20", "umbes 45"], 1),
    mc("Tekst 1. Kust rong väljub?", ["esimeselt platvormilt", "teiselt platvormilt", "kolmandalt platvormilt"], 0),
    mc("Tekst 2. Millal allahindlus kehtib?", ["terve päeva", "alates kella 18-st", "kuni kella 18-ni"], 1),
    tf("Tekst 2. Allahindlust saab ka kinkekaardiga makstes.", False),
    mc("Tekst 3. Milline on homne ilm pärastlõunal?", ["päikeseline", "sajab lörtsi", "sajab vihma ja on soe"], 1),
    mc("Tekst 4. Mida soovitatakse autojuhtidele?", ["sõita bussiga", "kasutada ümbersõitu", "sõita öösel"], 1),
    tf("Tekst 4. Bussid peavad samuti ümbersõitu kasutama.", False),
   ]},
  {"type": "dictation", "minutes": 10, "title": "Kellaajad ja kuupäevad",
   "instruction_ru": "Запишите время в формате 17.45, дату — как 3.12 (день.месяц).",
   "items": [
    {"audio": "kell seitseteist nelikümmend viis", "answer": ["17.45", "17:45"]},
    {"audio": "kell pool kaheksa õhtul", "answer": ["19.30", "19:30"]},
    {"audio": "veerand üheksa hommikul", "answer": ["8.15", "08.15", "8:15", "08:15"]},
    {"audio": "kolmas detsember", "answer": ["3.12", "03.12"]},
    {"audio": "kahekümne neljandal veebruaril", "answer": ["24.02", "24.2"]},
    {"audio": "kolmveerand kümme", "answer": ["9.45", "09.45", "9:45", "09:45"]},
   ]},
  {"type": "review", "minutes": 3, "title": "Enesekontroll", "text": "Внимание: «pool kaheksa» = 7:30 (половина восьмого), а не 8:30. «Veerand üheksa» = 8:15, «kolmveerand kümme» = 9:45. Повторите эти три формы вслух."}
 ]})

# ---------------------------------------------------------------- 13
L.append({
 "id": "d013", "day": 13, "version": 1, "skill": "kirjutamine",
 "title": "Ettepanek korteriühistule", "title_ru": "Предложение товариществу собственников",
 "topic": "eluase ja kogukond", "minutes": 40,
 "goal_ru": "Полуофициальное письмо-предложение (около 140 слов): описать проблему, предложить решение, обосновать.",
 "blocks": [
  vocab([
   ("korteriühistu", "товарищество собственников квартир", None),
   ("juhatus", "правление", None),
   ("üldkoosolek", "общее собрание", None),
   ("hoov", "двор", None),
   ("mänguväljak", "детская площадка", None),
   ("ettepanek", "предложение", "Teen ettepaneku …"),
   ("talgud", "толока, субботник", "Korraldame talgud."),
   ("eelarve", "бюджет", None),
   ("hääletama", "голосовать", None),
  ]),
  {"type": "phrases", "minutes": 6, "title": "Ettepaneku tegemine",
   "instruction_ru": "Выучите 4 фразы — они подходят для любого письма-предложения на экзамене.",
   "phrases": ["Pöördun teie poole ühe ettepanekuga.", "Olen märganud, et …", "Teen ettepaneku …(da)", "Võiksime näiteks …", "Selle eeliseks oleks see, et …", "Olen valmis ise …", "Palun arutada seda küsimust järgmisel üldkoosolekul."]},
  {"type": "writing", "minutes": 25, "title": "Kirjutamine: ettepanek",
   "prompt_et": "Teie maja hoov on halvas seisukorras: mänguväljak on vana ja prügikastide ümbrus räpane. Kirjutage korteriühistu juhatusele e-kiri. Kirjutage:\n• mis on probleem;\n• mida te ette panete (vähemalt kaks ideed);\n• kuidas te ise saaksite aidata.",
   "words": {"min": 120, "max": 160},
   "checklist": ["Обращение: Lugupeetud korteriühistu juhatus!", "Проблема описана конкретно", "Два предложения с обоснованием", "Ваш личный вклад", "Просьба (обсудить на собрании / ответить)", "Lugupidamisega + имя, номер квартиры", "120–160 слов"],
   "phrases": [],
   "model": "Lugupeetud korteriühistu juhatus!\n\nPöördun teie poole ühe ettepanekuga, mis puudutab meie maja hoovi. Olen märganud, et mänguväljak on väga vanaks jäänud: kiikede puit on mädanenud ja liivakastis on klaasikilde. Ka prügikastide ümbrus on sageli räpane, sest konteinereid on liiga vähe.\n\nTeen ettepaneku vahetada vana mänguväljak välja uue ja turvalisema vastu. Selle jaoks võiksime taotleda toetust linnalt, nii et ühistu eelarve ei kannataks. Lisaks oleks mõistlik paigaldada üks konteiner juurde ja panna sinna sorteerimise juhend.\n\nOlen valmis ise aitama: võiksin korraldada kevadel talgud, kus elanikud saaksid koos hoovi koristada. Usun, et paljud naabrid oleksid nõus kaasa lööma.\n\nPalun arutada seda küsimust järgmisel üldkoosolekul.\n\nLugupidamisega\nNimi Perekonnanimi\nkorter nr 12"},
  {"type": "review", "minutes": 4, "title": "Enesekontroll", "text": "Сравните письма дня 3 и дня 13: какие фразы вы теперь используете автоматически? Выпишите свой личный «шаблон письма» из 6–8 фраз."}
 ]})

# ---------------------------------------------------------------- 14
L.append({
 "id": "d014", "day": 14, "version": 1, "skill": "proovieksam",
 "title": "Väike proovieksam", "title_ru": "Мини-пробный экзамен",
 "topic": "kordamine", "minutes": 40,
 "goal_ru": "Все четыре части в сжатом виде, строго по таймеру. Итог двух недель.",
 "blocks": [
  {"type": "intro", "minutes": 1, "title": "Reeglid",
   "text": "Работайте без словаря и подсказок, как на экзамене. Не открывайте расшифровку и образцы до конца урока. Порядок частей как на настоящем экзамене: письмо → аудирование → чтение → речь."},
  {"type": "writing", "minutes": 12, "title": "1. Kirjutamine (lühike)",
   "prompt_et": "Teie kolleeg korraldab reedel sünnipäevapeo, aga te ei saa tulla. Kirjutage talle lühike kiri: vabandage, selgitage põhjust ja tehke ettepanek kohtuda mõnel teisel ajal.",
   "words": {"min": 60, "max": 90},
   "checklist": ["Обращение и прощание (неформальные: Tere, Kati! … Kallistades / Parimat!)", "Извинение + причина", "Конкретное предложение (день, место)"],
   "phrases": ["Kahjuks ei saa ma …", "Mul on väga kahju, aga …", "Kuidas oleks, kui …?"],
   "model": "Tere, Kati!\n\nAitäh kutse eest! Mul on väga kahju, aga kahjuks ei saa ma reedel sinu peole tulla. Mu ema sõidab nädalavahetuseks Narva ja ma lubasin ta õhtul rongi pealt ära tuua.\n\nKuidas oleks, kui läheksime järgmisel nädalal koos lõunale? Ma tahaksin sulle sünnipäeva puhul väikese kingituse üle anda. Näiteks kolmapäeval kell 12 kohvikus meie kontori kõrval?\n\nSoovin sulle toredat pidu!\nAnna"},
  {"type": "listening", "minutes": 7, "title": "2. Kuulamine", "plays": 1,
   "instruction_ru": "Как первое задание на экзамене — текст звучит только ОДИН раз.",
   "transcript": "Tere! Helistan teile Linnaraamatukogust. Te broneerisite meie juures keelekohviku koha neljapäevaks. Kahjuks peame keelekohviku sel nädalal ära jätma, sest meie juhendaja on haige. Järgmine kohtumine toimub tavapärasel ajal, see tähendab teisipäeval kell kuusteist kolmkümmend, kuid uues kohas: mitte teisel korrusel, vaid lasteosakonna kõrval esimesel korrusel. Teie broneering kantakse automaatselt üle. Kui teile uus aeg ei sobi, palun saatke meile e-kiri. Aitäh ja kohtumiseni!",
   "tasks": [
    mc("Miks keelekohvik ära jääb?", ["ruum on remondis", "juhendaja on haige", "liiga vähe osalejaid"], 1),
    mc("Millal toimub järgmine kohtumine?", ["neljapäeval kell 16.30", "teisipäeval kell 16.30", "teisipäeval kell 6.30"], 1),
    mc("Kus toimub järgmine kohtumine?", ["teisel korrusel", "esimesel korrusel", "lasteosakonnas"], 1),
    tf("Uue aja jaoks tuleb uuesti broneerida.", False),
   ]},
  {"type": "reading", "minutes": 10, "title": "3. Lugemine",
   "text": "Kuulutus\n\nOtsime oma meeskonda klienditeenindajat (täistööaeg)\n\nOleme kiiresti kasvav Tallinna jalgrattarendifirma. Sinu ülesanne on nõustada kliente telefoni, e-posti ja vestlusakna kaudu ning lahendada probleeme, mis tekivad rattarendi ajal.\n\nOotame sinult:\n• väga head eesti keele oskust ning vene ja inglise keele oskust suhtlustasemel;\n• rahulikku ja sõbralikku suhtlemisoskust;\n• valmisolekut töötada graafiku alusel, sh mõnel nädalavahetusel.\n\nPakume:\n• võimalust töötada kaks päeva nädalas kodust;\n• tasuta rattarenti endale ja pereliikmetele;\n• keelekursust, kui soovid oma inglise keelt parandada.\n\nCV ja lühike motivatsioonikiri saada hiljemalt 15. jaanuariks.",
   "tasks": [
    mc("Mis on klienditeenindaja põhiülesanne?", ["rataste parandamine", "klientide nõustamine", "rataste kohaletoimetamine"], 1),
    tf("Kandidaat peab oskama inglise keelt emakeele tasemel.", False),
    tf("Töötaja peab mõnikord töötama ka nädalavahetusel.", True),
    mc("Milline neist EI OLE kuulutuses pakutud soodustus?", ["kaugtöö võimalus", "tasuta rattarent perele", "tasuta eesti keele kursus"], 2, "Предлагают курс английского, а не эстонского."),
    gap("Dokumendid tuleb saata hiljemalt ___ jaanuariks (kirjutage numbriga).", ["15", "15."]),
   ]},
  {"type": "speaking", "minutes": 7, "title": "4. Rääkimine",
   "parts": [
    {"label": "Ettekanne", "prompt_et": "Te kandideerite kuulutuses kirjeldatud töökohale. Tutvustage end tööintervjuul: teie kogemus, oskused ja miks see töö teile sobib.", "prep_sec": 90, "talk_sec": 90,
     "hints": ["Mul on … aastat kogemust …", "Minu tugevad küljed on …", "Mind huvitab see töö, sest …"]},
    {"label": "Küsimus", "prompt_et": "Intervjueerija küsib: „Kuidas te käitute, kui klient on väga vihane?“ Vastake.", "prep_sec": 20, "talk_sec": 60}]},
  {"type": "review", "minutes": 3, "title": "Tulemus",
   "text": "Теперь откройте образцы и расшифровку. Проходной балл на экзамене — 60% от общей суммы, и ни одна часть не может быть 0. Отметьте, в какой части результат ниже 60% — с неё начнёте следующий круг. Цикл повторяется с дня 1; новые уроки приходят автоматически с обновлениями базы."}
 ]})
