DROP DATABASE IF EXISTS subreddit_db ;

CREATE DATABASE subreddit_db;
\c subreddit_db ;


DROP TABLE IF EXISTS day;
DROP TABLE IF EXISTS information;
DROP TABLE IF EXISTS lookup;

CREATE TABLE IF NOT EXISTS lookup (
  id INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  abbreviation VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE information (
  id SERIAL NOT NULL,
  subreddit_id INT NOT NULL,
  date TIMESTAMP NOT NULL,
  subscribers INT NULL DEFAULT NULL,
  active_subscribers INT NULL DEFAULT NULL,
  submission INT NULL DEFAULT NULL,
  comments INT NULL DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_lookup
    FOREIGN KEY (subreddit_id)
    REFERENCES lookup (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

create table day
(
	id serial not null
		constraint day_pk
			primary key
		constraint infold
			references information (id),
	day int not null
);

INSERT INTO lookup (id, name, abbreviation) VALUES (1, 'Rochester Institute of Technology', 'rit');
INSERT INTO lookup (id, name, abbreviation) VALUES (2, 'Minecraft', 'minecraft');
INSERT INTO lookup (id, name, abbreviation) VALUES (3, 'Bitcoin', 'bitcoin');
INSERT INTO lookup (id, name, abbreviation) VALUES (4, 'Wallstreet Bets', 'wallstreetbets');
INSERT INTO lookup (id, name, abbreviation) VALUES (5, 'Robinhood', 'robinhood');
INSERT INTO lookup (id, name, abbreviation) VALUES (6, 'GameStop', 'gamestop');
INSERT INTO lookup (id, name, abbreviation) VALUES (7, 'Sony PlayStation', 'playstation');
INSERT INTO lookup (id, name, abbreviation) VALUES (8, 'Microsoft Xbox', 'xbox');
INSERT INTO lookup (id, name, abbreviation) VALUES (9, 'Nintendo', 'nintendo');
INSERT INTO lookup (id, name, abbreviation) VALUES (10, 'Gaming', 'gaming');