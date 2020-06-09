CREATE TABLE Course (
    cno NUMERIC ( 6 ),
    cname VARCHAR ( 10 ) NOT NULL,
    ctype VARCHAR ( 10 ),
    credit NUMERIC ( 1 ),
    chour NUMERIC ( 2 ),
    ctime VARCHAR ( 20 ),
    cplace VARCHAR ( 20 ),
    restno NUMERIC ( 3 ),
    PRIMARY KEY ( cno ) 
);

CREATE TABLE Teacher (
    tno NUMERIC ( 6 ),
    tname VARCHAR ( 10 ) NOT NULL,
    sex VARCHAR ( 2 ),
    birthday DATE,
    place VARCHAR ( 20 ),
    dept VARCHAR ( 20 ),
    degree VARCHAR ( 10 ),
    title VARCHAR ( 10 ),
    PRIMARY KEY ( tno ) 
);

CREATE TABLE Student (
    sno NUMERIC ( 6 ),
    sname VARCHAR ( 10 ) NOT NULL,
    sex VARCHAR ( 2 ),
    birthday DATE,
    place VARCHAR ( 10 ),
    dept VARCHAR ( 20 ),
    major VARCHAR ( 20 ),
    sgrade VARCHAR ( 2 ),
    PRIMARY KEY ( sno ) 
);

CREATE TABLE SC (
    sno NUMERIC ( 6 ),
    cno NUMERIC ( 6 ),
    cgrade NUMERIC ( 3 ),
    FOREIGN KEY ( sno ) REFERENCES Student ( sno ),
    FOREIGN KEY ( cno ) REFERENCES Course ( cno ),
    PRIMARY KEY ( sno, cno ) 
);

CREATE TABLE TC (
    cno NUMERIC ( 6 ),
    tno NUMERIC ( 6 ) NOT NULL,
    FOREIGN KEY ( cno ) REFERENCES Course ( cno ),
    FOREIGN KEY ( tno ) REFERENCES Teacher ( tno ),
PRIMARY KEY ( cno ) 
);

