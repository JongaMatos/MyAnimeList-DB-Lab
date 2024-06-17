-- -------- < Apresetação TF > --------
--
--                    SCRIPT DE CRIACAO (DDL)
--
-- Data Criacao ...........: 11/06/2024
-- Autor(es) ..............: João Gabriel de Campos de Matos
--
-- Banco de Dados .........: MySQL 8.0
-- Base de Dados (nome) ...: MyAnimeList
--
-- PROJETO => 01 Base de Dados
--         => 06 Tabelas
--
-- ---------------------------------------------------------
-- Criando a base de dados (caso não tenha sido criada)
CREATE DATABASE IF NOT EXISTS MyAnimeList;

USE MyAnimeList;

CREATE TABLE ANIME (
	animeId BIGINT NOT NULL,
	title VARCHAR(100) NOT NULL,
	synopsis VARCHAR(3000) NOT NULL,
	aired VARCHAR(50) NOT NULL,
	episodes INT,
	members INT NOT NULL,
	score DECIMAL,
	img_url VARCHAR(500) NOT NULL,
	link VARCHAR(500) NOT NULL,
	CONSTRAINT ANIME_PK PRIMARY KEY (animeId)
) Engine = InnoDB;

CREATE TABLE GENRE (
	genreId BIGINT NOT NULL,
	name VARCHAR(20) NOT NULL,
	CONSTRAINT GENRE_PK PRIMARY KEY (genreId)
) Engine = InnoDB;

CREATE TABLE anime_genre (
	genreId BIGINT NOT NULL,
	animeId BIGINT NOT NULL,
	CONSTRAINT GENRE_anime_genre_FK FOREIGN KEY (genreId) REFERENCES GENRE (genreId) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT ANIME_anime_genre_FK FOREIGN KEY (animeId) REFERENCES ANIME (animeId) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT anime_genre_PK PRIMARY KEY (genreId, animeId)
) Engine = InnoDB;

CREATE TABLE PROFILE (
	profile VARCHAR(50) NOT NULL,
	gender ENUM('Male', 'Female'),
	birthday VARCHAR(19),
	link VARCHAR(500) NOT NULL,
	CONSTRAINT PROFILE_PK PRIMARY KEY (profile)
) Engine = InnoDB;

CREATE TABLE favorite (
	profile VARCHAR(50) NOT NULL,
	animeId BIGINT NOT NULL,
	CONSTRAINT ANIME_favorite_FK FOREIGN KEY (animeId) REFERENCES ANIME (animeId) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT PROFILE_favorite_FK FOREIGN KEY (profile) REFERENCES PROFILE (profile) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT favorites_PK PRIMARY KEY (profile, animeId)
) Engine = InnoDB;

CREATE TABLE REVIEW(
	reviewId BIGINT NOT NULL,
	profile VARCHAR(50) NOT NULL,
	animeId BIGINT NOT NULL,
	score DECIMAL NOT NULL,
	CONSTRAINT ANIME_REVIEW_FK FOREIGN KEY (animeId) REFERENCES ANIME (animeId) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT PROFILE_REVIEW_FK FOREIGN KEY (profile) REFERENCES PROFILE (profile) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT REVIEW_PK PRIMARY KEY (reviewId)
) Engine = InnoDB;