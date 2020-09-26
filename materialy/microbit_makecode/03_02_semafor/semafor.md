Title:   Semafor
Teacher:  True

# Semafor
## Ovládanie trioch LEDiek

// LEFT

![Obrázok BBC micro:bitu](images/header.jpg)

// RIGHT

*V tejto lekcii si zostrojíme funkčnú maketu svetelnej križovatky - pomocou červenej, žltej a zelenej LEDky a micro:bitu naprogramujeme semafor.*

**Potrebné pomôcky:**
BBC micro:bit, USB kábel, počítač pripojený na internet, krokosvorky, LED diódy, rezistory, [batérie pre BBC micro:bit] 

Pracovať budeme v online prostredí [makecode.microbit.org](https://makecode.microbit.org/)

// END


1. **Predstavenie aktivity**

Pre tvorbu malého modelu semaforu je potrebné zapojenie 3 LED diód a ich správne naprogramovanie.

Krátke video o rekonštrukcii križovakty - [https://www.youtube.com/watch?v=DyTXm3yc4yk](https://www.youtube.com/watch?v=DyTXm3yc4yk)

Toto video odporúčame pustiť na začiatku hodiny a otvoriť tým diskusiu, ako sú riadené svetelné križovatky, kto a ako sa určuje, kedy svieti aká farba.

V prípade, že je k dipozícii viac času a žiaci nemajú problém porozumieť anglickému videu, odporúčame pustiť 12 minútové video o svetelných križovatkách:

[https://www.youtube.com/watch?v=DP62ogEZgkI](https://www.youtube.com/watch?v=DP62ogEZgkI) 

Diskusia so žiakmi:



*   Ako fungujú svetelné križovatky?
*   V akom poradí idú svetlá na križovatke?
*   Kedy svieti žlté svetlo? (len žlté svieti tesne pred červenou, pred zelenou svieti vždy spolu s červeným svetlom)
*   Čo hrozí, ak nerešpektujeme svetelné križovatky?
2. **Zapojenie viacerých LED diód na jeden micro:bit**

Doposiaľ sme programovali iba 1 LED diódu na micro:bite. Pripojiť ich ale môže viac. Keď sa pozrieme na micro:bit, uvidíme, že má 3 programovateľné piny “0”, “1” a “2”, a teda môže programovať až 3 rôzne svetlá. Presne toľko potrebujeme na semafor.

Pre každú z 3 diód platí:



*   Plus (anóda) je zapojená cez vlastný rezistor na jeden z troch programovateľných pinov
*   Mínus (katóda) je zapojená ku “GND”  

Zapojenie s 2 LEDkami je nasledovné:



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




3. **Preblikávanie zelená-červená**

So zapojení z predchádzajúceho kroku vieme spraviť program, ktorý striedavo svieti buď červenou, alebo zelenou LEDkou. Vždy pri zmene musíme jednu LEDku zapnúť a druhú vypnúť.

 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")
** **

[https://makecode.microbit.org/_6TqVURRKKRDp](https://makecode.microbit.org/_6TqVURRKKRDp) 



4. **Tri LED diódy - zapojenie**

Zapojenie 3 LEDiek je analogické zapojeniu 2 LEDiek z predchádzajúcich krokov - každá LEDka má vlastný rezistor, ktorým je prepojená k pinu. Taktiež je každá mínusová Časť LEDky pripojená ku “GND”.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")




5. **Semafor - program**

Semafor sa dá na micro:bite naprogramovať rôznymi spôsobmi. Prvý, ktorý vyskúšame, je **manuálny semafor** - pri štarte semafor zapne červenú farbu, a potom prepíname do zelenej a späť pomocou tlačidiel “A” a “B”.

Pri stlačení tlačidla “A” sa chceme dostať z červenej na zelenú. Predpokladáme teda, že červená (P2) je zapnutá a zvyšné vypnuté. Zapneme teda žltú farbu (P1), počkáme sekundu, potom vypneme červenú (P2) a vypneme žltú (P1) a zapneme zelenú (P0). 

Pri stlačení tlačidla “B” sa chceme dostať zo zelenej na červenú. Predpokladáme teda, že zelená (P0) je zapnutá a zvyšné vypnuté. Vypneme teda zelený (P0) a zapneme žltú farbu (P1), počkáme dve sekundy, potom vypneme vypneme žltú (P1) a zapneme červenú (P2). 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


[https://makecode.microbit.org/_9jL9ccd3TCeV](https://makecode.microbit.org/_9jL9ccd3TCeV) 



Druhý typ semaforu, ktorý si naprogramujeme, je **automatický semafor** - sám sa v stanovenom intervale prepína. V našom prípade sa prepína každých 5 sekúnd.



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


[https://makecode.microbit.org/_Cq1TTzK4bb4m](https://makecode.microbit.org/_Cq1TTzK4bb4m) 





6. **Semafor - kartónová konštrukcia**

Aby sme vytvorili semafor, použijeme obyčajný kartón, ktorý podľa foto nižšie vystrihneme a spojíme. Nožnicami následne spravíme 3 diery, do ktorých vložíme LEDky. Pre lepšiu stabilitu môžeme semafor prelepiť, prípadne vytvoriť väčšiu podstavu. 



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")


Podobný semafor je možné si aj zakúpiť:

[https://www.kitronik.co.uk/5642-stopbit-traffic-light-for-bbc-microbit.html](https://www.kitronik.co.uk/5642-stopbit-traffic-light-for-bbc-microbit.html)



7. **Komplexná svetelná križovatka **

Ako väčší projekt by bolo možné vytvoriť maketu križovatky (namaľovaný kartón) na ktorom by sa nachádzalo niekoľko semaforov. Tie by prípadne mohli spolu komunikovať bezdrôtovo (viac o bezdrôtovej komunikácii v ďalších metodikách).



**Záverečná diskusia:**



*   Musíme pri zapájaní viacerých LEDiek mať viacero rezistorov?
*   V akej postupnosti svieta na svetelnej križovatke svetlá?
*   Čo znamená, že na svetelnej križovatke blikajú oranžové svetlá, i keď bežne svietia klasicky zelená, červená, žltá?
*   Vedľa semafóru, na ktorom svieti zelené svetlo, je tabuľa STOP. Kedy sa riadime podľa tabule a kedy podľa svetiel na semafore?
*   Kedy svieti len žltá na semafore? A kedy svieti spolu s červenou?
*   Čo znamená pre vodiča, keď vidí, že svieti žltá farba na senafore?

**Na konci hodiny vie žiak:**



*   Popísať, na čo slúži semafor a v akom poradí svietia rôzne kombinácie svetiel.
*   Pripojiť a naprogramovať viacero LED diód k BBC micro:bit.
*   Naprogramovať funkcionalitu semaforu pomocou BBC micro:bit