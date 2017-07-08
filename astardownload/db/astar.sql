# Host: localhost  (Version: 5.5.32)
# Date: 2017-07-07 11:21:02
# Generator: MySQL-Front 5.3  (Build 4.234)


CREATE DATABASE IF NOT EXISTS astar;


# /*!40101 SET NAMES gb2312 */;

#
# Structure for table "astar_action"
#

CREATE TABLE IF NOT EXISTS `astar_action` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) DEFAULT NULL,
  `fieid` varchar(255) DEFAULT NULL,
  `actioncode` varchar(255) DEFAULT NULL,
  `integralschange` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

#
# Data for table "astar_action"
#


#
# Structure for table "astar_file"
#

CREATE TABLE IF NOT EXISTS `astar_file` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) DEFAULT NULL,
  `remotepath` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `uploadtime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

#
# Data for table "astar_file"
#


#
# Structure for table "astar_search"
#

CREATE TABLE IF NOT EXISTS `astar_search` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) DEFAULT NULL,
  `searchstring` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

#
# Data for table "astar_search"
#


#
# Structure for table "astar_user"
#

CREATE TABLE IF NOT EXISTS `astar_user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `QQ` varchar(255) DEFAULT NULL,
  `telphone` varchar(15) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `realname` varchar(255) DEFAULT NULL,
  `IDcard` varchar(255) DEFAULT NULL,
  `registertime` varchar(255) DEFAULT NULL,
  `integrals` varchar(255) DEFAULT NULL,  
  PRIMARY KEY (`Id`)
);

#
# Data for table "astar_user"
#

