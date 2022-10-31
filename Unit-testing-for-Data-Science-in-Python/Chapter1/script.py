# Section1: How frequently is a function tested?
"""
A: A function is tested after the first implementation and then any time the function is modified, which happens mainly when new bugs are found, new features are implemented or the code is refactored.
"""
# Section2: Manual testing
"""
A: o. the function returns ["", "293,410"] for the argument "\t293,410\n" instead of the expected return value None.
############################################
A: Yes, the implementation returns the expected value in each case.
"""
# Section3: Your first unit test using pytest
"""
# Import the pytest package
import pytest
############################################
# Import the pytest package
import pytest

# Import convert_to_int() from the module preprocessing_helpers.py
from preprocessing_helpers import convert_to_int
############################################
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  pass
  # Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  pass
############################################
# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081
"""
# Section4: Running unit tests
"""
A: !pytest test_convert_to_int.py
"""
# Section5: What causes a unit test to fail?
"""
A:  exception is raised when running the unit test. This could be an AssertionError raised by the assert statement or another exception, e.g. NameError, which is raised before the assert statement can run.
"""
# Section6: Spotting and fixing bugs
"""
A: convert_to_int("2,081") is expected to return the integer 2081, but it is actually returning the string "2081".
############################################
def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))
"""
# Section7: Benefits of unit testing
"""
A: 1, 3, 4 and 6
"""
# Section8: Unit tests as documentation
"""
A: It converts data in a data file into a NumPy array
"""