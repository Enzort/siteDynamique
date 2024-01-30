-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 05 juin 2023 à 16:16
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `footus`
--

-- --------------------------------------------------------

--
-- Structure de la table `clubs`
--

DROP TABLE IF EXISTS `clubs`;
CREATE TABLE IF NOT EXISTS `clubs` (
  `nClub` int NOT NULL AUTO_INCREMENT,
  `nomClub` varchar(50) NOT NULL,
  `nomVille` varchar(30) NOT NULL,
  `budget` int NOT NULL,
  `nomStade` varchar(40) NOT NULL,
  `dateCrea` date NOT NULL,
  PRIMARY KEY (`nClub`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `clubs`
--

INSERT INTO `clubs` (`nClub`, `nomClub`, `nomVille`, `budget`, `nomStade`, `dateCrea`) VALUES
(1, 'New England Patriots', 'Foxborough', 230902712, 'Gillette Stadium', '1959-11-16'),
(2, 'Philadelphia Eagles', 'Philadelphie', 235626564, 'Lincoln Financial Field', '1933-07-08'),
(3, 'Cleveland Browns', 'Cleveland', 264278386, 'Cleveland Browns Stadium', '1944-06-04'),
(4, 'Minnesota Vikings', 'Minneapolis', 233453972, 'U.S. Bank Stadium', '1960-01-28'),
(5, 'Jacksonville Jaguars', 'Jacksonville', 226928830, 'TIAA Bank Field', '1993-11-30'),
(6, 'Tampa Bay Buccaneers', 'Tampa', 232311415, 'Raymond James Stadium', '1974-04-24'),
(7, 'Kansas City Chiefs', 'Kansas City', 227369049, 'GEHA Field at Arrowhead Stadium', '1959-08-14'),
(8, 'Los Angeles Rams', 'Inglewood', 214789198, 'SoFi Stadium', '1936-01-01');

-- --------------------------------------------------------

--
-- Structure de la table `joueurs`
--

DROP TABLE IF EXISTS `joueurs`;
CREATE TABLE IF NOT EXISTS `joueurs` (
  `nJoueur` int NOT NULL AUTO_INCREMENT,
  `nomJoueurs` varchar(30) NOT NULL,
  `prenomJoueurs` varchar(30) NOT NULL,
  `dateNaiss` date NOT NULL,
  `nationalite` varchar(35) NOT NULL,
  `poste` enum('QB','WR','OL','DL','RB','FB','TE','LB','CB','S','K','P','KR','PR','SP') NOT NULL,
  `nClub` int NOT NULL,
  `salaire` int NOT NULL,
  `taille` float NOT NULL,
  `poids` float NOT NULL,
  `sprint40y` float NOT NULL,
  PRIMARY KEY (`nJoueur`),
  KEY `nClub` (`nClub`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `joueurs`
--

INSERT INTO `joueurs` (`nJoueur`, `nomJoueurs`, `prenomJoueurs`, `dateNaiss`, `nationalite`, `poste`, `nClub`, `salaire`, `taille`, `poids`, `sprint40y`) VALUES
(1, 'Bourne', 'Kendrick', '1995-08-04', 'Americain', 'WR', 1, 6416666, 185, 86, 4.55),
(2, 'Scott', 'Boston', '1995-04-27', 'Americain', 'RB', 2, 1750000, 168, 92, 4.4),
(3, 'Njoku', 'David', '1996-07-10', 'Americain', 'TE', 3, 3328000, 193, 112, 4.64),
(4, 'Jefferson', 'Justin', '1999-06-16', 'Americain', 'WR', 4, 3578946, 185, 88, 4.43),
(5, 'Lawrence', 'Trevor', '1999-10-06', 'Americain', 'QB', 5, 8362156, 198, 97, 4.78),
(6, 'White', 'Devin', '1998-02-17', 'Americain', 'LB', 6, 9527759, 183, 108, 4.42),
(7, 'Mahomes', 'Patrick', '1995-09-17', 'Americain', 'QB', 7, 42403506, 188, 102, 4.8),
(8, 'Donald', 'Aaron', '1991-05-23', 'Americain', 'DL', 8, 29842645, 185, 127, 4.68);

-- --------------------------------------------------------

--
-- Structure de la table `transferts`
--

DROP TABLE IF EXISTS `transferts`;
CREATE TABLE IF NOT EXISTS `transferts` (
  `nTransfert` int NOT NULL AUTO_INCREMENT,
  `nJoueur` int NOT NULL,
  `Montant` int NOT NULL,
  `Date` date NOT NULL,
  `Acheteur` varchar(30) NOT NULL,
  PRIMARY KEY (`nTransfert`),
  KEY `nJoueur` (`nJoueur`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `joueurs`
--
ALTER TABLE `joueurs`
  ADD CONSTRAINT `joueurs_ibfk_1` FOREIGN KEY (`nClub`) REFERENCES `clubs` (`nClub`) ON DELETE CASCADE;

--
-- Contraintes pour la table `transferts`
--
ALTER TABLE `transferts`
  ADD CONSTRAINT `transferts_ibfk_1` FOREIGN KEY (`nJoueur`) REFERENCES `joueurs` (`nJoueur`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
