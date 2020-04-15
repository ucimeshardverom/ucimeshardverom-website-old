!!! warning "Pracujeme..."
    Táto kapitola je ešte rozpracovaná, zatiaľ tu nájdeš iba základné informácie. V najbližšom čase ju budeme ešte dopĺňať.

Micro:bit má na sebe dve tlačidlá, ktoré sú označené ako tlačidlo A a tlačidlo B a ktoré môžeme využiť v našich programoch. V tomto videu naprogramujeme z micro:bitu digitálne zvieratko, ktoré bude meniť náladu podľa toho, ktoré tlačidlo stlačíme.

## Tlačidlá
Pre prácu s tlačidlami použijeme triedy ``button_a`` a ``button_b`` z modulu ``microbit``.


## Vypísanie počtu stlačení

```python
from microbit import button_a

sleep(10000)
display.scroll(str(button_a.get_presses()))
```

Po nahratí na micro:bit niekoľko krát skúste stlačiť tlačidlo A. Počet stlačení by sa mal po 10 sekundách zobraziť na obrazovke.

## Zmena obrázku tlačidlami

```python
from microbit import display, Image, button_a

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
```

```python
from microbit import display, Image, button_a, button_b

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
    	display.show(Image.SAD)
```

```python
from microbit import display, Image, button_a, button_b

while True:
	if button_a.is_pressed() and button_b.is_pressed():
		display.show(Image.CONFUSED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
    	display.show(Image.SAD)

```

```python
from microbit import display, Image, button_a, button_b

while True:
	if button_a.is_pressed() and button_b.is_pressed():
		display.show(Image.CONFUSED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
    	display.show(Image.SAD)
    else:
    	display.clear()

```

Posledná zmena: **28.2.2020**