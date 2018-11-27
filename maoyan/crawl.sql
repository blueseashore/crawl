# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 192.168.31.100 (MySQL 5.7.22-log)
# Database: shengxi_v2
# Generation Time: 2018-11-27 09:46:54 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table sx_maoyan
# ------------------------------------------------------------

CREATE TABLE `sx_maoyan` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `my_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '猫眼影片ID',
  `movie_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片标题',
  `movie_alias` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '影片别名',
  `movie_tag` json NOT NULL COMMENT '影片标签',
  `movie_poster` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片海报',
  `movie_len` smallint(6) NOT NULL DEFAULT '0' COMMENT '影片长度，单位：分钟',
  `movie_starring` json DEFAULT NULL COMMENT '影片演员',
  `movie_intro` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片介绍',
  `movie_area` json NOT NULL COMMENT '影片产地国家/地区',
  `movie_type` json NOT NULL COMMENT '影评类型',
  `release_at` varchar(25) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '上映时间',
  `created_at` int(10) unsigned NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table sx_movie
# ------------------------------------------------------------

CREATE TABLE `sx_movie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `movie_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片标题',
  `movie_alias` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片别名',
  `movie_tag` json NOT NULL COMMENT '影片标签',
  `movie_poster` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片海报地址',
  `movie_starring` json NOT NULL COMMENT '影片演员',
  `movie_len` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '影片长度，单位：分钟',
  `movie_intro` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '影片介绍',
  `movie_score` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '影片得分，100分制',
  `movie_area` json NOT NULL COMMENT '影片产地国家/地区',
  `movie_type` json NOT NULL COMMENT '影评类型',
  `is_hot` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '是否热门，1=是，0=否',
  `user_num` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '影评人数',
  `comment_num` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '影片评论数',
  `movie_status` tinyint(3) unsigned NOT NULL DEFAULT '1' COMMENT '影片状态，1=正常，3=系统删除',
  `released_at` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '上映时间',
  `created_at` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `updated_at` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `deleted_at` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '删除时间',
  PRIMARY KEY (`id`),
  KEY `movie_movie_title_index` (`movie_title`),
  KEY `movie_movie_alias_index` (`movie_alias`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
