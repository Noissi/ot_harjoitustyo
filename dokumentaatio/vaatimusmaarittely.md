# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät luovat omia versioita MTG-korttipelistä omilla korteilla ja erikoissäännöillä. Sovelluksessa voi luoda useita eri peliversioita, jotka voivat olla yksityisiä tai jaettu muiden käyttäjien kanssa. Sovellus on tarkoitettu helpottamaan pelien kehitystä ja korttien luontia.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä päänäkymästä: kirjautumissivu, etusivu, peliversiosivu ja korttisivu. Lisäksi on mahdollisia muita näkymiä, kuten tilastot ja info.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuessa syötetään käyttäjätunnus ja salasana
  - Virheellisestä sisäänkirjautumisesta tulee ilmoitus käyttäjälle

### Kirjautumisen jälkeen

- Käyttäjä näkee luomansa sekä hänelle jaetut peliversiot
- Käyttäjä voi luoda uuden peliversion
  - Uusi peliversio voidaan jakaa valituille käyttäjille
- Käyttäjä voi valita tarkasteltavan peliversion
  - Käyttäjä voi selata peliversion kortteja
    - Kortit on jaettu valmiisiin ja luonnoksiin 
  - Käyttäjä voi hakea kortteja eri ominaisuuksilla
  - Käyttäjä voi luoda uusia kortteja peliversioon
  - Käyttäjä voi tuoda taulukossa tiedot uusista korteista ja lisätä ne versioon
  - Käyttäjä voi muokata ja poistaa kortteja
  - Käyttäjä voi kommentoida jaettujen peliversioiden kortteja
    - Kommentit näkyvät muille peliversion käyttäjille
  - Käyttäjä voi ladata korttitiedot sovelluksesta
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Peliversion etusivulla näkyy toimintoja, tilastoja sekä kortit
- Korttinäkymää voi vaihtaa haluamakseen (lista/kuvat) 
- Tarkempien tilastojen tarkastelu
- Ilmoitukset korttien lisäämisestä ja muokkaamisesta muille käyttäjille
- Käyttäjä voi "hyväksyä" muiden kortteja
- Näytä samankaltaisimmat kortit valitulle kortille
- Järjestä kortit valitulla tavalla (äänestetyimmät, uusimmat, kalleimmat, ...)
- Peliversion poisto
- Käyttäjätunnuksen poisto

