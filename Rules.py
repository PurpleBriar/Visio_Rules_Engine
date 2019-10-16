import json

from visio_classes import Person
from visio_classes import Product
from visio_classes import Condition
from visio_classes import Action
from visio_classes import Rule
from visio_classes import RulesEngine 


# read rules line by line from file; assume csv input with columns mapping to rule inputs
def loadRules():
    rules = []

    json_rule_file = open("JSON_Rules.json", "r")
    json_decode=json.load(json_rule_file)

    json_rule_list = json_decode.get("rules")

    for json_rule in json_rule_list:
        current_rule_name = json_rule.get("rule_name")

        current_json_rule_conditions = json_rule.get("rule_conditions")
        current_rule_conditions = []
        for current_json_rule_condition in current_json_rule_conditions:
            current_rule_condition_subject_type = current_json_rule_condition.get("subject_type")
            current_rule_condition_subject_attribute = current_json_rule_condition.get("subject_attribute")
            current_rule_condition_check = current_json_rule_condition.get("check")
            current_rule_condition_ref_value = current_json_rule_condition.get("ref_value")
            current_rule_conditions.append(Condition(current_rule_condition_subject_type,current_rule_condition_subject_attribute,current_rule_condition_check,current_rule_condition_ref_value))

        current_json_rule_action = json_rule.get("rule_action")
        
        current_rule_action_operator = current_json_rule_action.get("operator")
        current_rule_action_property_to_update = current_json_rule_action.get("property_to_update")
        current_rule_action_updated_value = current_json_rule_action.get("property_value")
        current_rule_action = Action(current_rule_action_operator,current_rule_action_property_to_update,current_rule_action_updated_value)
        
        rules.append(Rule(current_rule_name,current_rule_conditions,current_rule_action))

    json_rule_file.close()

    return rules


# SAMPLE RUNS
rules = loadRules()

rules_engine = RulesEngine()

test_person = Person(720,"Florida")
test_product = Product("7-1 ARM",0.0,False)

rules_engine.run_rules(test_person,test_product,rules)

print("Interest rate is " + str(test_product.properties["interest_rate"]))
print("Disqualified is " + str(test_product.properties["disqualified"]))
print("\n")

test_person = Person(719,"Florida")
test_product = Product("7-1 ARM",0.0,False)

rules_engine.run_rules(test_person,test_product,rules)

print("Interest rate is " + str(test_product.properties["interest_rate"]))
print("Disqualified is " + str(test_product.properties["disqualified"]))
print("\n")

test_person = Person(720,"Georgia")
test_product = Product("7-1 ARM",0.0,False)

rules_engine.run_rules(test_person,test_product,rules)

print("Interest rate is " + str(test_product.properties["interest_rate"]))
print("Disqualified is " + str(test_product.properties["disqualified"]))
