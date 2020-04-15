!!! warning "Pracujeme..."
    Táto kapitola je ešte rozpracovaná, zatiaľ tu nájdeš iba základné informácie. V najbližšom čase ju budeme ešte dopĺňať.

## Menovka

Ako si si mohol/mohla všimnúť, micro:bit má na svojej prednej strane 5x5 červených LED diód. MicroPython Ti dáva viacero možností, akými na displeji niečo vykreslovať či vypisovať.

Najbežnejším prvým programom pri učení sa nového programovacieho jazyka býva vypísanie textu "Ahoj, Svet!". 

V MicroPythone vieme napísať tento program v dvoch riadkoch kódu:

```
from microbit import display
display.scroll("Ahoj, Svet!")
```

Každý riadok vykaná niečo iné. Prvý riadok:
```
from microbit import dispay
```

povie micro:bitu, aby pre nás pripravil funkcionalitu ``display`` z modulu ``microbit``. Tento modul obsahuje predprogramované funkcie, ktoré ovládajú napríklad zobrazovanie textu na obrazovke. Takéto 'zavolanie' voláme ``import``. Moduly sa taktiež niekedy nazývajú aj knižnicami (no namiesto kníh majú v sebe kód).

Druhý riadok:
```
display.scroll("Ahoj, Svet!")
```

povie micro:bitu, aby na displej postupne vypísal reťazec znakov "Ahoj, Svet!". Slovo ``display`` je objekt z modulu ``microbit``, ktorý predstavuje fyzický displej zariadenia (hovoríme „objekt“ namiesto „hento“, „oné“ alebo „tá vec“). Za objekt sme napísali bodku, za ktorou nasleduje príkaz (po správnosti nazývaný `metóda`). V tomto prípade používame metódu ``scroll``, čo po slovensky znamená posúvať. Aby ale micro:bit vedel, aký text má na obrazovke posúvať, musíme ho označiť pomocou dvojitých úvodzoviek ``"`` (na začiatku a aj na konci) a poslať do príkazu scroll. To spravíme vložením textu do  zátvoriek za metódou ``scroll()``. Obsah zátvoriek nazývame argument. Takže display.scroll("Ahoj, svet!") znamená po slovensky „Chcem, aby si použil displej a posúval na ňom text ‚Ahoj, svet!‘“. Ak metóda nepotrebuje argumenty, musíme to dať jasne najavo použitím prádznych zátvoriek - takto: ``scroll()``.

Teraz svoj kód ešte skontroluj - či už opticky, alebo v `Mu editore` pomocou tlačidla `check` (veľký palec). Ak si v programe nenašiel žiadne chyby, nahraj ho na micro:bit (v Mu editore pomocou tlačidla `Flash`).

Ak by si chcel zistiť, aké iné argumenty môžeš pre príkaz ``scroll()`` použiť, pozri si [dokumentáciu](https://microbit-micropython.readthedocs.io/en/latest/display.html?highlight=scroll#microbit.display.scroll>)

!!! warning
    
    Je možné, že Ti program nebude fungovať hneď na prvý krát. Nezľakni sa, ani skúseným programátorom väčšinou nevýjde všetko hneď na prvý krát.

!!! primary "Úloha č. 1"
	Pozmeň program tak, aby si z neho spravil digitálnu menovku a vypisoval Tvoje (krstné) meno.

!!! primary "Úloha č. 2"
	Doplň program tak, aby okrem Tvojho mena zobrazoval aj to, v ktorom meste bývaš. Výsledný program by mal mať 3 riadky kódu (vrátane riadka, kde importujeme).

!!! primary "Kontrolné otázky"
	* Čo je to argument metódy?
	* Ak do metódy neposielam žiadne argumenty, musím písať zátvorky?

## Trvalé zobrazovanie textu

Podarilo sa nám text vypísať na obrazovku, avšak zatiaľ sa vždy vypíše iba jeden krát. No čo ak si chceme spraviť menovku, ktorá by stále ukazovala Tvoje krstné meno? Potrebujeme nejakým spôsobom docieliť, aby sa náš riadok kódu s príkazom ``display.scroll()`` donekonečna spúšťal. Môžme skúsiť daný riadok skopírovať čo najviac krát::

```
from microbit import display
display.scroll("Volam sa Marek")
display.scroll("Volam sa Marek")
display.scroll("Volam sa Marek")
display.scroll("Volam sa Marek")
display.scroll("Volam sa Marek")
# atď.
```

ale aj tak sa raz vykonávanie programu skončí. Potrebujeme preto nekonečný cyklus::

```
from microbit import display
while True:
    display.scroll("Volam sa Marek")
```

Príkaz ``while`` sa vždy pozerá na to, čo sme napísali za neho. Pokým je za ním pravdivá hodnota tak bude vykonávať všetky príkazy prislúchajúce do daného cyklu. A keďže ``True`` (anglicky `pravda`) je vždy pravdivé, tak micro:bit bude kód opakovať donekonečna. To, či nejaký kód patrí do cyklu zistíš tak, že ďaľšie riadky sú posunuté do prava o 4 medzerníky (jeden tabulátor - kláves nad CapsLock-om). Toto posunutie sa po slovensky volá `odsadenie` a po anglicky `indentation` čiže `indentácia`.

Všimni si, že na konci riadku s príkazom ``while`` sa nachádza dvojbodka. Tá sa vždy používa v kombinácií s príkazmi, po ktorých aspoň jeden ďaľší príkaz odsadíš a bude sa vykonávať na základe toho, aká je podmienka v riadku s dvojbodkou.

Pozrime sa teraz na tento kód:

```
from microbit import display
while True:
    display.scroll("Marek")
    display.scroll("Z Bratislavy")
display.scroll("toto sa nikdy nevypise")
```
Z kódu vieme vyčítať, že donekonečna budeme vypisovať "Marek" a "z Bratislavy". Príkaz s textom "toto sa nikdy nevypise" nie je odsadený, a tak nie je súčasťou while cyklu. Preto by sa vykonal až keď while cyklus skončí. Ten ale nikdy neskončí, keďže ``True`` má vždy pravdivú hodnotu, a tak sa tento riadok kódu nikdy nespustí.

Kým v predchádzajúcej ukážke sa posledný riadok kódu nikdy nespustí, aspoň sa nám zobrazovali príkazy "Marek" a "z Bratislavy". Čo ak by sme ale doplnili takýto riadok:

```
from microbit import display
while True:
    display.scroll("Marek")
    display.scroll("Z Bratislavy")
display.scroll("toto sa nikdy nevypise")
	display.scroll("dalsi riadok")
```

V tomto prípade by nám program vôbec nespustil a vypísal by chybu, pretože posledný riadok je odsadený aj keď by nemal byť.


!!! primary "Chyby sú bežné..."
	Skús spustiť posledný kód (s nesprávnym odsadzovaním) a zistiť, aký chybu vypíše micro:bit na displej.


!!! primary "Kontrolné otázky"

   * O koľko medzerníkov sa odsadzuje príkaz patriaci do cyklu?
   * Na čo v nekonečnom cykle využívame príkaz ``True``?
   * Koľko najviac príkazov za sebou môže byť v jednom nekonečnom cykle?

## Pauza medzi vypisovaním textu

Čo ak by sme chceli medzi dva výpisy textu na obrazovku pridať nejakú pauzu, napríklad 5 sekúnd? Využijeme príkaz, ktorý micro:bitu povie, aby chvíľu počkal::

```
from microbit import display, sleep

display.scroll("Ahoj")
sleep(5000)
display.scroll("Ako sa mas?")
```

Príkaz ``sleep()`` sme vložili medzi dva výpisy textu, a tak sa najprv zobrazí text "Ahoj", chvíľu počká a potom vypíše text "Ako sa mas?". To, ako dlho má čakať povieme micro:bitu pomocou argumentu, ktorý napíšeme do zátvoriek za metódou ``sleep``. Tento krát vkladáme číslo a nie reťazec, preto nepoužívame úvodzovky ``"``. Napíšeme tam, koľko milisekúnd má micro:bit čakať. Jedna milisekunda je tisícina sekundy, 1000 milisekúnd je 1 sekunda a 5000 milisekúnd je 5 sekúnd, čiže náš kód počká 5 sekúnd.

!!! primary "Úlohy"
	* Využi príkaz ``sleep()`` v nekonečnom cykle.
	* Uprav nasledujúci kód tak, aby micro:bit vypísal "Ahoj Martin", počkal 3 sekundy, vypísal "Ahoj Vanessa" a zas počkal 3 sekundy::

```
from microbit import display

while True:
    display.scroll("Ahoj Martin")
    display.scroll("Ahoj Vanessa")
```

!!! primary "Kontrolné otázky"

	* Čo sa stane, ako použijeme viac príkazov ``sleep()`` za sebou?
	* Akú chybu vypíše micro:bit ak by sme namiesto čísla poslali to metódy ``sleep`` reťazec označený úvodzovkami (napríklad ``sleep("5000")``)?

Posledná zmena: **28.2.2020**