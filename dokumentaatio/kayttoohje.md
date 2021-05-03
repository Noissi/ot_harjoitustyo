# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/Noissi/ot_harjoitustyo/releases): _Assets_ -> _Source code_.

## Konfigurointi

Tietokantatiedosto _database.db_ luodaan automaattisesti _src_-kansioon ohjelman käynnistyksessä, mikäli tiedostoa ei vielä ole olemassa. Ohjelma myös luo kansiot _imgcards_ ja _imguser_ korttien ja käyttäjän antamille kuville, jos niitä ei vielä ole. Polkujen ja tiedostonimien muuttaminen onnistuu tiedostossa _config.py_.

## Ohjelman käynnistäminen

Asenna riippuvuudet ennen sovelluksen käynnistämistä komennolla:

```
poetry install
```

Ohjelma käynnistyy komennolla:

```
poetry run invoke start
```

## Käyttö

### Käyttäjän luonti ja kirjautuminen

Luo aluksi uusi käyttäjä napista _Luo uusi käyttäjä_. Anna valitsemasi käyttäjätunnus ja salasana ja luo käyttäjä.
Kirjaudu sisään tunnuksilla syöttämällä ne tyhjiin kenttiin ja paina _Kirjaudu_-nappia.

![](./kuvat/login.png)

### Uuden kuben luonti ja tarkastelu

Luo uusi kube painamalla _Uusi kube_ -nappia ja syöttämällä valitsemasi nimi kubelle.
Voit tarkastella haluamaasi kubea painamalla sen kuvaketta, jolloin kubenäkymä avautuu.

### Uuden kortin luominen kubeen

Luo uusi kortti kubeen painamalla _Uusi kortti_ -nappia, jolloin siirryt kortinluontinäkymään.
Anna haluamasi tiedot kortille ja paina _Tallenna_, näet vielä yhteenvedon kortistasi. Pääset takaisin kubenäkymään painamalla _Takaisin_.

### Kortin tarkastelu ja muokkaus
Voit tarkastella haluamaasi kubea painamalla sen kuvaketta, jolloin korttinäkymä avautuu.
Voit muokata kortin tietoja painamalla _Muokkaa_-nappia, jolloin kortinmuokkaussivu avautuu. Kun olet tehnyt haluamais muutokset, voit tallentaa ne _Tallenna_-napista.
