# Topic 3: Input & Output
So far you've been writing values manually:

        name: str = "Avinash"

But real applications don't work like that.
Users provide information

## For example:

    - Login forms
    - Registration forms
    - ATM Machines
    - E-commerce websites
    - Banking applications

All require Input from users and produce Output.

## What is Input?
Input means data provided to a program

example:
    Enter your name: Avinash

Hear:

    Avinash

is the input

## What is output?
Output means information displayed by a program.

example:
    
    Welcome Avinash

This message is output

## Python Input Function
Python provides:
    input()

### Example:
    name: str = input("Enter your name: ")

    print(name)

## Syntax Breakdown

    input("Enter your name: ")

### input()
Built-in Python function

### "Enter your name:"
Prompt shown to user

## Import Concept
<b>input()</b> ALWAYS returns a string

### Example:

    age = input("Enter age: ")

    print(type(age))

### If user enters:

    38
### Output
    <class 'str'>

Not integer
This is one of the most important beginner concepts.

## Type Coversion
Convert string to integer:
    age: int = int(input("Enter age: "))

Convert string to float:
    salary: float = float(input("Enter salary: "))

Convert number to string:
    age: int = 38

    age_text: str = str(age)    

