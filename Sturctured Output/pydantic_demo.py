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

#make error
# new_student3 = {'name':  1}
# error_student = Student.model_validate(new_student3)
# print(error_student)

#setting default value
class Student1(BaseModel):
    name: str = 'milan'

new_student = {}

student4 = Student1(**new_student)
print(student4.name)


