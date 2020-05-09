*V tejto aktivite sa zoznámiš s tlačidlami na BBC micro:bit - ako ich využiť pri tvorení vlastného programu a ako
zistiť, či boli stlačené. Prepojíme ich potom s animáciami na displeji.*

![Obrázok BBC micro:bitu](images/microbit_two_smile.png)

**Potrebné pomôcky:**  
BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený k internetu

Pracovať budeme v online prostredí [makecode.microbit.org](https://makecode.microbit.org/)

---

**Obsah aktivity:**

[TOC]

---

## Tlačidlá, všade okolo nás

Tlačidlá sú jedným z najrozšírenejších elektronických komponentov vôbec - nachádzajú sa na ovládačoch, práčkach,
hracích konzolách, platobných termináloch,... Používame ich na ovládanie elektroniky - vždy, keď chceme, aby nejaký
mikroprocesor niečo vykonal (napríklad poslal na naše poschodie výťah) oznámime mu to pomocou tlačidla.

Micro:bit má 2 tlačidlá, ktoré vieme využiť v našom programe (sú označené ako tlačidlá A a B).

## Stlačenie jedného tlačidla

Snímanie stlačenia tlačidla je na micro:bite veľmi jednoduché - stačí použiť príkaz `keď sa tlačidlo A stlačí`
z kategórie `Vstup`. Skús naprogramovať jednoduchý program, ktorý na stlačenie tlačidla A zobrazí šťastného smajlíka
a na stlačenie tlačidla B smutného smajlíka. Program si najprv vyskúšaj v simulátore a až potom ho nahraj na micro:bit.

```makecode
_WotWzfe3edtk
```
## Stlačenie dvoch tlačidiel

Skúsime teraz náš jednoduchý program doplniť aj o tretieho smajlíka - tento krát zmäteného. Toho zobrazíme na stlačenie
oboch tlačidiel naraz. Ako si ale program odskúšaš v simulátore? Ak si pozorne všimneš, po pridaní príkazu
`keď sa tlačidlo A + B stlačí`  sa ti v simulátore na pravej spodnej strane micro:bitu zobrazí nové biele tlačidlo A+B.
To samozrejme na skutočnom micro:bite nenájteš, nachádza sa iba v simulátore, aby bolo možné odskúšať stlačenie oboch
tlačidiel naraz.
    
```makecode
_YYbcCri139yV
```

## Animácia - smajlík prichádza a odchádza

Doteraz sme jednoducho zobrazovali obrázky, bez nejakej animácie. To teraz ale zmeníme - vytvoríme animáciu smajlíka,
ktorý k nám postupne prichádza a potom naopak odchádza. Pozri sa na animáciu nižšie:

![Animácia micro:bitu](images/makecode_smile_animation.gif)

Chce docieliť, aby pri stlačení tlačidla A sa nám z pravej strany postupne posúval smajlík, až kým ho neuvidíme celého.
Následne, keď stlačíme tlačidlo B, smajlík sa bude posúvať ďalej do ľavej strany a postupne odíde. Využijeme na to príkaz
`zobraziť LED`, a pre každý jeden snímok animácie použijeme osobitný príkaz `zobraziť LED`.

```makecode
_6g4iuUideezy
```

## Animácia naprieč micro:bitmi

Pre túto časť aktivity budete potrebovať 2 micro:bity.

Smajlíka máme pekne animovaného, na displej nám prichádza aj odchádza, ďalším krokom je animovať ho naprieč viacerými
micro:bitmi. Postupne sa bude zobrazovať na jednom micro:bite, a potom postupne predje na druhý. Vytvoríme teda dve
animácie, na jednom micro:bite sa začne ihneď po stlačení oboch tlačidiel naraz a na druhom micro:bite až po niekoľkých
sekundách. Ako ale určiť, po koľkých sekundách? Najjednoduchšie je odmerač čas stopkami a potom na začiatku
animácie pre druhý micro:bit použiť príkaz `pozastaviť (ms)`.

![Animácia BBC micro:bitu](images/makecode_smile_animation_moving.gif) 

```makecode-no-link
_H8ViD53xecrd
```

```makecode-link-only
_bECDj52XxUzo
```

## Bliknutie srdiečkom
Poslednou úlohou aktivity je vytvoriť "bliknutie" srdiečkom - po stlačení tlačidla sa na 5 sekúnd zobrazí srdiečko,
a následne zmizne.

To, ako zobraziť obrázok na 5 sekúnd už vieme, ale ako vymazať obrazovku? Môžme to spraviť dvoma spôsobmi - buď
príkazom `zobraziť LED`, ktorý necháme prázdny, alebo príkazom `Vymazať obrazovku` z kategórie `Základné -> more`

```makecode
_0vjfTmdeMfCf
```

## Zhrnutie aktivity
V tejto aktivite sme sa naučili používať tlačidlá micro:bitu v našich programoch. Budeme ich používať často,
keďže tlačidlá sú jedným z najčastejšie používaným elektronickým komponenetom. Nie je to však jediný spôsob, akým vieme
micro:bitu povedať, aby niečo spravil - už v ďalšej aktivite sa pozrieme, ako ovládať micro:bit pomocou pohybu.

