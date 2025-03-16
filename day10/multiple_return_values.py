'''Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

Conditional Returns
When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.

e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False'''


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))
