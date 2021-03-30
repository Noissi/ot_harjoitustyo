# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät luovat omia versioita MTG-kortteista. Sovelluksessa voi luoda useita eri korttikokoelmia, jotka voivat olla yksityisiä tai jaettu muiden käyttäjien kanssa. Sovellus on tarkoitettu helpottamaan korttien luontia ja selailua sekä korttikokoelmien hallintaa. Itsetehdyt kortit ovat oivia etenkin cube-muotoiseen pelaamiseen. Lisätietoa [MTG-korteista](https://mtg.fandom.com/wiki/Card_type) ja [cubesta](https://mtg.fandom.com/wiki/Cube_Draft) englanniksi.

## Käyttöliittymäluonnos

Sovellus koostuu viidestä päänäkymästä: kirjautumissivu, etusivu, kokoelmasivu, korttisivu ja kortinmuokkaussivu. Lisäksi muita mahdollisia näkymiä ovat esimerkiksi tilastot ja info.

## Toiminnallisuudet

### Kirjautuminen ja käyttäjätunnuksen luonti

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuessa syötetään käyttäjätunnus ja salasana
  - Virheellisestä sisäänkirjautumisesta tulee ilmoitus käyttäjälle

### Kirjautumisen jälkeen

#### Etusivu

- Käyttäjä näkee etusivulla luomansa sekä hänelle jaetut korttikokoelmat
- Käyttäjä voi luoda uusia korttikokoelmia
  - Uusi korttikokoelma voidaan jakaa valituille käyttäjille
- Käyttäjä voi valita tarkasteltavan korttikokoelman
- Käyttäjä voi hakea kortteja eri ominaisuuksilla

#### Kokoelmasivu

- Käyttäjä voi selata kokoelman kortteja
  - Kortit on jaettu valmiisiin ja luonnoksiin 
  - Käyttäjä voi lajitella kortteja valittujen parametrien perusteella
- Käyttäjä voi hakea kortteja eri ominaisuuksilla
- Käyttäjä voi luoda uusia kortteja kokoelmaan
- Käyttäjä voi tuoda taulukossa tiedot uusista korteista ja lisätä ne kokoelmaan
- Käyttäjä voi valita tarkasteltavan kortin

#### Korttisivu

- Käyttäjä voi tarkastella korttia
- Käyttäjä voi muokata korttia
- Käyttäjä voi kommentoida jaettujen peliversioiden kortteja
  - Kommentit näkyvät muille peliversion käyttäjille
- Käyttäjä voi ladata korttitiedot sovelluksesta

####

- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Sovellukseen lisätään ajan salliessa esim. seuraavia toiminnallisuuksia:

- Kokoelmasivulla näkyy toimintoja, tilastoja sekä kortit
- Korttinäkymää voi vaihtaa haluamakseen (lista/kuvat) 
- Tarkempien tilastojen tarkastelu
- Ilmoitukset korttien lisäämisestä ja muokkaamisesta muille käyttäjille
- Käyttäjä voi "hyväksyä" muiden kortteja
- Näytä samankaltaisimmat kortit valitulle kortille
- Korttikokoelman poisto
- Käyttäjätunnuksen poisto

