*V tejto aktivite sa zoznámiš s akcelerometrom - senzorom, ktorý ti povie, ako hýbeš s micro:bitom
a aj ktorým smerom.*

![Obrázok BBC micro:bitu](images/microbit_hands.png)

**Potrebné pomôcky:**  
BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený k internetu

Pracovať budeme v online prostredí [makecode.microbit.org](https://makecode.microbit.org/)

---

**Obsah aktivity:**

[TOC]

---

## Čo je to akcelerometer?

Akcelerometer je senzor, ktorý meria akceleráciu (slovensky zrýchlenie). Je celkom rozšírený - nájdeš ho v autách,
mobiloch aj krokometroch. Často krát býva býva skombinovaný aj s ďalším senzorom - gyroskopom - senzorom naklonenia.
Ten meria, ktorým smerom a ako veľmi je micro:bit naklonený. Keďže tieto dva senzory (akcelerometer a gyroskop)
sú väčšinou skombinované do jednej súčiastky (nájdeš ju na zadnej strane micro:bitu) tak ich pre zjednodušenie
budeme obe nazývať spoločne "akcelerometer".

Kde sa využíva akcelerometer?

*   Mobilný telefón/tablet využíva senzor naklonenia na otáčanie obrazovky.
*   Airbagy v autách využívajú merač zrýchlenia na zistenie nárazu, kedy auto prudko spomalí (čiže opak zrýchlenia - spomalenie).
*   Krokomer využíva akcelerometer na rozpoznanie počtu krokov.

## Snímanie potrasenia 
Snímanie potrasenia micro:bitu je podobné snímaniu stlačenia tlačidiel. Stačí použiť príkaz `keď potrasenie`
z kategórie `Vstup`. Skús naprogramovať jednoduchý program, ktorý na pri spustení zobrazí smutného smajlíka
a na potrasenie zobrazí štastného smajlíka.

Program si najprv vyskúšaj v simulátore a až potom ho nahraj na micro:bit. Ako ale odsimulovať potrasenie v simulátore?
Vieme to spraviť dvoma spôsobmi - buď klikneme na biely kruh označený *SHAKE*, ktorú sa nám automaticky pridal na
hornú pravú stranu micro:bitu v simulátore. Druhým spôsobom je pár krát rýchlo prejsť myšou ponad micro:bit.

```makecode
_dri3y6FvAc28
```


## Snímanie naklonenia vľavo a vpravo
Okrem potrasenia vie micro:bit snímať akcelerometrom aj plno ďalších polôch, ako napríklad naklonenie vpravo
a naklonenie vľavo. Opäť na to využijeme príkaz `keď potrasenie` z kategórie `Vstup`, no tento krát klikneme
na `potrasenie` a príkaz pozmeníme. Skús naprogramovať micro:bit tak, aby pri naklonení vľavo zobrazoval šípku smerujúcu
vľavo a pri naklonení vpravo zobrazoval šípku smerujúcu vpravo.


```makecode
_8pz3t7dDvAgk
```

## Otáčanie smajlíka - ako na mobile
Senzory naklonenia majú v sebe vbudované aj mobilné telefóny a využívajú ich napríklad na to, aby vedeli,
do ktorej strany otočiť obrazovku keď otočíme mobilom. My teraz na micro:bite naprogramujeme to isté - na displeji
zobrazíme smajlíka, ktorý sa pri otáčaní micro:bitom bude otáčať tak, aby nikdy nebol dolu hlavou (analogické s otáčaním
obrazovky na smartfónoch).

Najprv naprogramujeme prvú časť programu - naklonenie smajlíka vpravo a naklonenie vľavo. Na to nám stačí pozmeniť
iba program z predchádzajúceho kroku.

```makecode
_4iCEzJa90P26
```

Program nahráme do micro:bitu a odskúšame. Ak funguje správne, doplníme ho o zostávajúce 2 obrázky - keď máme micro:bit
kolmo postavený k stolíku a keď ho máme dolu hlavou. To spravíme príkazmi `logo hore` a `logo dole`. Logom sa v tomto
prípade malá "tvárička" s dvoma očami nad displejom micro:bitu.

Po doplnení vyzerá program takto:

```makecode-no-link
_4iCEzJa90P26
```
```makecode-no-link
_RrCCpMcJ4654
```
```makecode-link-only
_3XuPAaH80F3K
```

Teraz si program nahraj na micro:bit a odskúšaj, či ti pri otáčaní zobrazí správny smajlík.

## Náhodné čísla - Hod mincou
Niekedy je rozhodovanie sa ťažké a vtedy si hádžeme mincou. Čo ak ale nemáme mincu pri sebe? Môžme využiť micro:bit.
Ten dokáže náhodne generovať čísla, ktoré môžme následne zobraziť na obrazovke.

Náhodné čísla v micro:bite získame príkazom `vybrať náhodne od 0 do 10` z kategórie `Matematika`. Keďže chceme vytvoriť
digitálnu mincu, tak namiesto čísel od `0 po 10` budeme generovať čísla iba od `0 po 1`. Nula bude znamenať nie a 
jednotka bude znamenať áno.

Číslo potom už stačí iba pri potrasení zobraziť. Na zobrazenie použijeme príkaz `zobraziť číslo` z kategórie `Vstup`.
Dôležité je použiť príkaz `zobraziť číslo` a nie `zobraziť reťazec`, nakoľko sú to dva rôzne príkazy.

Aby sa nám hodnota zobrazila iba na jednu sekundu použijeme príkazy `pozastaviť (ms)` a `Vymazať obrazovku`.

Riešenie:



```makecode
_DT8aFT6u4VUF
```


## Náhodné čísla - Digitálna kocka
Čo robiť v situácii, ak chceme hrať ktu *Človeče nehnevaj sa*, ale po otvorení krabice zistíme, že v balení chýba kocka.
Netreba zúfať, vytiahneme z vrecka micro:bit s cieľom premeniť ho na digitálnu kocku a po chvíli môžme hrať.

Skús naprogramovať micro:bit tak, aby pri zatrasení vypísal náhodné číslo od 1 po 6 (tak ako kocka).
Číslo sa po 1 sekunde zmaže. Program bude veľmi podobný ako v predchádzajúcom úlohe.

Riešenie:


```makecode
_KrUf6EUjrH2k
```




## Náhodné čísla - Generátor čísel
Posledný program, ktorý si v tejto aktivite spravíme je náhodný generátor čísel. Ten sa nám môže hodiť napríklad
pri lotérii. Pravidlá našej lotérie sú ale také, že sa žrebujú iba čísla od 23 po 55 (vrátane). Skús naprogramovať
micro:bit tak, aby ti vždy pri potrasení zobrazil náhodné číslo od 23 po 55 (vrátane) a zobrazoval ho iba jednu sekundu.
Následne sa obrazovka vymaže a môžeš micro:bitom potriasť opäť.

Riešenie:

```makecode
_FYv9j6U4J9km
```

## Zhrnutie aktivity

!!! primary "Kontrolné otázky"
    * Aký je rozdiel medzi akcelerometrom a gyroskopom?
    * Kde sa na micro:bite nachádza akcelerometer a gyroskop?
    * Akým príkazom v prostredí MakeCode generujeme náhodné čísla?
    * Kde všade v každodennom živote sa využívajú senzory zrýchlenia a naklonenia?

V tejto aktivite sme sa naučili používať vnútorný senzor zrýchlenia (akcelerometer) aj naklonenia (gyroskop). Zároveň
sme si vyskúšali generovať náhodné čísla a využiť ich pri tvorbe digitálnej mince, kocky či generátora náhodných čísel.