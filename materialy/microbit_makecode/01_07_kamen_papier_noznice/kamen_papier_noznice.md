Title:   Kameň, papier, nožnice
Teacher:  True

# Kameň, papier, nožnice
## Sprav si s kamarátmi turnaj

// LEFT

![Obrázok BBC micro:bitu](images/kamen.jpg)

// RIGHT

*V tejto lekcii si z micro:bitu spravíme pomôcku na hru Kameň, papier, nožnice.*

**Potrebné pomôcky:**  
BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený k internetu

Pracovať budeme v online prostredí [makecode.microbit.org](https://makecode.microbit.org/)

// END


// LEFT

#### Náhodné čísla na micro:bite
Základom elektronickej pomôcky pre hru Kameň, papier nožnice je náhoda - konkrétne náhodné vyberanie spomedzi kameňa, papiera a nožníc. V jednej z predchádzajúcich lekcií sme už s generovaním náhodných čísel pracovali (konkrétne v lekcii Senzor Pohybu)

!!! primary "Generovanie náhodných čísel"
    Náhodné čísla na micro:bite získame príkazom `vybrať náhodne od 0 do 10` z kategórie `Matematika`. Rozsah, z ktorých náhodné čísla micro:bit vyberá vieme ľubovoľne upraviť (napr. aby vyberal náhodné čísla od 1 do 3)


Keďže v hre Kameň, papier, nožnice máme 3 rôzne symboly, náš kód bude pri potrasení náhodne generovať číslo od 1 po 3 a podľa toho zobrazovať adekvátny symbol. Najprv si skúsime náhodné číslo vygenerovať, uložiť ho do premennej `ruka` a vypísať na displej micro:bitu (kód nižšie). Nezabudnite si najprv premennú `ruka` vytvoriť v kategórii "Premenné".

```makecode
_CbUcyz5osWEF
```


#### Symboly namiesto čísel

Predcházajúci kód síce náhodne generuje čísla, ale my by sme namisto nich chceli na micro:bite zobrazovať symboly. Na to použijeme príkaz `ak pravda potom` z kategórie "Logika", ktorý čísla premení na obrázky, konkrétne:

* Pri čísle 1 zobrazí papier
* Pri čísle 2 zobrazí kameň
* Pri čísle 3 zobrazí nožnice


// RIGHT

Výsledný program:

```makecode
_bWMKT2TKR1Tz
```

// END

// NEWPAGE

### Pridanie počítadla výhier

// LEFT

V tejto časti hodiny žiaci doplnia svoj kód o počítanie výhier. Po každej výhre žiak stlačí tlačidlo A, ktoré zvýši premennú “vyhry” o 1. Pre vypísanie stačí žiak tlačidlo B. Pre vynulovanie stlačí žiak tlačidlo RESET na zadnej strane micro:bitu. \
 \
Následne si žiaci môžu zahrať triedny turnaj dvoma rôznymi spôsobmi:


*   Žiaci si nájdu dvojicu a zahrajú hru. Žiak, ktorý prehrá vypadne a prestane hrať. Žiak, ktorý vyhrá si pripočíta výhru na micro:bite stlačením tlačidla A a nájde si ďalšieho spolužiaka, ktorý ešte nevypadol na ďalšiu hru. Hra sa končí, keď zostane už iba jeden hráč, avšak vyhráva žiak, ktorý má najvyšší počet výhier.
*   Žiaci v danom časovom intervale (hru odštartuje aj ukončí učiteľ) majú za úlohu vyhrať čo najviac hier s čo najviac spolužiakmi. V tejto hre sa nevypadáva, avšak nie je možné hrať s tým istým spolužiakom 2 krát za sebou. Vyhráva žiak, ktorý má po skončení turnaja najviac víťazstiev.

Na začiatku turnaja zdôraznite, že ide o férovú hru a že si navzájom veríte a nebudete podvádzať.** \
 **
 
// RIGHT

```makecode-no-link
_PvMHTqLMhXxu
```

```makecode-no-link
_6vz0tmi9JiEE
```

```makecode-link-only
_h5AXtUieqWwg
```

// END