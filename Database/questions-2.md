# University SQL Practice

## Tables
- `students`
- `departments`
- `courses`
- `instructors`
- `enrollments`

## Relationships
```text
students
   |
   | student_id
   v
enrollments
   |              |
   | course_id    | instructor_id
   v              v
courses       instructors
   |              |
   | department_id
   +-------> departments
```

Some students have no enrollments, and some courses have no enrollments.

# Level 1 — SELECT & WHERE
1. Display all students.
2. Display only `first_name`, `last_name`, and `city` of students.
3. Display all courses.
4. Find students whose age is greater than 22.
5. Find students from `Dhaka`.
6. Find courses worth more than 3 credits.
7. Find instructors from the `Computer Science` department.
8. Find students whose first name starts with `A`.
9. Find students whose age is between 20 and 25.
10. Find courses whose name contains the word `Data`.

# Level 2 — ORDER BY, LIMIT, DISTINCT
11. Display students from youngest to oldest.
12. Display students from oldest to youngest.
13. Display the 5 oldest students.
14. Display courses from highest credits to lowest.
15. Display all distinct student cities.
16. Display all distinct departments from courses.
17. Display instructors alphabetically by last name.
18. Display the 3 youngest students.
19. Display the 5 courses alphabetically.
20. Find the oldest student.

# Level 3 — Aggregate Functions
21. Count the total number of students.
22. Count the total number of courses.
23. Find the average student age.
24. Find the highest student age.
25. Find the lowest student age.
26. Count the total number of enrollments.
27. Find the average number of credits per course.
28. Count students in each city.
29. Count courses in each department.
30. Find the average credits for each department.

# Level 4 — GROUP BY & HAVING
31. Find cities having more than 2 students.
32. Find departments having more than 2 courses.
33. Find departments with an average course credit greater than 3.
34. Find the number of students enrolled in each course.
35. Find the number of courses taught by each instructor.
36. Find instructors teaching more than 1 course.
37. Find courses having more than 2 students.
38. Find cities whose average student age is greater than 23.
39. Find departments with more than 3 enrollments.
40. Find the department with the highest number of courses.

# Level 5 — JOINs
41. Display each student's name along with their enrollment date.
42. Display: `student name | course name`
43. Display: `student name | course name | grade`
44. Display: `course name | instructor name`
45. Display: `student name | course name | instructor name`
46. Find all courses taken by students from `Dhaka`.
47. Find all students enrolled in a `Computer Science` course.
48. Find all courses taught by instructors from the `Mathematics` department.
49. Display every student and their courses, including students who aren't enrolled in any course.
50. Display every course and its students, including courses with no students.

# Level 6 — JOIN + GROUP BY
51. Count how many courses each student is enrolled in.
52. Count how many students are enrolled in each course.
53. Count how many students each instructor teaches.
54. Find the student enrolled in the most courses.
55. Find the most popular course based on number of students.
56. Find the average grade/score for each course.
57. Find the average grade/score for each student.
58. Find departments with the highest number of enrolled students.
59. Find the instructor teaching the most students.
60. Find the top 5 students based on their average grade.

# Level 7 — Challenge Problems
61. Find students who are not enrolled in any course.
62. Find courses that have never been taken by any student.
63. Find students who are enrolled in more than one course.
64. Find the student with the highest average grade.
65. Find the course with the highest average grade.
66. Find students who are taking a course taught by an instructor from their own department.
67. Find the department whose students have the highest average grade.
68. Find the student who has taken the most credits.
69. Find the instructor whose students have the highest average grade.
70. Produce this report:
`student name | course name | instructor name | department | credits | grade | enrollment date`

## Recommended progression
```text
1–10   SELECT / WHERE
11–20  ORDER BY / LIMIT / DISTINCT
21–30  Aggregate functions
31–40  GROUP BY / HAVING
41–50  JOIN
51–60  JOIN + GROUP BY
61–70  Challenge
```
