import unittest

from visio_utils import isEqualTo
from visio_utils import isLessThan
from visio_utils import isLessThanOrEqualTo
from visio_utils import isMoreThan
from visio_utils import isMoreThanOrEqualTo

class TestOperators(unittest.TestCase):

    def test_is_equal_to(self):
        self.assertTrue(isEqualTo(1,1))
        self.assertFalse(isEqualTo(1,2))
        self.assertFalse(isEqualTo(1,1.0))
        self.assertFalse(isEqualTo(1,"a"))
        self.assertFalse(isEqualTo(1,True))
        self.assertFalse(isEqualTo(1,None))
        self.assertTrue(isEqualTo([],[]))
        self.assertTrue(isEqualTo(None,None))

    def test_is_less_than(self):
        self.assertTrue(isLessThan(0,1))
        self.assertFalse(isLessThan(0,0))
        self.assertFalse(isLessThan(1,0))
        self.assertRaises(ValueError,isLessThan, 1, "a")
        self.assertRaises(ValueError,isLessThan, None, "a")
        self.assertRaises(ValueError,isLessThan, None, 1)
        self.assertRaises(ValueError,isLessThan, False, 1)

    def test_is_less_than_or_equal_to(self):
        self.assertTrue(isLessThanOrEqualTo(0,1))
        self.assertTrue(isLessThanOrEqualTo(0,0))
        self.assertFalse(isLessThanOrEqualTo(1,0))
        self.assertRaises(ValueError,isLessThanOrEqualTo, 1, "a")
        self.assertRaises(ValueError,isLessThanOrEqualTo, None, "a")
        self.assertRaises(ValueError,isLessThanOrEqualTo, None, 1)
        self.assertRaises(ValueError,isLessThanOrEqualTo, False, 1)

    def test_is_more_than(self):
        self.assertFalse(isMoreThan(0,1))
        self.assertFalse(isMoreThan(0,0))
        self.assertTrue(isMoreThan(1,0))
        self.assertRaises(ValueError,isMoreThan, 1, "a")
        self.assertRaises(ValueError,isMoreThan, None, "a")
        self.assertRaises(ValueError,isMoreThan, None, 1)
        self.assertRaises(ValueError,isMoreThan, False, 1)

    def test_is_more_than_or_equal_to(self):
        self.assertFalse(isMoreThanOrEqualTo(0,1))
        self.assertTrue(isMoreThanOrEqualTo(0,0))
        self.assertTrue(isMoreThanOrEqualTo(1,0))
        self.assertRaises(ValueError,isMoreThanOrEqualTo, 1, "a")
        self.assertRaises(ValueError,isMoreThanOrEqualTo, None, "a")
        self.assertRaises(ValueError,isMoreThanOrEqualTo, None, 1)
        self.assertRaises(ValueError,isMoreThanOrEqualTo, False, 1)