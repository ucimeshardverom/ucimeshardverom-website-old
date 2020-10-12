Title:	Môj prvý program

Náš prvý program vyskúšame spraviť v online prostredí [makecode.microbit.org](https://makecode.microbit.org/).
V ňom si vytvoríme digitálnu "menovku", ktorá bude zobrazovať naše meno a aj nejaké obrázky. Bude nám k tomu stačiť iba
BBC micro:bit a micro USB kábel.

## Napísanie programu
V prostredí [MakeCode](https://makecode.microbit.org/) klikneme na *Nový projekt*. V prípade, že máte prostredie
v anglickom jazyku, prepnúť ho viete kliknutím na ozubené koliesko hore vpravo, kde v sekcii *Language* vyberieme
*Slovenčinu*.

![Animácia výberu jazyka v MakeCode](images/makecode_language.gif)

V našom prostredí máme 3 časti:

* Vpravo je miesto na tvorbu nášho programu.
* V strede je knižnica príkazov, ktoré môžeme použiť.
* Na ľavej strane je simulátor.

Keďže cheme vytvoriť menovku, musíme na displej vypísať naše meno. To spravíme príkazom *zobraziť reťazec* z kategórie
*Základné*, ktorý vložíme do príkazu *vždy*. Následne doň vpíšeme svoje meno, ktoré by sa nám malo na simulátore začať zobrazovať.

![Animácia tvorby kódu v MakeCode](images/makecode_string.gif)

Do programu ešte pridáme obrázok pomocou príkazu *zobraziť LED* z kategórie *Základné*.

![Animácia tvorby kódu v MakeCode](images/makecode_heart.gif)

Keď sme so svojím programom spokojní, môžeme kliknúť na tlačilo *Stiahnuť*, ktoré stiahne náš program s príponou *.hex* na
počítač.

Posledný krok, ktorý nám zostáva, je nahrať náš novo vytvorený program na samotný micro:bit. Ten si môžeme pripojiť
k počítaču pomocou klasického micro USB kábla, aký sa bežne používa na mobilné telefóny. V počítači potom uvidíš,
že micro:bit sa pripojil ako USB zariadenie, skoro ako keby to bolo klasické USB úložisko. Naň stačí už len stiahnutý
program s príponou *.hex* skopírovať. Indikačná LEDka na micro:bite by sa mala na chvíľu rozblikať a po chvíľke
začne micro:bit vypisovať naše meno spolu s obrázkom srdca.

Vždy pred nahratím vytvoreného programu vyskúšame správnosť na simulátore v ľavej strane online
prostredia. V tomto prípade by mal zobrazovať naše meno. Ak simulátor nezobrazuje to, čo bolo cieľom programu,
je potrebné doladiť program a nájsť v ňom chybu.