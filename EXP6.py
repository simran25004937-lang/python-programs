Aim: To write a Python program to demonstrate dictionaries and their related functions such as keys(), values(), items(), pop(), copy(), and clear().

Algorithm:
1. Start the program.
2. Create a dictionary containing book details such as title, author, price, and pages.
3. Display the original dictionary.
4. Access and display a dictionary element.
5. Add a new element to the dictionary.
6. Update the value of an existing element.
7. Display all keys, values, and key-value pairs using keys(), values(), and items().
8. Remove an element using pop().
9. Display the length of the dictionary using len().
10. Check whether a key exists using the in operator.
11. Copy the dictionary using copy().
12. Clear the copied dictionary using clear().
13. Display the results.
14. Stop the program.

Code:
# Program to demonstrate Dictionary and related functions

# Creating a dictionary
book = {
    "Title": "Python Programming",
    "Author": "James",
    "Price": 450,
    "Pages": 250
}

print("Original Dictionary:", book)

# Accessing dictionary elements
print("Title:", book["Title"])

# Adding a new element
book["Publisher"] = "ABC Publications"
print("After Adding Element:", book)

# Updating an element
book["Price"] = 500
print("After Updating Element:", book)

# Displaying keys
print("Keys:", book.keys())

# Displaying values
print("Values:", book.values())

# Displaying key-value pairs
print("Items:", book.items())

# Removing an element
book.pop("Pages")
print("After Removing Pages:", book)

# Displaying dictionary length
print("Length of Dictionary:", len(book))

# Checking whether a key exists
print("Is Title present?", "Title" in book)

# Copying a dictionary
new_book = book.copy()
print("Copied Dictionary:", new_book)

# Clearing the dictionary
new_book.clear()
print("After Clearing:", new_book)

Output:
Original Dictionary: {'Title': 'Python Programming', 'Author': 'James', 'Price': 450, 'Pages': 250}
Title: Python Programming
After Adding Element: {'Title': 'Python Programming', 'Author': 'James', 'Price': 450, 'Pages': 250, 'Publisher': 'ABC Publications'}
After Updating Element: {'Title': 'Python Programming', 'Author': 'James', 'Price': 500, 'Pages': 250, 'Publisher': 'ABC Publications'}
Keys: dict_keys(['Title', 'Author', 'Price', 'Pages', 'Publisher'])
Values: dict_values(['Python Programming', 'James', 500, 250, 'ABC Publications'])
Items: dict_items([('Title', 'Python Programming'), ('Author', 'James'), ('Price', 500), ('Pages', 250), ('Publisher', 'ABC Publications')])
After Removing Pages: {'Title': 'Python Programming', 'Author': 'James', 'Price': 500, 'Publisher': 'ABC Publications'}
Length of Dictionary: 4
Is Title present? True
Copied Dictionary: {'Title': 'Python Programming', 'Author': 'James', 'Price': 500, 'Publisher': 'ABC Publications'}
After Clearing: {}

Result:
Result: Thus, the Python program demonstrates dictionary creation and related functions using book details.
