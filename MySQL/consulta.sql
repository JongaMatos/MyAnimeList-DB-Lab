-- ---------------   Trabalho Final  -------------------
--
--                    SCRIPT DE CONSULTA
--
-- Data Criacao ...........: 20/06/2024
-- Autor(es) ..............: Paulo Abi Acl
-- Banco de Dados .........: MySQL 8.0
-- Base de Dados (nome) ...: myanimeList
--                        
-- PROJETO => 01 Base de Dados
--         => 06 Tabelas
--         => 04 Consultas
--
-- Últimas atualizações:
--
-- ---------------------------------------------------------

use myanimelist;

-- Quantidade de animes por gênero
SELECT Count(g.genreId) quantidadeAnimes, g.name as gênero
	FROM genre g 
LEFT JOIN anime_genre ag 
	ON ag.genreId = g.genreId
GROUP BY g.genreId
ORDER BY quantidadeAnimes DESC;

-- Quantidade de avaliações por perfil e nota média atribuida
SELECT p.profile, Count(p.profile) quantidadeAvaliacoes, avg(r.score) NotaMediaAtribuida
	FROM profile p 
LEFT JOIN review r 
	ON p.profile = r.profile
GROUP BY p.profile
ORDER BY quantidadeAvaliacoes DESC;

-- Nota média por anime
SELECT a.Title, count(r.animeId) QuantidadeReviews, avg(r.score) NotaMediaAnime
	FROM review r 
LEFT JOIN anime a
	ON a.animeId = r.animeId
GROUP BY r.animeId
ORDER BY QuantidadeReviews DESC;

-- Animes que mais foram favoritados
SELECT a.title AS Titulo, count(f.animeId) Favoritado  
	FROM Favorite f
INNER JOIN anime a
	ON a.animeId = f.animeId
GROUP BY f.animeId
ORDER BY Favoritado DESC;
