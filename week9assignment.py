"""You manage a university enrollment system and need to track courses,
student registrations, and academic performance.
Create a Student dataclass and a Course dataclass that manages enrollment,
grade tracking, and student comparison."""


from dataclasses import dataclass, field
@dataclass
class Student:
    name:str
    student_id: str
    assignments_done: int = 0
    scores: list[int] = field(default_factory=list)

    def submit(self, score: int):
        self.assignments_done += 1
        self.scores.append(score)

    def avg_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores)/len(self.scores)
    
@dataclass
class Course:
    course_name: str
    professor: str
    capacity: int
    students: list[Student] = field(default_factory=list)
    enrolled: int = field(init = False)

    def __post_init__(self):
        self.enrolled = len(self.students)

    def enroll(self, student: Student) -> bool:
        if self.capacity > self.enrolled:
            self.students.append(student)
            self.enrolled += 1
            return True
        return False
    
    def top_student(self) -> str:
        if not self.students:
            return 'No data'
        top = max(self.students, key=lambda s: s.avg_score())
        return top.name if top.avg_score() > 0 else 'No data'
    
    def course_stats(self) -> str:
        print(f"Data Structures ({self.professor}):")
        for student in self.students:
            print(f'  {student.name} - {student.assignments_done} assignmnets, avg {round(student.avg_score(),1)} pts')
        print(f'Enrolled: {self.enrolled}/{self.capacity}')

s1 = Student('Liam', 'S101')
s2 = Student('Nora', 'S102')
s3 = Student('Omar', 'S103')
s1.submit(72)
s1.submit(88)
s1.submit(91)
s2.submit(95)
s2.submit(89)
s3.submit(60)

c = Course('Data Stuctures', 'Prof. Kim', 3)
print(c.enroll(s1))
print(c.enroll(s2))
print(c.enroll(s3))
print(c.enroll(Student('Priya', 'S104')))
print(c.enrolled)
print(c.top_student())
c.course_stats()


            
    
    


    

