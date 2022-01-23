Title:   	Inteligentná klimatizácia
Subtitle:   Smart Home Kit

# Inteligentný alarm

// LEFT

<img src=images/uvod-alarm.PNG width="600" height="600">

// RIGHT

**Čo budeme potrebovať:**  
2 micro:bity, sensor:bit doska, senzor nárazu (crash sensor), OLED displej, prepojovacie vodiče.  

Programovať budeme v prostredí [makecode.microbit.org](https://makecode.microbit.org/).

// END

### 1. Testovanie senzora nárazu 
   
// LEFT

 Na spodnej časti dosky, na ľavej strane sú 4 otvory na kolíky (GVClCa). OLED displej do nich zapojíme. Kvôli prehľadnosti nasledujúcich schém na nich OLED displej nebude zobrazovaný, ale neodpájame ho.

<img src=images/OLED-zapojenie.png width="300" height="300">


// RIGHT

Teraz sa naučíme ako pracovať so senzorom nárazu. Senzor si káblikom (žlto-červeno-čierny) pripojíme k doske na kolík s číslom 1. Jeden koniec zacvakneme do senzora a druhú stranu, kde sú dierky nasadíme na kolíky, dávame pozor, aby išiel žltý káblik na žltý kolík, červený na červený a čierny na čierny.

<img src=images/crash-senzor-zapojenie.png width="300" height="300">

// END

// LEFT

V udalosti `počas spustenia` si inicializujeme OLED displej príkazom `initialize OLED with width 128 height 64` z kategórie `OLED`. Taktiež si musíme nastaviť na, ktorý kolík sme senzor pripojili pomocou príkazu `Setup crash sensor at pin P1` z kategórie `Smarthome`. My sme  senzor zapojili na kolík P1 (kolík/pin 1), čiže nemusíme nič meniť.

// RIGHT

```makecode-no-link
_H36WV1YvkaDq
```
// END

Senzor nárazu má len dva stavy a to buď je stlačený alebo nie je. Týmto stavom si priradíme čísla a to 0 pre stav kedy je senzor stlačený a 1 pre stav, kedy nie je stlačený. Tieto hodnoty vieme digitálne čítať z kolíka, kde máme senzor zapojený. Hodnoty budeme čítať opakovane, čiže čítanie dáme do cyklu `vždy`. Keď máme len dva stavy, kde čítame buď jednotku alebo nulu, tak požívame príkaz `digitálne načítať kolík P1`, ktorý nájdeme v sekcii `Pokročilé – Kolíky`. 



Na výpis na displej použijeme príkaz na zobrazenie reťazca `show (without newline) string` a príkaz `show (without newline) number` na zobrazenie čísla. Obe z kategórie `OLED`. Príkazy nám vedľa seba zobrazia informáciu o tom, čo meriame aj nameranú hodnotu. Ak by sme chceli vypisovať hodnoty pod seba môžeme požiť príkaz `show string` a `show number`, ktorý automaticky po výpise odriadkuje.

Vypisovať budeme hodnotu digitálne načítanú z kolíka 1. Nemôžeme zabudnúť na príkaz `clear OLED display`, ktorý nám zabezpečí že sa displej vždy vyčistí a zapíše sa nová hodnota. Ak chceme znížiť intenzitu blikania použijeme príkaz  `pozastaviť (ms) 100` z kategórie `Základné`. Takýto kód si môžeme stiahnuť do micro:bita.

<div markdown="1" class="mx-auto" style="width: 60%;">  

```makecode-no-link
_Tvm4cw81U40K
```
```makecode-link-only
_KFR6aa29pb19
``` 
</div>

### 2. Automatický alarm
    

Teraz si vďaka nášmu senzoru naprogramujeme alarm. Predstavíme si, že máme senzor nárazu pripevnený na dverácj. Keď sú dvere zatvorené, tak je aj spínač stlačený. Keď sa dvere otvoria, tak sa spínač tiež “otvorí”. Na základe tohto si nastavíme podmienky, keď sú dvere zavreté, tak je alarm neaktívny, no keď sa dvere otvoria, alarm by sa mal spustiť.

// LEFT

Do programu pridáme podmienený príkaz `ak ... potom... inak...` z kategórie `Logika`, kde budeme zisťovať či je senzor stlačený, a to pomocou príkazu `crash sensor pressed` z kategórie `Smarthome`. Príkaz vracia hodnotu `True`, keď je spínač stlačený alebo hodnotu `False`, keď je spínač rozopnutý. Ak je senzor stlačený môžeme na  OLED displej vypísať, že sú dvere zatvorené. Inak vypíšeme, že sú dvere otvorené a príkazom `spustiť melódiu ba ding opakovanie raz` z kategórie `Hudba` spustíme zvukovú signalizáciu. Nezabudneme, že ak chceme vypisovať na nový riadok musíme pred podmienený príkaz vložiť príkaz `insert newline`.

// RIGHT


```makecode-snippet
_0yXF2P654gRA
```
```makecode-link-only
_6AaPMW9Mt8Jh
``` 
// END


### 3. Automatický alarm s diaľkovým ovládaním 
    
V tejto časti sa zamyslíme ako funguje skutočný alarm. Ten musí vedieť majiteľ domu zapnúť, keď ide z domu preč ale aj vypnúť, keď je doma, aby sám alarm nespustil. Ďalšia vec, nad  ktorou sa musíme zamyslieť je, že keď niekto spustí alarm tým že otvorí dvere, nechceme aby ho dokázal vypnúť len tým, že ich za sebou zavrie. Deaktivovať alarm by mal vedieť teda len majiteľ domu. Na toto všetko si pomocou druhého micro:bita vytvoríme diaľkový ovládač, ktorým si budeme vedieť alarm aktivovať, tak že pošleme hodnotu 1 a deaktivovať, tak že pošleme hodnotu 0 a upravíme aj náš pôvodný automatický alarm.

// LEFT

Najprv si upravíme kód nášho existujúceho alarmu. Keďže chceme komunikovať s diaľkovým ovládaním, potrebujeme používať rádio komunikáciu medzi micro:bitmi. Do udalosti `počas spustenia` pridáme príkaz  `rádio nastaviť skupinu 1` z kategórie `Rádio`. Potrebujeme nastaviť skupinu, v ktorej budú micro:bit s ovládačom komunikovať. 

// RIGHT

<div markdown="1" class="mx-auto" style="width: 70%;">
```makecode-snippet
_PfsAquW856my
```
</div>

// END

// NEWPAGE

// LEFT

Z kategórie `Rádio` vyberieme príkaz `rádio pri prijatí čísla receivedNumber`, v ktorom vytvoríme a nastavíme premennú na hodnotu prijatého čísla. Vytvoríme premennú `alarm`. V kategórii `Premenná` stlačíme `Vytvoriť premennú` a zadáme meno premennej. Na nastavenie premennej použijeme `príkaz nastaviť premennú na 0` a priradíme jej hodnotu na `receivedNumber`. Túto hodnotu získame tak, že klikneme na parameter príkazu `rádio pri prijatí čísla receivedNumber` a potiahneme ho na požadované miesto.

// RIGHT

```makecode-snippet
_4vhPYCFYdYkg
```

// END

// LEFT

Zo slučky vždy vymažeme predchádzajúci podmienený príkaz, namiesto neho si vytvoríme iný. Vyberieme príkaz `ak ... potom... inak...` z kategórie `Logika` a klikneme na znamienko `plus` pod vetvou *inak*. Príkaz sme rozšírili o časť *inak ak*. Následne stlačíme na znamienko `mínus` umiestnenom pripríkaze *inak*, V kóde nám zostane len to čo potrebujeme a to štruktúra `ak potom inak`.

V prvej časti budeme porovnávať, či bolo prijaté číslo 1. Ak áno, tak vypíšeme, že je Alarm zapnutý. Keď je alarm zapnutý, musíme dávať pozor, či je zároveň stlačený aj spínač. Ak je senzor otvorený, tak musíme spustiť zvukovú signalizáciu, alarm. Do kódu vložíme ďalší podmienený príkaz `ak ... potom...`. Keďže nechceme zvukovú signalizáciu zapnúť v momente, keď je senzor stlačený ale naopak keď je senzor otvorený, tak podmienku príkazu `crash sensor pressed` znegujeme, dáme do príkazu `nie ...` z kategórie `Logika`.

Zvukovú signalizáciu spustíme príkazom `spustiť melódiu ba ding opakovanie vždy na pozadí` z kategórie `Hudba`. Nastavením opakovania prehrávania na *vždy na pozadí* zabezpečíme, že alarm začne vyhrávať, keď otvoríme dvere a aj keď ich následne zavrieme, tak neprestane, až kým nevypneme alarm.  V druhej časti nášho podmieneného príkazu `inak ak` budeme zisťovať či prijaté číslo bolo 0, ak áno vypíšeme, že je Alarm vypnutý a zastavíme zvukovú signalizáciu príkazom `zastaviť melódiu všetky` z kategórie `Hudba`. Kód môžeme nahrať do nášho micro:bita s funkciou alarmu. 

// RIGHT

```makecode-snippet
_MxPWxf4LqWLy
```
```makecode-link-only
_ajJYCtEopR6y
``` 
// END

// LEFT

Teraz si naprogramujeme mirco:bit s funkciou diaľkového ovládania. Na akciu počas spustenia si nastavíme rovnakú rádio skupinu ako na alarme.

// RIGHT

```makecode-no-link
_JvggchE00XKr
```
// END

// LEFT

Zapínať a vypínať alarm budeme stlačením tlačidiel A a B. Tlačidlom A alarm zapneme, čiže príkazom `rádio odoslať číslo` budeme posielať číslo 1. Tlačidlom B alarm vypneme, čiže príkazom `rádio odoslať číslo 0` budeme posielať číslo 0. Aby sme aj vizuálne vedeli, či máme alarm zapnutý alebo vypnutý zobrazíme si ikonu krížika, ak sme poslali 0 a ikonu fajky, ak sme poslali 1. Použijeme príkaz `Zobraziť ikonu ...` z kategórie `Základné`.

// RIGHT

```makecode-snippet
_LFL9riXFoPUu
```
```makecode-link-only
_1xyU16F8ffDt
``` 
// END

Tento program môžeme nahrať do micro:bita s funkciou ovládača. A teraz môžeme otestovať náš alarm.
