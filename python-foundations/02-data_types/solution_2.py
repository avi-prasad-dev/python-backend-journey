'''
### Create a program that stores the following information about yourself.

### Inputs
    - Full Name
    - Age
    - Monthly Salary (realistic or dummy value)
    - City
    - Are you learning Python? (True/False)
### Output

Print:

    Name:
    Age:
    Salary:
    City:
    Learning Python:

Then print the data type of every variable using type().


'''
full_name: str = "Avinash Prasad"
age: int = 38
monthly_salary: float = 50000.00
city: str = "Bangalore"
is_learning_python: bool = True

print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Salary: {monthly_salary}")
print(f"City: {city}")
print(f"Learning Python: {is_learning_python}")

print(type(full_name))
print(type(age))
print(type(monthly_salary))
print(type(city))
print(type(is_learning_python))



