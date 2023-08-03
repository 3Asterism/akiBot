/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80034 (8.0.34)
 Source Host           : localhost:3306
 Source Schema         : live_stats

 Target Server Type    : MySQL
 Target Server Version : 80034 (8.0.34)
 File Encoding         : 65001

 Date: 03/08/2023 18:31:54
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
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of bili_live_status
-- ----------------------------
INSERT INTO `bili_live_status` VALUES (6, 592507317, 22259479, 0, '烤鱼子Official', '2023-08-03 18:26:13', '????猫猫和雨????');
INSERT INTO `bili_live_status` VALUES (7, 1437582453, 22816111, 2, '東雪蓮Official', '2023-08-03 18:26:18', '八月第一天');
INSERT INTO `bili_live_status` VALUES (8, 7706705, 80397, 1, '阿梓从小就很可爱', '2023-08-03 18:26:19', '我来啦！！');
INSERT INTO `bili_live_status` VALUES (9, 1778026586, 25512465, 2, '米诺高分少女', '2023-08-03 18:26:20', '【3D】青春猪头少女');
INSERT INTO `bili_live_status` VALUES (10, 730732, 42062, 0, '瓶子君152', '2023-08-03 17:39:25', '一转正确');
INSERT INTO `bili_live_status` VALUES (11, 283886865, 9234980, 2, '说说Crystal', '2023-08-03 18:26:23', '进行一个杂的歌~!');
INSERT INTO `bili_live_status` VALUES (12, 3493271057730096, 27484357, 2, '妮莉安Lily', '2023-08-03 18:26:24', '☆ 歌回 8月你好~');
INSERT INTO `bili_live_status` VALUES (13, 188679, 685026, 2, 'Niya阿布', '2023-08-03 18:26:25', '【歌回】真的唱一会儿吧');
INSERT INTO `bili_live_status` VALUES (14, 1265680561, 22603245, 2, '永雏塔菲', '2023-08-03 18:26:26', '小原一会');
INSERT INTO `bili_live_status` VALUES (15, 1950658, 41682, 0, '早稻叽', '2023-08-03 17:39:32', '今天就把三伏通了！');
INSERT INTO `bili_live_status` VALUES (16, 1734978373, 22696954, 1, '小柔Channel', '2023-08-03 18:26:29', '唱歌~杂谈~');
INSERT INTO `bili_live_status` VALUES (17, 10850238, 594461, 2, '-阿蕊娅Aria-', '2023-08-03 18:26:30', '早上好~');
INSERT INTO `bili_live_status` VALUES (18, 513613827, 24402390, 0, '浙艺没有菲戈', '2023-08-03 17:39:35', '练琴');
INSERT INTO `bili_live_status` VALUES (19, 387636363, 21013446, 2, '雫るる_Official', '2023-08-03 18:26:31', '做行李');
INSERT INTO `bili_live_status` VALUES (20, 703018634, 22605289, 0, '莱妮娅_Rynia', '2023-08-03 17:39:38', '【FF14】红莲节还没结束吧');
INSERT INTO `bili_live_status` VALUES (21, 1104048496, 22642754, 2, '桃几OvO', '2023-08-03 18:26:33', '唱会歌');
INSERT INTO `bili_live_status` VALUES (22, 3461576189282324, 26168663, 2, '纱依shayi', '2023-08-03 18:26:33', '练练歌');
INSERT INTO `bili_live_status` VALUES (23, 2132180406, 25034104, 0, '明前奶绿', '2023-08-03 17:39:43', '【视频】奶GN评分中');

SET FOREIGN_KEY_CHECKS = 1;
