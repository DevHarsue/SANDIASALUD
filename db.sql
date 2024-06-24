/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `sandia_salud` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `sandia_salud`;

CREATE TABLE IF NOT EXISTS `antecedentes` (
  `id_antecedente` int(11) NOT NULL AUTO_INCREMENT,
  `antecedentes_patologicos` text DEFAULT NULL,
  `antecedentes_quirurjicos` text DEFAULT NULL,
  `tratamiento_actual` text DEFAULT NULL,
  `fecha_primera_relacion_sexual` date DEFAULT NULL,
  `id_paciente` int(11) NOT NULL,
  PRIMARY KEY (`id_antecedente`) USING BTREE,
  KEY `FK_antecedentes_pacientes` (`id_paciente`),
  CONSTRAINT `FK_antecedentes_pacientes` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id_paciente`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `citas` (
  `id_cita` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_proxima_cita` datetime DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cita`) USING BTREE,
  KEY `FK_citas_pacientes` (`id_paciente`),
  CONSTRAINT `FK_citas_pacientes` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id_paciente`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
  `id_paciente` int(11) NOT NULL,
  `diagnostico` text DEFAULT NULL,
  `tratamiento` text DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_consulta`) USING BTREE,
  KEY `FK__pacientes` (`id_paciente`) USING BTREE,
  CONSTRAINT `FK_consultas_pacientes` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id_paciente`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `embarazos` (
  `id_embarazo` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_ultima_regla` date DEFAULT NULL,
  `fecha_probable_parto` date DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_embarazo`) USING BTREE,
  KEY `FK_embarazos_pacientes` (`id_paciente`),
  CONSTRAINT `FK_embarazos_pacientes` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id_paciente`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `pacientes` (
  `id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `nacionalidad` varchar(1) NOT NULL,
  `cedula` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `dirección` text DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_paciente`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(20) NOT NULL,
  `contraseña_usuario` varchar(64) NOT NULL,
  `permiso_consultas` tinyint(1) DEFAULT NULL,
  `permiso_pacientes_editar_consulta` tinyint(1) DEFAULT NULL,
  `permiso_pacientes_editar_antecedentes` tinyint(1) DEFAULT NULL,
  `permiso_pacientes_editar_embarazo` tinyint(1) DEFAULT NULL,
  `permiso_configuraciones` tinyint(1) DEFAULT NULL,
  `permiso_agregar_usuarios` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

DELIMITER //
CREATE PROCEDURE `buscar_cita`(
	IN `fecha_inicio` DATETIME,
	IN `fecha_fin` DATETIME
)
BEGIN
SELECT id_cita,nacionalidad,cedula,nombre,apellido,fecha_proxima_cita
FROM citas c  JOIN pacientes p ON p.id_paciente=c.id_paciente
WHERE fecha_proxima_cita>=fecha_inicio AND fecha_proxima_cita<=fecha_fin;
END//
DELIMITER ;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
