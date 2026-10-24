import sqlite3 as sql

connection=sql.connect("test.db")

cursor=connection.cursor()

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    email TEXT UNIQUE,
    city TEXT,
    department TEXT,
    marks REAL,
    admission_date DATE,
    scholarship BOOLEAN DEFAULT 0,
    tuition_fee REALL)
"""
);
print("Table created successfully.")

cursor.execute("""
INSERT OR IGNORE INTO students
(first_name, last_name, age, gender, email, city,
 department, marks, admission_date, scholarship, tuition_fee)
VALUES
('Sohel', 'Rana', 23, 'Male', 'sohel@gmail.com', 'Kushtia',
 'CSE', 88.5, '2024-01-15', 1, 50000),

('Rahim', 'Ahmed', 22, 'Male', 'rahim@gmail.com', 'Dhaka',
 'EEE', 76.5, '2023-02-10', 0, 45000),

('Ayesha', 'Khan', 21, 'Female', 'ayesha@gmail.com', 'Khulna',
 'CSE', 92.0, '2024-03-12', 1, 50000),

('Nusrat', 'Jahan', 24, 'Female', 'nusrat@gmail.com', 'Dhaka',
 'BBA', 81.5, '2022-01-20', 0, 40000),

('Karim', 'Hasan', 25, 'Male', 'karim@gmail.com', 'Rajshahi',
 'CSE', 67.0, '2021-07-15', 0, 50000),

('Fatima', 'Akter', 20, 'Female', 'fatima@gmail.com', 'Kushtia',
 'EEE', 89.5, '2025-01-10', 1, 45000),

('Tanvir', 'Islam', 23, 'Male', 'tanvir@gmail.com', 'Chittagong',
 'BBA', 73.0, '2023-05-18', 0, 40000),

('Sadia', 'Rahman', 22, 'Female', 'sadia@gmail.com', 'Khulna',
 'CSE', 95.0, '2024-02-25', 1, 50000),

('Imran', 'Hossain', 26, 'Male', 'imran@gmail.com', 'Dhaka',
 'EEE', 58.5, '2020-09-12', 0, 45000),

('Mim', 'Chowdhury', 21, 'Female', 'mim@gmail.com', 'Rajshahi',
 'BBA', 86.0, '2025-02-01', 1, 40000),

('Rafi', 'Uddin', 24, 'Male', 'rafi@gmail.com', 'Kushtia',
 'CSE', 79.5, '2022-08-15', 0, 50000),

('Tania', 'Sultana', 23, 'Female', 'tania@gmail.com', 'Dhaka',
 'EEE', 91.5, '2023-11-20', 1, 45000),

('Hasan', 'Mahmud', 22, 'Male', 'hasan@gmail.com', 'Khulna',
 'BBA', 69.0, '2024-06-05', 0, 40000),

('Mariya', 'Islam', 20, 'Female', 'mariya@gmail.com', 'Chittagong',
 'CSE', 84.5, '2025-01-15', 1, 50000),

('Sakib', 'Alam', 25, 'Male', 'sakib@gmail.com', 'Rajshahi',
 'EEE', 77.0, '2021-03-22', 0, 45000),

('Nabila', 'Akter', 21, 'Female', 'nabila@gmail.com', 'Kushtia',
 'BBA', 93.5, '2024-09-10', 1, 40000),

('Arif', 'Haque', 24, 'Male', 'arif@gmail.com', 'Dhaka',
 'CSE', 62.5, '2022-04-18', 0, 50000),

('Jannat', 'Ferdous', 22, 'Female', 'jannat@gmail.com', 'Khulna',
 'EEE', 87.0, '2023-07-25', 0, 45000),

('Rashed', 'Khan', 23, 'Male', 'rashed@gmail.com', 'Chittagong',
 'BBA', 71.5, '2024-12-01', 0, 40000),

('Anika', 'Rahman', 20, 'Female', 'anika@gmail.com', 'Dhaka',
 'CSE', 96.0, '2025-03-05', 1, 50000);

""")

print("All the inserted successfully.")

student=cursor.execute("""
SELECT *FROM students
""")
print(student)
connection.commit()
connection.close()

