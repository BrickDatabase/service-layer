DROP TABLE IF EXISTS dayTable;
DROP TABLE IF EXISTS users;
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

create table schedule
(
	id serial not null,
	posted date,
	new_subscriber integer,
	new_comment integer,
	new_submission integer,
	new_active_subs integer,
	subreddit_id integer,
	total_subscriber integer,
	total_comment integer,
	total_submission integer,
	total_active_subs integer
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