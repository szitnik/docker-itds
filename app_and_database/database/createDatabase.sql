CREATE DATABASE IF NOT EXISTS data_science CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE data_science;

CREATE TABLE `data_science`.`employees` (
  `name` VARCHAR(50) NOT NULL,
  `hobbies` VARCHAR(5000) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`));

INSERT INTO employees (`name`,`hobbies`,`role`) VALUES ("John Doe", "I like cycling, mountain biking and skiing!!!", "Director of operations");
INSERT INTO employees (`name`,`hobbies`,`role`) VALUES ("Melanie Oesch", "As the best jodeling singer, the love of my life is singing all day long. I come from Switzerland and have achieved many prizes. Maybe I also visit your hometown and get to know you.", "Chairman of kids programme");
INSERT INTO employees (`name`,`hobbies`,`role`) VALUES ("Vladimir Zookeeper", "Animals are the nicest and very polite creatures in our world. I have observed many species already and I have not found an animal that would harm me without a reason (in comparison to a human being). My dream is to play with animals every day.", "Animal feeder");