🚀 100 Days of Python - Day 6
📌 Day 6: Functions - Simplifying Your Code
📝 What I Learned:
A function in Python is a reusable block of code that performs a specific task. Instead of repeating code, we can "wrap" it in a function and call it whenever needed, making our programs more efficient and readable.

🔑 Key Concepts:
✅ Defining a Function:
python
Copy
Edit
def <function_name>():
    # Block of code
    print("Hello")
    # More code here...
We use the def keyword to define a new function.
Indentation is very important; all code inside the function should be indented.
✅ Calling a Function:
python
Copy
Edit
<function_name>()
Simply use the function's name followed by parentheses to execute the code inside the function.
🧩 Example: Putting It All Together

# Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

# Outside the function
print("Hello")
get_user_name()  # Calling the function
Output:


Hello
What is your name?  # (I type Angela)
Hello Angela
💡 Why Use Functions?
Avoid repeating code.
Make code cleaner and easier to manage.
Simplify debugging and updating logic.
