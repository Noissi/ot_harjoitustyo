# Ohjelmistotekniikka, harjoitustyö

#### KorttiKube

Sovelluksen avulla käyttäjät luovat omia versioita MTG-kortteista. Sovelluksessa voi luoda useita eri korttikokoelmia, jotka voivat olla yksityisiä tai jaettu muiden käyttäjien kanssa. Sovellus on tarkoitettu helpottamaan korttien luontia ja selailua sekä korttikokoelmien hallintaa. Itsetehdyt kortit ovat oivia etenkin cube-muotoiseen pelaamiseen. Lisätietoa [MTG-korteista](https://mtg.fandom.com/wiki/Card_type) ja [cubesta](https://mtg.fandom.com/wiki/Cube_Draft) englanniksi.

### Dokumentaatio

* [Käyttöohje](https://github.com/Noissi/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

* [Vaatimusmäärittely](https://github.com/Noissi/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

* [Arkkitehtuurikuvaus](https://github.com/Noissi/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

<!-- * [Testaus](https://github.com/Noissi/ot_harjoitustyo/blob/master/dokumentaatio/testaus.md) -->

* [Työaikakirjanpito](https://github.com/Noissi/ot_harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

### Asennus
HUOM! Ohjelma vaatii toimiakseen vähintään Ubuntu 20 -käyttöjärjestelmään pohjautuvan käyttöjärjestelmän (esim Cubbli 20) tai vastaavan käyttöjärjestelmän.

Lataa projektin viimeisin [release](https://github.com/Noissi/ot_harjoitustyo/releases): _Assets_ -> _Source code_.

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

### Pylint
.pylintrc-tiedoston tarkistusten suorittaminen:
```
poetry run invoke lint
```

:chicken: 

