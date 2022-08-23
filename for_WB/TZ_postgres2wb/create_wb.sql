create database create_wb;

use create_wb;

CREATE TABLE `author` (
  `name` varchar(255) PRIMARY KEY,
  `path_to_home` varchar(511) UNIQUE,
  `path_to_subjects` varchar(511) NOT NULL,
  `path_to_subj_conf` varchar(511) NOT NULL,
  `path_to_templates` varchar(511) NOT NULL,
  `path_to_templ_conf` varchar(511) NOT NULL
);


CREATE TABLE `image_position` (
  `name` varchar(255) PRIMARY KEY
);


CREATE TABLE `brand` (
  `name` varchar(255) PRIMARY KEY
);



CREATE TABLE `print_zone` (
  `name` varchar(255) PRIMARY KEY,
  `width_px` int,
  `height_px` int
);



CREATE TABLE `infographic_color` (
  `name` varchar(255) PRIMARY KEY,
  `config` varchar(255)
);


CREATE TABLE `product_type` (
  `name` varchar(255) PRIMARY KEY,
  `class` varchar(127) ,
  `variety` varchar(127),
  `print_zone` varchar(255),
  `path_type` varchar(511)
);


CREATE TABLE `common_photo` (
  `name` varchar(255) NOT NULL,
  `product_type` varchar(255) NOT NULL,
  `path_dir` varchar(511) NOT NULL,
  PRIMARY KEY (`name`, `product_type`)
);


CREATE TABLE `subject` (
  `name` varchar(255) PRIMARY KEY,
  `count_arts` int,
  `template` varchar(255),
  `author` varchar(255),
  `path_subject` varchar(511)
);


CREATE TABLE `template_group` (
  `name` varchar(255) PRIMARY KEY,
  `path_image` varchar(511)
);

CREATE TABLE `template` (
  `name` varchar(255) PRIMARY KEY,
  `group` varchar(255),
  `author` varchar(255),
  `path_exel` varchar(511),
  `path_json` varchar(511)
);


CREATE TABLE `mockup` (
  `name` varchar(255),
  `product_type` varchar(255),
  `path_mockup1` varchar(511) NOT NULL,
  `params1` varchar(255) NOT NULL,
  `path_mockup2` varchar(511),
  `params2` varchar(255),
  `path_mockup3` varchar(511),
  `params3` varchar(255),
  PRIMARY KEY (`name`, `product_type`)
);


CREATE TABLE `infographic` (
  `name` varchar(190),
  `product_type` varchar(190),
  `mockup` varchar(190),
  `color` varchar(190),
  `path_infogr1` varchar(511),
  `path_infogr2` varchar(511),
  `path_infogr3` varchar(511),
  PRIMARY KEY (`name`, `product_type`, `color`, `mockup`)
);

CREATE TABLE `product_group` (
  `name` varchar(255) PRIMARY KEY,
  `subject` varchar(255),
  `product_type` varchar(191),
  `common_photo` varchar(255) DEFAULT "default",
  `mockup` varchar(191) DEFAULT "default",
  `infographic` varchar(191) DEFAULT "default",
  `infographic_color` varchar(191) DEFAULT "black",
  `scale_print` int DEFAULT 100,
  `brand` varchar(255),
  `image_position` varchar(255) DEFAULT "center",
  `backgr_color_mockup` varchar(511),
  `backgr_color_print` varchar(511),
  `path_product` varchar(511)
);

CREATE TABLE `product` (
  `name` varchar(255) PRIMARY KEY,
  `product_group` varchar(255) NOT NULL,
  `print_number` int NOT NULL,
  `count_of_sales` int DEFAULT 0,
  `path_mockups` varchar(511),
  `path_print` varchar(511)
);

CREATE TABLE `wb_base_card` (
  `product_type` varchar(255) UNIQUE,
  `article` varchar(511) NOT NULL,
  `barcode` varchar(31) NOT NULL,
  `price` int NOT NULL,
  `discount` int DEFAULT 0,
  `stock` int DEFAULT 0,
  `path_base_json` varchar(511) NOT NULL,
  `path_insert_json` varchar(511) NOT NULL
);

CREATE TABLE `wildberries` (
  `barcode` varchar(63) PRIMARY KEY,
  `article` varchar(255),
  `size` varchar(31) DEFAULT 0,
  `sale` int NOT NULL DEFAULT 0,
  `stock` int NOT NULL DEFAULT 900
);


CREATE TABLE `upload_list` (
  `product` varchar(255) UNIQUE,
  `wb` boolean DEFAULT False,
  `ozon` boolean DEFAULT False,
  `aliexprru` boolean DEFAULT False,
  `ymarket` boolean DEFAULT False
);


CREATE UNIQUE INDEX pr_type ON `product_type` (`class`, `variety`);

CREATE UNIQUE INDEX pr_group ON `product_group` (`subject`, `product_type`);

CREATE UNIQUE INDEX wildberries ON `wildberries` (`article`, `size`);

ALTER TABLE `wb_base_card` ADD FOREIGN KEY (`product_type`) REFERENCES `product_type` (`name`);

ALTER TABLE `wildberries` ADD FOREIGN KEY (`article`) REFERENCES `product` (`name`);

ALTER TABLE `upload_list` ADD FOREIGN KEY (`product`) REFERENCES `product` (`name`);

ALTER TABLE `product_type` ADD FOREIGN KEY (`print_zone`) REFERENCES `print_zone` (`name`);

ALTER TABLE `common_photo` ADD FOREIGN KEY (`product_type`) REFERENCES `product_type` (`name`);

ALTER TABLE `product` ADD FOREIGN KEY (`product_group`) REFERENCES `product_group` (`name`);

ALTER TABLE `subject` ADD FOREIGN KEY (`template`) REFERENCES `template` (`name`);

ALTER TABLE `subject` ADD FOREIGN KEY (`author`) REFERENCES `author` (`name`);

ALTER TABLE `template` ADD FOREIGN KEY (`group`) REFERENCES `template_group` (`name`);

ALTER TABLE `template` ADD FOREIGN KEY (`author`) REFERENCES `author` (`name`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`subject`) REFERENCES `subject` (`name`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`product_type`) REFERENCES `product_type` (`name`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`infographic`, `product_type`, `infographic_color`, `mockup`) REFERENCES `infographic` (`name`, `product_type`, `color`, `mockup`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`common_photo`, `product_type`) REFERENCES `common_photo` (`name`, `product_type`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`mockup`, `product_type`) REFERENCES `mockup` (`name`, `product_type`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`image_position`) REFERENCES `image_position` (`name`);

ALTER TABLE `product_group` ADD FOREIGN KEY (`brand`) REFERENCES `brand` (`name`);

ALTER TABLE `mockup` ADD FOREIGN KEY (`product_type`) REFERENCES `product_type` (`name`);

ALTER TABLE `infographic` ADD FOREIGN KEY (`color`) REFERENCES `infographic_color` (`name`);

ALTER TABLE `infographic` ADD FOREIGN KEY (`product_type`) REFERENCES `product_type` (`name`);

ALTER TABLE `infographic` ADD FOREIGN KEY (`mockup`, `product_type`) REFERENCES `mockup` (`name`, `product_type`);

select * from product;

select * from product_group;

select * from wb_base_card;

select * from upload_list;
