-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 29, 2020 at 04:09 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.28-3+ubuntu18.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Log-identificacion`
--

-- --------------------------------------------------------

--
-- Table structure for table `CycleSummary`
--

CREATE TABLE `CycleSummary` (
  `Id` int(11) NOT NULL,
  `IdTest` int(11) NOT NULL,
  `GuidTest` varchar(50) NOT NULL,
  `Ciclo` varchar(20) NOT NULL,
  `TotalIdentificacion` int(11) DEFAULT NULL,
  `TotalFrameReceived` int(11) NOT NULL,
  `TotalBeforeProcessing` int(11) NOT NULL,
  `TotalFaceAPIResults` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Identificacion`
--

CREATE TABLE `Identificacion` (
  `Id` int(11) NOT NULL,
  `Item` int(11) NOT NULL,
  `File` varchar(50) NOT NULL,
  `Timeline` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `PersonId` varchar(50) NOT NULL,
  `MatchProbability` float NOT NULL,
  `GroupId` varchar(50) NOT NULL,
  `LocalPersistedId` varchar(50) NOT NULL,
  `TestID` int(11) NOT NULL DEFAULT '-1',
  `CicloTest` int(1) NOT NULL,
  `StartCiclo` varchar(30) NOT NULL,
  `GuidTest` varchar(50) NOT NULL,
  `Hostname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Test`
--

CREATE TABLE `Test` (
  `Id` int(11) NOT NULL,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `GUID` varchar(50) NOT NULL,
  `Hostname` varchar(30) NOT NULL,
  `CameraMode` varchar(10) DEFAULT NULL,
  `IdentificationService` varchar(10) NOT NULL,
  `BetweenPictures` int(3) NOT NULL,
  `Version` varchar(30) NOT NULL,
  `TotalCiclos` int(5) NOT NULL,
  `Duracion` int(11) NOT NULL,
  `Descripcion` varchar(250) DEFAULT NULL,
  `Recurso` varchar(250) DEFAULT NULL,
  `IdentificacionTest` int(1) DEFAULT '0',
  `Resultado` int(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CycleSummary`
--
ALTER TABLE `CycleSummary`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `Identificacion`
--
ALTER TABLE `Identificacion`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `Test`
--
ALTER TABLE `Test`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CycleSummary`
--
ALTER TABLE `CycleSummary`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Identificacion`
--
ALTER TABLE `Identificacion`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Test`
--
ALTER TABLE `Test`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
