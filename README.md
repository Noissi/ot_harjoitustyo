# Ohjelmistotekniikka, harjoitustyö

### Dokumentaatio

<!-- * [Käyttöohje](https://github.com/Noissi/ot_harjoitustyo/blob/master/KorttiKube/dokumentaatio/kayttoohje.md)-->

* [Vaatimusmäärittely](https://github.com/Noissi/ot_harjoitustyo/blob/master/KorttiKube/dokumentaatio/vaatimusmaarittely.md)

<!-- * [Arkkitehtuurikuvaus](https://github.com/Noissi/ot_harjoitustyo/blob/master/KorttiKube/dokumentaatio/arkkitehtuurikuvaus.md)-->

<!-- * [Testaus](https://github.com/Noissi/ot_harjoitustyo/blob/master/KorttiKube/dokumentaatio/testaus.md) -->

* [Työaikakirjanpito](https://github.com/Noissi/ot_harjoitustyo/blob/master/KorttiKube/dokumentaatio/tyoaikakirjanpito.md)

### Asennus
HUOM! Ohjelma vaatii toimiakseen vähintään Ubuntu 20 -käyttöjärjestelmään pohjautuvan käyttöjärjestelmän (esim Cubbli 20) tai vastaavan käyttöjärjestelmän.

1. Riippuvuuksien asenntaminen
```
poetry install
```

2. Sovelluksen ajaminen
```
poetry run invoke start
```

### Testaus
Testien suorittaminen
```
poetry run invoke test
```
Testikattavuusraportti
```
poetry run invoke coverage-report
```

:chicken: 

