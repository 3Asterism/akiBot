/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80033 (8.0.33)
 Source Host           : localhost:3306
 Source Schema         : live_stats

 Target Server Type    : MySQL
 Target Server Version : 80033 (8.0.33)
 File Encoding         : 65001

 Date: 03/08/2023 01:29:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bili_live_status
-- ----------------------------
DROP TABLE IF EXISTS `bili_live_status`;
CREATE TABLE `bili_live_status`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `uid` bigint NOT NULL COMMENT '主播uid',
  `room_id` int NULL DEFAULT NULL COMMENT '主播直播间id',
  `live_status` int NULL DEFAULT NULL COMMENT '直播间状态',
  `uname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '直播者的姓名',
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '检测时间',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '直播间标题',
  PRIMARY KEY (`id`, `uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of bili_live_status
-- ----------------------------
INSERT INTO `bili_live_status` VALUES (6, 592507317, 22259479, 0, '烤鱼子Official', '2023-08-03 01:29:01', '????群峦????');
INSERT INTO `bili_live_status` VALUES (7, 1437582453, 22816111, 2, '東雪蓮Official', '2023-08-02 22:40:53', '八月第一天');
INSERT INTO `bili_live_status` VALUES (8, 7706705, 80397, 0, '阿梓从小就很可爱', '2023-08-02 23:57:00', '我来啦！');
INSERT INTO `bili_live_status` VALUES (9, 1778026586, 25512465, 2, '米诺高分少女', '2023-08-02 22:41:17', '【3D】青春猪头少女');
INSERT INTO `bili_live_status` VALUES (10, 730732, 42062, 0, '瓶子君152', '2023-08-02 23:57:00', '一转正确');
INSERT INTO `bili_live_status` VALUES (11, 283886865, 9234980, 2, '说说Crystal', '2023-08-03 00:22:32', '进行一个杂的歌~!');
INSERT INTO `bili_live_status` VALUES (12, 3493271057730096, 27484357, 2, '妮莉安Lily', '2023-08-03 00:35:16', '☆ 歌回 8月你好~');
INSERT INTO `bili_live_status` VALUES (13, 188679, 685026, 2, 'Niya阿布', '2023-08-03 00:39:51', '【歌回】真的唱一会儿吧');
INSERT INTO `bili_live_status` VALUES (14, 1265680561, 22603245, 2, '永雏塔菲', '2023-08-03 00:40:24', '潜水员戴菲');
INSERT INTO `bili_live_status` VALUES (15, 1950658, 41682, 0, '早稻叽', '2023-08-03 00:41:08', '今天就把三伏通了！');
INSERT INTO `bili_live_status` VALUES (16, 1734978373, 22696954, 2, '小柔Channel', '2023-08-03 00:41:42', '虚研社六周年画画接龙~');
INSERT INTO `bili_live_status` VALUES (17, 10850238, 594461, 2, '-阿蕊娅Aria-', '2023-08-03 00:42:21', '主播传送中');
INSERT INTO `bili_live_status` VALUES (18, 513613827, 24402390, 0, '浙艺没有菲戈', '2023-08-03 00:44:01', '练琴');
INSERT INTO `bili_live_status` VALUES (19, 387636363, 21013446, 2, '雫るる_Official', '2023-08-03 00:46:16', '做行李');
INSERT INTO `bili_live_status` VALUES (20, 703018634, 22605289, 0, '莱妮娅_Rynia', '2023-08-03 00:46:48', '【FF14】红莲节还没结束吧');

SET FOREIGN_KEY_CHECKS = 1;
