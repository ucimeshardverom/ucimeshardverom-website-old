# ZOZNÁMENIE SA S BBC MICRO:BIT
## Metodika pre učiteľa

// LEFT

**Pomocné materiály:**

* [Prezentácia](https://docs.google.com/presentation/d/1vOICpiGi3lTlwDjeM0e6PvuOnQ216CdlAWIpGqKuKeU/edit?usp=sharing)

**Potrebné pomôcky:**  
Pre každého žiaka (alebo skupinu žiakov) BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený na internet.


**Ciele:**

* Zozámiť sa s programovateľným mikropočítačom BBC micro:bit
* Spoznať hardvérové časti zariadenia BBC micro:bit
* Naučiť sa pracovať v prostredí MakeCode
* Využiť simulátor v prostredí MakeCode na ladenie programu


// RIGHT

**Potrebné predchádzajúce znalosti:**  
Žiadne, táto kapitola je určená začiatočníkom.

**Odhadovaný čas:** 45 minút (nezabudnite na čas potrebný na rozdanie pomôcok, zozbieranie a záverečnú
diskusiu/reflexiu)

**Harmonogram aktivít:**

[TOC]

// END


---

### Príprava pred hodinou

Príprava trvá približne 15 až 20 minút. Pred hodinou je vhodné nahrať na všetky micro:bity "zoznamovací" program s názvom
*Out of the Box Experience* určený na zoznámenie sa so zariadením.

Zároveň je vhodné ubezpečiť sa, že na micro:bitoch je najnovší firmvér a v prípade potreby ho aktualizovať (návod ako
nájdete v sekcii [Začni -> Firmvér](https://ucimeshardverom.sk/zacni/firmver/))

Úvodný program stiahnete tu: [https://support.microbit.org/helpdesk/attachments/19033089764](https://support.microbit.org/helpdesk/attachments/19033089764) 

---
### Priebeh hodiny

#### Úvod k mikroprocesorom [10 min]
Hodinu začneme diskusiou na tému využitia mikroprocesorov **(slajd č. 2)**.

Spýtajte sa žiakov otázky:

* Čo je to mikroprocesor?
* Kde sa používa? Skúste uviesť nejaké príklady.

Počkajte, kým žiaci uvedú niekoľko svojich nápadov, a potom prejdite na **(slajd č. 3)**. Okrem uvedených príkladov
(detailnejšie sú popísané v *návode* tejto kapitoly) skúste nadviazať aj na príklady, ktoré uviedli žiaci.

Následne premostite k tomu, ako mikroprocesory interagujú s okolím **(slajd č. 4)**. Uveďte konkrétne vstupy/výstupy
pre spomenuté zariadenia (napríklad mikroprocesor práčky má ako vstup tlačidlá a otočné gombíky, ako výstup zas displej
a ovládanie motora/čerpadla práčky).

#### Predprogramovaný micro:bit [5 min]
Táto časť hodiny je zameraná na zoznámenie sa so zariadením. Rozdajte žiakom micro:bit (naprogramovaný) a USB
kábel (osobitne, nie už zapojené). Žiadne iné pomôcky žiak zatiaľ nepotrebuje, ani batérie k micro:bitu.

Vyzvite žiakov, aby microbit pomocou kábla pripojili k počítaču a zistili, čo od nich micro:bit "chce" **(slajd č. 5)**.
Odporúčame žiakov chvíľu sa nechať “vytrápiť”, čiže nedať im hneď odpoveď na to, kam zapojiť kábel.
Ak niekto so žiakov správne pripojí micro:bit k počítaču, vyzvite ho, aby poradil spolužiakom.

Ako pomôcku pri prechádzaní predprogramovanou hrou môžte zobraziť žiakom **slajd č. 6**.

Nechajte žiakom chvíľu čas, nech si sami prejdú programom, a keď niektorí skončia skôr ako ostatní, nechajte ich hrať sa
hadíka na konci programu (stlačením oboch tlačidiel naraz).

// NEWPAGE

#### Skúmanie micro:bitu [5 min]
Spýtajte sa žiakov otázku **(slajd č. 7)**:

* Aké senzory má micro:bit?

Žiakov naveďte, aby si všimli porozorne dosku micro:bitu - senzory sú tam totižto vymenované. Pomôžte im prezentáciou
**(slajd č. 8)**.
 
Ku každej vymenovanej súčiastke môžete uviesť, na čo sa využíva (podľa popisu v *návode* tejto kapitoly). 

#### Vypísanie textu na displeji [10 min]

Táto časť hodiny je najkritickejšia, nakoľko žiaci sa musia naučiť vytvoriť si vlastnú program a stiahnuť si ho na
micro:bit. Keď ale zvládnu túto operáciu, ďalšia práca s micro:bitmi bude pre nich malinou :-)

Povedzte žiakom cieľ hodiny: vytvoriť menovku, ktorá bude neustále zobrazovať ich meno (prípadne obrázok k tomu).

Uistite sa, že všetci žiaci majú micro:bit pripojený k svojmu počítaču a povedzte im, aby si otvorili web stránku
[makecode.microbit.org](https://makecode.microbit.org) **(slajd č. 9)**.

V samotnom prostredí ešte skontrolujte, či nejaký žiak nepotrebuje pomôcť s prepnutím do Slovenského jazyka
**(slajd č. 10)**.

Žiakov naveďte na príkaz `zobraziť reťazec` z kategórie `Základné` podľa *návodu* tejto kapitoly **(slajd č. 11)**.
Následne im pomôžte stiahnuť program na micro:bit (po úspešnom odskúšaní programu v simulátore).

#### Zobrazovanie obrázkov [5 min]
Keď už žiaci majú vlastnú "menovku", ktorá vypisuje ich meno, doplnia ju o vlastný obrázok **(slajd č. 12)**.

Obrázkov môžu pridať aj niekoľko, či už príkazok `zobraziť LED` alebo `zobraziť ikonu`.

#### Pauzy medzi príkazmi [5 min]
Posledným krokom tvorby menovky je upaviť program tak, aby sa jeden obrázok zobrazil 15 sekúnd. Toto spravia žiaci pomocou
príkazu `pozastaviť (ms)` **(slajd č. 13)**.

Uistite sa, či žiaci rozumejú, čo sú to milisekundy - a ak nie, preveďte im niekoľko príkladov prevodu medzi sekundami
a milisekundami na tabuľu.

#### Diskusia a zhrnutie aktivít [5 min]

Na záver veďte so žiakmi diskusiu o microbitoch a o využití mikroprocesorov v každodennom živote:

Otázky:

* Kde ešte používame mikroprocesory (okrem už spomenutých na začiatku hodiny)?
* Aké veľké/malé sú mikroprocesory (aký veľký je mikroprocesor na micro:bite)?
* Aké vstupy môžu mať mikroprocesory?
* Aké výstupy môžu mať mikroprocesory?
* Ako by ste micro:bit využili vy? Čo by ste si spravili? **(slajd č. 14)**


!!! warning "Reflexia"
    
    Na konci hodiny je správny priestor aj na reflexiu žiakov. Pri nej sú žiaci vyzvaní, aby hodnotili nielen aktivity,
    ale aj svoju prácu na hodine, prípadne prácu svojich spolužiakov. Vytvoriť tým môžete aj väčšiu zodpovednosť
    u žiakov za vlastný proces vzdelávania.  
    
    Návodov, ako správne viesť reflexiu je mnoho, pekné zhrnutie nájdete na
    [eduworld.sk](https://eduworld.sk/cd/jaroslava-konickova/4005/ako-rozvijat-sebareflexiu-a-sebahodnotenie-ziakov)