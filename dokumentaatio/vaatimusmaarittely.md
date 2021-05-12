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
- [x] Sivu näyttää järkevältä

### Kirjautumisen jälkeen

#### Etusivu

- [x] Käyttäjä näkee etusivulla luomansa (sekä hänelle jaetut) korttikokoelmat
- [x] Käyttäjä voi luoda uusia korttikokoelmia
- [x] Käyttäjä voi valita tarkasteltavan korttikokoelman
- [x] Sivu näyttää järkevältä

#### Kubesivu

- [x] Käyttäjä voi selata kuben kortteja
- [x] Käyttäjä voi hakea kortteja eri ominaisuuksilla
- [x] Käyttäjä voi luoda uusia kortteja kubeen
- [x] Käyttäjä voi valita tarkasteltavan kortin
- [x] Käyttäjä voi muokata kubea (kuva)
- [x] Sivu näyttää järkevältä

#### Korttisivu

- [x] Käyttäjä voi tarkastella korttia
- [x] Käyttäjä voi muokata korttia
  - [x] Korteista tallennetaan käyttäjälle tulostettava kuva.
- [x] Käyttäjä voi poistaa kortin
- [x] Sivu näyttää järkevältä

#### Kortinmuokkaussivu

- [x] Käyttäjä voi tarkastella korttia
- [x] Käyttäjä voi muokata korttia
  - [x] Kortin ominaisuudet piirtyvät kortille
  - [x] Käyttäjä näkee muokkaukset reaaliajassa
- [x] Sivu näyttää järkevältä

####

- [x] Käyttäjä voi kirjautua ulos järjestelmästä
- [x] Luotujen korttien tiedot tallettuvat tietokantaan

## Jatkokehitysideoita

Sovellukseen lisätään ajan salliessa esim. seuraavia toiminnallisuuksia:

- [ ] Kokoelmasivulla näkyy toimintoja ja tilastoja
- [ ] Käyttäjä voi "hyväksyä" muiden kortteja
- [ ] Näytä samankaltaisimmat kortit valitulle kortille
- [ ] Uusi korttikokoelma voidaan jakaa valituille käyttäjille
- [ ] Kortit on jaettu valmiisiin ja luonnoksiin
- [ ] Käyttäjä voi tuoda taulukossa tiedot uusista korteista ja lisätä ne kokoelmaan
- [ ] Käyttäjä voi kommentoida jaettujen peliversioiden kortteja
  - [ ] Kommentit näkyvät muille peliversion käyttäjille
- [x] Käyttäjä voi ladata korttitiedot sovelluksesta tiedostoon
