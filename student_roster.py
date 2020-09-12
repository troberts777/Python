# Simple Student data management program in python
# Create class "Student"
class Student:
    # Constructor
    def __init__(self, stuID, name, age, email, degreeProg, classNum, g1, g2):
        self.stuID = stuID
        self.name = name
        self.age = age
        self.email = email
        self.degreeProg = degreeProg
        self.classNum = classNum
        self.g1 = g1
        self.g2 = g2

    # Function to create and append new student
    def accept(self, Name, stuID, email, age, degreeProg, classNum, grade1, grade2):
        # use ' int(input()) ' method to take input from user
        ob = Student(Name, stuID, email, age, degreeProg, classNum, grade1, grade2)
        ls.append(ob)

    # Function to display student details
    def display(self, ob):
        print("Student-ID: ", ob.stuID)
        print("Name: ", ob.name)
        print("Age: ", ob.age)
        print("Email: ", ob.email)
        print("Degree Program: ", ob.degreeProg)
        print("Current Class: ", ob.classNum)
        print("Pre-Assement: ", ob.g1)
        print("Overall Assessment: ", ob.g2)
        print("\n")

    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].stuID == rn):
                return i

    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].stuID = roll;



# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, '', 0, '', '', 0, 0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept(111, "Arthur", 52, "Arthur@mycollege.edu", "SECURITY", "C168", 93, 97)
obj.accept(222, "Bob", 59, "Bob@yahoo.com", "NETWORK", "C779", 92, 89)
obj.accept(333, "Charlie", 43, "Charlie@gmail.com", "SOFTWARE", "C867", 84, 88)

# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(222)
obj.display(ls[s])

# elif(ch == 4):
obj.delete(222)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 5):
obj.update(333, 222)
print(ls.__len__())
print("List after updating")
for i in range(ls.__len__()):
    obj.display(ls[i])

# else:
print("Thank You !")