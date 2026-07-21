"""
code sample demonstrating import, from {package} import, and aliasing
"""

# importing sqrt from the math module
from math import sqrt
sqrt
help(sqrt)

# let's check the module!
sqrt.__module__

from cmath import sqrt


# let's check the module again!
sqrt.__module__
help(sqrt)

# as we can see, functions/methods are simply objects and sequence matters

# alias?
from cmath import sqrt as complex_sqrt
from math import sqrt

complex_sqrt.__module__
sqrt.__module__

# we could also simply alias the package
# import entire package, then namespace
import math
import cmath

math.sqrt.__module__
cmath.sqrt.__module__

