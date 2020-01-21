## Tajný link
Ak chcete pridať ďalšiu kapitolu, avšak ešte ju nezverejniť, tak ju môžete pridať ako tajný link pomocou parametru `visible: False`. Taktiež treba pozmeniť tieto odkazy **dať na koniec**, pretože inak sa pokazí číslovanie!

Ukážka nezverejnenej kapitoly: [/materialy/help/secret](/materialy/help/secret)

```
content:

  - slug: secret
    title: Tajný link (na rozrobené materiály)
    visible: False
```

## Zdrojový kód

~~~
```
here be code
```
~~~

## Upozornenia/Varovania

~~~
!!! primary "Primary"
    Any number of other indented markdown elements.

    This is the second paragraph.
~~~

!!! primary "Primary"
    Any number of other indented markdown elements.

    This is the second paragraph.


!!! secondary "Secondary"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! success "Success"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! danger "Danger"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! warning "Warning"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! info "Info"
    Any number of other indented markdown elements.

    This is the second paragraph.

!!! light "Light"
    Any number of other indented markdown elements.

    This is the second paragraph.


!!! dark "Dark"
    Any number of other indented markdown elements.

    This is the second paragraph.

## Tabuľky

~~~
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
~~~

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

## Obrázky

```
![alt text](images/krokomer.jpg)
```

![alt text](images/krokomer.jpg)