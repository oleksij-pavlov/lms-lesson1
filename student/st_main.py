from st_student import Student
from st_group import Group, GroupFullException

gr = Group("PD1")

for i in range(10):
    st = Student("Male", 20 + i, f"Name{i}", f"Surname{i}", f"RB{i}")
    gr.add_student(st)


try:
    extra_st = Student("Male", 30, "Extra", "Student", "RB11")
    gr.add_student(extra_st)
except GroupFullException as e:
    print(f"Caught exception: {e}")