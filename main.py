from data import MENU , resources
#


starting_amount_water = resources["water"]
starting_amount_coffee = resources["coffee"]
starting_amount_milk = resources["milk"]
ingredient_for_espress = MENU['espresso']['ingredients']
water_amount_es = ingredient_for_espress["water"]
coffee_amount_es = ingredient_for_espress["coffee"]

ingredient_for_cap = MENU['cappuccino']['ingredients']
water_amount_cap = ingredient_for_cap["water"]
coffee_amount_cap = ingredient_for_cap["coffee"]
milk_amount_cap = ingredient_for_cap["milk"]

ingredient_for_latte = MENU['latte']['ingredients']
water_amount_latte = ingredient_for_latte["water"]
coffee_amount_latte = ingredient_for_latte["coffee"]
milk_amount_latte = ingredient_for_latte["milk"]

money_bank = []
quarter = 0.25
dimes = 0.10
nickel = 0.05
penny = 0.01


buy_coffee = True
while buy_coffee:
    choice_of_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice_of_user == "report":
        for i in resources:
            print(i , ":" , resources[i])
        choice_of_user = input("What would you like? (espresso/latte/cappuccino): ")
    # elif choice_of_user == "off":
    #     buy_coffee = False


    print("Please insert coins")
    num_quarter = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickel = int(input("how many nickles?: "))
    num_penny = int(input("how many pennies?: "))

    # def calculate_amount(quarters , dimes , nickels , pennies):
    total_quarter = num_quarter * quarter
    total_dimes = num_dimes * dimes
    total_nickel = num_nickel * nickel
    total_penny = num_penny * penny
    money_bank.append(total_quarter)
    money_bank.append(total_nickel)
    money_bank.append(total_dimes)
    money_bank.append(total_penny)
    # print(money_bank)

    customer_paid_amount = round(sum(money_bank),2)
    print(f"Money paid: ${customer_paid_amount}")

    list_of_coffee = []
    for key in MENU:
        list_of_coffee.append(key)
    if choice_of_user == "off":
        buy_coffee = False
        print("Machine off")
    if choice_of_user == "espresso":
        cost_of_esp = MENU['espresso']['cost']
        print(f"Cost of espresso: ${cost_of_esp}")
        if customer_paid_amount < cost_of_esp:
            print("Sorry your money is not sufficient")
        else:
            left_water = starting_amount_water - water_amount_es
            resources["water"] = left_water
            left_coffee = starting_amount_coffee - coffee_amount_es
            resources["coffee"] = left_coffee
            if choice_of_user == "report":
                print(resources)
            change_of_customer = round(customer_paid_amount - cost_of_esp , 2)
            print(f"Change: ${change_of_customer}")
            print(f"Here is your {list_of_coffee[0]} ☕ . Enjoy!")
    elif choice_of_user == "latte":
        cost_of_latte = MENU['latte']['cost']
        print(f"Cost of latte: ${cost_of_latte}")
        if customer_paid_amount < cost_of_latte:
            print("Sorry your money is not sufficient")
        else:
            left_water = starting_amount_water - water_amount_latte
            resources["water"] = left_water
            left_coffee = starting_amount_coffee - coffee_amount_latte
            resources["coffee"] = left_coffee
            left_milk = starting_amount_milk - milk_amount_latte
            resources["milk"] = left_milk
            print(resources)
            change_of_customer = round(customer_paid_amount - cost_of_latte , 2)
            print(f"Here is your change: ${change_of_customer}")
            print(f"Here is your {list_of_coffee[1]} ☕ . Enjoy!")
    elif choice_of_user == "cappuccino":
        cost_of_cap = MENU['cappuccino']['cost']
        print(f"Cost of cappuccino: ${cost_of_cap}")
        if customer_paid_amount < cost_of_cap:
            print("Sorry your money is not sufficient")
        else:
            left_water = starting_amount_water - water_amount_cap
            resources["water"] = left_water
            left_coffee = starting_amount_coffee - coffee_amount_cap
            resources["coffee"] = left_coffee
            left_milk = starting_amount_milk - milk_amount_cap
            resources["milk"] = left_milk
            print(resources)
            change_of_customer = round(customer_paid_amount - cost_of_cap , 2)
            print(f"Change: ${change_of_customer}")
            print(f"Here is your {list_of_coffee[2]} ☕ . Enjoy!")




# is_continue = True
# while is_continue:
#     choicess = input("enter something:")
#     if choicess == "report":
#         for i in resources:
#             print(i, ":", resources[i])
#     elif choicess == "hello":
#         print(2 + 2)
#     elif choicess == "off":
#         is_continue = False

    #
# coffee_maker()