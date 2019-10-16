import unittest

from visio_classes import Person
from visio_classes import Product
from visio_classes import Condition
from visio_classes import Action
from visio_classes import Rule
from visio_classes import RulesEngine

class TestClassMethods(unittest.TestCase):

    def test_condition_evaluation(self):

        # Create object instances to test
        test_person = Person(720,"Florida")
        test_product = Product("7-1 ARM",0.0,False)

        # Check evaluations on objects of type Person
        test_condition = Condition("Person","state","isEqualTo","Florida")
        self.assertTrue(test_condition.evaluate(test_person))

        test_condition = Condition("Person","state","isEqualTo","Georgia")
        self.assertFalse(test_condition.evaluate(test_person))

        test_condition = Condition("Person","credit_score","isMoreThanOrEqualTo",720)
        self.assertTrue(test_condition.evaluate(test_person))

        test_condition = Condition("Person","credit_score","isLessThan",720)
        self.assertFalse(test_condition.evaluate(test_person))

        # Check evaluations on objects of type Product
        test_condition = Condition("Product","name","isEqualTo","7-1 ARM")
        self.assertTrue(test_condition.evaluate(test_product))
        
        test_condition = Condition("Product","name","isEqualTo","5-1 ARM")
        self.assertFalse(test_condition.evaluate(test_product))

        # Verify that method handles incorrectly defined conditions
        # Case 1: Condition's reference value has wrong type
        test_condition = Condition("Person","credit_score","isLessThan","720")
        self.assertRaises(ValueError,test_condition.evaluate,test_condition)

        # Case 2: Condition's reference object has wrong type
        test_condition = Condition("Product","credit_score","isLessThan","720")
        self.assertRaises(ValueError,test_condition.evaluate,test_condition)

    def test_action_execution(self):

        # Create object instances to test
        test_person = Person(720,"Florida")
        test_product = Product("7-1 ARM",5.0,False)

        # Check executions on objects of type Product
        test_action = Action("addToValue","interest_rate",0.3)
        test_action.execute(test_product)
        self.assertEqual(test_product.properties["interest_rate"],5.3)

        test_action = Action("addToValue","interest_rate",-0.3)
        test_action.execute(test_product)
        self.assertEqual(test_product.properties["interest_rate"],5.0)

        # Verify that method handles incorrectly defined actions
        # Case 1: Incorrect reference value type
        test_action = Action("addToValue","interest_rate","-0.3")
        self.assertRaises(TypeError,test_action.execute,test_product)
        #       - Check that the right exception is raised
        with self.assertRaises(TypeError) as context_manager:
            test_action.execute(test_product)
        self.assertEqual("Updated value has wrong type",context_manager.exception.args[0])

        # Case 2: Check that executions on objects of type Person raise exceptions
        self.assertRaises(TypeError,test_action.execute,test_person)
        #       - Check that the right exception is raised
        with self.assertRaises(TypeError) as context_manager:
            test_action.execute(test_person)
        self.assertEqual("Needs input of type Product",context_manager.exception.args[0])

    def test_rule_condition_checking(self):

        # Create object instances to test
        test_person = Person(720,"Florida")
        test_product = Product("7-1 ARM",5.0,False)
        test_condition = Condition("Product","name","isEqualTo","7-1 ARM")
        test_action = Action("addToValue","interest_rate",0.3)

        test_conditions = []
        test_conditions.append(test_condition)
        test_rule = Rule("Adjust rates for 7-1 ARM",test_conditions,test_action)

        self.assertTrue(test_rule.check_conditions(test_product,test_person))

        test_condition.checked_object_type = None
        self.assertRaises(TypeError,test_rule.check_conditions,test_product,test_person)
        #       - Check that the right exception is raised
        with self.assertRaises(TypeError) as context_manager:
            test_rule.check_conditions(test_product,test_person)
        self.assertEqual("Unknown object type is subject of condition",context_manager.exception.args[0])




