# Section1: Place test modules at the correct location
"""
A: tests/visualization/test_plots.py
"""

# Section2: Create a test class
"""
import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)
"""

# Section3: One command to run them all
"""
A: !pytest
"""
# //////////////////////
"""
A: Passing: 15, Failing: 1
"""
# //////////////////////
"""
A: !pytest -x
"""
# //////////////////////
"""
A: 15
"""

# Section4: Running test classes
"""
import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        raise ValueError("Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError("Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    # Fill in with the correct float
    num_training = int(data_array.ndim * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]
"""
# //////////////////////
"""
A: !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets
"""
# //////////////////////
"""
A: !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_
"""
# //////////////////////
"""
A: !pytest -k "SplitInto"
"""

# Section5: Mark a test class as expected to fail
"""
A: The tests fail with NameError since the function model_test() has not yet been defined.
"""
# //////////////////////
"""
# Mark the whole test class as "expected to fail"
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
"""
# //////////////////////
"""
# Add a reason for the expected failure
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
"""

# Section5: Mark a test as conditionally skipped
"""
A: The test test_on_clean_file() fails with a NameError because Python 3 does not recognize the xrange() function.
"""
# //////////////////////
"""
# Import the sys module
import sys
"""
# //////////////////////
"""
# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
"""
# //////////////////////
"""
# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
"""

# Section6: Reasoning in the test result report
"""
A: !pytest -rx
"""
# //////////////////////
"""
A: !pytest -rs.
"""
# //////////////////////
"""
A: !pytest -rsx.
"""

# Section7: Build failing
"""
A: 
The package has bugs, which is either causing installation to error out or some of the unit tests in the test suite to fail.
"""

# Section8: What does code coverage mean?
"""
A: The test suite tests about 85% of the application code.
"""