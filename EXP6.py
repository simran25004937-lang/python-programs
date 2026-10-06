Aim:
To write a Python program to demonstrate dictionary and its related functions.
Program:

# Demonstration of Dictionary and related functions

student = {
    "Name": "Simran",
    "Age": 19,
    "Course": "BCA",
    "Marks": 85
}

print("Dictionary:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("Name"))

student["Marks"] = 90
print("Updated Dictionary:", student)

student.update({"City": "Bengaluru"})
print("After adding City:", student)

student.pop("Age")
print("After removing Age:", student)

print("Length of dictionary:", len(student))

Output:
Dictionary: {'Name': 'Simran', 'Age': 19, 'Course': 'BCA', 'Marks': 85}
Keys: dict_keys(['Name', 'Age', 'Course', 'Marks'])
Values: dict_values(['Simran', 19, 'BCA', 85])
Items: dict_items([('Name', 'Simran'), ('Age', 19), ('Course', 'BCA'), ('Marks', 85)])
Name: Simran
Updated Dictionary: {'Name': 'Simran', 'Age': 19, 'Course': 'BCA', 'Marks': 90}
After adding City: {'Name': 'Simran', 'Age': 19, 'Course': 'BCA', 'Marks': 90, 'City': 'Bengaluru'}
After removing Age: {'Name': 'Simran', 'Course': 'BCA', 'Marks': 90, 'City': 'Bengaluru'}
Length of dictionary: 4

Result:
Thus, the Python program to demonstrate dictionary and its related functions was successfully executed.
