Title:	Firmvér

## Čo je to firmvér?

**Hardvér** je fyzická časť micro:bitu (doska plošných spojov, senzory, konektory).

**Softvér** je tvoj program, ktorý vytvoríš napríklad v MakeCode alebo v MicroPythone a nahráš na micro:bit.

**Firmvér** je tá časť uprostred – je uložený na micro:bite a pomáha vykonávať tebou napísaný program. Firmvér sa nedá zmeniť klasickým nahrávaním programov na micro:bit či vypnutím/zapnutím micro:bitu, ale dá sa aktualizovať.

BBC micro:bit obsahuje firmvér už od výroby, takže teoreticky je možné začať programovať a zabudnúť na to, že vôbec
nejaký firmvér existuje. Napriek tomu ale niekedy sú dôvody, prečo firmvér aktualizovať – napríklad ak chcete
použiť WebUSB (funguje iba pri novších verziách firmvéru).

Najnovší firmvér na stiahnutie ako aj detailný návod nájdeš na stránke
[microbit.org/guide/firmware](https://microbit.org/guide/firmware)

## Zistenie verzie firmvéru na micro:bite

Ak chceš zistiť, aká verzia firmvéru je nahratá na micro:bite, stačí ho pripojiť cez USB kábel k počítaču
a keď sa zobrazí USB úložisko s názvom **MICROBIT**, otvor súbor **DETAILS.TXT** a nájdi riadok, ktorý
sa začína slovami **Interface Version**. V nasledujúcej ukážke je verzia firmvéru 0250:

```
# DAPLink Firmware - see https://mbed.com/daplink
Unique ID: 9900000031634e4500624014000000320000000097969901
HIC ID: 97969901
Auto Reset: 1
Automation allowed: 0
Overflow detection: 0
Daplink Mode: Interface
Interface Version: 0250
Git SHA: 682d8303e37355532402b8d93c4f240a3cec02a9
Local Mods: 0
USB Interfaces: MSD, CDC, HID, WebUSB
Interface CRC: 0x3f2b7e12
Remount count: 0URL: https://microbit.org/device/?id=9900&v=0250
```

## Ako aktualizovať firmvér

1. Odpoj USB kábel medzi micro:bitom a počítačom.
2. Stlač a drž tlačidlo **RESET** na zadnej strane micro:bitu. Počas toho, ako tlačidlo RESET držíš, pripoj micro:bit
USB káblom späť k počítaču. BBC micro:bit sa teraz ukáže ako úložisko s názvom **MAINTENANCE** (ak by tam stále bol
názov MICROBIT, odpoj micro:bit, podrž tlačidlo RESET a znovu zapoj).
3. Zo stránky [microbit.org/guide/firmware](https://microbit.org/guide/firmware) si stiahni najnovšiu verziu
firmvéru, ktorú nahraj na úložisko MAINTENANCE. Indikačná LEDka na micro:bite by sa mala rozblikať, tak ako keď
bežne presúvame na micro:bit naše programy.
4. Po nahratí sa úložisko MAINTENANCE odpojí a pripojí sa úložisko MICROBIT. Či sa nám firmvér aktualizoval správne
si vieme jednoducho overiť – otvoríme súbor **DETAILS.TXT** a porovnáme **Interface Version**.