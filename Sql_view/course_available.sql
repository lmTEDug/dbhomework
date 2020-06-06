CREATE VIEW course_available
  AS SELECT Course.cno,Course.cname,Course.ctype,Teacher.dept,Teacher.tname,Teacher.title,
       Course.credit,Course.chour,Course.ctime,Course.cplace,Course.restno
  FROM Course,Teacher,TC
  WHERE Course.cno=TC.cno AND TC.tno=Teacher.tno
  WITH CHECK OPTION ;

