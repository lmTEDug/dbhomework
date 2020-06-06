CREATE TABLE Teacher(
  tno NUMERIC(6),
  tname VARCHAR(10) NOT NULL,
  sex VARCHAR(2),
  birthdate DATE,
  place VARCHAR(20),
  dept VARCHAR(20),
  degree VARCHAR(10),
  title VARCHAR(10),
  PRIMARY KEY(tno));
