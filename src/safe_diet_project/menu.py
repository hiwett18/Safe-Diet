class EntireMenu:
    def __init__(self, breakfast=None, lunch=None, dinner=None):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
    

    def select_menu(self):
        which_menu = input('Would you like to have? 1. Breakfast, 2. Lunch, or 3. Dinner menu? Please input your number(1-3): ')
        while True: 
            try: 
                val = int(which_menu)
                if val > 0 and val < 4:
                    if val == 1: 
                        breakfast_menu = int(input('Breakfast Menu: 1. Oatmeal, 2. Scramble Egg with Vegi, 3. Pancake. Please make your breakfast selection using the number(1-3): '))
                        return breakfast_menu
                    elif val == 2: 
                        lunch_menu = int(input('Lunch Menu: 4. Quinoa Chicken Fried Rice, 5. BBQ Chicken Pita Pizza, 6. Pasta with Lean Protein and Veggies. Please make your lunch selection using the number(4-6):'))
                        return lunch_menu
                    elif val == 3: 
                        dinner_menu = int(input('Dinner Menu: 7. Spagetti Dish, 8. Salad Dish, 9. Fish with Veggi. Please make your dinner selection using the number(7-9):'))
                        return dinner_menu
                    break
                else:
                    print('Please try again')
                    which_menu = input('Would you like to have? 1. Breakfast, 2. Lunch, or 3. Dinner menu? Please input your number(1-3): ')
                    
            except ValueError:
                print("Choice must be a number, between 1-3") 
                which_menu = input('Would you like to have? 1. Breakfast, 2. Lunch, or 3. Dinner menu? Please input your number(1-3): ')  
                
        
   

# m1 = EntireMenu()
# print(m1.select_menu())
