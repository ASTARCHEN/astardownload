# Host: localhost  (Version: 5.5.53)
# Date: 2017-07-09 11:17:28
# Generator: MySQL-Front 5.3  (Build 4.234)

# /*!40101 SET NAMES utf8 */;

#
# Structure for table "astar_action"
#
CREATE DATABASE IF NOT EXISTS astar;

USE astar;

CREATE TABLE IF NOT EXISTS `astar_action` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `fileid` int(11) DEFAULT NULL,
  `actioncode` int(11) DEFAULT NULL,
  `integralschange` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

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
  `uploadtime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

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
  `searchtime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

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
  `registertime` datetime DEFAULT NULL,
  `integrals` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Data for table "astar_user"
#

