Title:   	Inteligentná klimatizácia
Subtitle:   Smart Home Kit

# Inteligentné zavlažovanie

// LEFT

<img src=images/uvod-zavlazovanie.PNG width="600" height="600">

// RIGHT

**Čo budeme potrebovať:**  
micro:bit, sensor:bit doska, senzor vlhkosti pôdy (soil moisture sensor), relátko (relay), čerpadlo (submersible pump), OLED displej, prepojovacie vodiče, kvetinku v kvetináči.  

Programovať budeme v prostredí [makecode.microbit.org](https://makecode.microbit.org/).

// END

### 1. 1.	Senzor vlhkosti pôdy  
   
// LEFT

Na spodnej časti dosky, na ľavej strane sú 4 otvory na kolíky (GVClCa). OLED displej do nich zapojíme. Kvôli prehľadnosti nasledujúcich schém na nich OLED displej nebude zobrazovaný, ale neodpájame ho.

<img src=images/OLED-zapojenie.png width="300" height="300">


// RIGHT

Teraz sa naučíme ako pracovať so senzorom vlhkosti. Senzor si káblikom (žlto-červeno-čierny) pripojíme k doske na kolík 1. Jeden koniec zacvakneme do senzora a druhú stranu, kde sú dierky nasadíme na kolíky, dávajme pozor, aby išiel žltý káblik na žltý kolík, červený na červený a čierny na čierny.

<img src=images/01-zapojenie.png width="300" height="300">

// END


// LEFT

V udalosti `počas spustenia` si inicializujeme OLED displej príkazom `initialize OLED with width 128 height 64` z kategórie `OLED`.

// RIGHT

```makecode-no-link
_YU7TuA0Yc3CK
```
// END

// LEFT

// NEWPAGE

V cykle `vždy` budeme merať a vypisovať hodnotu, keďže chceme aby sa výpis a meranie opakovalo. Na výpis na displej použijeme príkaz na zobrazenie reťazca `show (without newline) string` a príkaz `show (without newline) number` na zobrazenie čísla. Obe z kategórie `OLED`. Príkazy nám vedľa seba zobrazia informáciu o tom, čo meriame aj nameranú hodnotu. Ak by sme chceli vypisovať hodnoty pod seba môžeme požiť príkaz `show string` a `show number`, ktorý automaticky po výpise odriadkuje. 

Ukážeme si dva spôsoby ako budeme zo senzora vlhkosti čítať hodnoty. Prvý je cez príkaz, ktorý je určený pre prácu so SmartHome Kitom, `value of soil moisture(0-100) at pin P1` z kategórie `Smarthome`, kde si nastavíme kolík na ktorý sme senzor pripojili.

// RIGHT

```makecode-no-link
_3sdH4566eRak
```
```makecode-link-only
_C6XJzF9A8PKC
``` 
// END

// LEFT

Druhý je cez analógové čítanie z kolíka, na ktorom je senzor pripojený. Príkazom `analógové čítanie kolík P1` z kategórie `Kolíky`, kde si tiež nastavíme číslo kolíka na ktorý sme senzor pripojili. Na rozdiel od digitálneho čítania, kde sa vypisujú len dve hodnoty a to 0 pri nízkom napätí a 1 pri vysokom napätí, pomocou analógového čítania vypisujeme hodnoty napätia prepočítané na stupnicu 0 - 1023.

// RIGHT

```makecode-no-link
_Jx6UDqhCXJAM
```
```makecode-link-only
_H1q0M0D7s3jK
``` 
// END

Môžeme vyskúšať oboje a zisťovať citlivosť senzora a rozsah v akom senzor meria vlhkosť pôdy v kvetináči. Skúzme senzor namočiť aj priamo do vody, pozor len žltú časť senzora. Sledujme, aké hodnoty ukáže. 

Pozorovaním by sme mali zistiť:

* Snímač vlhkosti pôdy pôsobí ako rezistor. Čím viac vody je v pôde, tým je lepšia vodivosť medzi kolíkmi, čo spôsobí aj zníženie odporu a vyššie namerané hodnoty. 
* Pri použití príkazu z knižnice `smarthome` meria senzor hodnoty v rozsahu 0-100 a pri použití analógového čítania hodnoty v rozsahu 0-1023. 
 
**Na ďalšie projekty budeme používať príkaz `value of soil moisture(0-100) at pin P1`.**

### 2. Spúšťanie čerpadla 
    
// LEFT

Teraz sa naučíme ako pracovať s čerpadlom. Na zapojenie čerpadla musíme použiť relátko, ktoré bude regulovať pohon čerpadla. Relátko káblikom (žlto-červeno-čierny) pripojíme k doske na kolík označený číslom 2. Jeden koniec zacvakneme do čerpadla a druhý koniec, kde sú dierky nasadíme na kolíky. Dávajme pozor, aby išiel žltý káblik na žltý kolík, červený na červený a čierny na čierny.

Z Čerpadla trčia dva kábliky, jeden čierny a jeden červený. Čierny káblik pripojíme na čierny kolík (GND) s označním 16. Červený káblik zasunieme do stredného otvoru na relátku, na upevnenie použijeme malý skrutkovač, ktorý by mal byť súčasťou kitu. Z kitu vytiahneme ešte jeden káblik, ktorý má na jednej strane dutinku (samica) a na druhej strane kolík (samec). Dutinku dáme na napájací červený kolík (Voltage) s číslom 8 a kolík zasunieme do otvoru relátka, kde je nápis *NO*, na upevnenie použijeme malý skrutkovač.

// RIGHT

<img src=images/02-zapojenie.png width="300" height="300">

// END


Čerpadlo má len dva stavy a to buď čerpá alebo nečerpá. Týmto stavom sa priradíme čísla a to 0 pre stav kedy nečerpá a 1 pre stav kedy čerpá. Tieto hodnoty si budeme digitálne zapisovať na kolík, kde máme čerpadlo teda relátko zapojené, u nás P2 (kolík/pin 2). Hodnoty budeme zapisovať pri stlačení tlačidla, `keď sa tlačidlo A stlačí` čerpadlo zapneme a `keď sa tlačidlo B stlačí` ho vypneme. Budeme tak simulovať zapnutie a vypnutie zavlažovania manuálne cez vypínač. Keď máme len dva stavy, kde zapisujeme buď jednotku alebo nulu, tak požívame príkaz `digitálne zapísať kolík P1 hodnota 0`, ktorý nájdeme v sekcii `Pokročilé – Kolíky`. Keď zapisujeme digitálne hodnotu na kolík, tak sa v skutočnosti na kolík privedie nejaké napätie. Ak zapisujeme 0 je to veľmi nízke napätie, čiže čerpadlo sa nezapne a ak 1, tak sa privedie na kolík vyššie napätie a motor čerpadla sa zapne.


```makecode-snippet
_X8t1498z6LDq
```
```makecode-link-only
_dLUHFEH9qXmC
``` 


!!! info "TIP"
	Ak vám čerpadlo nepôjde zapnúť, skúste zapojiť baterky.

### 3. Automatické zavlažovanie 
     
Pri automatizácii zase spojíme všetky časti, čiže manuálne spúšťanie čerpadla nahradíme podmienkou automatického zapnutia. Podmienku, pri akej vlhkosti pôdy sa spustí naše zavlažovanie si určíme podľa predošlého pozorovania. Keď vlhkosť klesne pod danú hodnotu, čerpadlo sa zapne na pár sekúnd a potom sa vypne. Takto sa uistíme, že rastlinku neprepolievame.

Pri automatickom riešení nemusíme nič odpájať ani vymazať kód. Keď chceme hodnotou zo senzora použiť viackrát, je lepšie uložiť si hodnotu do samostatnej premennej, aby sme pri ďalších krokoch používali rovnakú hodnotu a aby sme nemuseli merať viackrát v jednom cykle. Na začiatku nastavíme premennú, do ktorej budeme ukladať nameranú vlhkosť. Premennú vytvoríme v kategórii `Premenná`, kde vyberieme `Vytvoriť premennú` a zadáme meno premennej. Vyberieme príkaz `nastaviť premennú na 0`, ktorý vložíme na začiatok slučky `vždy`. Namiesto 0 vložíme príkaz `value of soil moisture(0-100) at pin P1`.

<div markdown="1" class="mx-auto" style="width: 70%;">	

```makecode-snippet
_Lw4Udm0HX3MV
```
</div>

Do výpisu môžeme namiesto príkazu merania dať zobrazovať premennú, v ktorej je tá hodnota už uložená. 

<div markdown="1" class="mx-auto" style="width: 40%;">	

```makecode-snippet
_AezERWY0oCW4
```
</div>

// LEFT

Do kódu si ešte pridáme podmienku, kde budeme porovnávať vlhkosť s nami určenou hodnotou, ktorú si ideálne určíme na základe pozorovaní. Aby sa čerpadlo zaplo nastavíme hranicu tak, aby bola hodnota v podmienke o niečo vyššia ako aktuálna vlhkosť pôdy v kvetináči, ale nie o moc vysoká, aby sme kvetinku nepreliali.

Na podmienku použijeme príkaz `ak ... potom ... ` z kategórie `Logika`, pomocou ktorého budeme porovnávať nameranú vlhkosť s hodnotou ktorú sme si určili. Príkaz na porovnávanie `...< ...` nájdeme tiež v kategórii `Logika`. Keď bude vlhkosť nižšia ako nami určená hodnota, bude to znamenať, že je moc sucho a tak pomocou príkazu `digitálne zapísať kolík P2 hodnota 1` čerpadlo zapneme na 5 sekúnd a potom príkazom `digitálne zapísať kolík P2 hodnota 0` vypneme. Príkazy na zapnutie a vypnutie čerpadla môžeme zobrať z príkazov `keď sa tlačidlo A stlačí` a `keď sa tlačidlo B stlačí`, ktoré môžeme následne vymazať. Keď máme program hotový nahráme si ho do micro:bita.

// RIGHT

```makecode-snippet
_1cWPbsi3pF4x
```
```makecode-link-only
_5JK6PwDEWdMM
``` 

// END
