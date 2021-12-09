DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS watchlist;

CREATE TABLE user(
    uid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE movie(
	mid INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	picture TEXT NOT NULL,
	genre TEXT NOT NULL
);

CREATE TABLE watchlist(
	uid INTEGER NOT NULL,
	mid INTEGER NOT NULL,
	FOREIGN KEY (uid) REFERENCES user(uid),
	FOREIGN KEY (mid) REFERENCES movie(mid)
);

INSERT INTO movie (title, picture, genre) VALUES ("Darbar 2020", "https://justformoviefreaks.in/wp-content/uploads/2019/12/Darbar-Tamil-Movies-2020.jpg", "Action");
INSERT INTO movie (title, picture, genre) VALUES ("The Old Guard 2020", "https://pbs.twimg.com/media/EgAdv_MX0AEifvi.jpg", "Action");
INSERT INTO movie (title, picture, genre) VALUES ("Archenemy 2020", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGZcHjeatQTobLMU9CDx3eDMHfTaFiI5sObA&usqp=CAU", "Thriller");
INSERT INTO movie (title, picture, genre) VALUES ("World War Z 2017", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEAbt_cptz9tEfUCy4i49IJmZbz4HnYStpRw&usqp=CAU", "Horror");



