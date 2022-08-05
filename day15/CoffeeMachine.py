import Recipe

def retrieveRecipe(choice):
    recipe={}
    if choice =="a":
        #Espresso
        recipe = Recipe.MENU['espresso']
    elif choice == "b":
        #Latte
        recipe = Recipe.MENU['latte']
    elif choice == "c":
        #Cappuccino
        recipe = Recipe.MENU['cappuccino']
    else :
        print("Choice not available, please try again")
    return recipe

def checkResources(recipe):
    print("Checking resources")
    if not isEnough(recipe):
        return False
    return True
    
def isEnough(recipe):
    ingredients = recipe['ingredients']
    for ingredient in ingredients:
        if Recipe.resources[ingredient] - ingredients[ingredient] <0 :
            print(f"Sorry, not enough {ingredient} in the machine")
            return False
    return True

def processCoins(recipe):
    cost = recipe['cost']
    print(f"Please insert {cost}$")
    quarters = int(input("how many quarters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies ?: "))
    amount_inserted = quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    if amount_inserted<cost:
        print("not enough money")
        print(f"Take your change {amount_inserted}")
        return False
    elif amount_inserted==cost:
        Recipe.resources['money']+=cost
        return True
    else:
        Recipe.resources['money']+=cost
        print(f"Take your change {amount_inserted-cost:.2f}")
        return True

def prepare(recipe):
    print(f"Preparing your drink ...")
    ingredients = recipe['ingredients']
    for ingredient in ingredients:
        Recipe.resources[ingredient] -= ingredients[ingredient]
    print("Your drink is ready, you can take it")

running = True
while running :
    answer = input("What do you want ? A) Expresso, B) Latte, C) Cappuccino : \n").lower()
    if answer=="off":
        print("Shuting down")
        running=False
    elif answer =="report":
        print("Printing coffee machine report")
        print(Recipe.resources)
    else :
        recipe = retrieveRecipe(answer)
        if len(recipe)==0:
            print("Choose another drink")
        elif checkResources(recipe):
            if processCoins(recipe):
                prepare(recipe)
