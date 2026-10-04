
#setting default value
class Student1(BaseModel):
    name: str = 'milan'
    age: Optional[int] = None
    email: EmailStr
    gpa: float = Field(gt=0, lt=4)

new_student = {'age': 45, 'email': "milan@gmail.com", 'gpa': 3}

student4 = Student1(**new_student)
print(student4)