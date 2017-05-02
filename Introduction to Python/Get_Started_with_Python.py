
# coding: utf-8

# <p><a name="sections"></a></p>
# 
# 
# # Introduction to Python
# 
# - <a href="#simple">Simple Values and Expressions</a><br>
# - <a href="#lambda">Lambda Functions and Named Functions</a><br>
# - <a href="#list">List</a><br>
#     - <a href="#funcOnList">Defining Functions on Lists</a><br>
#     - <a href="#nList">Nested Lists</a><br>
# - <a href="#funcOper">Functional Operators</a><br>
#     - <a href="#map">map</a><br>
#     - <a href="#bool">Boolean Functions</a><br>
#     - <a href="#filter">filter</a><br>
# - <a href="#sol">Solutions</a><br>
# 
# <p><a name="simple"></a></p>
# # Values and Expressions
# 
# ** Expressions and Values**
# 
# We demonstrate the simplest expression syntax: Operators +, -, * and / work just like in most other languages; parentheses can be used for grouping.

# In[1]:

# Comment in Python starts with the hash character, # , and extend to the end of the physical line
1 + 2 * 3     # * has precedence over +


# In[6]:

(1 + 2) * 3+4


# - iPython notebook shows only the last statement in each cell. To inspect all of them, we may use the `print` statement:

# In[7]:

print 1 + 2 * 3
print (1 + 2) * 3


# - Now try more examples and check the output:

# In[3]:

print 17 / 3     # int / int -> int
print 17 / 3.0   # int / float -> float
print 17 // 3.0  # explicit integer division 
print 17 % 3     # remainder
print 2 ** 7     # 2 to the power of 7
print 8 * (7 + 6 * 5)       + 4 / 3 ** 2 - 1       # use backslash
print (8 * (7 + 6 * 5)    # use parentheses
       + 4 / 3 ** 2 - 1)


# **Syntactic note**:  Python does not have any special terminating character , so you must enter everything on one line.  If the line is too long, you can split it up either by enclosing the expression in parens or by adding a \ at the end:

# - **Note**: `\` must be the very last thing on the line (not even followed by spaces), and of course cannot be in a comment.

# ### **Varaiables**
# 
# Variables are used to give names to values.  This is to avoid having to re-type an expression, and so the computer doesn’t have to recompute it.  The equal sign "`=`" is used to assign a value to a variable.

# In[10]:

tax = 12.5 / 100   # An “assignment statement”
price = 100.50


# iPython notebook print nothing for assignments, as we see from above.

# In[9]:

price * tax


# **Calling functions**
# 
# - The Python interpreter has a number of functions built into it:

# In[10]:

abs(-5.0)


# There is also a way to put definitions in a file that you can load and use. Such a file is called a **module**.
# 
# - You use the functions in a module by importing the module and using its name plus the function’s name:

# In[11]:

import math 
import # import the math module
math.factorial(5)    # factorial of 5


# - Or, use a different import syntax and use the function name alone:

# In[12]:

from math import *
factorial(5)        # no module name


# To find the function you need, you might need the **documentation**:
# 
#  - Built-in functions:  [https://docs.python.org/2/library/functions.html](https://docs.python.org/2/library/functions.html)
#  - Math module:  [https://docs.python.org/2/library/math.html](https://docs.python.org/2/library/math.html)
#  - Google is your friend!
#  - And also the Tab key

# In[13]:

#### Try the Tab method with any module you like:


# **Naming convention**
# 
# - Variable names in Python should start with letters, and can contain any number of letters, digits, and  _.
# 
# - Python names are case sensitive.  This applies both to variable names and to function names imported from modules.
# 
# - By convention, Python variables usually start with lower-case letters.  Variables should have descriptive names; for multi-word names, separate the words by underscores.
#  - Good names:  first_index, random_nums
#  - One-letter names are used in certain circumstances - e.g. i, j, k when used as indexes - but are otherwise frowned upon.

# <p><a name="lambda"></a></p>
# # Lambda Functions and Named Functions
# 
# **Defining Functions**
# 
# - You have seen how to call functions.  Now we’ll see how to define them.
# - This function takes a number x and returns $x^2 + x^3$.

# In[14]:

def add_two_powers(x):
    return x**2 + x**3


# The keyword `def` introduces a function definition. It is followed by the function name and the parenthesized list of parameters. The statements in the body of the function start at the next line, and must be indented.
# 
# Call the function in the usual way (after the function has been defined, whether in the same cell or a later cell):

# In[15]:

add_two_powers(4)


# There is an alternative syntax for function definitions that will turn out to be handy.  It uses the `lambda` keyword. 
# 
# - Back to the previous problem, we could write:

# In[16]:

Add_two_powers = lambda x: x**2 + x**3
Add_two_powers(4)


# In[11]:

add = lambda x: x+x


# In[12]:

add(2)


# The two syntaxes for function definitions give the same result, but note the differences in syntax:
# 
# ```
# -------------------------
# def f(x):
#    return expression
# -------------------------   
# f = lambda x: expression
# -------------------------
# ```
# 
# 

# - The first version begins with "`def`” and has its argument in parentheses.  The second version looks like an assignment statement; it uses the keyword “`lambda`”, and the argument is not in parentheses.
# 
# - The first version uses the keyword “`return`”; the second version doesn’t.
# 
# To define a function with multiple arguments, just add more names to the variable list, separated by commas.

# In[17]:

import math

# def notation
def vector_length(x, y):
    return math.sqrt(x**2 + y**2)

# lambda notation
Vector_length = lambda x, y: math.sqrt(x**2 + y**2)

print vector_length(5,12)
print Vector_length(5,12)


# **Exercise 2**: Defining functions
# 
# - Define a function that takes the radius of a circle as input and return the area. (Remember the area of a circle = $\pi r^2$.) Define it with both syntaxes, def and lambda, calling them area and Area, respectively.
#  - *Note*: You need to use `math.pi`, which is defined in the math module.
#  
# - Calculate the area of a circle with radius 10 using both functions.

# In[20]:

#### Your code here
import math
def area(r):
    return r*r


# In[21]:

#### Your code here
Area = lambda r: r*r


# <p><a name="list"></a></p>
# # List
# 
# - The power of Python comes from having values other than numbers. The two other types of values we’ll use most often are lists and strings.
#  - Lists are ordered collections of values. Examples:  `[1, 2, 3, 4],  [7.5, 9.0, 2]`
#  - Strings are sequences of characters. Examples:  `'This class is about Python.'`  (Note that the space is considered a character.)
# 
# - We will look at lists first, but we’ll use strings in our examples.  We’ll do more with strings next week. **Syntactic note**:  Strings can be written with either single or double quotes.
# 
# - Lists can contain any types of values, including strings.

# **List operations and functions**
# 
# - You can manipulate lists in Python, meaning you can create new lists or get values out of lists.  We’ll spend some time going over the major list operations provided by Python.
# - As we’ve seen, you create a list by writing values in square brackets, separated by commas.
#   - Note that you can also have a list with no elements, written `[]`.  This list is astonishingly useful - kind of like the number zero.
# - Given two lists, use `+` to concatenate them:

# In[10]:

squares = [1,4,9,16,25]
alphabet = ['a','b','c','d']
squares + alphabet


# Find the length of a list using the `len()` function:

# In[11]:

len(squares)
print len(alphabet)
print len(squares + alphabet)


# The function range gives a list of integers:

# In[12]:

print range(10)
print range(10, 15)
print range(15, 10, -1)


# To create a list just one longer than an existing list - i.e. add an element to the end of a list - use concatenation:

# In[13]:

squares + [36]


# **Note**:  This operation does not change squares.  That is, it does not “add 36 to squares,” but rather creates a new list that has the same elements as squares, plus one more.

# In[14]:

squares


# There are several operations that apply to lists of numbers and perform operations on the entire list:
# - sum:  Take the sum of the numbers in a list
# - max, min:  Take the maximum or minimum of the numbers in a list.  (This can also apply to strings, using lexicographic order.)
# 

# In[15]:

print sum(squares)
print max(alphabet)


#  - sorted:  Sorts a list

# In[16]:

sorted([4, 3, 6, 2, 5])


# **Subscripting**
# 
# Get a single element of a list by subscripting with a number. We number the elements from zero (which is pretty common for computer languages, but takes some getting used to). We can also subscript from the end by using negative numbers (-1 being the last element).

# In[17]:

print squares[3]
print squares[-1]
print alphabet[6]   #Be careful about this one


# Subscripting can also be used to get more than one element of a list (called a “slice” of a list).  E.g. list[m:n] returns a list that has the mth through (n-1)th element of list (again, counting from zero).

# In[30]:

print squares[1:3]
print alphabet[2:]


# ** Exercise** List operations
# 
# - Define `x` to be the list `[1, 2, 3, 4, 3, 2, 1]`.  Do this by using range twice and concatenating the results.
# - Use subscripting to print both 2’s from x.

# In[31]:

#### Your code here
[1,2,3,4,5,6,7,8]


# <p><a name="funcOnList"></a></p>
# ## Defining Functions on Lists
# 
# - Functions are defined on lists in exactly the same way as on numbers. (We continue defining every function in both syntaxes, just for practice.)
# - A function that returns the first element of a list:

# In[32]:

def firstelt(L):
    a = L+L
    return a

Firstelt = lambda L: L[0]

print firstelt(squares)
print Firstelt(squares)


# A function that takes a list `L` and a value `v`, and returns a list that is the same as `L` except that its first element is `v`.

# In[33]:

def replacefirst(L, v):
    return [v] + L[1:]

Replacefirst = lambda L, v:  [v] + L[1:]

print replacefirst(squares, 7)
print Replacefirst(squares, 7)

#### What might give you problem in this function?


# A function that has an integer argument `n`, and returns a list containing `n`, `n+1`, and `n+2`:

# In[34]:

def threevals(n):
    return [n, n+1, n+2]

Threevals = lambda n: [n, n+1, n+2]


# In[38]:

print(Threevals)


# A function that takes a list `L` and returns a list containing the first, third, and fifth elements of `L`.

# In[ ]:

def list135(L):
    return [L[0], L[2], L[4]]

List135 = lambda L: [L[0], L[2], L[4]]


# **Exercise** List operations
# 
# - Then define the following functions. Define them with both notations, changing the first letter of the name to a capital to distinguish them:
#  - A function sum2 that returns the sum of the first two elements of a list.
#    ```
#    sum2([4, 7, 9, 12]) ---> 11
#    ```
#  - A function that concatenates a list to itself.
#    ```
#    double_lis([4, 7, 9, 12])
#        ---> [4, 7, 9, 12, 4, 7, 9, 12]
#    ```

# In[ ]:

#### Your code here
def sum2(L):
    


# In[ ]:

#### Your code here
Sum2 = lambda L: 


# In[ ]:

#### Your code here
def double_lis(L):
    


# In[ ]:

#### Your code here
Double_lis = lambda L:


# <p><a name="nList"></a></p>
# ## Nested Lists
# 
# - Lists can contain any type of values, including other lists.  This can be confusing, but the principle is the same as with any other elements.
# - The list `[v1, v2, …, vn]` has n elements.  The first is `v1`, the second is `v2`, etc.  This is true no matter what the types of the elements are:
# 
#  - `[1, 2, 3]` has three elements.  (Try `len([1,2,3])`.)
#  - `[1, 2, [3, 4, 5]]` also has three elements.
#  - `[1, ["ab", "cd"], [3, 4, 5]]` also has three elements.
#  - `[[], ["ab", "cd"], [3, 4, 5]]` also has three elements.
# 
# The operations we’ve seen above like “`+`”, `len()` and subscripting work the same on nested lists as on non-nested lists.

# In[16]:

x = [[], 1, ['ab', 'cd'], [3, 4, 5]]
len(x)


# In[ ]:

y = [['q', 'r', 's'], 2]
len(y)


# In[ ]:

x[2]


# In[ ]:

x[2][0]


# In[ ]:

x + y


# **Exercise** Nested lists
# 
# - Write a function `firstfirst` (in both syntaxes) that takes a nested list as input and returns the first element of the first element.  (The first element must be a non-empty list).
# ```
# y = [['q', 'r', 's'], 2]
# firstfirst(y) ---> 'q'
# ```
# - Write a function `subscr2` that takes two arguments: a nested list and a list with two integers.  It uses those two integers as indexes into the nested list:
# ```
# y = [['q', 'r', 's'], 2]
# subscr2(y, [0, 2]) ---> 's'
# ```

# In[ ]:

#### Your code here

#1
def firstfirst(L):


# In[ ]:

#### Your code here
Firstfirst = lambda L: 


# In[ ]:

#### Your code here

#2
def subscr2(L, indexes):
    


# In[ ]:

#### Your code here
Subscr2 = lambda L, indexes: 


# <p><a name="funcOper"></a></p>
# # Functional Operators
# 
# ### `map`
# 
# - You will often want to apply a function to all elements of a list.
# - Suppose a list `L` has elements that are all numbers, and `f` is a function on numbers.  Then `map(f, L)` is the result of applying `f` to every element of `L`.

# In[18]:

import math
L = [4, 9, 16]
map(math.sqrt, L)


# In[ ]:

map(add_two_powers, L)


# In[ ]:

map(Add_two_powers, L)


# You can apply any one-argument function, as long as the values in the list are of the type that function expects.

# In[ ]:

nested_list1 = [[], ["ab", "cd"], [3, 4, 5]]
map(len, nested_list1) #len applies to lists


# In[ ]:

map(threevals, [1, 10, 20]) # three_vals applies to numbers


# In[ ]:

# firstelt applies to lists that are of non-zero length
map(firstelt, nested_list1)


# In[ ]:

map(firstelt, nested_list1[1:])


# Functions can use `map` just as they can use any other function.

# In[ ]:

def get_lengths(L):
    return map(len, L)

Get_lengths = lambda L: map(len, L)

print get_lengths(nested_list1)
print Get_lengths(nested_list1)


# In[ ]:

def get_first_elements(L):
    return map(firstelt, L)

Get_first_elements = lambda L: map(firstelt, L)

print get_first_elements(nested_list1[1:])
print Get_first_elements(nested_list1[1:])


# ** Exercise **   
# ### `map`
# 
# - `square_all` squares every element of a numeric list.  (Define `sqr` to square a number, and map it over the list.)
# ```
# squaree_all([1, 2, 3]) ---> [1, 4, 9]
# ```
# - `get_second` gets the second element of every list in a nested list. (Define snd to get the second element of a list, and map it.)
# ```
# get_second([[1, 2, 3], [4, 5], [6, 7, 8]]) ---> [2, 5, 7]
# ```
# - `tot_length` finds the total length of the lists in a nested list.
# ```
# tot_length([[1, 2, 3], [4, 5], [6, 7, 8]]) ---> 8
# ```

# In[ ]:

#### Your code here

#1
def sqr(x):
    

def square_all(L):
    

Square_all = lambda L: 


# In[ ]:

#### Your code here

#2
snd = lambda x: 


def get_second(L):
    

Get_second = lambda L: 


# In[ ]:

#### Your code here

#3
def tot_length(L):
    
    
Tot_length = lambda L:


# <p><a name="bool"></a></p>
# ## Boolean Functions
# 
# - Boolean functions return one of the truth values `True` or `False`.
# - There are built-in operators and functions that return booleans:
#  - Arithmetic comparison operators: `==`, `!=`, ...
# - Conditions can be combined using `and`, `or`, and `not`:

# In[ ]:

x = 6
x > 5 and x < 7


# In[ ]:

x != -1 or x >= 10


# Defining boolean functions is no different from defining any other kind of functions.

# In[ ]:

# Test whether a list is empty
def is_empty(L):
    return L == []

Is_empty = lambda L: L == []

print is_empty([])
print Is_empty([])


# In[ ]:

print Is_empty(squares)
print is_empty(squares)


# In[39]:

# Test if the first two elements of a list are the same
def same_start(L):
    return L[0] == L[1]

Same_start = lambda L: L[0] == L[1]

print same_start([1,1,2])
print Same_start([1,1,2])


# In[40]:

print same_start([1,2,2])
print Same_start([1,2,2])


# <p><a name="filter"></a></p>
# ## `filter`
# 
# Filter is used to find elements of a list that satisfy some condition. The condition is given in the form of a boolean function.

# In[41]:

def non_zero(x):
    return x != 0
non_zero(1)


# In[42]:

non_zero(0)


# In[43]:

# Get a list of all the non-zero elements of a list
filter(non_zero, [1, 2, 0, -3, 0, -5])


# Let’s write some functions using filter.

# In[45]:

# Return the elements that are greater than ten
def greater_than_ten(x):
    return x > 10
filter(greater_than_ten, [11, 2, 6, 42])


# In[46]:

# Return all the non-empty lists from a nested list
def is_not_empty(L):
    return L != []
filter(is_not_empty, [[], [1,2,3], [], [4,5,6], []])


# ** Exercise**
# 
# - Define a boolean function increase2 that tests with the first two elements of a list are in increasing order.
# ```
# increase2([2, 5, 4, 9]) ---> True
# increase2([2, 2, 5, 0]) ---> False
# ```
# 
# - Define a function increasing_lists that selects from a nested list only those lists that satisfy increase2:
# ```
# increasing_lists([[2, 5, 4, 9], [2, 2], [3, 4, 5]]) 
#     ---> [[2, 5, 4, 9], [3, 4, 5]]
# ```

# In[47]:

#### Your code here

#1
def increase2(L):

Increase2 = lambda L: 


# In[ ]:

#### Your code here

#2
def increasing_lists(L):

Increasing_lists = lambda L:


# ** Anonymous functions**
# 
# We have been using two notations for defining functions because they will turn out to be useful in different ways. The “`def`” notation is much more common, and we will see that it has some real advantages. But the “`lambda`” notation has one big advantage we can use right now:
#  - Lambda functions can be used without assigning them to variables - that is, without naming them.
#  ```
#  map(lambda x: x**2 + x**3, [2,3,4]) ---> [12, 36, 80]
#  filter(lambda x: x != 0, [1, 2, 0, 3, 0, 6]) ---> [1, 2, 3, 6]
#  ```
# 
# When lambda functions are defined this way, they are called "anonymous functions". As we use `map`, `filter`, and other similar operations more and more, anonymous functions will be really handy.

# ** Exercise**
# 
# Rewrite functions get_second (from exercise 6) and increasing_lists (from exercise 7), using anonymous functions.  That is, they should have the form:
# 
# ```
# def get_second2(L):
#    return map(anonymous_function, L)
# 
# get_second2([[1, 2, 3], [4, 5], [6, 7, 8]]) ---> [2, 5, 7]
# 
# ```
# 
# 
# ```
# def increasing_lists2(L):
#    return filter(anonymous_boolean_function, L)
# 
# increasing_lists2([[2, 5, 4, 9], [2, 2], [3, 4, 5]]) ---> [[2, 5, 4, 9], [3, 4, 5]]
# ```

# In[ ]:

#### Your code here

def get_second2(L):
    


# In[ ]:

#### Your code here

def increasing_lists2(L):
    


# ## Classes
# Classes are user types that let you combine several fields and functions that operate on that data. It lets you group all of it together and treat it as a single abstract thing.
# In Python, the class statement is used to define a new type.

# In[18]:

class People(object):
    '''
    definitions
    '''


# Classes can inherit attributes from other classes, in this case People inherits from the object class.
# 
# People is said to be a subclass of object, object is a superclass of People.
# 
# The subclass can overwrite inherited attributes of the superclass.
# 
# ## Class
# When creating an instance of a class, we usually want to provide some initial values.
# 
# To do this, define an __init__ method:

# In[19]:

class People(object):
    def __init__(self, Name, Id, Age):
        self.Name = Name
        self.Id = Id
        self.Age = Age


# Method is a procedure that “belongs” to this class.
# When calling a method of an object(for example, the People object), Python always passes the object(People) as the first argument. By convention, we use self as the name of the first argument of methods.
# 
# The “.” operator is used to access an attribute of an object. So the __init__ method above is defining three attributes for the new People object: Name, Id and Age.
# 
# When an object is created, the __init__ method is called.

# ## Create a Instance

# In[20]:

Jack = People('Jack', 1, 20)
Lucy = People('Lucy', 2, 22)


# Don’t provide argument for self, Python does this automatically.

# In[21]:

print "My name is %s, I'm %s years old. My Id number is %s." %(Jack.Name, Jack.Age, Jack.Id)
print "My name is %s, I'm %s years old. My Id number is %s." %(Lucy.Name, Lucy.Age, Lucy.Id)


# ### Representation of an object

# In[22]:

print Jack


# Python uses an uninformative print presentation for an object.
# 
# This __str__ method will be called when the object needs a string to print.

# In[23]:

class People(object):
    def __init__(self, name, Id, age):
        self.Name = name
        self.Id = Id
        self.Age = age
        
    def __str__(self):
        return "My name is %s, I'm %s years old. My Id number is %s." %(self.Name, self.Age, self.Id)


# In[24]:

Jack = People('Jack', 1, 20)
Lucy = People('Lucy', 2, 22)


# In[25]:

print Jack
print Lucy


# ### Adding more methods

# In[27]:

class People(object):
    def __init__(self, Name, Id, Age):
        self.Name = Name
        self.Id = Id
        self.Age = Age
        
    def __str__(self):
        return "My name is %s, I'm %s years old. My Id number is %s." %(self.Name, self.Age, self.Id)
        
    def addAge(self):
        self.Age = self.Age + 1
    
    def alterName(self, newName):
        self.Name = newName


# In[28]:

Jack = People('Jack', 1, 20)
type(Jack)


# In[29]:

isinstance(Jack, People)


# In[30]:

print Jack
Jack.addAge() # one year later, Jack is 21
print Jack


# In[32]:

print Jack
Jack.alterName('John') # change his name to John
print Jack


# 
# ### Inheritance
# In this case, create a men class inherits from the object People.
# men is said to be a subclass of People, People is a superclass of men.

# In[33]:


class men(People):
    def __init__(self, Name, Id, Age):
        People.__init__(self, Name, Id, Age)
        self.sex = 'M'


# In[37]:

Aron = men('Aron', 3, 15)
print type(Aron)
print isinstance(Aron, men)
print isinstance(Aron, People)


print Aron.Name
print Aron.Id
print Aron.Age
print Aron
print Aron.sex


# ### More Methods

# In[38]:

class men(People):
    def __init__(self, Name, Id, Age):
        People.__init__(self, Name, Id, Age)
        self.sex = 'M'
    
    def isAdult(self):
        return self.Age >= 18
    
    def __str__(self):
        if self.isAdult():
            status = 'man'
        else:
            status = 'boy'
        return "My name is %s, I'm a %s years old %s." %(self.Name, self.Age, status)


# In[39]:

Aron = men('Aron', 3, 17)
print Aron

Aron.addAge()
print Aron


# ### Files, Reading Files and wrinting to Files

# In[ ]:

f = open('data/foo.txt', 'w')

print type(f)
print isinstance(f, file)


# When open a file, the mode can be
# 
# 'r': reading (default)
# 
# 'w': writing
# 
# 'a': appending.
# 
# 'r+': opens the file for both reading and writing.
# 
# In this case the mode is 'w', so we either overwrite the file "foo.txt" or create a new file "foo.txt".

# ### Writing Files

# In[ ]:

f.write('this is some text.\nThis is another line.\n')
f.close()


# 
# Do not forget to close the file after using. Otherwise, you can not open the file with the other applications.
# 
# Print out the contents by using shell command.

# In[ ]:

get_ipython().system(u'cat data/foo.txt')


# ### Reading Files
# Now let's try to read the file. The read method return contents as a string.

# In[ ]:

f = open('data/foo.txt', 'r') 
f.read()`


# Run f.read() the second time will return nothing. Because all the contents have already been print out.

# In[ ]:

f.read()


# In[ ]:

f.close()


# ### Sort a dictionary
# 
# In this case, we create a new class myfile which is a subclass of the file class, and add some more methods, such as wordCountSort method used to sort the frequencies of the words.
# 
# Before I show you all the codes, it's necessary to know how to sort a dictionary.
# 
# Since dictionary is unordered, you need to convert it to a list by using .items method.
# 
# Then the function sorted can be used to sort a list.

# In[ ]:

d = {'a': 5, 'b': 3, 'c':2}
d = d.items() # convert to a list
d


# In[ ]:

sorted(d, key = lambda x: x[1])


# ### Basic String Manipulations
# 
# The operations on string you have seen:
# 
# length: the number of characters in a string.

# In[43]:

len('abcd')


# In[44]:

# indexing
'abcd'[0] # the first element


# In[46]:

# slicing
'abcd'[0:2] # the first and second element

s = 'abcdefg'
print s[-1] # -1 means the first character from the right side
print s[-2] # -2 means the second character from the right side


# ### Basic String Manipulations - 2 

# In[50]:

print ('ABcd'.lower()) # convert to lower case 
print ('ABcd'.upper()) # convert to upper case 

print ('ABcd'.swapcase()) # swap case(lower -> upper, upper -> lower) 


# In[51]:

print ('acd acd'.title())


# ### Basic String Manipulations - 3

# In[52]:

'a b c d'.split(' ') # split by ' ' 


# In[53]:

'a b c d'.replace(' ', '>') # replace ' ' with '>'


# In[54]:

'a b c d'.count(' ') # count the number of ' ' appears


# In[55]:

' '.join(['a', 'b', 'c'])


# ### Advanced String Manipulations: Regular Expressions
# 
# So far we have seen some basic and intermediate functions for handling and working with strings.
# 
# However, if you truly want to unleash the power of strings manipulation, it's necessary to learn regular expressions.
# 
# #### Concept
# 
# A **regular expression** is a special text string for describing a certain amount of text.
# This “certain amount of text” receives the formal name of pattern. Hence we say that a regular expression is a pattern that describes a set of strings.
# 
# The goal of using regular expression is extracting specific characters from text by describing its pattern.
# 
# #### Pattern
# For example, both gray and grey match the pattern gr.y in which the dot . refers to a arbitrary character.
# 
# #### Metacharacters
# A simplest form of regular expressions is a pattern that matches a single character, for example 'a' matches exactly the character 'a'.
# 
# However, there are some special characters that have a reserved status and they are known as metacharacters.
# . ^ $ * + ? { } [ ] \ | ( )
# 
# 
# These metacharacters have special meaning when working with regular expressions. So a|b does not match exactly a|b.
# 
# The backslash \ is called escape operator, which is used for making these metacharacters to normal characters. For example, a\|b in regular expression matches exactly the character a|b.

# In[56]:

import re

raw_string = 'Hi, how are you today?'
print re.search('Hi', raw_string)


# In[57]:

print re.search('Hello', raw_string)


# In[59]:

s = re.search('Hi', raw_string)


# In[60]:

print s.start() # the starting position of of the matched string
print s.end()   # the ending position index of the matched string
print s.span()  # a tuple containing the (start, end) positions of the matched string


# In[61]:

print s.group() # the matched string
print raw_string[s.start():s.end()] # same


# ###  The meaning of metacharacters
# 
# re.search(pattern, string) != None is True if the string matches the pattern. We will use this function to test our regular expressions.
# 
# **dot**
# 
# . refers to any single characters. For example, a. matches any two characters start with 'a': aa, ab, an, a1, a#, etc.

# In[62]:

print re.search('a.', 'aa') != None
print re.search('a.', 'ab') != None
print re.search('a.', 'a1') != None
print re.search('a.', 'a#') != None


# #### question mark & plus & asterisk & {}
# ? matches a character either once or zero times.
# 
# + matches a character at least once.
# 
# * matches a character arbitrary times.
# 
# {m,n} matches a character at least m times and at most n times.
# 
# For example, ba?b matches bab and bb.

# In[63]:

print re.search('ba?b', 'bb') != None    # match
print re.search('ba?b', 'bab') != None   # match
print re.search('ba?b', 'baab') != None  # does not match


# In[64]:

print re.search('ba+b', 'bb') != None    # does not match
print re.search('ba+b', 'bab') != None   # match
print re.search('ba+b', 'baab') != None  # match
print re.search('ba+b', 'baaaab') != None  # match
print re.search('ba+b', 'baaaaaab') != None  # match


# In[65]:

print re.search('ba*b', 'bb') != None    # match
print re.search('ba*b', 'bab') != None   # match
print re.search('ba*b', 'baaaaaab') != None  # match


# In[66]:

print re.search('ba{1,3}b', 'bab') != None    # match
print re.search('ba{1,3}b', 'baab') != None   # match
print re.search('ba{1,3}b', 'baaab') != None  # match

print re.search('ba{1,3}b', 'bb') != None     # does not match
print re.search('ba{1,3}b', 'baaaab') != None # does not match


# ####  caret & dollar sign
# ^ refers to the beginning of a text, while $ refers to the ending of a text.
# 
# For example, ^a matches all the text begins with character a.

# In[67]:

print re.search('^a', 'abc') != None    # match
print re.search('^a', 'abcde') != None  # match
print re.search('^a', ' abcde') != None # does not match


# In[68]:

# a$ matches all the text ends with character a.
print re.search('a$', 'aba') != None    # match
print re.search('a$', 'abcba') != None  # match
print re.search('a$', ' aba ') != None  # does not match


# #### bracket
# [] is used for specifying a set of characters that you wish to match. For example, [123abc] will match any of the characters 1, 2, 3, a, b, or c ; this is the same as [1-3a-c], which uses a range to express the same set of characters. Further more [a-z] matches all the lower letters, while [0-9] matches all the numbers.

# In[69]:

print re.search('[123abc]', 'defg')  != None   # does not match
print re.search('[123abc]', '1defg') != None   # match
print re.search('[1-3a-c]', '2defg') != None   # match
print re.search('[123abc]', 'adefg') != None   # match
print re.search('[1-3a-c]', 'bdefg') != None   # match


# () is very similar to the mathematical meaning, they group together the expressions contained inside them, and you can repeat the contents of a group with a repeating qualifier.
# 
# For example, the pattern (abc){2,3} matches abc 2 or 3 times.

# In[70]:

print re.search('(abc){2,3}', 'abc')  != None         # does not match
print re.search('(abc){2,3}', 'abcabc')  != None      # match
print re.search('(abc){2,3}', 'abcabcabc')  != None   # match


# What will the following expression return? True or False?

# In[72]:

# print re.search('(abc){2,3}', 4*'abc')  != None


# #### vertical bar
# 
# | is a logical operator. For examples, a|b matches a and b, which is similar to [ab].

# In[73]:

print re.search('[ab]', 'a') != None   # match
print re.search('[ab]', 'b') != None   # match
print re.search('[ab]', 'c') != None   # does not match


# In[74]:

print re.search('abc|123', 'a') != None   # does not match
print re.search('abc|123', '1') != None   # does not match
print re.search('abc|123', '123') != None # match
print re.search('abc|123', 'abc') != None # match


# #### backslash
# If you want to match exactly ?, it is necessary to add a backslash \?.

# In[75]:

print re.search('\?', 'Hi, how are you today?') != None


# Otherwise, the character ? will be treated as a metacharacter. ? matches a character(group) either once or zero times.

# In[76]:

print re.search('?', 'Hi, how are you today?') != None


# ### Useful functions
# re.split(pattern, string): Split the string into a list by the pattern.
# 
# re.sub(pattern, replace, string): Replace the substrings in the string that matches the pattern with the argument replace.
# 
# re.findall(pattern, string): Find all substrings where the pattern matches, and returns them as a list.
# 
# In the base library, the strings already have methods like str.split and str.replace do similar works.
# 
# str.split is similar to re.split, str.replace is similar to re.sub.
# 
# Since we can use regular expressions in re module, re.split and re.sub are much more powerful!

# In[3]:

#re.sub

s = '''The re module was added in Python 1.5, 
and provides Perl-style regular expression patterns. 
Earlier versions of Python came with the regex module, 
which provided Emacs-style patterns. 
The regex module was removed completely in Python 2.5.'''


# **Question**
# 
# Suppose we want to split this sentence into a list in which each element is a word. The separators are dot(.), dash(-), comma(,) and blank space( ).
# 
# **Solution**
# 
# How to solve the problem in the base library?
# 
# Since we can not split a string by multiple separators, an alternative way is replacing all the separators with blank space.
# Split the replaced the text with blank space.

# In[78]:

s2 = s
for i in [',', '.', '-', '\n']:
    s2 = s2.replace(i, ' ')
s2.split(' ')


# In[79]:

s3 = s
s3 = re.sub('[\n,.-]', ' ', s3)
print s3
re.split(' +', s3) 
# since there are empty characters in the result,
# \ we split it by one or more blank space


# #### re.split
# A simpler way is using regular expression to split the text by multiple separators directly.

# In[81]:

re.split('[\n ,\.-]+', s)


# #### re.findall
# Similar to re.split, re.findall also works well in this case.
# 
# Just select letters in the string s by using re.findall.

# In[82]:

re.findall('[a-zA-Z]+', s) # if you want number too, run re.findall('[a-zA-Z0-9]+', s)


# ### Operations
# Typically, regular expression patterns consist of a combination of using various operators.
# 
# Among the various types of operators, their main use reduces to four basic operations for creating regular 
# 
# ##### expressions:
# Concatenation: concatenating a set of characters together. For example 'abcd', which just matches the single string 'abcd'.
# 
# Logical OR: denoted by the vertical bar | or []. For example 'ab|cd', which matches two strings 'ab' and 'cd', while '[abcd] matches 'a', 'b', 'c' or 'd'.
# 
# Replication: define a pattern that matches under multiple possibilities. ?,+,*,{m,n}.
# 
# Grouping: denoted with a expression inside parentheses ( ).
# 
# ### wordCount
# 
# Now let's rewrite a function wordCount.

# In[1]:

import re
def wordCount(x, number=False):
    '''
    x: string to count
    number: whether to count the numbers
    '''
    ## tolower and find words
    x = x.lower()
    if number:
       word_list = re.findall('\w+', x)
    else:
        word_list = re.findall('[a-zA-Z]+', x)
    ## count and return
    result = {}
    for word in word_list:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result 


# In[4]:

wordCount(s)


# ### Is it a e-mail address?
# In this case, we write a function to test whether a e-mail address is valid.
# 
# Usually, email addresses have one or a similar variant of the following forms:
# 
# somename9@gmail.com
# 
# some_name@yahoo.com
# 
# contact@supstat.com.cn
# 
# some.name@an-email.com
# 
# some.name@an.email.com
# 
# some_name@163.com
# 
# 
# Think about how to test if a string is a valid e-mail address?
# 
# Generally, it can be splitted into three parts:
# 
# user name(somename9, some_name)
# 
# @
# 
# domain name(gmail.com, yahoo.com, supstat.com.cn)
# Our goal is writing regular expressions to describe the 
# pattern.
# 
# **user name**
# Try to write a regular expression to match the following user names?
# 
# somename9
# some_name
# contact
# some.name
# some.name
# some_name
# 
# The first part, user name pattern, can be expressed:
# 
# ^[a-z0-9]+[_\.]?[a-z0-9]+
# 
# ^[a-z0-9]+: begin with letter or numbers
# 
# [_\.]?: may contain a underline(_) or dot (.)
# 
# [a-z0-9]+: following with numbers and letter

# In[5]:


users = ['somename9', 'some_name', 'contact', 'some.name', 'some.name', 'some_name']
for i in users:
    if re.search('^[a-z0-9]+[_\.]?[a-z0-9]+', i) != None:
        print "Match!"
    else:
        print "Does not match!"


# ## Introduction to Numpy
# 
# NumPy is a matrix type for python, and a large number of functions to operate on these matrices.
# 
# It’s a library that makes doing calculations easy and faster to execute, because the calculations are done in C rather than python.
# 
# There are two mainly data types in NumPy: the array and the matrix.
# 
# The operations on arrays and matrices are slightly different.
# But both types allow you to remove loops.
# 
# #### Array in Numpy
# Import array from numpy, add up two arrays directly without a for loop in regular Python.

# In[7]:

import numpy as np
a1 = array([1, 1, 1])
a2 = array([1, 2, 3])
a1 + a2

am = array([[1, 2, 3], [4, 5, 6]])
am


# In[4]:

am[0] # acess the first row


# In[5]:

am[0][1] # access the elements like lists


# In[6]:

am[0, 1] # same with am[0][1]. access the elements like a matrix


# In[8]:

np.arange(10) # start from 0 in default


# In[9]:

np.arange(2, 10) # start from 2


# In[10]:

np.arange(1, 10, 0.3) # start from 1 and increment by 0.5, end with a number less than 10.


# In[11]:

np.linspace(10, 20) 
# start from 10, end with 20(included!), length is 50 in default


# In[12]:

np.linspace(10, 20, 21) 
# start from 10, end with 20, and the length is 21.


# In[13]:

np.zeros([3, 2]) # 3 rows, 2 columns


# In[14]:

np.ones([3, 2]) # 3 rows, 2 columns


# In[15]:

np.eye(3)


# In[18]:

from numpy import mat, matrix
m1 = mat([1, 2, 3])
m1


# In[19]:

m1 = mat([[1, 2, 3], [4, 5, 6]])
m2 = mat([[1, 2, 3], [4, 5, 6]])
print m1 + m2
print m1 - m2
print m1 / m2


# **Transpose**
# The transpose of a matrix is just flipping the rows and columns. For a matrix  A∈Rm×nA∈Rm×n , the transpose which is denoted by  AT∈Rn×mAT∈Rn×m . The elements of  ATAT  is given by:
# 
# A(Transpose)ij=Aji
#  
#  
# The .T method is used to transpose a matrix, it can also be applied on a array object.

# In[20]:

m1.T


# In[21]:

array(m1)


# ## Operation in Matrices
# Multiplication
# 

# In[22]:

m2 = array(m2) # transfer the matrix m2 to a array object
print type(m2)
m1 * m2.T


# In[23]:

from numpy import shape
m1 = mat([[1, 2, 3], [4, 5, 6]])
a1 = array([[1, 2, 3], [4, 5, 6]])
print shape(m1)
print shape(a1)


# In[24]:

a1.reshape([6, 1])


# In[26]:

# identity matrix
m = mat([[1, .5], [.5, 1]])


m * m.I


# In[27]:

m = mat([[1, 2, 3], [2, 3, 5]])
mi = m.I
mi


# In[28]:

# To apply methods to Matrix, first change them to array

m = mat([3, 2, 1])
a = array(m) # convert a matrix to array
print a.mean()
print m.mean()


# In[29]:

m = mat([3, 2, 1])
m.sort()
m


# ### Random sampling in Numpy
# 
# There is a group of functions used to generate random data and sampling method:
# 
# **rand(d0, d1, ..., dn)**: Random values in a given shape from [0, 1] uniformly.
# 
# **randn(d0, d1, ..., dn)**: Return a sample (or samples) from the “standard normal” distribution.
# 
# **randint(low[, high, size])**: Return random integers from low (inclusive) to high (exclusive).
# 
# **random_integers(low[, high, size])**: Return random integers between low and high, inclusive.
# 
# **random_sample([size])**: Return random floats in the half-open interval [0.0, 1.0).
# 
# **random([size])**: Return random floats in the half-open interval [0.0, 1.0).
# **ranf([size])**: Return random floats in the half-open interval [0.0, 1.0).
# 
# **sample([size])**: Return random floats in the half-open interval [0.0, 1.0).
# 
# **choice(a[, size, replace, p])**: Generates a random sample from a given 1-D array

# In[30]:

#Ramndom sampling
from numpy import random
random.rand(2, 3)


# In[31]:

random.randn(2, 3)


# In[32]:

random.randint(5, size=10)


# In[33]:

random.randint(low=1, high=6, size=(5, 5))


# In[34]:

random.rand(3, 3) # 3-3 array


# In[35]:

all_set = [1, 2, 3, 5, 8, 13, 21, 34, 55]
random.choice(all_set, size=10)


# In[36]:

random.choice(all_set, size=5, replace=False)


# ### More Functions
# **Function	Description**
# abs, fabs	Compute the absolute value element-wise for integer, floating point, or complex values. Use fabs as a faster alternative for non-complex-valued data.
# 
# sqrt	Compute the square root of each element.
# 
# square	Compute the square of each element.
# 
# exp	Compute the exponent e x of each element
# 
# log, log10, log2, log1p	Natural logarithm (base e), log 
# 
# base 10, log base 2, and log(1 + x), respectively
# 
# sign	Compute the sign of each element: 1 (positive), 0 (zero), or -1 (negative)
# 
# ceil	Compute the ceiling of each element, i.e. the 
# 
# smallest integer greater than or equal to each element
# 
# floor	Compute the floor of each element, i.e. the 
# 
# largest integer less than or equal to each element
# 
# rint	Round elements to the nearest integer, preserving the dtype
# 
# modf	Return fractional and integral parts of array as separate array
# 
# isnan	Return boolean array indicating whether each value is NaN (Not a Number)
# 
# isfinite, isinf	Return boolean array indicating whether each element is finite (non- inf , non- NaN ) or 
# infinite, respectively
# 
# cos, cosh, sin, sinh, tan, tanh	Regular and hyperbolic trigonometric functions
# 
# arccos, arccosh, arcsin, arcsinh, arctan, arctanh	Inverse trigonometric functions

# # Mathematics review: Probability Theory
# 
# ## Probability
# 
# Probabilities are real numbers between 0 and 1.
# 
# All possible events for a trial sum to 1.
# 
# If two events are independent, say A and B, the probability of A and B happening is:
# 
# P(AandB)=P(A)P(B)P(AandB)=P(A)P(B) 
# 
# The probability of A or B happening is:
# 
# P(AorB)=P(A)+P(B)P(AorB)=P(A)+P(B) 
# 
# If two events are not independent, we might be interested in their conditional probability.
# 
# P(A|B)=P(AandB)P(B)P(A|B)=P(AandB)P(B) 
# 
# **What is the probability of  A|BA|B  if they are independent?**
# 
# **What is the probability of  A|BA|B  if they are mutually exclusive?**
# 
# ### Descriptive statistics
# 
# Descriptive statistics are what you are probably most familiar with - some examples are the mean and variance of a sample.
# 
# These are measures of central tendency(mean), spread(variance) and shape(skewness, kurtosis) respectively.
# 
# **Mean/Average**
# 
# It can be visualized as the center of gravity of the data, usually denoted by  μ  or  E(x) .
# 
# μ=E(x)=1n∑i=1nxi
# μ=E(x)=1n∑i=1nxi
#  
# There is a built-in function sum in python, but there is no mean.
# 
# Write a function to do this calculation will enhance your understanding.

# In[37]:

def mean(x):
    return sum(x) / len(x)


# In[38]:

mean([1, 2, 3, 4, 5])


# In[39]:

import numpy as np
print np.mean([1, 2])
print np.mean([1, 2, 3, 4, 5])


# ### Variance
# Variance measures the spread of a distribution, defined as the mean quadratic deviation of the variate from its mean value.
# 
# σ2=var(x)=E[(x−μ)2]
# 
# σ2=var(x)=E[(x−μ)2]
#  
# Here the variance is denoted by  σ2σ2 , and  σσ  refers to the standard deviation.

# In[40]:

def var(x):
    xMean = mean(x)
    xCenter = [(i - xMean) ** 2 for i in x] 
    return mean(xCenter)


# In[41]:

var([1, 2 ,3 ,4, 5])


# In[42]:

# Using Numpy directly
print np.var([1, 2 ,3 ,4, 5])
print np.var([1, 2])


# ### Skewness
# 
# Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.
# 
# γ=E((x−μ)**3/σ)
#  

# In[43]:

x = [1, 2, 3, 4, 5]
def skew(x):
    x = np.array(x)
    return np.mean(((x - np.mean(x)) / np.std(x)) ** 3)
skew(x)


# In[44]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 12, 6
f, ax = plt.subplots(1, 3)
ax[0].hist([1, 2, 3, 4, 5])
ax[0].set_title('symmetric: $skewness = 0$')
ax[1].hist([1, 2, 2, 3, 4])
ax[1].set_title('non-symmetric: $skewness = 0.27$')
ax[2].hist([1, 2, 3, 3, 4])
ax[2].set_title('non-symmetric: $skewness = -0.27$')


# ### Kurtosis
# 
# Kurtosis is a measure of the "peakedness" of the data. In a similar way to the concept of skewness, kurtosis is a descriptor of the shape of a probability distribution.
# 
# β=E(x−μ)**4(E(x−μ)**2)**2 = E((x−μ)**4/σ2)
#  

# In[45]:

def kurtosis(x):
    x = np.array(x)
    return np.mean((x - np.mean(x))**4) / np.var(x)**2
kurtosis([1, 2, 3 ,4 ,5])


# In[46]:

kurtosis([1, 2, 3, 3, 4])


# In[47]:

f, ax = plt.subplots(1, 3)
ax[0].hist([1, 2, 3, 4, 5])
ax[0].set_title('$kurtosis = 1.7$')
ax[1].hist([1, 2, 2, 3, 4])
ax[1].set_title('$kurtosis = 1.96$')
ax[2].hist([1, 2, 3, 3, 4])
ax[2].set_title('$kurtosis = 1.96$')


# ### Distributions
# 
# In addition to looking at summary values, we can also look at the data as a whole and see how it is shaped, or distributed.
# 
# One of the easiest ways is through a histogram. We choose a number of buckets and store the count of each member that belongs to that bucket.
# What data strucutes could we use for representing histograms?
# 
# The mode is the most frequent value. How would we find that with your histogram data structure?
# 
# ### Matplotlib
# 
# **pyplot**
# 
# We will mainly learn the sub-module pyplot in matplotlib.

# In[51]:

import matplotlib.pyplot as plt
print plt.__doc__
print dir(plt)


# In[53]:

get_ipython().magic(u'matplotlib inline')


# In[54]:

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)


# In[55]:

plt.plot(x, y, '.') # point marker


# 
# ### color & legend
# **
# Add two more arguments**: color and label(for legend).
# 
# Then plt.legend will automatically generate legends, loc is used to define the location of legend.
# 
# loc:
# 
# 1: topright
# 
# 2: topleft
# 
# 3: bottomleft
# 
# 4: bottomright

# In[57]:

y2 = np.cos(x)
plt.plot(x, y, color = 'blue', label='sin(x)')
plt.plot(x, y2, color = 'red', label='cos(x)')
plt.legend(loc=1)


# ### fill with color
# 
# plt.fill used to fill a arbitrary area with color. The area is defined by a series of points.

# In[58]:

plt.plot(x, y, color = 'blue', label='sin(x)')
plt.plot(x, y2, color = 'red', label='cos(x)')
plt.legend(loc=1)

intersection = np.linspace(0.7854044, 3.926992, 100) 
# 0.78 and 3.92 is the root of sin(x) - cos(x) = 0
plt.fill(intersection, np.sin(intersection), color='grey', alpha = 0.3)
plt.fill(intersection, np.cos(intersection), color='grey', alpha = 0.3)
# alpha is used to define the transparency


# ### title & text
# 
# plt.title: add a title.
# 
# plt.text: add text in the figure.
# 
# Note that you can add mathematical expressions both in text and title.
# 
# The way to add mathematical expressions is similar to  LatexLatex .

# In[59]:

y2 = np.cos(x)
plt.plot(x, y, color = 'blue', label='sin(x)')
plt.plot(x, y2, color = 'red', label='cos(x)')
plt.legend(loc=1)
### fill polygon
plt.fill(np.concatenate([intersection, intersection[::-1]]),         np.concatenate([np.sin(intersection), np.cos(intersection[::-1])]),         color= 'grey', alpha = 0.3)
### add title and text
plt.title('$sin(x)$ VS $cos(x)$', fontsize = 25)
plt.text(1.6, 0, '$sin(x) > cos(x)$', fontsize = 20)
plt.text(1, -0.5, '$y = cos(x)$', fontsize = 20)
plt.text(3, 0.3, '$y = sin(x)$', fontsize = 20)


# ### axis
# 
# plt.xlabel
# 
# plt.ylabel
# 
# plt.xticks
# 
# plt.yticks
# 
# plt.xlim
# 
# plt.ylim
# 
# These functions are used to control the labels, ticks and ranges on the  xx and  yy  axis respectively.

# In[60]:

y2 = np.cos(x)
plt.plot(x, y, color = 'blue', label='sin(x)')
plt.plot(x, y2, color = 'red', label='cos(x)')
plt.legend(loc=1)
### fill polygon
plt.fill(np.concatenate([intersection, intersection[::-1]]),         np.concatenate([np.sin(intersection), np.cos(intersection[::-1])]),         color= 'grey', alpha = 0.3)
### add title and text
plt.title('$sin(x)$ VS $cos(x)$', fontsize = 25)
plt.text(1.6, 0, '$sin(x) > cos(x)$', fontsize = 18)
plt.text(1, -0.5, '$y = cos(x)$', fontsize = 20)
plt.text(3, 0.3, '$y = sin(x)$', fontsize = 20)
### axis
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.xticks(fontsize=10,rotation=45);
plt.yticks(fontsize=10,rotation=45);
plt.xlim(-0.5, 5.5)
plt.ylim(-1.5, 1.5)


# ### Statistical plots
# 
# Commonly used plots:
# 
# scatter: show the correlation of two variables.
# 
# histogram: show the distribution of continuous variable.
# 
# barplot: show the difference between factors.
# 
# boxplot: show the quantiles.

# ### Save
# Use the function savefig to save the picture.

# In[65]:

plt.rcParams['figure.figsize'] = 12, 6
import numpy as np
x = np.linspace(-5, 5, 100)
y = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y, color = 'blue', label='sin(x)')
plt.plot(x, y2, color = 'red', label='cos(x)')
plt.legend(loc=1)
### fill polygon
intersection = np.linspace(0.7854044, 3.926992, 100) 
plt.fill(np.concatenate([intersection, intersection[::-1]]),         np.concatenate([np.sin(intersection), np.cos(intersection[::-1])]),         color= 'grey', alpha = 0.3)
### save
plt.savefig('matplot.png')


# In[66]:

from IPython.display import Image
Image('pic/matplot.png')


# # Scipy

# In[67]:

import scipy
from scipy import stats
scipy.info(stats)


# ### stats.itemfreq
# 
# There is a function named itemfreq which is used to count the frequency of each element.

# In[ ]:

#ringsFre = stats.itemfreq([i.rings for i in abalones])
#ringsFre


# In[71]:

key = ['a', 'b', 'c']
value = [1, 2, 3]
zip(key, value)


# # Distributions
# 
# ### Norm distribution
# The normal distribution is a continuous distribution or a function that can take on values anywhere on the real line. The normal distribution is parameterized by two parameters: the mean of the distribution  μμ  and the 
# 
# **variance  σ^2** .
# 
# The PDF(probability density function) is used to describe continuous variables. Here is the PDF of normal 
# distribution  N(μ,σ2) .
# 
# P(x;μ,σ)=1/sqrt(2πσ^2)*exp(−(x−μ)^2/2σ^2)
# 
#  
# E(X)=μVar(x)=σ^2
#  
# The **CDF(cumulated distribution function)** of a variable  X is denoted by F(x) , which is defined as:
# F(x)=P(X≤x)
#  
# print the details of normal distribution in stats.

# In[72]:

stats.norm.rvs(10, 5) # rvs is short for random variables


# In[70]:

stats.norm.cdf(3) - stats.norm.cdf(-3) 
# cdf is short for cumulated distribution function


# In[73]:

# pdf is short for probability density function
stats.norm.pdf(0) 


# In[74]:

mu = 0
sigma = 1
x = np.arange(mu-5, mu+5, 0.1)
y = stats.norm.pdf(x, mu, sigma)
plt.rcParams['figure.figsize'] = 8, 6
plt.plot(x, y)

theta = np.linspace(-3, 3, 100) 
r = stats.norm.pdf(theta)
theta = np.concatenate([[-3], theta, [3]])
r = np.concatenate([[0], r, [0]])
                        

plt.fill(theta, r, alpha = 0.3)
plt.title('Normal: $\mu$=%.2f, $\sigma^2=%.2f$'%(mu, sigma))
plt.text(-1.9, 0.05, '$p(-3 < x < 3)=%.4f$'%(1 - 2*stats.norm.cdf(-3)), size = 15)
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()


# ## Poisson Distribution
# 
# A random variable  X  that has a Poisson distribution represents the number of events occurring in a fixed time interval with a rate parameters  λ .  λ  tells you the rate at which the number of events occur. The average and variance is  λ.
# 
# The **PMF(probability mass function)** is used to describe discrete variables. Here is the PMF of poisson distribution  P(λ).
# 
# Concretely, the PMF shows the probability of each possible value that the variable may take.
# 
# P(X=k)=λ^k*e^−λ/k!
#  
# E(X)=λVar(X)=λ
# 
#  
# What is probability of observing 4 accidents at an intersections in a day given the rate of accidents is 2 per day?

# In[75]:

stats.poisson.pmf(4, 2) 
# equivalent to stats.poisson.cdf(4, 2) - stats.poisson.cdf(3, 2) 
# p(x <= 4) - p(x <= 3) = p(x=4)


# In[76]:

lam = 2
sequence = np.arange(0, 10)
plt.bar(sequence, stats.poisson.pmf(sequence, lam), alpha=0.3)
plt.title('Poisson distribution: $\lambda=%s$'%lam)
plt.xlabel('x')
plt.show()


# You can notice that the number of accidents peaks around the mean. On an average you can expect lambda number of events.
# 
# Try different values of lambda and n, then see how shape of the distribution changes.

# ### Binomial Distribution
# 
# A random variable X that has a binomial distribution represents the number of successes in a sequence of **n** independent yes/no trials, each of which yields success with probability  **p** .
# 
# A random variable quantifies the outcomes of a number.
# 
# For example, a random variable for a coin flip can be represented as
# 
# x = { 1 (if head), 0 (if tail)}
# 
# Let  X  denotes the number of heads when flipping  nn  coins, the PMF of  XX is:
# 
# P(X=k)=n!/k!(n−k)!*p^k(1−p)^n−k
#  
# E(X)=npVar(X)=np(1−p)
#  
# What is the probability of getting 2 heads out of 10 flips of a fair coin?

# In[77]:

stats.binom.pmf(2, 10, 0.5)


# In[78]:

n = 10
p = 0.5
sequence = np.arange(0, n+1)
plt.bar(sequence, stats.binom.pmf(sequence, n, p), alpha=0.3)
plt.title('Binomial distribution: $n=%s, p=%.2f$'%(n, p))
plt.xlabel('x')
plt.xlim(0, n+1)
plt.show()


# # Hypothesis Testing
# 
# ## Lady testing tea
# 
# A lady claimed to be able to tell whether the tea or the milk was added first to a cup. A gentle man named Fisher proposed to give her 8 cups, four of each variety, in random order.
# 
# For each cup, a normal people does not have the special ability have the probability of 0.5 to guess the right answer.
# 
# What's the probability of a normal people getting 8 right answers?

# In[79]:

0.5 ** 8


# What about the probability of a normal people getting 7 right answers?

# In[ ]:

0.5 ** 7 * (1-0.5) * 8


# What's the probability of a normal people getting more than 6 right answers? Hint:  p(x=7)+p(x=8)p(x=7)+p(x=8) 

# In[81]:

0.5 ** 7 * (1-0.5) * 8  + 0.5 ** 8


# The distribution of number of right answers that a normal people get is a binomial distribution  Binom(8,0.5). The probability of x(0≤x≤8) answers is  
# 
# C^x base 8 * 0.5^x * (1−0.5)^(8−x)=C^x base 8 *0.5^8
# 
# We can calculate the probability directly by using the function **stats.binom**

# In[82]:

for i in range(9):
   print "The probability of getting %s right answers is: %f"%(i, stats.binom.pmf(i, 8, 0.5))


# In[84]:

for i in range(9):
    print "The probability of getting at least %s right answers is: %f"%(i, 1 - stats.binom.cdf(i-1, 8, 0.5))
# 1 - p(X <= x- 1) = P(X >= x)


# In[88]:

plt.bar(range(9), [stats.binom.pmf(i, 8, 0.5) for i in range(9)], alpha = 0.3)


# In[89]:

print "The expectation is: %f" %stats.binom.mean(8, 0.5)
print "The variance    is: %f" %stats.binom.var(8, 0.5)


# The lady testing tea experiment was designed by Ronald A. Fisher, and it was reported in his book The Design of Experiments. The lady in question was Muriel Bristol, she finnaly hitted all of right answers.
# 
# Assume that the lady does not have the ability. According to the calculation, she has 0.003906 probability of getting 8 cups right.
# 
# The probability 0.003906 is very small, it unlikely to happen in an experiment, so we infer that the lady has the "magic".
# 
# That is the idea of Hypothesis testing.
# 
# Steps of **Hypothesis testing**:
# 
# - Propose a null hypothesis.
# 
# - Run an experiment and get a result.
# 
# - Calculate the probability of the occured result and a 
# more extremely result occur.
# 
# - If the probability is small then a pre-defined 
# threshold, reject the null hypothesis.
# 
# 
# The probability of the effect happening under the null hypothesis is called p-value in the statistic. Usually, the pre-defined threshold is 0.05.
# 
# In the lay testing tea case:
# 
# - null hypothesis: Muriel Bristol does not have the ability, the probability of guess one correctly is $p=0.5$.
# 
# - result: hit all the correct answers.
# 
# - probability: 0.003906
# 
# - 0.003906 < 0.05, reject null hypothesis.
# 
# Production Yield
# In manufacturing industry, people usually sample a center number of products to test the production yield.
# Suppose that the production yield should be at least 99%. We sample 1000 products, and 5 of them are rejects.
# Are this batch of products qualified?
# 
# Null Hypothesis:  H0:p<=0.99 ,  H1:p>0.99.
# 
# **p** is the probability of qualified product.
# 
# The number of rejects follows a binomial distribution  B(1000,0.99).

# In[90]:

pValue = 1 - stats.binom.cdf(994, 1000, 0.99) # p(n >= 995)
pValue


# In[91]:

pValue < 0.05


# #### So we do not reject the null hypothesis.

# In[92]:

1 - stats.binom.cdf(995, 1000, 0.99) # p(n >= 996)


# The number of qualified products should be at least 996 so that the null hypothesis will be rejected.
# 
# 
# ### Student's one-sample t-test
# 
# The t-test for a single sample tests whether the population mean is equal to a given constant.

# In[93]:


x = np.random.normal(loc = 10, scale = 10, size=100)
# equivalent to x = stats.norm.rvs(loc=10, scale=10, size=100)
x


# In[94]:

plt.hist(x, alpha= 0.3)


# Is the mean of x equal to 15? Say the null hypothesis is  x¯=15x¯=15 .

# In[95]:

stats.ttest_1samp(x, 15)


# It return a array whose first element is the value of t-statistic, and the second value is the p-value.
# 
# In this case, p-value is less than 0.05. So we reject the null hypothesis that  x¯=15.
# 
# ### Student's one-sample t-test
# 
# 'HighSchoolGrad.txt' contains the wage of 971 people with high degrees, while 'CollegeGrad.txt' contains the wage of 685 people with college degrees.

# In[ ]:

HighSchool = np.loadtxt('data/HighSchoolGrad.txt')
College = np.loadtxt('data/CollegeGrad.txt')


# In[ ]:

print HighSchool.shape
HighSchool[:5]


# In[ ]:

print College.shape
College[:5]


# The question is, whether their wage has significant difference.

# In[ ]:

plt.rcParams['figure.figsize'] = 12, 6
f, wage = plt.subplots(1, 2, sharex=True)
wage[0].hist(HighSchool, alpha = 0.3)
wage[0].set_title('Wage From High School')
wage[1].hist(College, alpha = 0.3)
wage[1].set_title('Wage From College')


# In[ ]:

f, wage = plt.subplots(1, 2, sharex=True)
wage[0].boxplot(HighSchool)
wage[0].set_title('Wage From High School')
wage[0].set_xticks([])
wage[1].boxplot(College)
wage[1].set_title('Wage From College')
wage[1].set_xticks([])


# In[ ]:

names = ["size", "min/max", "mean", "variance", "skewness", "kurtosis"]
{name: stat for name, stat in zip(names, stats.describe(HighSchool))}


# In[ ]:

{name: stat for name, stat in zip(names, stats.describe(College))}


# In[ ]:

stats.ttest_ind(HighSchool, College)


# Since  p<<0.05 , we consider that the wage of people that have college degree is significantly higher.
# 
# ### Analysis of Variance (ANOVA)
# 
# The two-sample t-test allows us to check whether the value of a particular variable is significantly different between two groups (or samples).
# 
# What if we have more than two categories?
# 
# Analysis of Variance is a way of treating these kind of cases.

# In[ ]:

Mheight = [i.height for i in abalones if i.sex=='M']
Fheight = [i.height for i in abalones if i.sex=='F']
Iheight = [i.height for i in abalones if i.sex=='I']


# The height of M(Male), F(Female), I(Infant)

# In[ ]:

plt.rcParams['figure.figsize'] = 12, 9
plt.subplot2grid((2, 3), (0, 0), colspan=3)
plt.boxplot([Mheight, Fheight, Iheight])
plt.ylim(0, 0.3)
plt.xticks([1, 2, 3], ('M', 'F', 'I'), fontsize = 15)

plt.subplot2grid((2, 3), (1, 0))
plt.hist(Mheight, color='blue', alpha=0.5)
plt.xlabel('M')
plt.ylim(0, 1200)


plt.subplot2grid((2, 3), (1, 1))
plt.hist(Fheight, color='red', alpha = 0.5)
plt.xlabel('F')
plt.ylim(0, 1200)

plt.subplot2grid((2, 3), (1, 2))
plt.hist(Iheight, color='pink', alpha = 0.5)
plt.xlabel('I')
plt.ylim(0, 1200)


# In[ ]:

stats.f_oneway(Mheight, Fheight, Iheight)


# f_oneway is used to implement one-way analysis of variance, in which one-way means just one factor, in this case it is sex.
# The p-value here is about  7×10−290 , which is extremely small.
