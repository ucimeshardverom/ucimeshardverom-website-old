# Senzor pohybu (Akcelerometer)
##  Metodika pre učiteľa

// LEFT

**Pomocné materiály:**

* [Prezentácia](https://docs.google.com/presentation/d/1vIrbrzFEmu905d2a8P9mzpyC8LPfcjY8WM7HbR1yXBU/edit?usp=sharing)

**Potrebné pomôcky:**  
Pre každého žiaka (alebo skupinu žiakov) BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený na internet.

**Ciele hodiny:**

* Zoznámiť sa s použitím senzoru pohybu v zariadení.
* Zistiť, kde sa senzory pohybu a naklonenie využívajú v každodennom živote.
* Naučiť sa genrovať náhodné čísla na micro:bite.

// RIGHT

**Potrebné predchádzajúce znalosti:**  
Vedieť nahrávať programy na micro:bit, poznať prostredie MakeCode, vedieť zobrazovať na displeji text a obrázky
a pracovať s pauzami.

**Odhadovaný čas:** 45 minút (nezabudnite na čas potrebný na rozdanie pomôcok, zozbieranie a záverečnú
diskusiu/reflexiu)

**Harmonogram:**

[TOC]

// END

---
### Príprava pred hodinou

Pred touto hodinou nie je potrebná špecifická príprava pomôcok.

---
### Priebeh hodiny

#### Opakovanie z minulej hodiny [5 min]
Na úvod hodiny je dobré pripomenúť si prácu v prostredí MakeCode - najmä prácu s tlačidlami.
To môžte spraviť jednoduchou opakovacou úlohou - naprogramujte na micro:bite jednoduchý program,
ktorý pri stlačení tlačidla A zobrazí štastného smajlíka a pri stlačení tlačidla B smutného smajlíka.
**(slajd č. 2)**

#### Čo je to akcelerometer? [5 min]
Pred začiatkom aktivít veďte so žiakmi diskusiu: **(slajd č. 3)**

* Čo je to akcelerometer (senzor zrýchlenia)?
* Kde sa akcelerometre používajú?
* Čo je to gyroskop (senzor naklonenia)?
* Kde sa gyroskopy používajú?
* Kde sa akcelerometer a gyroskop na micro:bite nachádzajú?

Správne odpovede aj s vysvetlením nájdete v návode tejto kapitoly **(slajd č. 4)**.

#### Snímanie potrasenia [5 min]
Žiakom predstavte príkaz `keď potrasenie` z kategórie `Vstup`. Náledne im zadajte úlohu, aby ich micro:bit pri spustení
zobrazil smutného smajlíka a pri potrasení zobrazil štastného smajlíka **(slajd č. 5)**.

#### Snímanie naklonenia vľavo a vpravo [5 min]
Žiakom povedzte, aby preskúmali, aké možnosti ponúka príkaz `keď potrasenie` a čo iné okrem potrasenia vedia snímať.
Následne im zadajte úlohu, aby ich micro:bit zobrazoval pri naklonení vľavo šípku smerujúcu vľavo a pri naklonení
vpravo šípku smerujúcu vpravo **(slajd č. 6)**.

#### Otáčanie smajlíka - ako na mobile [10 min]
Na predchádzajúcu aktivitu nadviažte, avšak tento krát namiesto šípok budú žiaci otáčať smajlíka a bude sa otáčať
do všetkých štyroch strán **(slajd č. 7)**.

Vhodné je pre názornosť vytiahnuť pred žiakov mobil a otáčať ním, pričom zdôraznite, že podľa otočenia sa otáča aj
obrazovka.

Taktiež sa uistite, že žiaci rozujemú pojmu "logo hore" a kde sa logo nachádza.

#### Náhodné čísla [10 min]
Nasledujúce tri úlohy (hod mincou, digitálna kocka a generátor čísel) môžte postupne predstavovať
podľa rýchosti žiakov, a žiaci ich môžu robiť nezávisle od zvyšku triedy **(slajd č. 8)**.

Predstavte žiakom príkaz `vybrať náhodne 0 do 10` z kategórie `Matematika`, a taktiež zdôraznite,
že na zobrazovanie čísel na obrazovke sa používa iný príkaz ako na zobrazovanie textu (reťazcov).

Následne predstavujte úlohy Hod mincou, Digitálna kocka a Generátor čísel podľa návodu tejto kapitoly.


#### Diskusia a zhrnutie aktivít [5 min]

Na záver veďte so žiakmi diskusiu o senzoroch zrýchlenia a naklonenia a o ich využití
v každodennom živote:

Otázky:

* Aký je rozdiel medzi akcelerometrom a gyroskopom?
* Kde sa na micro:bite nachádza akcelerometer a gyroskop?
* Akým príkazom v prostredí MakeCode generujeme náhodné čísla?
* Kde všade v každodennom živote sa využívajú senzory zrýchlenia a naklonenia?


!!! warning "Reflexia"
    
    Na konci hodiny je správny priestor aj na reflexiu žiakov. Pri nej sú žiaci vyzvaní, aby hodnotili nielen aktivity,
    ale aj svoju prácu na hodine, prípadne prácu svojich spolužiakov. Vytvoriť tým môžete aj väčšiu zodpovednosť
    u žiakov za vlastný proces vzdelávania.  
    
    Návodov, ako správne viesť reflexiu je mnoho, pekné zhrnutie nájdete na
    [eduworld.sk](https://eduworld.sk/cd/jaroslava-konickova/4005/ako-rozvijat-sebareflexiu-a-sebahodnotenie-ziakov)