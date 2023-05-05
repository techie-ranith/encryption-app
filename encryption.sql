-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2023 at 03:20 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `encryption`
--

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE `info` (
  `id` int(4) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`id`, `username`, `password`, `email`) VALUES
(1, 'Ranith', '123', '123ranith@gmail.com'),
(2, 'Gunawardana', '', 'gunawardana@gmail.com'),
(3, 'Perera', '', 'perera@gmail.com'),
(4, 'kamal', 'k123', 'kumara@gmail.com'),
(5, 'galaxy', '', 'galaxy@email.com'),
(6, 'user', '', 'user@gmail.com'),
(7, 'Cipla', 'cipla123', 'cipla@gmail.com'),
(8, 'Cipla', 'cipla123', 'cipla@gmail.com'),
(9, 'Cipla', 'cipla123', 'cipla@gmail.com'),
(10, 'regal', 'regal123', 'regal@hotmail.com'),
(11, 'Shemila', 'shemila123', 'shemila@gmail.com'),
(12, 'samsung', 'samsung123', 'samsung@gmail.com'),
(13, 'samsung', 'samsung123', 'samsung@gmail.com'),
(14, 'Tree', '123', 'tree@gmail.com'),
(15, 'youtube', 'youtube123', 'youtube@gmail.com'),
(16, 'shemila', '', ''),
(17, 'sonali', '', ''),
(18, 'Kaveesha', 'kaveesha123', 'kaveesha@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `info`
--
ALTER TABLE `info`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
