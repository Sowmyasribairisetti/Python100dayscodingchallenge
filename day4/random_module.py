'''Pseudorandom Number Generators
Computers are not random, because they are built with circuits and switches. But randomness is very important when building software, especially games. It would be really boring if every move in a video game was pre-determined.

So, some computer scientists invented pseudorandom number generators. e.g. https://en.wikipedia.org/wiki/Mersenne_Twister

If you want to learn more about pseudorandom number generators, I recommend watching this video by Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

The Random module in Python
Read the docs here: https://docs.python.org/3/library/random.html

To use it you need to first import it:

import random

Random Whole Numbers Within a Range
import random
rand_num = random.randint(1, 10)

#This will produce a random whole number between 1 and 10 (inclusive).
Modules in Python
Python allows us to put code into different files and import that code if needed. This means that we can better organise and modularise our code.

You can create a new module simply by creating a new .py file, and then you can import variables or functions from that file just by using the import keyword.

Random Floats
You can generate a random number between 0.0 (inclusive) and 1.0 (not inclusive) using the following code from the random module:

import random
rand_num_0_to_1 = random.random()
It can also be represented like this

0.0 <= random.random() < 1.0

You can expand the range of random numbers generated by this method using multiplication.

e.g. random.random() * 5

Will generate a random number between 0 and 5.

Another way to generate random floating point numbers is to use the uniform() function.

import random
random_float = random.uniform(1, 10)
#This will generate a random floating point number between 1 and 10. 
This method may or may not include the upper bound depending on the rounding of the floating point number. So it's best represented as:

a <= random.uniform(a,b) <= b

So depending on if you want the upper bound included you will choose whether to use random.random() or random.uniform().
'''


import random
list1= ["apple","banana","carrot","orange","peach"]
rm = random.choice(list1)
print(rm)
random_index = random.randint(0,4)
print(list1[random_index])
