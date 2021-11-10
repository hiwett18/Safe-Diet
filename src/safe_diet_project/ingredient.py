from menu import EntireMenu

class Food:
    def __init__(self, food_ing=None):
        self.food_ing = food_ing
        

    def food_ingredeients(self):
        while True: 

            m2 = EntireMenu()
            selected_mn = m2.select_menu()
            val = int(selected_mn)
            
            oatmeal = ['oatmeal', 'milk', 'water', 'cinammon', 'strawberry','salt']
            egg = ['oil', 'egg', 'bell pepper', 'kale', 'spinach', 'salt']
            pancake = ['low carb pancake mix', 'egg', 'water', 'maple syrup']
            
            try: 
                if val >=1 and val <= 4:
                   
                    if val == 1:     
                        return oatmeal
                    elif val  == 2:
                        return egg
                    elif val  == 3:
                        return pancake 
                    break
                else:
                    print('Please try again')
                    
            except ValueError:
                print("Choice must be a number, between 1-3")   
        
        

            quinoa_chicken_fried_rice = ['oil', 'quinoa', 'carrots', 'peas', 'garlic', 'salt', 'red bell pepper', 'onion', 'egg', 'chicken']
            BBQ_Chicken_Pita_Pizza = ['whole-grain pita bread', 'low-sodium barbecue sause', 'onion', 'provolone', 'cooked chicken', 'garlic powder']
            Pasta_With_Lean_Protein_and_Veggies = ['white pasta', 'chicken', 'bell pepper', 'brussle sprout', 'carrots', 'onions', 'spinach', 'salt'] 
            
            try: 
                val1 = val
                if val1 >=4 and val <= 6:
                    if val1  == 4:
                        return quinoa_chicken_fried_rice
                    elif val1  == 5:
                        return BBQ_Chicken_Pita_Pizza
                    elif val1  == 6:
                        return Pasta_With_Lean_Protein_and_Veggies
                    break
                else:
                    print('Please try again')
                    
            except ValueError:
                print("Choice must be a number, between 4-6")   
                
        

            spagetti_dish = ['oil', 'onion', 'ground beef', 'tomato', 'salt', 'white pasta']
            salad_dish = ['lettus','spinach', 'bell peper', 'cucumber', 'onion', 'oil', 'salt', 'dressing']
            fish_with_veggi = ['fish', 'black paper', 'oil', 'salt', 'spinach'] 
            
            try: 
                val2 = val
                if val2 >=7 and val <= 9:
                    if val2 == 7:
                        return spagetti_dish
                    elif val2 == 8:
                        return salad_dish
                    elif val2 == 9:
                        return fish_with_veggi
                    break
                else:
                    print('Please try again')
                    
            except ValueError:
                print("Choice must be a number, between 7-9")   
                

       


# f1 = Food()
# print(f1.food_ingredeients())


           