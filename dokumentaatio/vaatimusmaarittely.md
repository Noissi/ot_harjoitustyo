# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät luovat omia versioita MTG-kortteista. Sovelluksessa voi luoda useita eri korttikokoelmia, jotka voivat olla yksityisiä tai jaettu muiden käyttäjien kanssa. Sovellus on tarkoitettu helpottamaan korttien luontia ja selailua sekä korttikokoelmien hallintaa. Itsetehdyt kortit ovat oivia etenkin cube-muotoiseen pelaamiseen. Lisätietoa [MTG-korteista](https://mtg.fandom.com/wiki/Card_type) ja [cubesta](https://mtg.fandom.com/wiki/Cube_Draft) englanniksi.

## Käyttöliittymäluonnos

Sovellus koostuu kuudesta päänäkymästä: kirjautumissivu, käyttäjän luonti -sivu, etusivu, kubesivu, korttisivu ja kortinmuokkaussivu. Lisäksi muita mahdollisia näkymiä ovat esimerkiksi tilastot ja info.

## Toiminnallisuudet

### Kirjautuminen ja käyttäjätunnuksen luonti

- [x] Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  -  [x] Käyttäjätunnuksen täytyy olla uniikki
- [x] Käyttäjä voi kirjautua järjestelmään
  - [x] Kirjautuessa syötetään käyttäjätunnus ja salasana
  - [x] Virheellisestä sisäänkirjautumisesta tulee ilmoitus käyttäjälle

### Kirjautumisen jälkeen

#### Etusivu

- [x] Käyttäjä näkee etusivulla luomansa (sekä hänelle jaetut) korttikokoelmat
- [x] Käyttäjä voi luoda uusia korttikokoelmia
- [x] Käyttäjä voi valita tarkasteltavan korttikokoelman

#### Kokoelmasivu

- [x] Käyttäjä voi selata kokoelman kortteja
- [ ] Käyttäjä voi hakea kortteja eri ominaisuuksilla
- [x] Käyttäjä voi luoda uusia kortteja kokoelmaan
- [x] Käyttäjä voi valita tarkasteltavan kortin

#### Korttisivu

- [x] Käyttäjä voi tarkastella korttia
- [x] Käyttäjä voi muokata korttia
  - [x] Korteista tallennetaan käyttäjälle tulostettava kuva.

#### Kortinmuokkaussivu

- [x] Käyttäjä voi tarkastella korttia
- [x] Käyttäjä voi muokata korttia
  - [x] Käyttäjä näkee muokkaukset reaaliajassa

####

- [x] Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Sovellukseen lisätään ajan salliessa esim. seuraavia toiminnallisuuksia:

- [ ] Kokoelmasivulla näkyy toimintoja ja tilastoja
- [ ] Korttinäkymää voi vaihtaa haluamakseen (lista/kuvat)
- [ ] Ilmoitukset korttien lisäämisestä ja muokkaamisesta muille käyttäjille
- [ ] Käyttäjä voi "hyväksyä" muiden kortteja
- [ ] Näytä samankaltaisimmat kortit valitulle kortille
- [ ] Korttikokoelman poisto
- [ ] Käyttäjätunnuksen poisto
- [ ] Uusi korttikokoelma voidaan jakaa valituille käyttäjille
- [ ] Kortit on jaettu valmiisiin ja luonnoksiin
- [ ] Käyttäjä voi tuoda taulukossa tiedot uusista korteista ja lisätä ne kokoelmaan
- [ ] Käyttäjä voi kommentoida jaettujen peliversioiden kortteja
  - [ ] Kommentit näkyvät muille peliversion käyttäjille
- [ ] Käyttäjä voi ladata korttitiedot sovelluksesta
