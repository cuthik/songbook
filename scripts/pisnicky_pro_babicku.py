#!/usr/bin/python
# -*- coding: utf-8 -*- 

## Documentation for file
#
# More details. 
#
# @file pisnicky_pro_babicku.py
# @author cuto <Jakub.Cuth@cern.ch>
# @date 2014-08-07

from songbook import *

## Documentation for main
#
# More details. 
if __name__ == '__main__' :
    sbk = songbook()

    # filling songbook
    sbk.SetDataDir("./data/")

    sbk.AddSong_youtube_lyrics_list([
[
"Vlasta Redl",
"Sbohem Galanecko", 
"https://www.youtube.com/watch?v=b2YdEwOKAdM",
"""
Sbohem, galánečko, já už musím jí - ti. 2x
Kyselé vínečko, kyselé vínečko
podalas' mi k pití. 2x

2. [:Sbohem, galánečko, rozlučme sa v pánu, :]
[:kyselé vínečko, kyselé vínečko
podalas' mi v džbánu. :]

3. [:Ač bylo kyselé, přeca sem sa opil, :]
[:eště včil sa stydím, eště včil sa stydím,
co sem všecko tropil, :]

4. [:Ale sa nehněvám, žes mňa ošidila, :]
[:to ta moja žízeň, to ta moja žízeň,
ta to zavinila. :]
"""
],
[
"Lidova pisn",
"Rez Rez Rez",
"https://www.youtube.com/watch?v=4lNbBfnHr6E",
"""
Rež rež rež, drobná rež, prečo sa ty moja milá za mnú dreš
Rež rež rež, drobňúčká, prečo sa ty moja milá malučká.

Háj, háj, háj háj, zelený háj, na mňa sa moja milá nespoléháj.
Budeš li sa spoléhati, eej veru budeš banovati.

Ej, chrást, ej, chrást zelený chrást, ej daj ně bože něčo ukrásť,
Lebo koňa lebo voly, ej lebo dievča po mej voli.

/:Po potoce chodila, na kačeny volala:/
/:Kač, kač kač, kačena, nasypem ti zeleného jačmeňa.:/

/:Já jačmeňa nejídám, ošidit sa ti nedám:/
/:Falešné oči máš, za jinýma, za jinýma pozeráš:/

/:Za jinýma každý deň, za mnú jednú za týdeň.:/
/:To ešče v sobotu, keď má dievča, keď má dievča robotu.:/

/:Keď má divča, keď má sac, ty jí prijdeš zavadzac:/
/:A keď má buchty pect, ty jí přindeš, ty jí přindeš šecky zesc:/

Hopsa s ňú pod třešňu,
nech sa jí ty čerešnice zatřesu.
Hopsa s ňú, stará je,
zuby sa jí drkocajú, ráda je.
"""
],
[
"Lidova pisen",
"U muziky su ja chlap",
"https://www.youtube.com/watch?v=2sI3VQ7sp-g",
"""
U muziky su já chlap,
doma koně žerú žlab.absA já povím tatovi,
dajte koně rasovi.

Z kože budú remeně,
z kostí budú hrebeně.
Z hlavy bude hrkadlo,
z očí bude zrkadlo.

Husárovi dobre je,
nic nerobí len pije.
Štyry groše na deň má,
eště z toho milej dá.
"""
],
[
"Lidova pisen",
"Mela jsem ja muza",
"https://www.youtube.com/watch?v=KjrRH3rhaRE",
"""
Měla sem já muža,
ten sa ježa bál.
A on po tri noci,
doma neležal.

Jak sem ho dom dostala,
do měkka ho vecpala.
Tu mně mužu lež,
dojde na ťa jež.

Měla sem já muža...abs
Jak sem ho dom dostala...
"""
],
[
"Lidova pisen",
"U Hradista na travnicku",
"https://www.youtube.com/watch?v=cj8dYhGmHHI",
"""
U Hradišťa na trávníčku,
stavjajú tam šibeničku.
Pro koho tá šibenička,
pro švarného šohajíčka

Šibenička rovno stójí,
šohaj sa jí nic nebójí.
Nebójí sa není vinen,
celá obec stójí při něm.

Celá obec, všeci páni,
že je šohaj malovaný.
Celá obec aj dědina,
aj tá jeho roztomilá.
"""
],
[
"Lidova pisen",
"Vinecko bile",
"https://www.youtube.com/watch?v=Ge4hZkjph6I",
"""
Vínečko bílé,
jsi od mej milej,
budu ta pít,
co budu žít,
vínečko bílé.

Vínečko rudé,
jsi od tej druhej,
budu ta pít,
co budu žít,
vínečko rudé.

Vínečka obě,
frajárky moje,
budu vás pít,
co budu žít,
vínečka obě.
"""
],
[
"Lidova pisen",
"Kdyz jsem sel z Hradista",
"https://www.youtube.com/watch?v=y8jQCsAoCQA",
"""
Když sem šel z Hradišťa z požehnání,
potkal sem děvčicu z nenadání.
Potkala mě, neznala mě,
červené jablůčko dávala mně.

Že sem byl šohajek nerozumný,
vzal sem si jablúčko z ručky její.
To jablúčko je kyselé,
a moje srdénko zarmúcené.

Neber si šohajku, co kdo dává,
z takových jablúček bolí hlava.
Hlava bolí, srdce svírá,
všecko cos miloval, konec mívá.
"""
],
[
"Lidova pisen",
"Isiel Macek do Malacek",
"https://www.youtube.com/watch?v=CzUOfBmqdsw",
"""
Išiel Macek do Malacek, šošovicku mlácic,
zabudol si cepy doma , mosel sa on vrácic.

Eeeeeeeeej Macejko macejko ko- ko-ko-ko,
zahraj mi an cenko,ko-ko-ko-ko.
Na tú cenkú strunú. nu-nu-nu-nu,
ej, dzunu,dzunu,dzunu,nu-nu-nu-nu.

Zahral Macek dzunu, dzunu
potom prestal hráci,
husle sa mu rozsypaly,
cepom po nich mlácil.

Eeeeeeeeej Macejko macejko ko- ko-ko-ko,
zahraj mi an cenko,ko-ko-ko-ko.
Na tú cenkú strunú. nu-nu-nu-nu,
ej, dzunu,dzunu,dzunu,nu-nu-nu-nu.
"""
],
[
"Lidova pisen",
"Chodila po poli",
"https://www.youtube.com/watch?v=rkcryLLmtkw",
"""
Chodila po poli,
trhala kúkolí.
Plakala, volala,
že ju hlava bolí.

Chodila po hájku,
trhala polajku.
Plakala, volala,
prídi k nám šohajku.
"""
],
[
"Lidova pisen",
"Nepij Jano, nepij vodu",
"https://www.youtube.com/watch?v=ZdIoylHFZPQ",
"""
Nepij, Jano, nepij vodu, voda je ti len na škodu,


napij sa ty radšej vína, to je dobrá medecína.

Prečo sa ty za mnú vláčíš, keď ma ani něopáčíš
ani večer, ani ráno ať už si ty sprostý Jano.

Svobodnému není dobre, oženit sa není dobre
lebo žena ťažké jarmo, musíš uživit nadarmo.

Pěknú ženu nechcem míti, lebo je s ňú ťažké žíti
keby mně ju druhý lúbil, co by som já smutný robil
"""
],
[
"Lidova pisen",
"Esce som sa neozenil",
"https://www.youtube.com/watch?v=4br3HatyZfU",
"""
Ešče som sa neoženil, už ma žena bije.
a ja som si naruboval tri dubove kyje.
/:S jedzim budzem zenu bici a stim druhym dzeci, dzeci, moje dzeci.
A s tim tretim kyja kyjačiskom, podzem na zálety.:/

Kam ty zajdeš, aj já zajdu, podzeme do mlýna.
Opítáme se mlynára, co že za novina.
/:Kolečka sa otáčajú, žitečko sa mele, mele, mele, mele.
Moja milá sa vydává, podzem na veselie.. :/
"""
],
[
"Lidove pisne",
"Perina ma styri rozky",
"https://www.youtube.com/watch?v=viKYA_KeQRU",
"""
Perina má štyry rožky pod perinu štyry nožky.
Perina má štyry rožky pod perinu štyry nožky.
Ej javor,javor,javor zelený milej pod okénkom saděny.
Ej javor,javor,javor zelený milej pod okénkom saděny.

Rád ťa vidím pri posteli ešče račej na posteli.
Rád ťa vidím pri posteli ešče račej na posteli.
Ej javor,javor,javor,zelený milej pod okénkom saděny.
Ej javor,javor,javor,zelený milej pod okénkom saděny.

Cukor jedla kávu pila aby bola pěkná bílá.
Cukor jedla kávu pila aby bola pěkná bílá.
Ej javor,javor,javor zelený milej pod okénkom saděny.
Ej javor,javor,javor zelený milej pod okénkom saděny.

Cukor,káva něpomáhá brůžko sa jej rozrůstáva.
Cukor,káva něpomáhá brůžko sa jej rozrůstáva.
Ej javor,javor,javor zelený milej pod okénkom saděny.
Ej javor,javor,javor zelený milej pod okénkom saděny.
"""
],
[
"Lidova pisen",
"Po kalisku",
"https://www.youtube.com/watch?v=Epv3DIbwghI",
"""
Pokalíšku, pokalíšku, pokalíšku, pokalíšku.
/:Pokalíšku dáme, pak si zazpíváme.
Po kalíšku, po kalíšku.:/
/:Hoja hoj, hoja hoj, alkohol je síly zdroj. Hoja hoj, hoja hoj, abstinenci boj!:/
"""
],
[
"Lidova pisen",
"Zaspala nevesta",
"https://www.youtube.com/watch?v=8sSijAn_8U0",
"""
/:Zaspala nevěsta v zelenej dubině:/
Prišla pro ňú mamka, prišla pro ňú mamka,
vstaň nevěsto hore, vstaň nevěsto hore.

/:Vstaň nevěsto hore, snad sas už vyspala.:/
Běž podojit krávy, běž podojit krávy.
Které sa dostala, které si dostala.

/:Šak byste věděli, že su sirotečka:/
Že vám nedovedu, že vám nedovedu,
krávy do dvorečka, krávy do dvorečka.
"""
],
[
"Lidova pisen",
"Vesela je dedina",
"https://www.youtube.com/watch?v=KyzdreMqnIw",
"""
Veselá je dědina, kde sa milá zrodila.
Veselá je dědina, kde sa milá zrodila.

A ještě je veselejší, kde se zrodil nejmilejší.
A eště je veselejší, kde sa zrodil, najmilejší.

Estli ty mňa ráda máš, rataj pole, kde co máš.
Estl ty mňa ráda máš, rataj pole, kde co máš.

Prodám pole vinohrady, a vyplať dám ho z tej vojny.
Prodám pole, vinohrady a vyplať dám ho z tej vojny.

Vinohrady neprodám, dobré vínko ráda mám.
Vinohrady neprodám, dobré vínko ráda mám.

Dobré vínko ráda piju, kořalenku nevyleju.
Dobré vínko ráda piju, kořalenku nevyleju.
"""
],
[
"Lidova pisen",
"Ked som ja bol mlady",
"https://www.youtube.com/watch?v=tMMxPSc9bdQ",
"""
Keď som já bol mladý, tak 62 ročný, bolo mi na ženěnie. Vzal som si já ženu, nemladú nestarú, mal som s ňou len trapenie.
|: Očko mala len jedno, aj na to mala belmo, (hop šup) vlasy mala sivé, nohy mala krivé, zuba ani jedneho :|

|: to něbolo šecko, mal som s ňou aj děcko, aj to bolo krpaté :|
|: Očko malo len jedno, aj na to malo belmo, (hop šup), vlasy malo sivé, nohy malo krivé, zuba ani jedného :|

Keď som išel, vyšel, z nohavic mi vyšel šáteček vyšívaný. Všeci sa mi smiali, že mám taký malý šáteček vyšívaný.
|: Očko mala len jedno, aj na to mala belmo,(hop šup) vlasy mala sivé, nohy mala krivé, zuba ani jedneho :|)))
"""
],
[
"Lidova pisen",
"Oci oci cierne oci",
"https://www.youtube.com/watch?v=35aApVTDUYI",
"""
A                     
Oči, oči, čierne oči
E  A     E A  H7E    
Čo mám s vami robiť
A                      
Oči, oči, čierne oči,
E  A     E A  H7E    
Čo mám s vami robiť
E7     A     D      H     
Nechcú spať, nechcú spať
H7     E7    A       
Len po fraji chodiť
E7     A     D      H     
Nechcú spať, nechcú spať
H7     E7    A       
Len po fraji chodiť

A ja som ti povedala
Povedala dávno
A ja som ti povedala
Povedala dávno
Nechodievaj do nás
Lebo chodíš darmo
Nechodievaj do nás
Lebo chodíš darmo

Darmo chodíš, darmo chodíš
Darmo do nás kráčaš
Darmo chodíš, darmo chodíš
Darmo do nás kráčaš
Darmo si čižmičky
Vo vodički zmáčaš
Darmo si čižmičky
Vo vodički zmáčaš
"""
],
[
"Lidova pisen",
"Kdo ma pocernu galanku",
"https://www.youtube.com/watch?v=Cqa99Myr8z0",
"""
kdo má počernú galánku
ligotala sa vězdička, anděl moj.
|: Kdo má počernú galánku,
ten má pokojnú myšlenku,
ligotala sa vězdička, anděl moj. :|

Ale já mám popelavú,
ligotala sa vězdička, anděl moj.
|: Ale já mám popelavú,
a ta trápí moju hlavu,
ligotala sa vězdička, anděl moj. :|

Milá, milá, milušičká,
ligotala sa vězdička, anděl moj.
|: Milá, milá, milušičká,
daj ně bozkat svoje líčka,
ligotala sa vězdička, anděl moj. :|

Priložíme líčko k líčku,
ligotala sa vězdička, anděl moj.
|: Priložíme líčko k líčku,
pozdravíme večerničku,
ligotala sa vězdička, anděl moj. :|
"""
],
[
"Lidove pisen",
"Ceresnicky ceresnicky",
"https://www.youtube.com/watch?v=GJIfr1qpYUY",
"""
Čerešničky, čerešničky, čerešně,
vy ste sa mně rozsypaly na cestě.

Kdo vás najde, ten vás posberá,
já som mala včera večer frajara.

Bol to frajar malovaný jak růža,
toho bych si vyvolila za muža.
"""
],
[
"Lidova pisen",
"Cervena ruzicko",
"https://www.youtube.com/watch?v=eIoes6AyZDM",
"""
Červená růžičko, proč se nerozvíjíš
Červená růžičko, proč se nerozvíjíš
Proč ty k nám, Pepíčku
Proč ty k nám, Pepíčku, proč ty k nám nechodíš
Proč ty k nám, Pepíčku
Proč ty k nám, Pepíčku, proč ty k nám nechodíš

Já bych k vám rád chodil, ty by jsi plakala
Já bych k vám rád chodil, ty by jsi plakala
Červeným šátečkem
S bílým okraječkem oči utírala
Červeným šátečkem
S bílým okraječkem oči utírala

Proč bych já plakal, když mě nic nebolí
Proč bych já plakal, když mě nic nebolí
Milovali jsme se
Milovali jsme se jako dva holubi
Milovali jsme se
Milovali jsme se jako dva holubi

Jako dva holubi, jako dvě hrdličky
Jako dva holubi, jako dvě hrdličky
Dávali jsme sobě
Dávali jsme sobě slaďoučké hubičky
Dávali jsme sobě
Dávali jsme sobě slaďoučké hubičky
"""
],
[
"Lidova pisen",
"Cize su to kone",
"https://www.youtube.com/watch?v=vxlidesALRA",
"""
Čí že sú to koně, čí že sú to koně ve dvore
Co že s nima žádný, co že s nima žádný neore?
Čí že by, čí že by to byli, moje sú
Oni ma k mej milej, holubence sivej donesú
Čí že by, čí že by to byli, moje sú
Oni ma k mej milej, holubence sivej donesú

Hop koníčky moje, hop koníčky moje do skoku!
Budem ležat milej, holuběnce sivéj, pri boku
Nebudem sa, nebudem sa modlit otčenáš!
Hop, teraz ma milá, holuběnka sivá, pobozkáš
Nebudem sa, nebudem sa modlit otčenáš!
Hop, teraz ma milá, holuběnka sivá, pobozkáš

Tancoval by som, tancovala by som, sama som!
Kup mi, milý, čižmy, kup mi, milý, čižmy, bosá som!
Aj keď mi ty tie čižmičky nekúpíš, nebudem ťa bozkat
Nebudem s tebú spat, uvidíš
Aj keď mi ty tie čižmičky nekúpíš, nebudem ťa bozkat
Nebudem s tebú spat, uvidíš
"""
],
[
"Tri Sestry",
"Venda",
"https://www.youtube.com/watch?v=lzlYdDnOooY",
"""
horkej letní den
před bouřkou
a město
halí těžkej mrak
Venda
vyjíždí sám

má helmu v zápěstí on nezná strach
s bambulí v zánovních Nike trenýrkách
burácí hrom ten záhy zaniká
ve výfuků ránách

Venda, Venda, Venda se svou motorkou
točí plyn a ušklíbá se za holkou
hudrovadlo stačí Venda zahlídnout
má dost síly
dívky kvílí

já na tu chvíli často vzpomínám
jak blázen zastavil
pak na mě sáh

náhle jsem zmámená zůstala stát
kéž by mě chtěl sbalit já chci se dát
dál ulicí s ním jedem do Říčan
všech losů cíl já znám

Venda, Venda, Venda se svou motorkou
točí plyn a ušklíbá se za holkou
hudrovadlo stačí Venda zahlídnout
má dost síly
dívky kvílí

Venda, Venda

Venda, Venda, Venda se svou motorkou
točí plyn a ušklíbá se za holkou
Venda, Venda, Venda holky šílí
Venda, Venda
"""
],
[
"Tri Sestry",
"Mexico",
"https://www.youtube.com/watch?v=yfc7cumzpTY",
"""
Kolem kaktusy
Je horko tak to si
Na hlavu nasadím sombrero grande

Viva Zapata
Mě hoří za pata-
mám v Porto Pueblo rande

Snad má mě ráda
A piňacoláda
Na cestu neškodí když je chlap macho

Do kapsy tortilly
A láhev tequilly
Má milá mi přihřeje nachos

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Strašlivý vedro
A můj mezek Pedro
Klopýtá okolo malého ranče

A to není celý
Taky je skvělý
Že tu slyším výt Komanče

Jsem speedy Gonzalez
Však radši bych zalez
Tam kde je nejbližší kojotí nora

Však nehledě k tomu
Že pospíchám domu
Mě vyhlíží krásná seňora

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Vylétla kulka
Z mé hlavy je půlka
Než jsem spad už bylo od krve poncho

Teď nade mnou stojí
Už pět neděl svoji
Má milá a sousedů Pancho

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá

Mexiko, Mexiko sombrero grande tequila
Donde esta zapateria čeká mě milá
"""
],
[
"Tri Sestry",
"Kovarna I.",
"https://www.youtube.com/watch?v=dkxXwYuFWM4",
"""
Ve středu jsem na Kovárně, ve čtvrtek jsem na Kovárně,
i v pátek jsem na Kovárně, v sobotu zas na Kovárně.
Ve středu jsem na Kovárně, ve čtvrtek jsem na Kovárně,
i v pátek jsem na Kovárně, v sobotu zas na Kovárně.

Můj dědek byl kovář a má bába kovářka,
muj strejda byl notář, moje teta notářka.
Můj táta je kovář a má máma kovářka,
muj brácha je notář a ségra je notářka.

Středa, čtvrtek, pátek, sobota a neděle, každej den jsem na Kovárně,
na Kovárně v Bráníku.

Vilu mám jen malou a v ní kupu dětí,
umím jenom kovat, roky rychle letí,
až já z toho umřu, na krchov mě nesou,
na rakev mi dají půllitr mou milóóóůů.

Středa, čtvrtek, pátek, sobota a neděle, každej den jsem na Kovárně,
na Kovárně v Bráníku.

Rakev mi ozdobí hustou bílou pěnou,
syn se bude sklánět nad mou kovadlinou.
Muj syn bude kovář, jeho žena kovářka
a jejich syn notář, jejich dcera notářka.
Už nebudu kovat, už nebudu kovat,
všichni budou kovat, všichni budou kovat, jen já:

Středa, čtvrtek, pátek, sobota a neděle, každej den jsem na Kovárně,
na Kovárně v Bráníku.
"""
],
[
"Tri Sestry",
"Prusa",
"https://www.youtube.com/watch?v=X2gSF7MHRSc",
"""
Z hospody na návsi je slyšet polku, jo ho ho ho ho,
v úplňku na hrázi v křoví se krčí, jo ho ho ho ho,
posedlý potřebou chytit si holku, jo ho ho ho ho,
funí do rákosí a temně vrčí, jo ho ho ho ho. Ho ho.

Stejně si samy za to holky můžou,
že nechtěj chodit po vsi s Petrem Průšou,
tak to zkusil aspoň s tou blbou Růžou,
pod rouškou násilí tmou, tmou, tmou, tmou.

Skončila zábava, Růža se vrací, Průša je úchyl,
sama jde po hrázi a nemá strach, Průša je úchyl,
tlustá a opilá chvílemi zvrací, Průša je úchyl,
častěji upadne, polyká prach, Průša je úchyl.

Stejně si samy za to holky můžou,
že nechtěj chodit po vsi s Petrem Průšou,
tak to zkusil aspoň s tou blbou Růžou,
pod rouškou násilí tmou, tmou, tmou, tmou.

Teď došla k Průšovi mátoha tlustá, Průša je úchyl,
deviant útočí, mizí s ní v pýru, Průša je úchyl,
drtí jí ňadra a líže ústa, Průša je úchyl,
hledá kde nechal tesař díru, Průša je úchyl.

Stejně si samy za to holky můžou,
že nechtěj chodit po vsi s Petrem Průšou,
tak to zkusil aspoň s tou blbou Růžou,
pod rouškou násilí tmou, tmou, tmou, tmou.

Průša už usíná ukojen doma, Průša je úchyl
naplněn pocitem jaký maj rváči, Průša je úchyl
Růženu opouští lihové koma, Průša je úchyl
Nic neví, k domovu po hrázi kráčí, Průša je úchyl.abs
Stejně si samy za to holky můžou,
že nechtěj chodit po vsi s Petrem Průšou,
tak to zkusil aspoň s tou blbou Růžou,
pod rouškou násilí tmou, tmou, tmou, tmou.
"""
],
[
"Trampske perly",
"Stanky",
"https://www.youtube.com/watch?v=pTlPuPKx2w0",
"""
U stánků na levnou krásu
postávaj a smějou se času
s cigaretou a s holkou, co nemá kam jít.

Skleniček pár a pár tahů z trávy,
uteče den, jak večerní zprávy,
neuměj žít a bouřej se a neposlouchaj.

Ref:
Jen zahlídli svět, maj na duši vrásky,
tak málo je, málo je lásky,
ztracená víra hrozny z vinic neposbírá.

U stánků na levnou krásu
postávaj a ze slov a hlasů
poznávám, jak málo jsme jim stačili dát.

Ref: 2x
Jen zahlídli svět, maj na duši vrásky,
tak málo je, málo je lásky,
ztracená víra hrozny z vinic neposbírá.
"""
],
[
"Trampske perly",
"Buraky",
"https://www.youtube.com/watch?v=hMc6pAxOI9w",
"""


Když sever válčí s jihem a zem jde do války,
na polích místo bavlny teď rostou bodláky.
Ve stínu u silnice vidím z jihu vojáky,
jak válejí se s kvojerem a louskaj buráky.

Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.
Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.

Plukovník je v sedle, volá Yenkyové jdou,
ale mužstvo stále křičí, že dál už nemohou.
Plukovník se votočí a koukne do dálky,
jak jeho slavná milice tam louská buráky.

Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.
Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.

Až tahle válka skončí, a my zas budem žít,
své milenky a ženy pak půjdem políbit.
Až zeptaj se tě "Hrdino, cos dělal za války?"
Já flákal sem se s kvérem a louskal buráky.

Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.
Hej hou, hej hou, nač chodit do války,
je lepší doma sedět a louskat buráky.
""
"""
],
[
"Trampske perly",
"Severni vitr",
"https://www.youtube.com/watch?v=Qv7pexG2U_o",
"""
Jdu s děravou patou,
mám horečku zlatou,
jsem chudý, jsem sláb, nemocen.
Hlava mě pálí
a v modravé dáli
se leskne a třpytí můj sen.

Kraj pod sněhem mlčí,
tam jsou stopy vlčí,
tam zbytečně budeš mi psát.
Sám v dřevěné boudě
sen o zlaté hroudě
já nechám si tisíckrát zdát.

Severní vítr je krutý,
počítej lásko má s tím.
K nohám ti dám zlaté pruty
nebo se vůbec nevrátím.

K nohám ti dám zlaté pruty
nebo se vůbec nevrátím.

Tak zarůstám vousem
a vlci už jdou sem,
už slyším je výt blíž a blíž.
Už mají mou stopu,
už větří, že kopu
svůj hrob, a že stloukám si kříž.

Zde leží ten blázen,
chtěl dům a chtěl bazén
a opustil tvou krásnou tvář.
Má plechovej hrnek
a pár zlatejch zrnek
a nad hrobem polární zář.

Severní vítr je krutý,
počítej lásko má s tím.
K nohám ti dám zlaté pruty
nebo se vůbec nevrátím.

K nohám ti dám zlaté pruty
nebo se vůbec nevrátím.
"""
],
[
"Barbora Polakova",
"Krava",
"https://www.youtube.com/watch?v=AzXHd8hSml4",
"""
Skoro měsíc je v čudu,
místo kluka mám mičudu,
(skoro mesiac je preč
a ty si voľná heč)
docela to vypadalo, že nám bude hezky,
na to že byl zo Žiliny, mluvil plyně česky.

Nedals mi kytku na Valentýna,
(no tak ti ju nedal no)
Sedím tu s tvou ségrou a s litrem vína,
Každej lok prokládám mléčnou Milkou,
Brambůrky došly před malou chvilkou.
(nežer už)

Ref:
Nedals mi kytku na Valentýna,
Čekám, že mě pozveš aspoň do kína.
Ty se někde couráš,
Ani jedna zpráva,
Úplně mě bouráš,
Bože já jsem krááá va va va

(vadilo by ti, keby som si dala cigu ??)
Vadilo..

Vdyť já vím, že Valentýn je jen reklamní bublina,
Jak se ale bránit můžu? Jsem cílová skupina.
(Ja myslím že Valentýn je len komerčný sviatok,
to mi príde logičtějši sviatok na deň matok)
ty jsi těhotná ??
(nie)
Aha..

Fajn, tak já si teda počkám na prvního máje,
Snad mě vezme na Petřín pod třešní přečte Máje.
(dobre moja rozumiem, máj je lepší sviatok,
môj brat to je strašný debil, dovalí karafiátok)

Nedals mi kytku na Valentýna,
(nerieš to)
Sedím tu s tvou ségrou a s litrem vína,
Každej lok prokládám mléčnou Milkou,
Hermelín došel před malou chvilkou.
(ešte je tam ementál)

Ref:
Nedals mi kytku na Valentýna,
Sýru mám po krk, už je mi malá mikína,
Ty se někde couráš, ani jedna zpráva,
Úplně mě bouráš,
Bože já jsem krá...va...va...va
(vážne to musíš tak prežívať?)

Ref:
Kráááá va va va 
"""
],
[
"Osvaldova Vasut",
"Nemuzu si pomoct",
"https://www.youtube.com/watch?v=CT1B5qGbhj0",
"""
Kdybych  ti řek,
jak moc  pro mě znamenáš,
myslím , že bys to nepochopila,
takže  počkám počkám,
dokud  tenhle den nepřijde,
kdyby  tys to pochopila

nemůžu si pomoc,
nemůžu se zastavit,
zblázňuji se nyní,
nemůžu se zastavit,
neumím se ovládat
zblázňuji se nyní

II:já miluji tě
já chci tě,
já chcimluvit s tebou
já chci být s tebou:II já chci být s tebou

nemůžu to změnit
vždyť já z toho tolik
neenanedělám
nemůžu se vobrátit nazpět
musím čelit té skutečnosti
život bez tebe je mlhavý

II:já miluji tě
já chci tě,
já chci mluvit s tebou
já chci být s tebou:II

polib mě,  vzruš mě neeluč se

drž mě  miluj mě neeluč se
 ououoooo  neeluč se

nemůžu si pomoc,
nemůžu se zastavit,
zblázňuji se nyní,
nemůžu se zastavit,
neumím se ovládat
zblázňuji se nyní
já miluji tě…
ououooo
polib mi ČAU
"""
],


])

    # exporting songbook
    sbk.MakeHTML_karaoke("./output/html/")
    pass

