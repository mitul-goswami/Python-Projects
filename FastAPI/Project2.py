from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Student:
    def __init__(self, id, name, age, course, grade):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

class StudentRequest(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=150)
    course: str = Field(min_length=1, max_length=100)
    grade: int = Field(gt=-1, lt=11)

STUDENTS = [
    Student(1, 'John Doe', 20, 'Computer Science', 8),
    Student(2, 'Jane Smith', 22, 'Mathematics', 9),
    Student(3, 'Alice Johnson', 19, 'Physics', 7),
    Student(4, 'Bob Brown', 21, 'Chemistry', 6),
    Student(5, 'Charlie Davis', 23, 'Biology', 10)
]


@app.get("/students/filter-grade/")
async def filter_by_grade(grade: int = Query(gt=-1, lt=11)):
    students_to_return = []
    for student in STUDENTS:
        if student.grade == grade:
            students_to_return.append(student)
    if not students_to_return:
        raise HTTPException(status_code=404, detail="No students found with the specified grade")

@app.get("/students")
async def read_all_students():
    if not STUDENTS:
        raise HTTPException(status_code=404, detail="No students found")
    return STUDENTS

@app.get("/students/{student_id}")
async def read_student(student_id: int = Path(gt=0)):
    for student in STUDENTS:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students/create-student")
async def create_student(student: StudentRequest):
    new_student = Student(**student.dict())
    STUDENTS.append(new_student)
    return new_student

@app.put("/students/update-student/{student_id}")
async def update_student(student_id: int = Path(gt=0), updated_student : StudentRequest):
    for student in STUDENTS:
        if student.id == student_id:
            student.name = updated_student.name
            student.age = updated_student.age
            student.course = updated_student.course
            student.grade = updated_student.grade
            return student
    raise HTTPException(status_code=404, detail="Student not found")


