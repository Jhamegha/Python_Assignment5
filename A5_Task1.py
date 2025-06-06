#Task 1: Create a Dictionary of Student Marks

Dict={"Nick":68,"John":90,"Ketty":95,"Niti":96}
name=input("Enter the student's name: ")
# print(Dict[name])
if name in Dict:
    print("{}'s Marks: {}".format(name, Dict[name]))
else:
    print("Student not found.")