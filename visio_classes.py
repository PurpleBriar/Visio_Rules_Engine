import visio_utils

# Person class
class Person(object):
    def __init__(self,credit_score,state):
        self.properties = {}
        self.properties["credit_score"] = credit_score
        self.properties["state"] = state
    
    def __str__(self):
        return "Person: " + str(self.properties["credit_score"]) + " " +self.properties["state"]

# Product class
class Product(object):
    def __init__(self,name,interest_rate,disqualified):
        # self.name=name
        self.properties = {}
        self.properties["name"] = name
        self.properties["interest_rate"] = interest_rate
        self.properties["disqualified"] = disqualified

    
    def __str__(self):
        return {self.name} + ": " + str(self.properties["interest_rate"]) + " " + str(self.properties["disqualified"])

# CONDITION CLASS:
# ================

# Class instances describe a condition as an operator and reference value
# evaluate() method compares an object's property to the reference value
# and returns true or false or None if the rule does not run
class Condition(object):
    def __init__(self,checked_object_type,checked_property,condition_check,ref_value):
        if condition_check in visio_utils.RULE_CONDITIONS:
            self.condition_check = visio_utils.RULE_CONDITIONS[condition_check]
        self.condition_ref_value = ref_value
        self.checked_object_type = checked_object_type
        self.checked_property = checked_property
    
    def evaluate(self,object_instance):
            
        if not (self.checked_object_type == object_instance.__class__.__name__):
            # return None
            raise ValueError("Input object type does not match condition\'s reference object type")
        elif self.checked_property not in object_instance.properties:
            raise ValueError(f"Condition subject has no property called {self.checked_property}")
        if (self.condition_check and object_instance.properties[self.checked_property]):
            return (self.condition_check(object_instance.properties[self.checked_property],self.condition_ref_value))
        return None
    
    def __str__(self):
        return f"{self.checked_object_type}: {self.condition_check},{self.checked_property},{self.condition_ref_value}"

# ACTION CLASS:
# =============

# Implements an action limited to updating attribute values of product
class Action(object):
    def __init__(self,action,property_to_update,updated_value):
        self.updated_value = updated_value
        self.action = visio_utils.RULE_ACTIONS[action]
        self.property_to_update = property_to_update

    def execute(self,product):
        if product.__class__.__name__ != "Product":
            raise TypeError("Needs input of type Product")
        if (self.property_to_update in product.properties):
            if product.properties[self.property_to_update] and (product.properties[self.property_to_update].__class__ != self.updated_value.__class__):
                raise TypeError("Updated value has wrong type")

            self.action(product,self.property_to_update,self.updated_value)
    
    def __str__(self):
        return f"{self.action}: {self.property_to_update},{self.updated_value}"

    

# RULE CLASS:
# ===========

# Pairs the result of a series of conditions with an action
# i.e., if ALL of these conditions are met, execute action
class Rule(object):
    def __init__(self,name,conditions,action):
        self.name = name
        self.conditions = conditions
        self.action = action

    # take as input person or product property and compare to ref value
    def check_conditions(self,product,person):
        for condition in self.conditions:
            if condition.checked_object_type == "Product":
                object_instance = product
            elif condition.checked_object_type == "Person":
                object_instance = person
            else:
                raise TypeError("Unknown object type is subject of condition")
                
            if (condition.evaluate(object_instance) != True):
                return False
        return True

    def run_rule(self,product,person):
        if self.check_conditions(product,person):
            self.action.execute(product)
            print("Applied update: " + self.name)
    
    def __str__(self):
        if len(self.conditions) == 0:
            return f"{self.name}: \n\tno conditions\n\t{self.action}"
        return f"{self.name}: \n\t{self.conditions[0]}\n\t{self.action}"

# RULE ENGINE CLASS:
# ==================

# rule engine definition
class RulesEngine(object):
    def run_rules(self,person,product,rules):
        for rule in rules:
            # print(rule)
            rule.run_rule(product,person)
