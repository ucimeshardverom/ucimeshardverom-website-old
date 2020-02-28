!!! warning "Pracujeme..."
    Táto kapitola je ešte rozpracovaná, zatiaľ tu nájdeš iba základné informácie. V najbližšom čase ju budeme ešte dopĺňať.


Čo sa týka grafického umenia, MicroPython ja asi rovnako dobrý ako človek, ktorý má k dispozícii iba 5x5 červených LED diód. Napriek tomu má MicroPython pomerne veľa možností, ako ovládať displej, a vytvoriť si tým rôyne efekty a animácie.

## Predprogramované obrázky
Ako prvé si vyskúšame zobraziť na displeji už predprogramované obrázky. Opäť budeme používať displej, a preto z knižnice microbit importujeme modul displej, no tento raz z tej istej knižnice importujeme aj triedu s predprogramovanými obrázkami Image.

```
from microbit import display, Image

display.show(Image.HAPPY)
```

Keď chceme obrázok zobraziť na displeji, namiesto metódy scroll zavoláme metódu ``show`` (píšeme ``display.show()``). Aby micro:bit vedel, čo má zobraziť, posielame v zátvorkách ako parameter obrázok z triedy ``Image`` - napríklad ``happy`` (``Image.HAPPY``). Predprogramovaných obrázkov je veľké množstvo, nájdete ich v dokumentácii.


Prvý obrázok sme zobrazili, teraz sa pokúsme zobraziť dva, ktoré sa budú donekonečna striedať. Asi už tušíte, že opäť využijeme nekonečný cyklus ``while True:``, a príkaz display ``show`` pod ním odsadíme o štyri medzerníky, alebo jeden tabulátor.

```
from microbit import display, Image, sleep

while True:
	display.show(Image.HAPPY)
	sleep(1000)
	display.show(Image.HAPPY)
	sleep(1000)
```

Tento program zobrazuje najprv jeden a potom druhý obrázok, ale keby sme tam nedali žiadne pauzy, robil by to tak rýchlo, že by sme ich tam ani nevideli a obrázky by splinuli. Preto vždy, keď vykreslíme obrázok musíme na chvíľu pozastaviť, aby naše oko stihlo obrázok vidieť. Na to použijeme príkaz ``sleep`` z knižnice ``microbit``. Prvý krok je importovať ``sleep``, a následne ho použiť za oboma obrázkami. Ako parameter udávame, koľko milisekúnd má program čakať - číslo nedávame do úvodzoviek, pretože sa jedná o číslo a nie o text. Aby sa nám menili každú sekundu, ako parameter vpíšeme číslo 1000.



## Vlastný obrázok

```
from microbit import display, Image, sleep

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")
while True:
	display.show(Image.HAPPY)
	sleep(1000)
	display.show(Image.HAPPY)
	sleep(1000)
	display.show(boat)
	sleep(1000)
```

Obrázkov môžeme pridať aj viac, no môžeme skúsiť pridať aj vlastné. Vytvorme si napríklad vlastnú loďku. Ešte pred nekonečným cyklom si zadefinujeme, ako má vyzerať. Opäť pomocou triedy ``Image``, ale tentokrát ako parameter vkladáme 5 riadkov, v každom 5 čísel, jedno pre každú LED diódu. 0 znamená, že LEDka nesvieti, 9 naopak, svieti naplno. Teraz sme vytvorili loďku s dvoma sťažňami. Dvojbodky na konci riadkov označujú koniec riadku na LED displeji. Náš nový obrázok sme si pomenovali ``boat``, a ak ho chceme zobraziť, stačí ho vložiť do ``display.show(boat)``

Tento kód je možné skrátiť aj na:

```
from microbit import display, Image, sleep

boat = Image("05050:05050:05050:99999:09990")

while True:
	display.show(Image.HAPPY)
	sleep(1000)
	display.show(Image.HAPPY)
	sleep(1000)
	display.show(boat)
	sleep(1000)
```
Takéto skrátenie je ale veľmi neprehľadné, a preto odporúčame radšej prvý spôsob.

[Návod na tvorbu vlastných obrázkov](https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html#diy-images) je v dokumentácii
