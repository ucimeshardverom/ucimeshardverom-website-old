!!! warning "Online editor je fajn, ale..."
    odporúčame radšej používať Mu editor, nakoľko má viac funkcionalít. Online editor pomôže tam, kde potrebujeme rýchlo nahrať nejaký program do Micro:bitu bez inŠtalácie Mu editoru (napríklad aj na workshopoch).


[Online MicroPython Editor](http://python.microbit.org/) je ďaľší online editor, no tento krát je určený pre tvorby MicroPython kódu. Ani pri tomto spôsobe programovania nie je potrebná inštalácia softvéru na počítač či administrátorské práva, stačí prístup na internet a internetový prehliadač.


Na obrazovke sa Vám ukáže jednoduchý program:
```python
# Add your Python code here. E.g.
from microbit import *


while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)
```

* __from micobit import \*__ - tento príkaz nám v kóde sprístupní všetku funkcionalitu knižnice microbit, vďaka ktorej vieme pristupovať k hardérovej funkcionalite micro:bitu.
* __while True:__ - tento príkaz nám bude donekonečna vykonávať kód, ktorý prislúcha do daného while cyklu
* __Indentácia__ . v Pythone (na rozdiel od iných jazykov) sa kód prislúchajúci do bloku neoznačuje zátvorkami, ale pomocou odsadzovania, čiže indentácie. Aby nejaký kód prislúchal pod príkaz _while_, musí byť odsadený aspoň o jeden tabulátor (štyri medzerníky)
* __display.scroll()__ vypíše daný reťazec na obrazovku
* __display.show(Image.HEART)__ vykreslí daný obrázok na obrazovku
* __sleep()__ - funkcia sleep pozastaví micro:bit na zadaný počet milisekúnd
* __poznámky__ - poznámky sa v Pythone tvoria mriežkou (#)

Ako ale zistíme, aké možné obrázky môžeme vykresliť? Na to nám slúži [online micro:bit MicroPython dokumentácia](http://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html), v ktorej je zoznam všetkých príkazov, ktoré je možné použiť.