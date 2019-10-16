# Visio_Rules_Engine

## Overview
This project includes an implementation of a simple rule engine that determines whether a person qualifies for a given product and sets the interest rate and disqualification status for the person based on predefined rules. The rulebase is designed to be easily updated, with rules defined and implemented separately from the code that executes them. The rules described in the problem statement have been implemented in the file ***JSON_Rules.json:***, along with an additional rule to illustrate the rule base's extensibility.

## Instructions
The code is written in Python (Python 3) and can be run from the command line. To add new rules, update the file ***JSON_Rules.json:***  using the format for existing rules. See **Contents** section for details.

## Contents
***visio_utils.py:*** This file contains helper functions such as operators and functions that enable comparisons

***test_visio_utils.py:*** This file contains the unit tests for functions defined in ***visio_utils.py:***. It can be run from the command line using the command ***python -m unittest visio_utils.py:***

***visio_classes.py:*** This file contains the class definitions for classes that enable rule implementation and execution. Classes defined here are: Person, Product, Condition, Action, Rule, RulesEngine.

***test_visio_classes.py:*** This file contains the unit tests for class methods defined in ***visio_classes.py:***. It can be run from the command line using the command ***python -m unittest visio_classes.py:***

***Rules.py:*** This file includes the definition of the function ***loadRules***, which loads rules defined in the file ***JSON_Rules.json:***. Several sample class instances are defined in this file to showcase rule implementation and execution. The file can be run from the command line using the command ***python Rules.py***

***JSON_Rules.json:*** This file contains rules stored in ***json*** format. Rules match a set of conditions with an action and are defined as dictionaries that include a name (as a string), a set of conditions (as a list of dictionaries), and an action (as a single dictionary). An example is shown below:

```
        {   
            "rule_name": "Disqualify Florida Applicants", 

            "rule_conditions": 
            [
                {
                    "subject_type": "Person", 
                    "subject_attribute": "state", 
                    "attribute_type": "STRING", 
                    "check": "isEqualTo",
                    "ref_value": "Florida"
                }
            ], 

            "rule_action": 
            {
                "operator": "setEqualTo", 
                "property_to_update": "disqualified", 
                "property_type": "BOOLEAN", 
                "property_value": true
            }
        }
```

## Problem Statement

You have been tasked by a stakeholder to develop a solution that allows the business to dynamically generating product pricing from a set rules defined by the finance team. The finance team has given you an initial set of rules on how to price the products, however, these rules could change at any time so we need to be able to update the rules easily and rerun the product pricing to see the new prices of the products. 
 
Initial Rules: 
 
- All products start at 5.0 interest_rate. 
- If the person lives in Florida (condition), we do not offer the product to them and the product is to be disqualified (action). 
- If the person has a credit score greater than or equal to 720(condition) then we reduce the interest_rate on the product by .3 (action that has an input of “.3”, remember the business may decide in the future they want to reduce it by .5). 
- If the person has a credit score lower than 720 we increase the interest_rate on the product by .5. 
- If the name of the product is “7-1 ARM” then we need to add .5 to the interest_rate of the product. 
 
Example:   
```
class Person:   
  credit_score: integer   
  state: string     
 
class Product:   
  name:  string   
  interest_rate: decimal   
  disqualified: boolean     
  
class RulesEngine   
  def runRules(person, product, rules)     
    person = new Person(720, ‘Florida’)     
    product = new Product(‘7-1 ARM’, 5.0) 
  
rules_engine = new RulesEngine() 
 
rules = loadRules() // Rules are loaded at runtime!     

rules_engine.runRules(person, product, rules**); 
```
 
**Hint: We have not defined how the rules are represented, they could be json, csv, etc. The only thing that matters is that rule definitions can be extended upon and defined outside of the code, the rule definitions should define an action, any parameters an action needs, and under what condition to execute the action. 
 
The output of the above code example should be: 
``` 
product.interest_rate == 5.2 ( 5.0 - .3 + .5 ) 
 
product.disqualified == true  
```

## Expectations: 
 
1. Build a rules engine to accomplish what the business has asked above. 
 
2. Exhaustively test all possible rule outcomes and assert that the rules engine works as expected and meets the business requirements. 
 
3. Show the extendibility of your rules engine and create your own rule definition to execute an additional action on a product. 
