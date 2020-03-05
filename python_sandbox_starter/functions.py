""" Functions """

# A function is a block of code which only runs when it is called.
# In Python, we do not use parentheses and curly brackets, we use
# indentation with tabs or spaces

# Create function
def say_hello(name="John Doe"):
    """ Print \"Hello name\" on screen """
    print(f"Hello {name}")


# Return values
def get_sum(num1, num2):
    """ Return the sum of num1 and num2. """
    total = num1 + num2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one
# expression. Very similar to JS arrow functions

get_sum = lambda num1, num2: num1 + num2

print(get_sum(3, 4))
