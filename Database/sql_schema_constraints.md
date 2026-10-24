# SQL Schema & Constraints — Quick Reference

## 1. What is a Database Schema?

A **database schema** describes the structure of a database.

It defines:
- Tables
- Columns
- Data types
- Relationships
- Constraints
- Keys

Example:

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
);
```

---

# 2. Table

A **table** stores data in rows and columns.

```sql
CREATE TABLE students (
    student_id INTEGER,
    name TEXT,
    age INTEGER
);
```

- Column = attribute/field
- Row = record

---

# 3. Column

A column represents one type of information about an entity.

```sql
CREATE TABLE students (
    student_id INTEGER,
    name TEXT,
    age INTEGER
);
```

---

# 4. Data Types

A data type defines what kind of value a column can store.

| Data Type | Purpose | Example |
|---|---|---|
| `INTEGER` | Whole numbers | `25` |
| `REAL` | Decimal numbers | `85.5` |
| `TEXT` | Text/string | `'Sohel'` |
| `BOOLEAN` | True/False | `TRUE` |
| `DATE` | Date | `'2026-10-08'` |
| `TIMESTAMP` | Date + time | `'2026-10-08 14:30:00'` |

> Data types vary between database systems. SQLite, PostgreSQL, and MySQL do not handle every type exactly the same way.

---

# 5. Constraints

**Constraints** are rules placed on columns or tables to control what data can be stored.

Common constraints:

1. `PRIMARY KEY`
2. `FOREIGN KEY`
3. `NOT NULL`
4. `UNIQUE`
5. `CHECK`
6. `DEFAULT`

---

# 6. PRIMARY KEY

A **primary key** uniquely identifies each row.

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
);
```

Rules:
- Uniquely identifies a row.
- Cannot contain `NULL`.
- A table normally has one primary-key definition.
- It can contain multiple columns (composite primary key).

---

# 7. FOREIGN KEY

A **foreign key** connects one table to another.

```sql
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

Relationship:

```text
departments
     |
     | department_id
     ↓
students
```

It helps maintain **referential integrity**.

### SQLite note

SQLite foreign-key enforcement should be enabled:

```sql
PRAGMA foreign_keys = ON;
```

Python:

```python
connection.execute("PRAGMA foreign_keys = ON")
```

---

# 8. NOT NULL

`NOT NULL` means a column must have a value.

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

This is invalid:

```sql
INSERT INTO students (student_id, name)
VALUES (2, NULL);
```

---

# 9. UNIQUE

`UNIQUE` prevents duplicate values.

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE
);
```

### UNIQUE vs PRIMARY KEY

| PRIMARY KEY | UNIQUE |
|---|---|
| Identifies a row | Prevents duplicate values |
| Cannot be `NULL` | `NULL` handling depends on DB |
| Normally one PK definition | Multiple UNIQUE constraints are possible |

---

# 10. CHECK

`CHECK` ensures that a value satisfies a condition.

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    age INTEGER CHECK (age >= 0)
);
```

Another example:

```sql
grade REAL CHECK (grade >= 0 AND grade <= 100)
```

---

# 11. DEFAULT

`DEFAULT` provides a value automatically when one is not supplied.

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'active'
);
```

If `status` is omitted, it becomes `'active'`.

---

# 12. Composite Primary Key

A primary key can contain multiple columns.

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id)
);
```

The **combination** must be unique.

```text
student_id | course_id
-----------|----------
1          | 101
1          | 102
2          | 101
```

But this duplicate combination is not allowed:

```text
1 | 101
1 | 101
```

---

# 13. One-to-Many Relationship

One department can have many students.

```text
departments
     |
     | 1
     |
     |----------------
     |       |       |
  Student Student Student
     |       |       |
     N       N       N
```

The foreign key goes on the **many side**:

```sql
students.department_id
```

references:

```sql
departments.department_id
```

---

# 14. Many-to-Many Relationship

Students can take many courses, and courses can have many students.

Use a junction/bridge table:

```text
students
    ↕
enrollments
    ↕
courses
```

Example:

```sql
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);
```

---

# 15. NULL

`NULL` means the value is missing, unknown, or not provided.

It is not the same as:
- `0`
- `''`
- `'NULL'`

Check for NULL:

```sql
WHERE phone_number IS NULL
```

Check for non-NULL:

```sql
WHERE phone_number IS NOT NULL
```

Do not use:

```sql
WHERE phone_number = NULL
```

---

# 16. University Practice Database Schema

The practice database uses:

```text
                         departments
                        /            \
                       ↓              ↓
                  courses        instructors
                     ↑                ↑
                     |                |
                     └── enrollments ─┘
                           ↑
                           |
                        students
```

## Students

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT NOT NULL,
    age INTEGER NOT NULL
);
```

## Departments

```sql
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT UNIQUE NOT NULL,
    building TEXT NOT NULL
);
```

## Courses

```sql
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    credits INTEGER NOT NULL,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

## Instructors

```sql
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

## Enrollments

```sql
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    enrollment_date TEXT NOT NULL,
    grade REAL NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id),

    FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
);
```

---

# 17. Constraint Summary

| Constraint | Main Purpose |
|---|---|
| `PRIMARY KEY` | Uniquely identify rows |
| `FOREIGN KEY` | Connect tables |
| `NOT NULL` | Require a value |
| `UNIQUE` | Prevent duplicates |
| `CHECK` | Enforce a condition |
| `DEFAULT` | Provide an automatic value |

---

# 18. Quick Mental Model

When designing a table, ask:

```text
What is this table about?
        ↓
What uniquely identifies each row?
        ↓
What information does each row contain?
        ↓
Which columns must have values?
        ↓
Which values must be unique?
        ↓
Does this table depend on another table?
        ↓
What foreign keys are needed?
        ↓
Are there values that need rules?
```

Example:

```text
Student
   ↓
student_id → PRIMARY KEY
name       → NOT NULL
email      → UNIQUE + NOT NULL
age        → NOT NULL / CHECK if needed
department_id → FOREIGN KEY
```

---

# 19. Constraints vs Query Clauses

Do not confuse **constraints** with query clauses.

### Constraints

Define rules for the data:

```sql
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
CHECK
DEFAULT
```

### Query clauses

Retrieve or manipulate data:

```sql
SELECT
FROM
WHERE
JOIN
GROUP BY
HAVING
ORDER BY
LIMIT
```

Think:

```text
Schema + Constraints
        ↓
Define how data is structured and what is allowed

SQL Queries
        ↓
Retrieve and manipulate the data
```

---

# 20. Most Important Things to Remember

### PRIMARY KEY
> "Who is this row?"

```sql
student_id INTEGER PRIMARY KEY
```

### FOREIGN KEY
> "Which row in another table does this belong to?"

```sql
department_id INTEGER,
FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
```

### NOT NULL
> "This value is required."

```sql
name TEXT NOT NULL
```

### UNIQUE
> "Two rows cannot have the same value here."

```sql
email TEXT UNIQUE
```

### CHECK
> "This value must satisfy a rule."

```sql
age INTEGER CHECK (age >= 0)
```

### DEFAULT
> "Use this value if the user doesn't provide one."

```sql
status TEXT DEFAULT 'active'
```


* SQL
* 1. Querying ← 
   * SELECT
      * WHERE
      * JOIN
      * GROUP BY
      * HAVING
* 2. Advanced querying
   * Subqueries
      * CTEs
      * Window functions
      * CASE
      * UNION
* 3. Database design
   * Primary keys
      * Foreign keys
      * Constraints
      * Normalization
      * Relationships
* 4. Performance
   * Indexes
      * Query optimization
      * EXPLAIN
* 5. Database operations
   * Transactions
      * Locks
      * Concurrency
   


