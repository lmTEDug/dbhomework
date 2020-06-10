ALTER TABLE Course ADD
    CONSTRAINT course_credit CHECK (credit BETWEEN 0.5 AND 6);
ALTER TABLE Course ADD
    CONSTRAINT course_hour CHECK (chour >= 0);
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

