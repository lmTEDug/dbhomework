CREATE TABLE TC(
  cno NUMERIC(6),
  tno NUMERIC(6) NOT NULL ,
  FOREIGN KEY (cno) REFERENCES Course(cno),
  FOREIGN KEY (tno) REFERENCES Teacher(tno),
  PRIMARY KEY (cno));


