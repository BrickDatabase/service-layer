DROP SCHEMA IF EXISTS `subreddit_db` ;

CREATE SCHEMA IF NOT EXISTS `subreddit_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `subreddit_db` ;

DROP TABLE IF EXISTS `subreddit_db`.`subreddit_reference_lookup` ;

CREATE TABLE IF NOT EXISTS `subreddit_db`.`subreddit_reference_lookup` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `abbreviation` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `subreddit_db`.`information` ;

CREATE TABLE IF NOT EXISTS `subreddit_db`.`information` (
  `row_id` INT UNSIGNED AUTO_INCREMENT,
  `subreddit_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `subscribers` INT NULL DEFAULT NULL,
  `active_subscribers` INT NULL DEFAULT NULL,
  `submission` INT NULL DEFAULT NULL,
  `comments` INT NULL DEFAULT NULL,
  PRIMARY KEY (`row_id`),
  INDEX `fk_information_subreddit_reference_lookup_idx` (`subreddit_id` ASC) VISIBLE,
  CONSTRAINT `fk_information_subreddit_reference_lookup`
    FOREIGN KEY (`subreddit_id`)
    REFERENCES `subreddit_db`.`subreddit_reference_lookup` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);