Zdravím priaznivcov robotiky a programovania, ktorým sa do rúk dostal výučbový mikropočítač micro:bit a robot Ring:bit car V2.0. Spomínané produkty som kúpil v internetovom obchode [www.rlx.sk](https://www.rlx.sk) pre moju malú dcéru, aby som v nej vzbudil záujem o IT. Mikropočítač vo mne vyvolal spomienky z detstva, keď bol 'in' domáci počítač Didaktit Gama s programovacím jazykom Basic, ktorý bohužiaľ nebol do takej miery 'user friendly', ako je tomu pri programovaní mikropočítača micro:bit s využitím platformy Microsoft MakeCode.


Platforma **Microsoft MakeCode** umožňuje jednoduchým spôsobom sa naučiť základy programovania v jazyku JavaScript za využitia Blokov, ktoré obsahujú základné príkazy tohto jazyka. Dokonca podporuje aj slovenčinu a češtinu, čiže nie som nútený písať program v angličtine a poznať anglické príkazy. Veľkým prínosom je možnosť pridania rozširujúcich Blokov, čomu sa nevyhnem pri programovaní robota Ring:bit a jeho príslušenstva.

Skôr než som si naprogramoval robot Ring:bit, tak som si vyskúšal, čo všetko dokáže mikropočítač **micro:bit**, ktorý je vybavený:

- displej (tvorí ho 25 programovateľných červených LED diód)
- dvomi programovateľným tlačidlami
- 25 externými spojeniami (pinmi) na spodnej časti
- svetelným a teplotným senzorom
- pohybovými senzormi (akcelerometer a kompas)
- bezdrôtovou komunikáciou ( Radio a Bluetooth)
- USB rozhraním

Väčšinu vybavenia som si otestoval aj v praxi, avšak najväčší potenciál vidím vo využití pinov a v bezdrôtovej komunikácii (Bluetooth), čo je možné najlepšie uplatniť pri použití robota Ring:bit a jeho príslušenstva.

Robot **Ring:bit car V2.0** používa ako zdroj energie 3 batérie typu AAA a na pohon slúžia dva kontinuálne servomotory. Taktiež je možné, ako zdroj energie, použiť 'powerbank' pripojenú cez USB rozhranie, avšak pri pripojení viac ako jedného príslušenstva neposkytne dostatočný prúd. Aby som zdroj energie robota vyriešil dlhodobo a ekologicky, tak som si kúpil nabíjačku batérií AAA aj s nabíjateľnými batériami.

K uvedenému robotu sa dá kúpiť nasledovné príslušenstvo: 

- snímač čiary (slúži na pohyb po čiernej čiare)
- snímač vzdialenosti (slúži na vyhýbanie sa predmetom)
- LED nárazník (slúži na svetelný 'cool' efekt)

Najviac ma zaujal LED nárazník, ktorý je možné v platforme Microsoft MakeCode ľahko naprogramovať za pomoci rozširujúceho Bloku Neopixel. Na programovanie snímača vzdialenosti treba použiť rozširujúci Blok Sonar. Snímač čiary a pohon tohto robota sa dá naprogramovať s využitím rozširujúceho Bloku RingbitCar.

**Príslušenstvo** robota **Ring:bit car V2.0** je možné použiť len jednotlivo, lebo výrobca počíta len s „plnohodnotnými“ analógovými pinmi P0, P1 a P2. Z toho vyplýva, že piny P1 a P2 sú trvalo určené na pohon dvoch servomotorov a pin P0 je určený na pripojenie príslušenstva. Avšak pri analýze zvyšných 22 pinov je zrejmé, že na pripojenie príslušenstva je možné využiť aj „neplnohodnotné“ analógové piny P3, P4 a P10, pričom displej mikropočítača micro:bit je nutné vypnúť. Piny P3, P4 a P10 je možné ľahko využiť, ak micro:bit zasuniete do modulu edge:bit, ktorý je plne kompatibilný s robotom Ring:bit.

Modul **edge:bit** umožňuje využitie „neplnohodnotných“ pinov mikropočítača micro:bit za použitia jumperov (koncovky male-male) a konektorov NSL 25-3. Celkom som si vystačil s pinmi P3 a P4, lebo na pin P10 som už nemal čo pripojiť.

Prvý konektor NSL 25-3 odporúčam prepojiť pomocou troch jumperov s pinmi P3, V (napätie) a G (uzemnenie). Druhý konektor NSL 25-3 odporúčam prepojiť pomocou dvoch jumperov s pinmi P4 a G (uzemnenie), pričom stredný kontakt na konektore bude neobsadený.

Na prehrávanie tónov z mikropočítača micro:bit odporúčam vytvoriť si ešte príslušenstvo **reproduktor**, za použitia konektora NSG 25-3 (neobsadený stredný kontakt), dvoch jumperov a minireproduktora, resp. bzučiaka.

Po posúdení možností **kombinácií príslušenstva** pre robot **Ring:bit car V2.0** odporúčam nasledovný 'layout' pinov:

P0 – snímač vzdialenosti, resp. čiary  
P1 – servomotor  
P2 – servomotor  
P3 – LED nárazník (vypnúť displej mikropočítača)  
P4 – reproduktor (vypnúť displej mikropočítača, programovanie tónov cez Blok Kolíky)

Treba počítať s tým, že pri súčasnom využití pinov P0 až P4 dochádza k **vyššiemu zaťaženiu** troch **batérií AAA** (odporúčam nepoužívať 'powerbank') a pri použití 'opotrebovaných' batérií robot Ring:bit car V2.0 nemusí fungovať optimálne. Môže sa to prejaviť napr. zníženou rýchlosťou pohybu. Odporúčam použiť nové, resp. nabité batérie a znížiť jas LED nárazníka na minimum. 

Následne som mohol začať **programovať v** platforme **Microsoft MakeCode** za použitia rozširujúcich Blokov spomenutých v predchádzajúcom texte. Najskôr som si vyskúšal naprogramovať príslušenstvo robota Ring:bit car V2.0 jednotlivo (v balení boli priložené karty s popisom jednoduchých programov), čiže som použil len 'plnohodnotné' analógové piny P0, P1 a P2. Následne som skombinoval LED nárazník (pin P3) so snímačom vzdialenosti (pin P0) a nakoniec som pridal tóny (pin P4), ktoré prehral reproduktor. 

Po úspešnom skombinovaní jednoduchých programov príslušenstva robota Ring:bit car V2.0 do celistvého programu, som začal postupne testovať funkčnosť **snímača vzdialenosti spolu s LED nárazníkom a reproduktorom**, čiže som využil piny P0 až P4. Po viacerých úpravách celistvého programu sa mi nakoniec podarilo robot spojazdniť za optimálneho fungovania spomínaného príslušenstva. Prikladám finálnu verziu programu:

```
let sonar = 0
led.enable(false)
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
RingbitCar.freestyle(40, 40)
pins.analogSetPitchPin(AnalogPin.P4)
let strip = neopixel.create(DigitalPin.P3, 10, NeoPixelMode.RGB)
strip.setBrightness(2)
basic.forever(function () {
    sonar = sonarbit.sonarbit_distance(Distance_Unit.Distance_Unit_cm, DigitalPin.P0)
    if (sonar < 9 && sonar != 0) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        strip.clear()
        strip.show()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        RingbitCar.freestyle(-40, -40)
    } else if (sonar < 27 && sonar >= 9) {
        music.playTone(349, music.beat(BeatFraction.Whole))
        strip.clear()
        strip.show()
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Orange))
        strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Orange))
        strip.show()
        RingbitCar.freestyle(-10, 0)
    } else {
        music.playTone(494, music.beat(BeatFraction.Double))
        strip.clear()
        strip.show()
        strip.showRainbow(1, 360)
        RingbitCar.freestyle(40, 40)
    }
})
```

Potom som na pin P0 namiesto snímača vzdialenosti pripojil snímač čiary, pričom piny P1 (servomotor), P2 (servomotor) a P4 (reproduktor) zostali bez zmeny. Bohužiaľ LED nárazník som už nemohol použiť, lebo na jeho fungovanie by som potreboval ďalšiu rozširujúcu dosku, takú istú, na ktorú už bol priskrutkovaný snímač čiary. Avšak som vynašiel 'hack', ako využiť aspoň dve LED diódy na tejto rozširujúcej doske spolu so snímačom čiary. Pred zapnutím robota Ring:bit car V2.0 som prepol spínač na spomínanej doske na pozíciu 'Rainbow LED', následne som zapol robot a po rozsvietení dvoch LED diód tejto dosky som prepol spínač do polohy 'Other modules'. Použitím tohto postupu zostali svietiť tieto dve LED diódy za súčasného optimálneho fungovania snímača čiary. Následne som upravil horeuvedený program tak, aby tento robot bezproblémovo fungoval s pripojeným **snímačom čiary, reproduktorom** a za súčasného rozsvietenia **dvoch LED diód rozširujúcej dosky.** Po testovaní som sa dopracoval k finálnej verzii programu:

```
led.enable(false)
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
pins.analogSetPitchPin(AnalogPin.P4)
let strip = neopixel.create(DigitalPin.P0, 2, NeoPixelMode.RGB)
strip.setBrightness(2)
strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
strip.show()
basic.forever(function () {
    if (RingbitCar.tracking(RingbitCar.TrackingStateType.Tracking_State_2)) {
        music.playTone(262, music.beat(BeatFraction.Eighth))
        RingbitCar.freestyle(30, 0)
        basic.pause(300)
    }
    if (RingbitCar.tracking(RingbitCar.TrackingStateType.Tracking_State_1)) {
        music.playTone(330, music.beat(BeatFraction.Eighth))
        RingbitCar.freestyle(0, 30)
        basic.pause(300)
    }
    RingbitCar.freestyle(10, 10)
})
```

```makecode-no-link
_a2RXczW23YYJ
```
```makecode-no-link
_bptD7572CTJo
```

```makecode-link-only
_PE8A2jhxwVED
```

Oba uvedené programy sú napísané v platforme Microsoft MakeCode so znalosťami začiatočníka a ich hlavným cieľom je ukázať plnohodnotné využitie robota Ring:bit car V2.0 a jeho príslušenstva, s ktorým neráta ani sám výrobca. Zároveň som si tým rozšíril 'knowledge' hravou formou, čo je hlavným poslaním daného robota.

**Záverom** sa chcem poďakovať za prečítanie môjho článku až do konca. Verím, že ste si rozšírili 'horizon' a moje poznatky využijete pri programovaní micro:bit a testovaní Ring:bit car V2.0.
V budúcom článku sa chcem venovať bezdrôtovému ovládaniu uvedeného robota a jeho príslušenstva za využitia technológie 'Bluetooth Low Energy' mikropočítača micro:bit.