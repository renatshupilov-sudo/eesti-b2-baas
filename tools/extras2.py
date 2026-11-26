# -*- coding: utf-8 -*-
# Правки по отзыву Renat (26.11.2026): слова уровня B2, упражнения на связки с автопроверкой,
# полезная грамматика вместо порядка слов, живое аудирование ERR Jupiter.
from lessons_01_07 import mc, gap

def V(*rows):
    return [{"et": a, "ru": b, "example": c} for a, b, c in rows]

VOCAB = {
 "d001": V(
  ("paindlik töökorraldus", "гибкая организация работы", "Paindlik töökorraldus aitab tööd ja pereelu ühendada."),
  ("piiri tõmbama (mille vahele?)", "провести границу", "Kodus on raske tõmmata piiri töö ja eraelu vahele."),
  ("meeskonnatunne", "командный дух", "Kohvipausid tugevdavad meeskonnatunnet."),
  ("tootlikkus", "производительность", "Kaugtöö ei pruugi tootlikkust vähendada."),
  ("vastutustunne", "чувство ответственности", "Kontrolli puudumine võib vähendada vastutustunnet."),
  ("kohanema (millega?)", "адаптироваться (к чему)", "Uuel töötajal on raske organisatsiooni kultuuriga kohaneda."),
  ("varjukülg", "обратная (теневая) сторона", "Igal lahendusel on oma varjuküljed."),
  ("ühene", "однозначный", "Kaugtöö mõju ei ole sugugi ühene."),
  ("kippuma (+ ma-infinitiiv)", "иметь склонность, норовить", "Tööpäev kipub venima hilisõhtuni.")),
 "d002": V(
  ("tipptund", "час пик", "Tipptunnil sõidab tööle kõige rohkem inimesi."),
  ("ülerahvastatud", "переполненный", "Hommikused bussid on sageli ülerahvastatud."),
  ("end õigustama", "оправдать себя", "Tasuta ühistransport on end osaliselt õigustanud."),
  ("koormust vähendama", "снизить нагрузку", "Paindlik tööaeg aitab hommikust koormust vähendada."),
  ("eelistama (mida millele?)", "предпочитать (что чему)", "Paljud eelistavad autot bussile."),
  ("harjumusi muutma", "менять привычки", "Autojuhid ei ole oma harjumusi muutnud."),
  ("usaldusväärne", "надёжный", "Sõiduplaan peab olema usaldusväärne."),
  ("meelitama", "привлекать, заманивать", "Kuidas meelitada autojuhte bussi peale?"),
  ("kaaluma", "взвешивать, рассматривать", "Ettevõtted võiksid kaaluda paindlikku tööaega.")),
 "d003": V(
  ("defektne", "неисправный, с браком", "Defektse toote võib poodi tagastada."),
  ("tagastama", "возвращать", "Ostu võib tagastada 14 päeva jooksul."),
  ("hüvitama", "возмещать", "Pood hüvitas saatmiskulud."),
  ("garantii kehtib", "гарантия действует", "Garantii kehtib kaks aastat."),
  ("lepingust taganema", "отказаться от договора", "E-poe ostu puhul on õigus lepingust 14 päeva jooksul taganeda."),
  ("tarbijakaitse", "защита прав потребителей", "Probleemi korral võib pöörduda tarbijakaitse poole."),
  ("pretensiooni esitama", "предъявить претензию", "Kliendil on õigus esitada pretensioon kahe aasta jooksul."),
  ("pettuma (milles?)", "разочароваться (в чём)", "Olen teie teeninduses pettunud."),
  ("tarne hilinemine", "задержка доставки", "Vabandame tarne hilinemise pärast.")),
 "d004": V(
  ("elukestev õpe", "обучение в течение всей жизни", "Elukestev õpe on tänapäeval vajalik."),
  ("ümberõpe", "переподготовка", "Riik toetab täiskasvanute ümberõpet."),
  ("end täiendama", "повышать квалификацию", "Tahan end erialal täiendada."),
  ("õppemaks", "плата за обучение", "Tööandja maksab poole õppemaksust."),
  ("töö kõrvalt õppima", "учиться без отрыва от работы", "Paljud täiskasvanud õpivad töö kõrvalt."),
  ("paigal tammuma", "топтаться на месте", "Tundsin, et olen paigal tammunud."),
  ("takistus", "препятствие", "Vanus ei ole õppimisel takistus."),
  ("vastutasuks", "взамен", "Vastutasuks lubas ta ettevõttesse jääda."),
  ("süüdi tundma (end)", "чувствовать себя виноватым", "Ta tundis end süüdi, et lastele ei jätkunud aega.")),
 "d005": V(
  ("ennetama", "предупреждать, предотвращать", "Haigusi on lihtsam ennetada kui ravida."),
  ("tervisekontroll", "медосмотр", "Iga-aastane tervisekontroll aitab probleeme varakult märgata."),
  ("haigusleht", "больничный лист", "Võtsin kolmeks päevaks haiguslehe."),
  ("vastuvõtule kirja panema", "записать на приём", "Pange end arsti vastuvõtule kirja."),
  ("krooniline", "хронический", "Kroonilised haigused vajavad pidevat ravi."),
  ("immuunsus", "иммунитет", "Piisav uni tugevdab immuunsust."),
  ("istuv eluviis", "сидячий образ жизни", "Istuv eluviis kahjustab tervist."),
  ("varakult märkama", "вовремя заметить", "Probleemi on oluline varakult märgata."),
  ("retseptiravim", "рецептурное лекарство", "Retseptiravimit saab apteegist osta ainult retsepti alusel.")),
 "d006": V(
  ("jäätmekäitlus", "обращение с отходами", "Jäätmekäitlus on kohaliku omavalitsuse ülesanne."),
  ("taaskasutama", "повторно использовать", "Pakendeid saab taaskasutada."),
  ("ladestama", "захоранивать (отходы)", "Segaprügi ladestatakse prügilasse."),
  ("keskkonnasõbralik", "экологичный", "Kõige keskkonnasõbralikum prügi on see, mida ei teki."),
  ("tekitama", "создавать, образовывать", "Me tekitame liiga palju jäätmeid."),
  ("kohustuslik", "обязательный", "Sorteerimine on muutunud kohustuslikuks."),
  ("tõele vastama", "соответствовать действительности", "See arvamus ei vasta tõele."),
  ("märgatavalt", "заметно", "Sorteerimine vähendab prügiarvet märgatavalt."),
  ("ohtlikud jäätmed", "опасные отходы", "Patareid on ohtlikud jäätmed.")),
 "d007": V(
  ("vabatahtlik", "доброволец; добровольный", "Ta on kolm aastat toidupangas vabatahtlik."),
  ("annetama", "жертвовать", "Poed annetavad toitu, mille säilivusaeg hakkab lõppema."),
  ("abivajaja", "нуждающийся", "Toidupank aitab abivajajaid."),
  ("sattuma (kuhu?)", "попасть (случайно)", "Kuidas sa toidupanka sattusid?"),
  ("kahetsema", "сожалеть", "Ma ei kahetse oma otsust."),
  ("rahuldust pakkuma", "приносить удовлетворение", "See töö pakub mulle rahuldust."),
  ("paljulapseline pere", "многодетная семья", "Abi saavad ka paljulapselised pered."),
  ("kodanikuühiskond", "гражданское общество", "Vabatahtlik töö tugevdab kodanikuühiskonda."),
  ("panustama (millesse?)", "вкладываться (во что)", "Igaüks saab ühiskonda panustada.")),
 "d008": V(
  ("tähelepanu hajub", "внимание рассеивается", "Telefoni tõttu hajub tähelepanu."),
  ("küberkiusamine", "кибербуллинг", "Küberkiusamine algab sageli koolipäeva jooksul."),
  ("sõltuvus", "зависимость", "Nutisõltuvus on noorte seas levinud."),
  ("vastutustundlikult", "ответственно", "Lapsed peavad õppima tehnoloogiat vastutustundlikult kasutama."),
  ("seisukohta põhjendama", "обосновать позицию", "Põhjendage oma seisukohta näidetega."),
  ("vastuargument", "контраргумент", "Hea arvamuskirjutis sisaldab ka vastuargumenti."),
  ("keeldu kehtestama", "ввести запрет", "Mitu kooli on kehtestanud telefonikeelu."),
  ("osaliselt nõustuma", "частично согласиться", "Sellega võib osaliselt nõustuda."),
  ("mõistlik", "разумный", "Mõistlik lahendus on kokkulepe.")),
 "d009": V(
  ("kinnisvara", "недвижимость", "Kinnisvara hinnad on pealinnas kõrged."),
  ("kodulaen", "ипотека", "Maja ostmiseks võtsid nad kodulaenu."),
  ("endale lubama", "позволить себе", "Pealinnas oleksime saanud endale lubada ainult väikese korteri."),
  ("kohalik omavalitsus", "местное самоуправление", "Kohalik omavalitsus toetab noori peresid."),
  ("vallavanem", "волостной старейшина (глава волости)", "Vallavanem rõhutas teede olulisust."),
  ("suundumus", "тенденция", "See suundumus on viimastel aastatel tugevnenud."),
  ("elukvaliteet", "качество жизни", "Paljudele on elukvaliteet olulisem kui palk."),
  ("tööteekond", "дорога на работу", "Lühike tööteekond säästab aega."),
  ("tühjenema", "пустеть", "Maapiirkonnad tühjenevad.")),
 "d010": V(
  ("lavastus", "постановка, спектакль", "Uus lavastus esietendub järgmisel nädalal."),
  ("esietendus", "премьера", "Esietendusele olid piletid kohe välja müüdud."),
  ("väljapanek", "экспозиция", "Muuseumi uus väljapanek räägib Eesti ajaloost."),
  ("kultuuripärand", "культурное наследие", "Laulupidu on osa Eesti kultuuripärandist."),
  ("harrastus", "хобби, увлечение", "Laulmine on minu peamine harrastus."),
  ("elamus", "впечатление, переживание", "Kontsert oli tõeline elamus."),
  ("lõõgastuma", "расслабляться", "Lõõgastun kõige paremini metsas jalutades."),
  ("osalema (milles?)", "участвовать (в чём)", "Ma osalen laulukooris."),
  ("välja müüdud", "распроданы", "Kõik piletid olid nädal enne kontserti välja müüdud.")),
 "d011": V(
  ("kättesaadav", "доступный", "Vestlusrobotid said laialdaselt kättesaadavaks."),
  ("tulemuslik", "результативный", "Keelamine ei osutunud tulemuslikuks."),
  ("valeinfo", "ложная информация", "Masin võib enesekindlalt esitada valeinfot."),
  ("allikakriitika", "критическая оценка источников", "Allikakriitika on infoajastul hädavajalik."),
  ("mõttekäik", "ход мысли", "Õpilane peab oskama oma mõttekäiku selgitada."),
  ("eitama", "отрицать", "Probleeme ei saa eitada."),
  ("infotulv", "поток информации", "Õpetaja aitab infotulvas orienteeruda."),
  ("asendama", "заменять", "Tehisintellekt ei asenda õpetajat."),
  ("juhendaja", "руководитель, наставник", "Õpetajast saab üha enam juhendaja.")),
 "d012": V(
  ("tehniline rike", "техническая неисправность", "Rong hilineb tehnilise rikke tõttu."),
  ("tavapärane", "обычный", "Rong väljub tavapärase platvormi asemel esimeselt."),
  ("ebamugavus", "неудобство", "Vabandame ebamugavuste pärast."),
  ("kehtima", "действовать (о правиле)", "Allahindlus ei kehti kinkekaartidega."),
  ("lörts", "мокрый снег", "Pärastlõunal läheb lumi üle lörtsiks."),
  ("libedus", "гололёд", "Teedel on oodata libedust."),
  ("eeldatavalt", "предположительно", "Teetööd kestavad eeldatavalt mai lõpuni."),
  ("piirama", "ограничивать", "Liiklus on piiratud ühele sõidurajale."),
  ("mõjutama", "влиять", "Muudatused bussiliiklust ei mõjuta.")),
 "d013": V(
  ("korteriühistu", "товарищество собственников квартир", "Korteriühistu juhatus otsustab remondi üle."),
  ("üldkoosolek", "общее собрание", "Seda küsimust arutatakse üldkoosolekul."),
  ("ettepanekut tegema", "вносить предложение", "Teen ettepaneku hoov korrastada."),
  ("talgud", "толока, субботник", "Kevadel korraldame hoovis talgud."),
  ("toetust taotlema", "подать заявку на поддержку", "Ühistu võiks taotleda linnalt toetust."),
  ("eelarve", "бюджет", "Ühistu eelarve on piiratud."),
  ("kaasa lööma", "принять участие", "Paljud naabrid on nõus kaasa lööma."),
  ("paigaldama", "устанавливать", "Hoovi paigaldatakse uus konteiner."),
  ("seisukord", "состояние", "Mänguväljak on halvas seisukorras.")),
}

# Пункт «фразы» → упражнения с автопроверкой и пояснениями.
PHRASE_TASKS = {
 "d001": ("Связки для мнения. Сначала прочитайте список, затем впишите подходящую связку — ответ проверится автоматически.", [
   gap("___ poolt on kaugtööl palju eeliseid, teiselt poolt tunnevad paljud end üksildasena.", ["Ühelt", "ühelt"], None, "Пара «ühelt poolt … teiselt poolt» — «с одной стороны … с другой стороны»."),
   gap("Kaugtöö sobib mulle, ___ säästan iga päev tunni aega.", ["sest", "kuna"], None, "Причина: sest / kuna (потому что / так как)."),
   gap("Kodus on lihtne keskenduda. ___ on raske tõmmata piiri töö ja eraelu vahele.", ["Samas", "Teisalt", "Kuid", "samas", "teisalt", "kuid"], None, "Противопоставление: samas / teisalt / kuid. После «Samas» глагол на втором месте: Samas on …"),
   gap("___ võib öelda, et hübriidtöö on parim lahendus.", ["Kokkuvõttes", "Seega", "kokkuvõttes", "seega"], None, "Вывод в конце текста: kokkuvõttes / seega."),
   gap("Kõik ___ sellest, kuidas tööd korraldada.", ["oleneb", "sõltub"], None, "olenema / sõltuma + MILLEST: kõik oleneb sellest, kuidas …"),
 ]),
 "d006": ("Связки причины и следствия: впишите подходящую — ответ проверится автоматически.", [
   gap("Prügi tasub sorteerida, ___ segaprügi äravedu on kallim.", ["sest", "kuna"], None, "Причина → sest / kuna."),
   gap("Elanikud sorteerivad hoolikalt. ___ on nende prügiarve väiksem.", ["Seetõttu", "Seepärast", "Seega", "seetõttu", "seepärast", "seega"], None, "Следствие → seetõttu / seepärast; глагол «on» сразу после связки."),
   gap("___ sorteerimisele saab pakenditest teha uusi tooteid.", ["Tänu", "tänu"], None, "tänu + аллатив (-le): tänu sorteerimisele — благодаря сортировке (положительная причина)."),
   gap("Prügiauto ei käinud kaks nädalat, ___ tekkis hoovis ebameeldiv lõhn.", ["mistõttu"], None, "mistõttu — «из-за чего»: вводит следствие и стоит после запятой."),
   gap("Vale sorteerimise ___ võib ühistu saada trahvi.", ["tõttu", "pärast"], None, "Послелог с родительным: vale sorteerimise tõttu — из-за неправильной сортировки (отрицательная причина)."),
 ]),
 "d011": ("Устойчивые сочетания уровня B2: выберите правильный вариант.", [
   mc("Koolid annavad suulistele esitlustele rohkem ___.", ["tähtsust", "tähtsus", "tähtis"], 0, "tähtsust andma — придавать значение; объект в частичном падеже."),
   mc("Arutelu lõpus ___ me ühisele järeldusele.", ["jõudsime", "tulime", "saime"], 0, "järeldusele jõudma — прийти к выводу."),
   mc("Tehnoloogia ___ hariduses üha suuremat rolli.", ["mängib", "teeb", "annab"], 0, "rolli mängima — играть роль."),
   mc("Õpilane peab allikaid ___.", ["kontrollima", "kontrollida", "kontrollides"], 0, "pidama (быть должным) + ma-инфинитив: peab kontrollima."),
   mc("Õpetajad on selle probleemi pärast ___.", ["mures", "murelikult", "muret"], 0, "mures olema — беспокоиться: olen mures (millegi pärast)."),
 ]),
 "d013": ("Фразы для письма-предложения: впишите пропущенное слово.", [
   gap("Teen ___ hoov korda teha.", ["ettepaneku"], None, "ettepanekut tegema → завершённое «вношу предложение»: teen ettepaneku + da-инфинитив."),
   gap("Olen ___, et prügikastide ümbrus on räpane.", ["märganud"], None, "Olen märganud, et … — Я заметил(а), что … (перфект с -nud)."),
   gap("Selle ___ oleks see, et lapsed saaksid turvaliselt mängida.", ["eeliseks"], None, "eelis → eeliseks (транслатив): «преимуществом было бы то, что …»."),
   gap("Palun ___ seda küsimust järgmisel üldkoosolekul.", ["arutada", "arutage"], None, "Официальная просьба: Palun arutada (da-инфинитив) или вежливое повелительное: Palun arutage."),
   gap("Olen valmis talgute korraldamisel kaasa ___.", ["lööma"], None, "kaasa lööma — принять участие; valmis + ma-инфинитив."),
 ]),
}

# Пункт 5 урока 1: вместо простого порядка слов — словообразование (нужно для чтения и письма B2).
D001_GRAMMAR = {"type": "grammar", "minutes": 6, "title": "Sõnamoodustus",
 "rule_ru": "Словообразование расширяет словарь без зубрёжки: -ja — деятель (pooldama → pooldaja); -mine — процесс (kohanema → kohanemine); -us/-kus — свойство (tootlik → tootlikkus, vastutav → vastutus); -lik/-ne — прилагательное (üksildus → üksildane, tervis → tervislik).",
 "tasks": [
  gap("Kaugtöö ___ (pooldama → kes?) rõhutavad aja kokkuhoidu.", ["pooldajad"], None, "-ja + мн. ч.: pooldaja → pooldajad."),
  gap("Kodus on ___ (tootlik → omadus) sageli sama suur kui kontoris.", ["tootlikkus"], None, "tootlik → tootlikkus (свойство, -kus с удвоением k)."),
  gap("Uue töötaja ___ (kohanema → protsess) võtab aega.", ["kohanemine"], None, "Процесс: kohane- + mine = kohanemine."),
  gap("Juhid kardavad, et kontrolli ___ (kaduma → protsess) vähendab vastutustunnet.", ["kadumine"], None, "kadu- + mine = kadumine (исчезновение)."),
  gap("Kodus töötamine võib olla ___ (üksildus → milline?).", ["üksildane"], None, "Прилагательное на -ne: üksildus → üksildane."),
 ]}

# Живое аудирование: настоящие передачи ERR (ссылка; без автопроверки).
JUPITER = {"type": "external", "minutes": 10, "optional": True, "title": "Lisaks: päris raadio (ERR Jupiter)",
 "url": "https://jupiter.err.ee",
 "instruction_ru": "Необязательно, если есть время. Откройте ERR Jupiter → Raadio → Vikerraadio и включите короткий выпуск новостей «Päevakaja» или любую передачу по теме урока. Послушайте 5–10 минут без субтитров и запишите 3 факта, которые вы поняли. Затем прослушайте ещё раз и проверьте себя. Автопроверки здесь нет: это тренировка на живой речи с нормальной скоростью."}
