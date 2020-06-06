CREATE VIEW course_grade
  AS SELECT Student.sno,Course.cno,Course.cname,Course.ctype,Course.credit,Teacher.dept,
    Teacher.tname,SC.cgrade
  FROM Course,TC,Teacher,SC,Student
  WHERE Course.cno=TC.cno AND TC.tno=Teacher.tno AND Course.cno=SC.cno AND
   Student.sno=SC.sno
  WITH CHECK OPTION ;