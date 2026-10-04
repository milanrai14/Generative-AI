from pydantic import BaseModel


class Student(BaseModel):
    name: str

new_student = {'name': 'milan'}

student = Student(**new_student)
print(student)

#Another way : model_validate()
student1 = Student.model_validate(new_student)
print(student1)
print(type(student1))