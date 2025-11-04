import sys
if len(sys.argv)==3:
script name=sys.argv[0]
name=sys.argv[1]
rollno=sys.argv[2]
print("User provided input values:")
else:
script name=sys.argv[0]
name="Shalina"
rollno="61"
print("No input given-using default values:")
print("Script Name:",script name)
print("Student Name:",name)
print("Roll No:",rollno)
