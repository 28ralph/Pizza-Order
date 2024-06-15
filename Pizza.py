"""
A pizza restaurant program. You can order a small, medium or large pizza. There are 4 available toppings. We also sell sodas like Coke, Sprite and Sunkist. We 
also offer desserts like cheesecake and chocolate cake

"""

cheesecake="0"
chocolate_cake = "0"
total_topping_price = 0
num_soda = 0
topping_list = []
total_pizza_price = 0
num_topping = ""

def prices():
    #menu prices
    print("Welcome to Ralph's Pizza Restaurant")
    print()
    price = {}
    
    price["Small Pizza"] = "\t\t$5.99"
    price["Medium Pizza"] = "\t\t$7.99"
    price["Large Pizza"] = "\t\t$9.99"
    
    price["Small Topping"] = "\t\t$.50"
    price["Medium Topping"] = "\t$1.00"
    price["Large Topping"] = "\t\t$1.50"
    
    price["Coke, Sprite, Sunkist"] = "\t$1.50"
    
    price["Cheesecake"] = "\t\t$3.50"
    price["Chocolate Cake"] = "\t$4.00"
    
    for key, value in price.items():
        print("{}: {}".format(key, value))

def menu():
    
    choice_list = ['a', 'b', 'c', 'd'] #valid choices for pizza selection
    while True:
       
        order = ""
        
        print()
        print("a) Pizzas")
        print("b) Sodas")
        print("c) Desserts")
        print("d) Order finished")
        print()
        order = input("What do you want to order (enter a, b, c or d)? ") #input what consumer wants to order
        order = order.lower()
        while order not in choice_list: #while order is invalid ask for input again and again until input is valid
            print("Invalid input. Pleas try again ")
            order = input("What do you want to order? ")
            order = order.lower()
        
        if order == "a":
            pizza() #call pizza() function which asks how many pizza consumer wants to buy, toppings, and sizes
            
            
        if order == "b":
            soda() # call soda() function to take soda drinks order
        elif order == "c":
            
            desserts() #call desserts() function to take dessert order
            
        elif order == "d": # exit program and print receipt
            print("Have a nice day!")
            break;
            
        else:
            pass
        
    
    
def topping_menu():
    print("a)Pepperoni")
    print("b)Mushroom")
    print("c)Black Olives")
    print("d)onions")
    
def pizza_size():
    print("a) Small")
    print("b) Medium")
    print("c) Large")
    
    
def soda():
    
    global num_soda
    soda = ""
    coke = 0
    sprite = 0
    sunkist = 0
    
    print("We have Coke, Sprite and Sunkist.")
    print()
    
    coke = input("How many coke(s) do you want? ")
    while not coke.isnumeric():
        print("Invalid input. Please try again")
        coke = input("How many coke(s) do you want? ")
    coke = int(coke)
    coke = coke  
    sprite = input("How many sprite(s) do you want? ")
    while not sprite.isnumeric():
        print("Invalid input. Please try again")
        sprite = input("How many sprite(s) do you want? ")
    sprite = int(sprite)
    sprite = sprite
    
    sunkist = input("How many sunkist(s) do you want? ")
    while not sunkist.isnumeric():
        print("Invalid input. Please try again")
        sunkist = input("How many sunkist(s) do you want? ")
    sunkist = int(sunkist)   
    sunkist = sunkist
    num_soda += coke + sprite + sunkist
    
   

    
def desserts():
    global cheesecake
    global chocolate_cake
    
    
    print("We have cheesecake and chocolate cake")
    
    cheesecake = input("How many cheesecakes do you want? ")
    while not cheesecake.isnumeric():
        print("Invalid input. Please try again. ")
        cheesecake = input("How many cheesecakes do you want? ")
    cheesecake = int(cheesecake)
    
    chocolate_cake = input("How many chocolate cakes do you want? ")
    while not chocolate_cake.isnumeric():
        print("Invalid input. Please try again. ")
        chocolate_cake = input("How many chocolate cakes do you want? ")
    chocolate_cake += int(chocolate_cake)
    
    
    
def pizza():
    small = 0
    medium = 0
    large = 0
    SMALL_PRICE = 5.99
    MEDIUM_PRICE = 7.99
    LARGE_PRICE = 9.99
    small_topping = .5
    medium_topping = 1  
    large_topping = 1.5
    topping_choice_list = ['a', 'b', 'c','d']
    pizza_num = 0
    size = ""
    topping_string = ""
    topping = ""
    
    global total_pizza_price
    global total_topping_price
    global num_topping
    
    pizza_size_list = ['a', 'b', 'c']
   
    pizza_num = input("How many pizza do you want to order? ")
    
    while not pizza_num.isnumeric():
        print("Invalid input. Please try again ")
        pizza_num = input("How many pizza do you want to order? ")
    pizza_num = int(pizza_num)
    for i in range(pizza_num):
       
        pizza_size()
        size = input("What size for pizza " + str(i + 1) + " ? ")
        while size not in pizza_size_list:
            print("Invalid input. Please try again. ")
            size = input("What size for pizza " + str(i + 1) + " ? ")
        if size == "a":
            small += 1  
            
            topping_string += "Small: "
           
            num_topping = input("How many toppings do you want (4 limit)? ")
            while not num_topping.isnumeric() or int(num_topping) > 4:
                print("Invalid input. Please try again ")
                num_topping = input("How many toppings do you want? ")
                
            num_topping = int(num_topping)
                
            for i in range(num_topping):
                topping_menu()
                
                topping = input("Which topping? ")
                
                while topping not in topping_choice_list:
                    topping_menu()
                    print("Invalid input. Please try again.")
                    topping = input("Which topping? ")
                
                if topping == "a":
                    topping_string += "Pepperoni "

                elif topping == "b":
                    topping_string += "Mushroom "

                elif topping == "c":
                    topping_string += "Olives "
                elif topping == "d":
                    topping_string += "Onions "
            topping_list.append("\b" + topping_string + "\n")
            topping_string= ""
            total_topping_price += num_topping * small_topping
            total_pizza_price = small * SMALL_PRICE
            
        elif size == "b":
            
            medium += 1
            topping_string += "Medium: "
            
            num_topping = input("How many toppings do you want(4 limit)? ")
            while not num_topping.isnumeric() or int(num_topping) > 4:
                print("Invalid input. Please try again ")
                num_topping = input("How many toppings do you want? ")
                
            num_topping = int(num_topping)
            for i in range(num_topping):
                topping_menu()
                topping = input("Which topping? ")
                
                while topping not in topping_choice_list:
                    topping_menu()
                    print("Invalid input. Please try again.")
                    topping = input("Which topping? ")
                
                if topping == "a":
                    topping_string += "Pepperoni "

                elif topping == "b":
                    topping_string += "Mushroom "

                elif topping == "c":
                    topping_string += "Olives "

                elif topping == "d":
                    topping_string += "Onions "

            
            topping_list.append("\b" + topping_string + "\n")
            topping_string = ""
            
            total_topping_price += num_topping * medium_topping
            total_pizza_price += medium * MEDIUM_PRICE

            
            
        elif size == "c":
            large += 1
            topping_string += "Large: "

            num_topping = input("How many toppings do you want (4 limit)? ")
            while not num_topping.isnumeric() or int(num_topping) > 4:
                print("Invalid input. Please try again ")
                num_topping = input("How many toppings do you want? ")
                
            num_topping = int(num_topping)
            for i in range(num_topping):
                topping_menu()
                
                topping = input("Which topping? ")
                
                while topping not in topping_choice_list:
                    topping_menu()
                    print("Invalid input. Please try again.")
                    topping = input("Which topping? ")
                
                if topping == "a":
                    topping_string += "Pepperoni "

                elif topping == "b":
                    topping_string += "Mushroom "

                elif topping == "c":
                    topping_string += "Olives "

                elif topping == "d":
                    topping_string += "Onions "

            
            topping_list.append("\b" + topping_string + "\n")
            topping_string = ""
            
            total_topping_price += num_topping * large_topping
    
        total_pizza_price += large * LARGE_PRICE

    
    
    
    
    
def receipt():
    global total_topping_price
    global total_pizza_price
    total_price_before_tax = 0
    tax = .075
    SODA_PRICE = 1.5
    CHEESECAKE_PRICE = 3.5
    CHOCOLATE_CAKE_PRICE = 4
    if total_pizza_price > 0:
        print()
        print("Pizza ordered: ")
        print()
        print(*topping_list) 
    if total_pizza_price > 0:
        print("Topping price:\t\t\t\t" + "$" + format((total_topping_price), ".2f"))
        print("Total pizza price:\t\t\t" + "$" + format((total_pizza_price), ".2f"))
        
    if num_soda > 0: 
        print("Total soda price:\t\t\t" + "$" + format((num_soda * SODA_PRICE), ".2f"))
    if int(cheesecake) > 0:
        print("Ordered " + str(cheesecake) + " cheesecake(s)\t\t\t" + "$"+ format((cheesecake * CHEESECAKE_PRICE),".2f"))
    if int(chocolate_cake) > 0:
        print("Ordered " + str(chocolate_cake) + " chocolate cake(s)\t\t" + "$" + format((chocolate_cake * CHOCOLATE_CAKE_PRICE), ".2f"))
    
    total_price_before_tax = total_topping_price + total_pizza_price + num_soda * SODA_PRICE + int(cheesecake) * CHEESECAKE_PRICE + int(chocolate_cake) * CHOCOLATE_CAKE_PRICE
    total_price_with_tax = total_price_before_tax * 1.075
    print()
    print("Subtotal:\t\t\t\t" + "$" + format(total_price_before_tax, ".2f" ))
    print("Plus 7.5% tax\t\t\t\t" + "$" + format(tax * total_price_before_tax, ".2f"))
    print("Total:\t\t\t\t\t" + "$" + format(total_price_with_tax, ".2f"))
    
    
    
def main():
    prices()
    menu()
    receipt()
    k = input("Press enter to exit!")
    
    
main()




