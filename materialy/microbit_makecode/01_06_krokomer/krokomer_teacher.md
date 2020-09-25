# Krokomer
## Metodika pre učiteľa

// LEFT

**Pomocné materiály:**

* [Prezentácia]()

**Potrebné pomôcky:**  
Pre každého žiaka (alebo skupinu žiakov) BBC micro:bit, USB kábel, batériu k micro:bitu, počítač pripojený na internet,
papierová lepiaca páska (ľahšie sa dá dať dolu z oblečenia ako klasická páska), nožnice, topánky

**Ciele hodiny:**

* Predstaviť žiakom princíp snímania krokov a využitie krokomeru v praxi
* Diskutovať o dôležitosti pohybu a odporúčanom počte krokov

// RIGHT

**Potrebné predchádzajúce znalosti:**  
Vedieť nahrávať programy na micro:bit, poznať prostredie MakeCode, vedieť pracovať s displejom a tlačidlami na
micro:bite, vedieť pracovať s premennými v prostredí MakeCode

**Odhadovaný čas:** 25 minút

**Harmonogram:**

[TOC]

// END


---
### Príprava pred hodinou

Pred touto hodinou je potrebné pripraviť lepiacu pásku a nožnice.

---
### Priebeh hodiny
Táto aktivita je kratšia ako na celú hodinu a preto je vhodné kombinovať ju s ďalšou aktivitou,
ako napríklad Počítadlo ľudí (v nej sa predstavuje koncept premenných).

#### Krokomer [3 min]
Na začiatku hodiny vedťe so žiakmi krátku diskusiu, či už použili niekedy krokomer, na čo slúži
a prečo pre nás môže byť zo zdravotného hľadiska užitočné vedieť, koľko krokov sme za deň spravili.

Pri diskusii môžete využiť informácie z návodu tejto kapitoly.
 
#### Program pre krokomer [10 min]
Začnite spolu so žiakmi spisovať požiadavky na vytváraný krokomer. Ozrejmite žiakom postup:
 
1. Navrhneme si požiadavky pre náš krokomer (aký má byť výsledok)
2. Vytvoríme softvér
3. Odskúšame v simulátori
4. micro:bit pripevníme na topánku a otestujeme

Príklad definovaných požiadaviek nájdete v návode tejto kapitoly. Odpovede žiakov môžete zaznamenávať
v odrážkach na tabuľu. Pomôcky k diskusii nájdete tu:

*   Čo chceme dosiahnuť?  
    Odpoveďou by mala byť jedna alebo dve ucelené vety, ktoré jasne definujú výsledok, napr. “Výsledkom je krokomer, ktorý
    meria počet spravených krokov, je napájaný batériou, počet krokov zobrazuje na displeji a je vynulovateľný.”
*   A čo naopak nemá robiť?  
    Častokrát pri programovaní zabúdame na túto otázku. Odpoveďou by mohlo byť napríklad “Krokomer nezobrazuje počet krokov
    stále, ale iba pri stlačení tlačidla.”

Po vyjasnení požiadaviek môžeme prejsť k realizácii. Softvér pre krokomer bude využívať iba príkazy, ktoré už žiaci poznajú
z predchádzajúcich hodín.

Pri vývoji hardvéru sa bežne na overenie funkčnosti využívajú simulátory. Takéto testovanie je oveľa rýchlejšie
a lacnejšie, ako vždy program nahrať do hardvéru a testovať ho tam. Preto je dobré sa so žiakmi porozprávať o výhodách
testovania softvéru v simulátori a viesť ich k tomu, aby pred každým nahratím kódu na micro:bit najprv overili funkčnosť v simulátori. 



#### Hardvér pre krokomer [10 min]
Výsledný program si žiaci nahrajú na micro:bit a lepiacou páskou si micro:bit pripevnia na topánku.

Zadajte žiakom úlohy:

* Zistite, aký presný je micro:bit krokomer.  
  (Riešenie: žiak spraví 20 krokov a zistí, koľko krokov zaznamenal krokomer)
* Aké umiestnenie na topánke je najlepšie, ak chceme najpresnejšie meranie krokov?
  (Riešenie: podobné ako v predchádzajúcej úlohe, len žiaci vyskúšajú viacero miest na pripevnenie)
 
#### Diskusia a zhrnutie hodiny [2 min]
Na záver veďte so žiakmi diskusiu o krokomeroch a dôležitosti chôdze:

*   Na čo slúži krokomer?
*   Aký senzor používa na snímanie krokov?
*   Koľko krokov by mal človek denne spraviť?
*   Čo hrozí človeku, ktorý sa dostatočne nehýbe?
*   Ako presné sú krokomery?


!!! warning "Reflexia"
    
    Na konci hodiny je správny priestor aj na reflexiu žiakov. Pri nej sú žiaci vyzvaní, aby hodnotili nielen aktivity,
    ale aj svoju prácu na hodine, prípadne prácu svojich spolužiakov. Vytvoriť tým môžete aj väčšiu zodpovednosť
    u žiakov za vlastný proces vzdelávania.  
    
    Návodov, ako správne viesť reflexiu je mnoho, pekné zhrnutie nájdete na
    [eduworld.sk](https://eduworld.sk/cd/jaroslava-konickova/4005/ako-rozvijat-sebareflexiu-a-sebahodnotenie-ziakov)
