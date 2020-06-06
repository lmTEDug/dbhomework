CREATE TABLE SC(
  sno NUMERIC(6),
  cno NUMERIC(6),
  cgrade NUMERIC(3),
  FOREIGN KEY (sno) REFERENCES Student(sno),
  FOREIGN KEY (cno) REFERENCES Course(cno),
  PRIMARY KEY (sno,cno));
