CREATE VIEW course_available AS SELECT
Course.cno,
Course.cname,
Course.ctype,
Teacher.dept,
Teacher.tname,
Teacher.title,
Course.credit,
Course.chour,
Course.ctime,
Course.cplace,
Course.restno 
FROM
	Course,
	Teacher,
	TC 
WHERE
	Course.cno = TC.cno 
	AND TC.tno = Teacher.tno WITH CHECK OPTION;

CREATE VIEW course_grade AS SELECT
Student.sno,
Course.cno,
Course.cname,
Course.ctype,
Course.credit,
Teacher.dept,
Teacher.tname,
SC.cgrade 
FROM
	Course,
	TC,
	Teacher,
	SC,
	Student 
WHERE
	Course.cno = TC.cno 
	AND TC.tno = Teacher.tno 
	AND Course.cno = SC.cno 
	AND Student.sno = SC.sno WITH CHECK OPTION;
    
CREATE VIEW course_table AS SELECT
Student.sno,
Course.cno,
Course.cname,
Course.ctype,
Teacher.dept,
Teacher.tname,
Course.credit,
Course.chour,
Course.ctime,
Course.cplace 
FROM
	Student,
	Course,
	SC,
	TC,
	Teacher 
WHERE
	Student.sno = SC.sno 
	AND SC.cno = Course.cno 
	AND SC.cno = TC.cno 
	AND TC.tno = Teacher.tno WITH CHECK OPTION;