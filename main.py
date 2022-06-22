
from data import MENU , resources
profit = 0
def is_resources_enough(user_ingred):
    is_enough = True
    for item in user_ingred:
        if user_ingred[item] >= resources[item] :
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_money():
    # returns total money
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
    
    
def is_transaction_success(money_received, drink_cost):
    # checks if the money is sufficient to purchase
    if money_received >= drink_cost:
        global profit
        change_of_customer = round(money_received - drink_cost , 2)
        print(f"Here is your change: ${change_of_customer}")
        profit += drink_cost
        return True
    else:
        print("Sorry your money is not sufficient")
        return False
    
def make_coffee(drink_name,order_ingredients):
    # deduct ingredients 
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy! ")
is_on = True
while is_on:
    choice_of_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice_of_user == "off":
        is_on = False
    elif choice_of_user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:  ${profit}")
    
    else:
        drink = MENU[choice_of_user]
        if is_resources_enough(drink["ingredients"]):
            payment = process_money()
            is_transaction_success(payment, drink["cost"])
            make_coffee(choice_of_user, drink["ingredients"])
               