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


ALTER TABLE Course ADD
    CONSTRAINT course_credit CHECK (credit BETWEEN 0.5 AND 6);
ALTER TABLE Course ADD
    CONSTRAINT course_restno CHECK (restno >= 0);

ALTER TABLE Teacher ADD
    CONSTRAINT teacher_sex CHECK (sex IN ('男','女',NULL));
ALTER TABLE Teacher ADD
    CONSTRAINT teacher_degree CHECK (degree IN ('本科','硕士','博士','博士后',NULL));
ALTER TABLE Teacher ADD
    CONSTRAINT teacher_title CHECK (title IN ('助教','讲师','副教授','教授',NULL));

ALTER TABLE Student ADD
    CONSTRAINT student_sex CHECK (sex IN ('男','女',NULL));

ALTER TABLE SC ADD
    CONSTRAINT sc_grade CHECK ((cgrade BETWEEN 0 AND 100) OR (cgrade IS NULL));

