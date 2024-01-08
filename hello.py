# Added the add function:

def addition(num1, num2):
    add = num1 + num2 
    return add

result = addition(10, 20) 
print(result)



# Here we are adding a function that asks the user for their name and surname and prints out their full name. 

f_name = input("Enter your first name: ") 
l_name = input("Enter your last name: ")

def full_name():
    """Prints the full name."""
    full_name = f_name + " " + l_name
    return full_name

full = full_name()
print(full) 

