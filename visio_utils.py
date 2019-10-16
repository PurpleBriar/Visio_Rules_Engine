RULE_ACTIONS = dict()
RULE_CONDITIONS = dict()

def register_action(func):
    """Register a function as a plug-in"""
    RULE_ACTIONS[func.__name__] = func
    return func

def register_condition(func):
    """Register a function as a plug-in"""
    RULE_CONDITIONS[func.__name__] = func
    return func

def str_to_bool(s):
    if s == "True":
         return True
    elif s == "False":
         return False
    else:
         raise ValueError("Cannot convert {} to a bool".format(s))
    
# property setter
@register_action
def setEqualTo(product,propertyToUpdate,updatedValue):
    product.properties[propertyToUpdate] = updatedValue

# Binary operators
@register_action
def addToValue(product,propertyToUpdate,amountToAdd):
    if not isinstance(product.properties[propertyToUpdate], amountToAdd.__class__):
        return 
    # float_amountToAdd = float(amountToAdd)
    # product.properties[propertyToUpdate]+=float_amountToAdd
    product.properties[propertyToUpdate]+=amountToAdd

# conditions    
@register_condition
def isEqualTo(inputValue,refValue):
    if not isinstance(inputValue, refValue.__class__):
        return False
    return (inputValue == refValue)  

@register_condition
def isLessThan(inputValue,refValue):

    if not isinstance(inputValue, (int, float)):
        raise ValueError("Incorrect input value object type")
    if not isinstance(refValue, (int, float)):
        raise ValueError("Incorrect reference value object type")
    if isinstance(inputValue,bool):
        raise ValueError("Incorrect input value object type")
    if isinstance(refValue,bool):
        raise ValueError("Incorrect reference value object type")

    if not isinstance(inputValue, refValue.__class__):
        return False

    return (inputValue < refValue) 

@register_condition
def isLessThanOrEqualTo(inputValue,refValue):

    if not isinstance(inputValue, (int, float)):
        raise ValueError("Incorrect input value object type")
    if not isinstance(refValue, (int, float)):
        raise ValueError("Incorrect reference value object type")
    if isinstance(inputValue,bool):
        raise ValueError("Incorrect input value object type")
    if isinstance(refValue,bool):
        raise ValueError("Incorrect reference value object type")

    if not isinstance(inputValue, refValue.__class__):
        return False

    return (inputValue <= refValue)  

@register_condition
def isMoreThan(inputValue,refValue):

    if not isinstance(inputValue, (int, float)):
        raise ValueError("Incorrect input value object type")
    if not isinstance(refValue, (int, float)):
        raise ValueError("Incorrect reference value object type")
    if isinstance(inputValue,bool):
        raise ValueError("Incorrect input value object type")
    if isinstance(refValue,bool):
        raise ValueError("Incorrect reference value object type")

    if not isinstance(inputValue, refValue.__class__):
        return False

    return (inputValue > refValue) 

@register_condition
def isMoreThanOrEqualTo(inputValue,refValue):

    if not isinstance(inputValue, (int, float)):
        raise ValueError("Incorrect input value object type")
    if not isinstance(refValue, (int, float)):
        raise ValueError("Incorrect reference value object type")
    if isinstance(inputValue,bool):
        raise ValueError("Incorrect input value object type")
    if isinstance(refValue,bool):
        raise ValueError("Incorrect reference value object type")

    if not isinstance(inputValue, refValue.__class__):
        return False
        
    return (inputValue >= refValue)
