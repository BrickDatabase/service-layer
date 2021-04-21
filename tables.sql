DROP DATABASE IF EXISTS subreddit_db ;

CREATE DATABASE subreddit_db;
\c subreddit_db ;


DROP TABLE IF EXISTS own;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS day;
DROP TABLE IF EXISTS information;
DROP TABLE IF EXISTS lookup;

CREATE TABLE IF NOT EXISTS lookup (
  id SERIAL,
  name VARCHAR(45) NOT NULL,
  abbreviation VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

CREATE UNIQUE INDEX lookup_abbreviation_uindex
ON lookup (abbreviation);


CREATE TABLE information (
  id SERIAL,
  subreddit_id INT NOT NULL,
  date TIMESTAMP NOT NULL,
  subscribers INT NULL DEFAULT 0,
  active_subscribers INT NULL DEFAULT 0,
  submission INT NULL DEFAULT 0,
  comments INT NULL DEFAULT 0,
  PRIMARY KEY (id),
  CONSTRAINT fk_lookup
    FOREIGN KEY (subreddit_id)
    REFERENCES lookup (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

create table day
(
	id SERIAL
		CONSTRAINT day_pk
			PRIMARY KEY
		CONSTRAINT infold
			REFERENCES information (id),
	day int NOT NULL
);

create table users
(
	id serial
		constraint user_pk
			primary key,
	username varchar(45) NOT NULL,
	password varchar(150) NOT NULL,
  role INT
);

create table own
(
    user_id int NOT NULL,
    subreddit_id int NOT NULL,
    CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT subreddit_id FOREIGN KEY (subreddit_id) REFERENCES lookup(id)

);





INSERT INTO lookup (name, abbreviation) VALUES ('Rochester Institute of Technology', 'rit');
INSERT INTO lookup (name, abbreviation) VALUES ('Minecraft', 'minecraft');
INSERT INTO lookup (name, abbreviation) VALUES ('Bitcoin', 'bitcoin');
INSERT INTO lookup (name, abbreviation) VALUES ('Wallstreet Bets', 'wallstreetbets');
INSERT INTO lookup (name, abbreviation) VALUES ('Robinhood', 'robinhood');
INSERT INTO lookup (name, abbreviation) VALUES ('GameStop', 'gamestop');
INSERT INTO lookup (name, abbreviation) VALUES ('Sony PlayStation', 'playstation');
INSERT INTO lookup (name, abbreviation) VALUES ('Microsoft Xbox', 'xbox');
INSERT INTO lookup (name, abbreviation) VALUES ('Nintendo', 'nintendo');
INSERT INTO lookup (name, abbreviation) VALUES ('Gaming', 'gaming');