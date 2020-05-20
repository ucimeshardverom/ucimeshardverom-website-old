
**Elektrické obvody a vodivosť materiálov**

**Úvod do pripájania hardvérových komponentov k micro:bitom**

**Cieľ hodiny:** Zoznámiť sa s konceptom vodivosti materiálov, snímať uzatvorenie elektrického okruhu pomocou BBC micro:bit.

**Priebeh hodiny:** Učiteľ postupne zadáva úlohy žiakom, ktorí pracujú samostatne (alebo vo dvojici) pri vlastnom počítači. V niektorých aktivitách na zisťovanie vodivosti žiaci medzi sebou voľne spolupracujú.

**Trvanie hodiny:** 45 minút, pričom je potrebné počítať s časom na rozdanie hardvérových sád na začiatku hodiny (2-3 minuty), a ich pozbieranie a záverečnú diskusiu na konci hodiny (približne 5 minút).

**Potrebný hardvér:** BBC micro:bit, USB kábel, batérie pre BBC micro:bit, krokosvorkové káble, počítač pripojený na internet.

**Ďalšie pomôcky:** hliníková fólia (alobal), rôzne vodivé a nevodivé predmety (napr. kovový príbor, kovové nožnice, neizolovaný drôt, izolovaný drôt, atď.)

**Príprava pred hodinou:** Je potrebné na hodinu priniesť pomôcky (viď vyššie).

**Priebeh vyučovacej hodiny**


Diskusia so žiakmi:

*   Čo znamená, že je nejaký materiál vodivý? Čo ním preteká?
*   Vymenujte vodivé a nevodivé predmety.
*   Je ľudské telo vodivé? Čo by sa stalo, ak by sme sa chytili elektrického vedenia? Prečo by nám to uškodilo?

Učiteľ následne povie žiakom, že micro:bit vie snímať, že sme na jeho pinoch uzatvorili elektrický obvod. Piny sú malé kovové plôšky na spodnej strane micro:bitu (pomenovanie “pin” je z anglického jazyka, v slovenčine sa prekladá ako “kolík”, avšak toto pomenovanie môže byť na micro:bite zmätočné a preto používame pomenovanie “pin”). Na micro:bite sa nachádza 5 väčších pinov:



Diskusia: Čo by ste chceli ovládať pomocou micro:bitu? Čo by ste chceli skúmať/snímať?

Následne učiteľ zadá žiakom úlohu na naprogramovanie micro:bitu tak, aby snímal uzatvorenie okruhu na medzi pinom GND a pinom 0. Pri uzatvorení okruhu jedným krokosvorkovým káblom, micro:bit na chvíľu zobrazí srdce, a následne ho vymaže. Úlohou žiakov je zistiť, aký príkaz by mohli použiť na snímanie uzatvoreného okruhu (odpoveď: príkaz _keď sa kolík P0 stlačí_ z kategórie _Vstup_).

** Alobalové elektródy a človek ako súčasť obvodu**
V tomto kroku žiaci ku každému z káblov pripoja kus alobalu a obvod budú uzatvárať prstami alebo rukami.

Diskusia: Je táto aktivita bezpečná? Nie je zlé, že telom prechádza prúd?

_Odpoveď: Napätie a najmä prúd prechádzajúci telom pri tejto aktivite je tak malý, že nehrozí žiadne nebezpečenstvo. Ak by sme takto uzatvorili obvod v zásuvke, bolo by to smrteľne nebezpečné._


## Merač lásky
**Žiaci si v tejto aktivite vytvoria merač lásky medzi spolužiakmi. Ten funguje tak, že dvaja žiaci sa chytia buď pinu 0 alebo pinu GND (podobne ako v predchádzajúcej aktivite). Keď sa dotknú rukami, micro:bit zobrazí náhodné číslo od 0 po 100, ktoré symbolizuje, ako veľmi sa spolužiaci ľúbia (0 je vôbec, 100 je najviac).


```makecode
_LR1MzDbHeiPC
```

Žiaci následne prechádzajú po triede a zisťujú, ako veľmi sa “ľúbia".




Merač lásky so symbolmi**
Kód je možné upraviť tak, aby zobrazoval namiesto čísel symboly, a to nasledovne:



*   Ak je láska viac ako 80, zobraz srdce
*   Ak je láska viac ako 60, zobraz šťastného smajlíka
*   Ak je láska viac ako 40, zobraz zmäteného smajlíka
*   Ak je láska viac ako 20, zobraz smutného smajlíka
*   Inak zobraz nahnevaného smajlíka



```makecode
_iupRAT7jXg4T
```
