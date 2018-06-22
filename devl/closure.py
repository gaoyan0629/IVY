# When to use closures?
# So what are closures good for?
# Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

# When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.
#
# Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

# the beauty is that the argument n will now be memorized by multiplier

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

#now we have two instance
