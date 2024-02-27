-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-02-2024 a las 02:33:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bahaleon.db`
--
CREATE DATABASE IF NOT EXISTS `bahaleon.db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bahaleon.db`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `produccion`
--
-- Creación: 26-02-2024 a las 22:19:20
-- Última actualización: 26-02-2024 a las 23:02:55
--

CREATE TABLE `produccion` (
  `id_produccion` int(11) NOT NULL,
  `pcepl` decimal(10,2) NOT NULL,
  `pcspl` decimal(10,2) NOT NULL,
  `rtso` decimal(10,2) NOT NULL,
  `rmlp` decimal(10,2) NOT NULL,
  `pcept` decimal(10,2) NOT NULL,
  `pcspt` decimal(10,2) NOT NULL,
  `rtph` decimal(10,2) NOT NULL,
  `rmtp` decimal(10,2) NOT NULL,
  `pcepd` decimal(10,2) NOT NULL,
  `pcspd` decimal(10,2) NOT NULL,
  `rtcas` decimal(10,2) NOT NULL,
  `rmcp` decimal(10,2) NOT NULL,
  `pnoiepr` decimal(10,2) NOT NULL,
  `pchospr` decimal(10,2) NOT NULL,
  `rtcascho` decimal(10,2) NOT NULL,
  `rmpcho` decimal(10,2) NOT NULL,
  `rmermatotal` decimal(10,2) NOT NULL,
  `fecreacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `produccion`
--

INSERT INTO `produccion` (`id_produccion`, `pcepl`, `pcspl`, `rtso`, `rmlp`, `pcept`, `pcspt`, `rtph`, `rmtp`, `pcepd`, `pcspd`, `rtcas`, `rmcp`, `pnoiepr`, `pchospr`, `rtcascho`, `rmpcho`, `rmermatotal`, `fecreacion`) VALUES
(1, 1000.00, 900.00, 100.00, 10.00, 800.00, 700.00, 100.00, 12.50, 700.00, 600.00, 100.00, 14.29, 600.00, 500.00, 100.00, 16.67, 53.46, '2024-02-26 23:02:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--
-- Creación: 26-02-2024 a las 22:24:29
-- Última actualización: 26-02-2024 a las 22:28:02
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `usuario` text NOT NULL,
  `clave` text NOT NULL,
  `privi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `usuario`, `clave`, `privi`) VALUES
(1, 'admin', '12345', 0),
(3, 'usuario', '12345', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `produccion`
--
ALTER TABLE `produccion`
  ADD PRIMARY KEY (`id_produccion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `produccion`
--
ALTER TABLE `produccion`
  MODIFY `id_produccion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
