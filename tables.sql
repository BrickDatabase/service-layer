DROP DATABASE IF EXISTS subreddit_db ;

CREATE DATABASE subreddit_db;
\c subreddit_db ;

DROP TABLE IF EXISTS subreddit_reference_lookup ;

CREATE TABLE IF NOT EXISTS subreddit_reference_lookup (
  id INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  abbreviation VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE information (
  row_id SERIAL,
  subreddit_id INT NOT NULL,
  date TIMESTAMP NOT NULL,
  subscribers INT NULL DEFAULT NULL,
  active_subscribers INT NULL DEFAULT NULL,
  submission INT NULL DEFAULT NULL,
  comments INT NULL DEFAULT NULL,
  PRIMARY KEY (row_id),
  CONSTRAINT fk_information_subreddit_reference_lookup
    FOREIGN KEY (subreddit_id)
    REFERENCES subreddit_reference_lookup (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (1, 'Rochester Institute of Technology', 'rit');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (2, 'Minecraft', 'minecraft');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (3, 'Bitcoin', 'bitcoin');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (4, 'Wallstreet Bets', 'wallstreetbets');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (5, 'Robinhood', 'robinhood');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (6, 'GameStop', 'gamestop');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (7, 'Sony PlayStation', 'playstation');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (8, 'Microsoft Xbox', 'xbox');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (9, 'Nintendo', 'nintendo');
INSERT INTO subreddit_reference_lookup (id, name, abbreviation) VALUES (10, 'Gaming', 'gaming');