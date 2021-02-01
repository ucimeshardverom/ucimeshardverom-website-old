Title:   	Zvuk

# Zvuk
## micro:battle #2

// LEFT

![](images/bananovy-klavir.png)

// RIGHT

<div markdown="1" class="lection-desc">
Táto hodina je zameraná na tvorbu jednoduchého banánového klavíra pomocou micro:bitov.  
Pred hodinou je vhodné, aby žiaci a žiačky už mali skúsenosti s prehrávaním hudby na micro:bite.
</div>

**Potrebné pomôcky:** BBC micro:bit, USB kábel, krokosvorkové káble, banány, alobal a počítač.  
Pracovať budeme v online prostredí [makecode.microbit.org](https://makecode.microbit.org/)

Pred aktivitami s micro:bitmi by si žiaci a žiačky mali pozrieť video youtubera GoGa [s hudobným producentom Yakshom](https://www.youtube.com/watch?v=kq7v1HTrulw) (ako prípravu na hodinu).

// END

Táto hodina neobsahuje postup, ako pripojiť k micro:bitu reproduktor a ako prehrávať tóny. Ten nájdete v digitálnej databáze enter.study -- [lekcia "PROGRAMOVANIE HUDBY"](https://enter.study/navod/programovanie-hudby-zahraj-kohutika-jarabeho/) (odporúčame si ju prejsť so žiakmi a žiačkami pred tvorbou banánového klavíra).

### 1. Otvorenie hodiny

Pred začatím aktivít s micro:bitmi sa žiakov a žiačok spýtajte, čo nové sa dozvedeli vo videu [s GoGom a Yakshom](https://www.youtube.com/watch?v=kq7v1HTrulw). Možné témy:

* Na akom hudobnom nástroji hrali GoGo a Yaksha vo videu? *(Banánový klavír.)*
* Hranie na banánovom klavíri vo videu veľmi nefungovalo. Vedeli by žiaci a žiačky odhadnúť prečo? *(Banány sú vodivé a keďže boli poukladané husto vedľa seba, navzájom sa dotýkali. Dotyk jedného banánu preto micro:bit mohol vyhodnotiť ako dotyk viacerých banánov. Detailnejšie tomu bude možné porozumieť po prejdení si nasledujúcich aktivít.)*
* Ako technológie ovplyvňujú hudobnú produkciu? *(Vo videu bola spomenutá napr. hudba vytvorená čisto umelou inteligenciou.)*

### 2. Zapojenie banánového klavíra

// LEFT

Zapojenie banánového klavíra je relatívne jednoduché, postačuje k tomu micro:bit, krokosvorkové káble, reproduktor, kúsok alobalu a samozrejme banány. Pripojenie reproduktoru k micro:bitu je vysvetlené v [lekcii "PROGRAMOVANIE HUDBY"](https://enter.study/navod/programovanie-hudby-zahraj-kohutika-jarabeho/), no pri banánovom klavíri je potrebné zapojenie trošku upraviť -- kolík *GND* neprepájame s *3,5 mm JACKom* priamo, ale pomocou dvoch krokosvorkových káblikov, medzi ktoré dáme kúsok alobalu. Toho sa budeme pri hraní na klavíri jednou rukou držať.

Dva banány je potrebné prepojiť krokosvorkovými káblikmi ku *kolíku 1* a *kolíku 2* na micro:bite. Pri zapájani môže pomôcť schéma zapojenia (vpravo) alebo fotka výsledného zapojenia (hore).

// RIGHT

![Schéma zapojenia banánov a reproduktoru](images/schema.png)

// END

!!! info "Programovanie hudby na micro:bite"
    Micro:bit dokáže prehrávať melódie pomocou kategórie *"Hudba"* v prostredí MakeCode:

    - Prehrávanie predprogramovaných melódií príkazom *"spustiť melódiu"*.
    - Prehrávanie vlastných piesní a melódií tón po tóne pomocou príkazu *"prehrať tón Stredné C trvanie 1 úder"*.

    Detailný návod, ako prehrávať hudbu na micro:bite, nájdete v [lekcii "PROGRAMOVANIE HUDBY"](https://enter.study/navod/programovanie-hudby-zahraj-kohutika-jarabeho/).

// NEWPAGE

### 3. Program pre banánový klavír

// LEFT

Najjednoduchší spôsob, ako pri dotyku banánu prehrať tón na reproduktore, je pomocou príkazu `keď sa kolík P1 stlačí` z kategórie "Vstup" a príkazu `prehrať tón Stredné C trvanie 1 úder` z kategórie "Hudba". Pri dotknutí prvého banánu (pripojeného ku kolíku 1) sa prehrá tón *"Stredné C"* a pri dotknutí druhého banánu sa prehrá tón *"Stredné D"*. Výsledný program sa nachádza vpravo.

Po nahratí programu na micro:bit môžu žiaci a žiačky klavír vyskúšať -- jednu ruku položia na kúsol alobalu a druhou rukou sa iba krátko dotknú jedného z banánov. Micro:bit by mal následne prehrať tón.

// RIGHT


```makecode-no-link
_4a3Cko7HY8i2
```

```makecode-no-link
_3RDCELHe0L1Y
```

```makecode-link-only
_HHh4m1gqFcJu
```
// END

Žiaľ, keďže micro:bit má iba tri programovateľné kolíky, z čoho jeden sa používa na pripojenie reproduktora, zostávajú už iba dva na pripojenie banánov. Na dvojtónovom klavíri toho ale žiaci veľa nezahrajú -- práve preto môžu viacerí žiaci a žiačky pracovať na tvorbe jedného veľkého klavíra, a to tak, že každý vytvorí časť klavíra. Prvý žiak alebo žiačka pripojí k micro:bitu reproduktor a dva banány a bude prehrávať tóny *"Stredné C"* a *"Stredné D"*. Druhý žiak alebo žiačka tiež pripojí k svojmu micro:bitu reproduktor a dva banány, no bude prehrávať tóny *"Stredné E"* a *"Stredné F"*. Micro:bit tretieho žiaka alebo žiačky bude prehrávať tóny *"Stredné G"* a *"Stredné A"*. Nakoniec žiaci a žiačky svoje micro:bity aj s banánmi a reproduktormi vedľa seba poukladajú a vznikne jeden veľký klavír. Aby prehrávanie fungovalo, je vhodné prepojiť všetky tri kúsky alobalu, ktoré sú pripojené ku kolíkom *GND*, navzájom krokosvorkovými káblikmi.

!!! info "Prečo mi to nefunguje?"
    * Je na micro:bite nahratý správny program? Niekedy je vhodné "overiť" si to opätovným nahratím programu na micro:bit.
    * Sú banány a reproduktor správne pripojené? Porovnajte si zapojenie s obrázkom zapojenia vyššie. Krokosvorky sa na micro:bite musia dotýkať vždy iba jedného veľkého kolíka bez toho, aby sa dotýkali menších kolíkov (kovových plôšok) po stranách.
    * Banány sa nesmú navzájom dotýkať a tiež nie je možné prehrať oba tóny naraz dotknutím sa oboch banánov.
    * Niekedy snímanie dotyku banánov nefunguje správne, ak je micro:bit napájaný z počítača pomocou USB kábla. Vtedy odporúčame odpojiť micro:bit z počítača a napájať ho pomocou batérií.


### 4. Záverečná diskusia

V rámci záverečnej diskusie môžete nechať žiakov a žiačky porozmýšľať, ako by sa dal banánový klavír vylepšiť. Tu máte niekoľko návrhov:

* Prehrávané tóny by nemuseli trvať rovnako dlho, ale micro:bit by začal daný tón hrať v momente, kedy sa banánu dotkneme, a prestane ho hrať hneď, ako banán pustíme. *(Toto je možné aj so súčasným hardvérovým zapojením, no program v MakeCode by bol náročnejší -- vyžadoval by využitie podmienok a premenných.)*
* Namiesto toho, aby mal každý micro:bit svoj vlastný reproduktor, vylepšený klavír by mohol mať reproduktor iba na jednom z micro:bitov a zvyšné micro:bity by mu bezdrôtovo posielali príkazy, kedy má prehrať ktorý tón. *(Videonávod, ako to spraviť, nájdete na stránke enter.study v sekcii [Ako na to](https://enter.study/ako-na-to/). Je ale potrebné, aby najprv žiaci vedeli pracovať s kategóriou "Rádio" v prostredí MakeCode.)*

Zároveň sa môžete so žiakmi a žiačkami vrátiť k problému z videa, v ktorom prehrávanie hudby nefungovalo správne -- nechajte ich odskúšať, či bude prehrávanie hudby fungovať aj v prípade, že sa banány navzájom dotýkajú.

!!! info "Aktivity navyše"
    - Žiaci a žiačky môžu namiesto banánov vyskúšať aj iné ovocie. *(Na pripájanie krokosvoriek na povrch ovocia sú najlepšie banány a citrusy s hrubou kôrou. Jablká a hrušky sú horšie -- väčšinou je potrebné zatlačiť krokosvorku až do vnútra dužiny, pričom z ovocia môže kvapkať šťava.)*
    - Žiaci a žiačky majú pomocou internetu nájsť nejakú skladbu alebo album, ktorý zložila umelá inteligencia.  
    *(Napríklad album [I AM AI](https://refresher.sk/46496-Umela-inteligencia-vytvorila-svoj-prvy-hudobny-album-Ma-sa-stat-hudobnou-revoluciou) alebo [AI/DC](https://break.cas.sk/2020/05/19/bude-umela-inteligencia-pre-nas-skladat-aj-hudbu/).)*