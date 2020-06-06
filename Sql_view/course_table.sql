CREATE VIEW course_table
  AS SELECT Student.sno,Course.cno,Course.cname,Course.ctype,Teacher.dept,
    Teacher.tname,Course.credit,Course.chour,Course.ctime,Course.cplace
  FROM Student,Course,SC,TC,Teacher
  WHERE Student.sno=SC.sno AND SC.cno=Course.cno AND SC.cno=TC.cno
         AND TC.tno=Teacher.tno
  WITH CHECK OPTION ;