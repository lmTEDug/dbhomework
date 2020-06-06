CREATE TABLE Course(
  cno NUMERIC(6),
  cname VARCHAR(10) NOT NULL,
  ctype VARCHAR(10),
  credit NUMERIC(1),
  chour NUMERIC(2),
  ctime VARCHAR(20),
  cplace VARCHAR(20),
  restno NUMERIC(3),
  PRIMARY KEY(cno));
