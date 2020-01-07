modele rolet:

- **numer**
- nzawa modelu
- opis

Roleta:

- **id**
- model -> modele rolet
- kolor materiału
- kolor mocowań
- wymiar

Sprzedaż:

- **numer transakcji**
- Klient (imię, nazwisko, adres)
- liczba
- roleta -> Roleta
- cena

```mysql
CREATE DATABASE rolety_baza;
USE rolety_baza;
CREATE TABLE modele_rolet(
	Numer_modelu int NOT NULL,
	nazwaModelu varchar(255),
	opis text,
    PRIMARY KEY (Numer_modelu)
);
CREATE TABLE rolety(
	id int NOT NULL,
    Numer_modelu int NOT NULL,
    kolor_materialu varchar(255),
    kolor_mocowan varchar(255),
    ID_wymiaru int NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE wymiary(
    id int NOT NULL,
    wymiar_rolety_mm_0 int,
    wymiar_rolety_mm_1 int,
    wymiar_rolety_mm_2 int,
    wymiar_rolety_mm_3 int,
    wymiar_rolety_mm_4 int,
    wymiar_rolety_mm_5 int,
    Na_zamowienie bool,
    PRIMARY KEY (id)
);
CREATE TABLE sprzedaz(
	numer_transakcji int NOT NULL,
    imie_klienta varchar(127),
    nazwisko_klienta varchar(127),
    adres_klienta varchar(511),
    liczba_rolet int,
    id_rolety int NOT NULL,
    cena DECIMAL(18, 2),
    PRIMARY KEY (numer_transakcji)
);

```

