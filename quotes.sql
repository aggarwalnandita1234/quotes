CREATE DATABASE  IF NOT EXISTS `quotes` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `quotes`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: quotes
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favorites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `quote_id` int(11) NOT NULL,
  `favorites_of` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_favorites_users1_idx` (`user_id`),
  KEY `fk_favorites_quotes1_idx` (`quote_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES (32,2,16,3),(33,3,18,3),(35,3,18,4),(37,3,18,4),(38,2,16,4),(39,3,18,2),(40,2,16,2);
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(45) DEFAULT NULL,
  `quote` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_quotes_table1_idx` (`user_id`),
  CONSTRAINT `fk_quotes_table1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (1,'Douglas Adams','This is quote1 by Douglas',1),(2,'author2','This is quote 1 by author2',1),(3,'Author 3','This is quote 1 by author 3',1),(4,'author4','This is quote 1 by author 4',1),(5,'author4','This is quote 1 by author 4',1),(6,'author5','seeing if session is clearing',1),(7,'author6','this is quote 6',1),(8,'author 7','This is quote 1 by athor 7',1),(9,'author 7','This is quote 1 by athor 7',1),(10,'Author8','This is review by author8',1),(11,'Author8','This is quote by author8',1),(15,'author 10','some quote by author 10',1),(16,'Shakespeer','This is absolutely new by user 2',2),(17,'Debabrata Dash','He has not written anything yet',3),(18,'Isha dash','keep playing, keep smiling and keep messing around',3),(19,'Author11','This is a new author being added by user 4',4);
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `dob` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user1','user','email1@abc.com','$2b$12$egCOSRUY5xlBmHWHNTHo1OMSavWflXXAcgsq44lwluCtqSbLOMGQa',NULL),(2,'user2','user','email2@abc.com','$2b$12$9hAptrpy8iatiQzN0tIwheSTbKR2Vet9XPbhn3/bLpbED9mHdCu3S',NULL),(3,'user3','user','email3@abc.com','$2b$12$SlC24.1URsdZiiAJKVu9teW.MN/lLBr5xomC3oohsf7LhI6FexDUi',NULL),(4,'user4','user','email4@abc.com','$2b$12$w41DcgUSHfSunYi6ChgCXOCqkLWhrcCGZ60JF5mPXvWl5i9fUZP8O',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-22 15:47:12
