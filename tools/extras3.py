# -*- coding: utf-8 -*-
# Аудирование как на экзамене (отзыв Renat, 26.11.2026): вместо отдельных предложений —
# короткие диалоги 30–40 с с вопросами; длинный текст 5–8 минут; выбор голоса.
from lessons_01_07 import mc, tf

def short(transcript, tasks):
    return {"type": "listening", "minutes": 5, "title": "Lühidialoog", "plays": 2,
            "instruction_ru": "Короткий диалог (30–40 секунд), как в первых заданиях экзамена. Сначала прочитайте вопросы, потом слушайте. Расшифровку откройте только после проверки.",
            "transcript": transcript, "tasks": tasks}

SHORT = {
 "d001": short(
  "Naine: Kas sa kuulsid juba? Alates jaanuarist võime kolm päeva nädalas kodust töötada.\n"
  "Mees: Kuulsin küll, aga mulle tundub, et see ei ole kõigile hea uudis. Mul on kodus väike laps ja keskenduda on peaaegu võimatu.\n"
  "Naine: Sel juhul ei pea sa ju kodust töötama. Juhataja ütles, et igaüks võib ise valida.\n"
  "Mees: Tõsi. Siis tulen kontorisse esmaspäeval, kolmapäeval ja neljapäeval. Aga kuidas koosolekutega jääb?\n"
  "Naine: Need jäävad kolmapäevale, kui kõik on kohal.", [
  mc("Mitu päeva nädalas võib alates jaanuarist kodust töötada?", ["kaks", "kolm", "viis"], 1, "«kolm päeva nädalas kodust töötada»."),
  mc("Miks mees kahtleb?", ["Tal on kodus väike laps.", "Tal ei ole kodus arvutit.", "Ta elab kontori lähedal."], 0, "«Mul on kodus väike laps ja keskenduda on peaaegu võimatu»."),
  mc("Millal toimuvad koosolekud?", ["esmaspäeval", "kolmapäeval", "neljapäeval"], 1, "«Need jäävad kolmapäevale» — переносятся/остаются на среду."),
 ]),
 "d002": short(
  "Naine: Vabandage, kas buss number kakskümmend kaks peatub siin?\n"
  "Mees: Tavaliselt küll, aga teetööde tõttu peatub ta praegu järgmises peatuses, umbes kolmesaja meetri kaugusel.\n"
  "Naine: Ahah. Ja millal järgmine buss tuleb?\n"
  "Mees: Sõiduplaani järgi kell kaheksateist kakskümmend, aga õhtuti hilinevad bussid sageli viis-kuus minutit.\n"
  "Naine: Aitäh! Kas piletit saab bussis osta?\n"
  "Mees: Ei saa. Kaardiga tuleb lihtsalt validaatorit puudutada.", [
  mc("Miks buss praegu siin ei peatu?", ["teetööde tõttu", "streigi tõttu", "õnnetuse tõttu"], 0, "«teetööde tõttu» — из-за дорожных работ."),
  mc("Millal tuleb järgmine buss sõiduplaani järgi?", ["kell 18.02", "kell 18.20", "kell 19.20"], 1, "«kaheksateist kakskümmend» = 18.20. Ловушка: kaksteist (12) и kakskümmend (20)."),
  mc("Kuidas sõidu eest maksta?", ["juhile sularahas", "kaardiga validaatoris", "mobiilirakendusega"], 1, "«Kaardiga tuleb lihtsalt validaatorit puudutada»."),
 ]),
 "d003": short(
  "Mees: Tere, helistan seoses tellimusega, mis jõudis eile kohale. Jope on mulle kahjuks väike.\n"
  "Naine: Kahju kuulda. Kas soovite selle suurema vastu vahetada või raha tagasi saada?\n"
  "Mees: Pigem vahetada. Kas see on tasuta?\n"
  "Naine: Esimene vahetus on tasuta. Peate lihtsalt jope neljateistkümne päeva jooksul pakiautomaati viima. Uue jope saadame siis, kui oleme vana kätte saanud.\n"
  "Mees: Aga kui suuremat suurust enam ei ole?\n"
  "Naine: Siis tagastame raha viie tööpäeva jooksul.", [
  mc("Mis on probleem?", ["Jope on katki.", "Jope on liiga väike.", "Jope on vale värvi."], 1, "«Jope on mulle kahjuks väike»."),
  mc("Millal saadab pood uue jope?", ["kohe", "kui pood on vana jope kätte saanud", "14 päeva pärast"], 1, "«Uue jope saadame siis, kui oleme vana kätte saanud»."),
  tf("Kui suuremat suurust ei ole, saab klient raha tagasi viie tööpäeva jooksul.", True, "«tagastame raha viie tööpäeva jooksul»."),
 ]),
 "d005": short(
  "Naine: Perearstikeskus, tere.\n"
  "Mees: Tere. Mul on juba nädal aega köha ja palavik ei lange. Kas saaksin arsti juurde tulla?\n"
  "Naine: Arsti vabad ajad on alles järgmisel nädalal, aga pereõde saab teid vastu võtta juba homme kell üheksa.\n"
  "Mees: Sobib. Kas pean midagi kaasa võtma?\n"
  "Naine: Ainult isikut tõendava dokumendi. Ja kui palavik tõuseb üle kolmekümne üheksa kraadi, helistage kohe perearsti nõuandeliinile.", [
  mc("Kui kaua on mehel köha olnud?", ["üks päev", "nädal aega", "kuu aega"], 1, "«Mul on juba nädal aega köha» — уже неделю."),
  mc("Kelle vastuvõtule mees homme läheb?", ["perearsti", "pereõe", "apteekri"], 1, "«pereõde saab teid vastu võtta juba homme»."),
  mc("Mida teha, kui palavik tõuseb üle 39 kraadi?", ["tulla kohe kohale", "helistada nõuandeliinile", "võtta haigusleht"], 1, "«helistage kohe perearsti nõuandeliinile» — консультационная линия семейного врача (в Эстонии 1220)."),
 ]),
 "d006": short(
  "Mees: Vabandust, aga sellesse konteinerisse ei tohi pappkaste panna. See on ainult pakendite jaoks.\n"
  "Naine: Tõesti? Ma arvasin, et papp on ka pakend.\n"
  "Mees: Loogiline küll, aga meie majas kogutakse paberit ja pappi eraldi. Sinine konteiner on seal nurga taga.\n"
  "Naine: Ah, ma ei olnud seda märganudki. Aga kuhu panna vanad patareid?\n"
  "Mees: Need viige poodi. Peaaegu igas suuremas poes on patareide kogumiskast.", [
  mc("Mis oli naise viga?", ["Ta pani papi pakendikonteinerisse.", "Ta viskas patareid prügikasti.", "Ta jättis prügi ukse taha."], 0, "«sellesse konteinerisse ei tohi pappkaste panna. See on ainult pakendite jaoks»: картон положили в контейнер для упаковки."),
  mc("Mis värvi on paberi ja papi konteiner?", ["kollane", "sinine", "pruun"], 1, "«Sinine konteiner on seal nurga taga»."),
  mc("Kuhu tuleb vanad patareid viia?", ["prügilasse", "poodi", "pakendikonteinerisse"], 1, "«Need viige poodi» — в магазинах есть ящики для батареек."),
 ]),
 "d008": short(
  "Naine: Kas sa lugesid kooli kirja? Alates järgmisest kuust peavad telefonid terve koolipäeva kapis olema.\n"
  "Mees: Lugesin. Ausalt öeldes olen sellega nõus. Meie poeg istus vahetundides ainult telefonis.\n"
  "Naine: Mina kardan, et me ei saa siis lapsega ühendust. Ta käib pärast kooli trennis.\n"
  "Mees: Kirjas oli ju öeldud, et pärast viimast tundi võivad nad telefoni kätte võtta. Ja kiire asja korral saab helistada kooli sekretärile.", [
  mc("Mis muutub järgmisest kuust?", ["Telefonid peavad olema terve koolipäeva kapis.", "Telefonid on keelatud ainult tundides.", "Õpilased ei tohi telefoni kooli tuua."], 0, "«peavad telefonid terve koolipäeva kapis olema» — весь учебный день, не только на уроках."),
  mc("Miks naine muretseb?", ["Laps hilineb trenni.", "Lapsega ei saa ühendust.", "Kapid ei ole turvalised."], 1, "«Mina kardan, et me ei saa siis lapsega ühendust»: не смогут связаться с ребёнком."),
  mc("Mida teha kiire asja korral?", ["helistada lapsele", "helistada sekretärile", "kirjutada õpetajale"], 1, "«kiire asja korral saab helistada kooli sekretärile»."),
 ]),
 "d009": short(
  "Mees: Vaatasin seda maja Raplamaal. Hind on poole väiksem kui meie korteril Tallinnas.\n"
  "Naine: Kõlab hästi, aga mõtle, kui kaua sa iga päev tööle sõidaksid.\n"
  "Mees: Ma käiksin kontoris ainult kaks korda nädalas. Rongiga on see veidi üle tunni.\n"
  "Naine: Ja lasteaed? Kuulsin, et seal on pool aastat järjekorda.\n"
  "Mees: See on tõsi. Võib-olla peaksime kõigepealt seal suve veetma ja siis otsustama.", [
  mc("Kui palju maksab maja võrreldes nende korteriga?", ["sama palju", "poole vähem", "kaks korda rohkem"], 1, "«Hind on poole väiksem» — вдвое меньше."),
  mc("Mitu korda nädalas käiks mees kontoris?", ["üks", "kaks", "viis"], 1, "«Ma käiksin kontoris ainult kaks korda nädalas» (условное наклонение: ходил бы)."),
  mc("Mida mees lõpuks ette paneb?", ["kohe maja osta", "veeta seal enne otsustamist suvi", "otsida lasteaeda Tallinnas"], 1, "«peaksime kõigepealt seal suve veetma ja siis otsustama» — сначала провести там лето, потом решать."),
 ]),
 "d010": short(
  "Naine: Kas sa tuled laupäeval Kumusse kaasa? Seal avati uus näitus.\n"
  "Mees: Tahaksin küll, aga mul on juba piletid õhtusele kontserdile. Mis kell sa minna plaanid?\n"
  "Naine: Mõtlesin kella kaheteistkümne paiku. Kontsert algab ju alles seitsmest.\n"
  "Mees: Siis sobib. Aga kaua ma jääda ei saa, sest kell viis pean koeraga jalutama minema.\n"
  "Naine: Pole hullu, kaks-kolm tundi piisab täiesti.", [
  mc("Kuhu nad laupäeval lähevad?", ["kinno", "näitusele", "teatrisse"], 1, "«Kumusse … Seal avati uus näitus» — Kumu — художественный музей, идут на выставку."),
  mc("Mis kell algab kontsert?", ["kell 12", "kell 17", "kell 19"], 2, "«algab alles seitsmest» — с семи (вечера) = 19."),
  mc("Miks mees ei saa näitusel kaua olla?", ["Ta peab koeraga jalutama.", "Ta peab tööle minema.", "Ta on väsinud."], 0, "«kell viis pean koeraga jalutama minema»."),
 ]),
 "d011": short(
  "Õpetaja: Mari, su essee oli väga sujuv, aga mõned faktid ei klapi. Kas sa kasutasid tehisintellekti?\n"
  "Õpilane: Jah, ideede kogumiseks, aga teksti kirjutasin ise.\n"
  "Õpetaja: Selles pole midagi halba, aga allikad tuleb alati üle kontrollida. Näiteks Tartu ülikool ei ole asutatud aastal tuhat kuussada nelikümmend kaks, vaid tuhat kuussada kolmkümmend kaks.\n"
  "Õpilane: Oi, see on piinlik. Kas ma saan essee parandada?\n"
  "Õpetaja: Saad. Too see reedeks.", [
  mc("Milleks Mari tehisintellekti kasutas?", ["kogu essee kirjutamiseks", "ideede kogumiseks", "vigade parandamiseks"], 1, "«ideede kogumiseks, aga teksti kirjutasin ise»."),
  mc("Mis oli essees valesti?", ["Tartu ülikooli asutamise aasta", "ülikooli nimi", "linna nimi"], 0, "Ошиблась в годе: 1642 вместо 1632."),
  mc("Millal peab Mari parandatud essee tooma?", ["homme", "reedeks", "järgmisel nädalal"], 1, "«Too see reedeks» — к пятнице (транслатив -ks = срок)."),
 ]),
 "d012": short(
  "Naine: Vabandage, kas rong Tartusse väljub ikka kell seitseteist nelikümmend viis?\n"
  "Mees: Täna kahjuks mitte. Rike on parandatud, aga rong väljub alles kell kaheksateist kümme.\n"
  "Naine: Ma pean Tartus olema hiljemalt pool üheksa.\n"
  "Mees: Siis jõuate. Rong on Tartus kümme minutit kaheksa läbi.", [
  mc("Mis kell väljub rong täna?", ["17.45", "18.10", "18.45"], 1, "«kaheksateist kümme» = 18.10; 17.45 — обычное время."),
  mc("Mis kell peab naine Tartus olema?", ["19.30", "20.10", "20.30"], 2, "«pool üheksa» = половина девятого = 20.30 (не 9.30!)."),
  mc("Millal jõuab rong Tartusse?", ["20.10", "20.30", "18.10"], 0, "«kümme minutit kaheksa läbi» = 10 минут девятого = 20.10."),
 ]),
 "d013": short(
  "Mees: Kas sa tuled homme üldkoosolekule?\n"
  "Naine: Kahjuks ei saa, olen komandeeringus. Kas ma saan kuidagi hääletada?\n"
  "Mees: Saad volitada kedagi teist enda eest hääletama. Kirjuta lihtsalt lühike volitus ja allkirjasta see digitaalselt.\n"
  "Naine: Hea mõte. Kas sa võiksid minu eest hääletada? Ma toetan uue mänguväljaku ehitamist.\n"
  "Mees: Muidugi. Saada volitus mulle täna õhtul e-postiga.", [
  mc("Miks naine koosolekule ei tule?", ["Ta on haige.", "Ta on komandeeringus.", "Ta on puhkusel."], 1, "«olen komandeeringus» — в командировке."),
  mc("Kuidas saab naine hääletada?", ["telefoni teel", "volitusega naabri kaudu", "pärast koosolekut"], 1, "volitama — доверить; volitus — доверенность."),
  mc("Mida naine toetab?", ["uue mänguväljaku ehitamist", "hoovi parkla laiendamist", "prügikastide vahetamist"], 0, "«Ma toetan uue mänguväljaku ehitamist»."),
 ]),
}

# Урок 7: длинный текст (около 5–6 минут при скорости 0,8×) на тему «природа».
D007 = {
 "title": "Eesti mets", "title_ru": "Эстонский лес", "topic": "loodus",
 "goal_ru": "Длинное аудирование (около 5–6 минут), как в последних заданиях экзамена: лекция о лесе, споры о вырубке, право каждого.",
 "vocab": [
  ("metsa majandama", "вести лесное хозяйство", "Metsaomanikul on õigus oma metsa majandada."),
  ("raie", "рубка, вырубка", "Keskkonnakaitsjate arvates on raiet liiga palju."),
  ("liigirikas", "богатый видами", "Vana mets on liigirikkam kui noor."),
  ("haruldane", "редкий", "Vanas metsas elavad haruldased linnud."),
  ("süsinikku siduma", "связывать углерод", "Kiiresti kasvavad puud seovad palju süsinikku."),
  ("taastuma", "восстанавливаться", "Vana metsa taastumiseks kulub sadu aastaid."),
  ("üksmeelel olema", "быть единодушными", "Teadlased ei ole selles küsimuses üksmeelel."),
  ("igameheõigus", "право каждого (свободно находиться в природе)", "Igameheõigus lubab teise inimese metsas liikuda."),
  ("pesitsusaeg", "период гнездования", "Kevadel on lindude pesitsusaeg."),
 ],
 "listening": {"type": "listening", "minutes": 20, "title": "Raadioloeng: Eesti mets", "plays": 2,
  "instruction_et": "Kuulake loengut kaks korda ja vastake küsimustele.",
  "instruction_ru": "Длинный текст: сначала 1 минута на чтение вопросов. Во время первого прослушивания отмечайте ответы, во время второго — проверяйте. Голос (мужской или женский) и скорость можно выбрать.",
  "transcript": "Tere, head kuulajad! Minu nimi on Kati Lepik ja ma olen metsateadlane. Täna räägin teile Eesti metsast: sellest, miks see on meile nii tähtis ja miks selle üle nii palju vaieldakse.\n"
  "Alustame faktidest. Mets katab ligikaudu poole Eesti maismaast. See tähendab, et Eesti on üks metsarikkamaid riike Euroopas. Kõige levinumad puuliigid on mänd, kask ja kuusk. Enamik eestlasi elab metsast vaid mõne kilomeetri kaugusel ning paljude jaoks on metsas käimine osa igapäevaelust: korjatakse marju ja seeni, matkatakse või puhatakse lihtsalt linnamürast.\n"
  "Mets on olnud eestlaste jaoks tähtis juba sajandeid. Rahvaluules on palju lugusid pühadest hiitest ja puudest, mida ei tohtinud raiuda. Ka tänapäeval peavad paljud inimesed metsa kohaks, kus saab rahuneda ja mõtteid koguda. Küsitlused näitavad, et enamik eestlasi peab metsa üheks Eesti suurimaks väärtuseks, isegi kui nad ise metsas väga tihti ei käi.\n"
  "Mets ei ole aga ainult puhkusekoht. Metsasektor annab tööd kümnetele tuhandetele inimestele, eriti maapiirkondades. Puitu kasutatakse ehituses, mööblitööstuses ja energia tootmisel. Eesti puitmajad on hinnatud ka välismaal ning nende eksport on viimastel aastatel kasvanud.\n"
  "Just siin algab vaidlus. Ühelt poolt on metsaomanikel ja ettevõtetel õigus metsa majandada ehk puid raiuda ja müüa. Teiselt poolt muretsevad keskkonnakaitsjad, et raiet on liiga palju. Nende hinnangul jääb järjest vähem vanu metsi, kus elavad haruldased linnud, samblikud ja putukad. Kui vana mets maha võetakse, kulub selle taastumiseks sadu aastaid.\n"
  "Metsandusettevõtted vastavad, et iga raiutud ala asemele istutatakse uus mets ning seadus kohustab seda tegema. Nende sõnul on noor mets kliima jaoks isegi kasulik, sest kiiresti kasvavad puud seovad palju süsinikku. Teadlased ei ole selles küsimuses üksmeelel. Mitmed uuringud näitavad, et vana mets talletab süsinikku ka pinnasesse ja on liigirikkam, mistõttu ei saa noort metsa vanaga võrdsustada.\n"
  "Metsa mõjutab ka kliimamuutus. Talved on muutunud soojemaks ja lumi püsib maas lühemat aega. Sagenenud tormid murravad puid ning soojemas kliimas levivad kiiremini kahjurid, näiteks kuuse-kooreürask, mis võib lühikese ajaga hävitada suuri kuusikuid. Kuivadel suvedel kasvab metsatulekahjude oht. Seetõttu soovitavad teadlased istutada senisest rohkem erinevaid puuliike, sest segamets peab muutustele paremini vastu kui ühe liigi istandik.\n"
  "Oluline küsimus on ka see, kes metsa omab. Umbes pool Eesti metsast kuulub riigile ja seda majandab riigimetsa majandamise keskus. Ülejäänud mets kuulub eraomanikele, keda on kokku üle saja tuhande. Paljudel neist on vaid mõni hektar metsa, mille nad on pärinud vanematelt või vanavanematelt. Väikeomanikud ei tea sageli, kuidas oma metsa hoolikalt majandada, ning müüvad raieõiguse esimesele pakkujale. Seepärast pakuvad metsaseltsid neile tasuta nõustamist.\n"
  "Mida siis teha? Minu arvates ei ole lahendus raie täielik keelamine, sest see kahjustaks maapiirkondade majandust. Küll aga peaksime rohkem kaitsma kõige väärtuslikumaid vanu metsi ja tegema otsuseid teadusandmete põhjal. Oluline on ka see, et kohalikud elanikud saaksid kaasa rääkida, kui nende kodu lähedal metsa raiutakse. Paljudes valdades on juba hakatud korraldama avalikke arutelusid, kus metsaomanikud, ametnikud ja elanikud otsivad koos kompromissi.\n"
  "Ka igaüks meist saab midagi ära teha. Kui ostate puidust mööblit või ehitusmaterjali, uurige, kas sellel on säästva metsanduse sertifikaat. Metsas käies järgige lihtsaid reegleid: ärge tehke lõket selleks mitte ettenähtud kohas, ärge jätke prügi maha ja hoidke kevadel koerad rihma otsas, sest siis on lindude pesitsusaeg.\n"
  "Eestis kehtib nii-nimetatud igameheõigus. See tähendab, et teise inimese metsas võib vabalt liikuda ning korjata marju ja seeni, kui omanik ei ole seda keelanud ega ala piiranud. Paljud välismaalased imestavad selle õiguse üle. Kuid õigusega kaasneb ka vastutus: mets peab alles jääma ka meie lastele ja lastelastele.\n"
  "Aitäh kuulamast! Järgmises saates räägime sellest, kuidas kliimamuutused mõjutavad Eesti loodust.",
  "tasks": [
   mc("Kui suure osa Eesti maismaast katab mets?", ["umbes veerandi", "umbes poole", "umbes kolm neljandikku"], 1, "«Mets katab ligikaudu poole Eesti maismaast»."),
   mc("Millised on Eestis kõige levinumad puuliigid?", ["mänd, kask ja kuusk", "tamm, vaher ja pärn", "kuusk, saar ja lepp"], 0, "«Kõige levinumad puuliigid on mänd, kask ja kuusk» — сосна, берёза и ель."),
   mc("Mille pärast muretsevad keskkonnakaitsjad?", ["Vanu metsi jääb järjest vähemaks.", "Puit on liiga kallis.", "Metsa ei istutata enam juurde."], 0, "«jääb järjest vähem vanu metsi»."),
   mc("Miks peavad metsandusettevõtted noort metsa kliimale kasulikuks?", ["Noor mets talletab süsinikku pinnasesse.", "Kiiresti kasvavad puud seovad palju süsinikku.", "Noores metsas elab rohkem linde."], 1, "Это аргумент компаний; про почву говорят исследования о старом лесе — ловушка."),
   tf("Teadlased on üksmeelel, et noor mets on kliimale kasulikum kui vana.", False, "«Teadlased ei ole selles küsimuses üksmeelel»."),
   mc("Milline on lektori seisukoht?", ["Raie tuleks täielikult keelata.", "Tuleks kaitsta väärtuslikke vanu metsi ja otsustada teadusandmete põhjal.", "Raiet tuleks majanduse huvides suurendada."], 1, "«ei ole lahendus raie täielik keelamine … peaksime rohkem kaitsma kõige väärtuslikumaid vanu metsi»."),
   mc("Mis aitab teadlaste sõnul metsal kliimamuutustele paremini vastu pidada?", ["ühe puuliigi istandik", "erinevate puuliikide istutamine", "vähem raiet talvel"], 1, "«segamets peab muutustele paremini vastu kui ühe liigi istandik»."),
   mc("Kellele kuulub umbes pool Eesti metsast?", ["riigile", "välismaistele ettevõtetele", "kohalikele omavalitsustele"], 0, "«Umbes pool Eesti metsast kuulub riigile»; остальное — частным владельцам."),
   tf("Kevadel tuleb metsas koerad rihma otsas hoida, sest siis on lindude pesitsusaeg.", True, "«hoidke kevadel koerad rihma otsas, sest siis on lindude pesitsusaeg»."),
   tf("Igameheõigus lubab korjata marju ka siis, kui omanik on ala piiranud.", False, "Можно, «kui omanik ei ole seda keelanud ega ala piiranud» — если владелец НЕ запретил и НЕ огородил."),
   mc("Millest räägitakse järgmises saates?", ["metsatulekahjudest", "kliimamuutuste mõjust Eesti loodusele", "puitmajade ekspordist"], 1, "Последняя фраза: «Järgmises saates räägime sellest, kuidas kliimamuutused mõjutavad Eesti loodust»."),
  ]},
}
