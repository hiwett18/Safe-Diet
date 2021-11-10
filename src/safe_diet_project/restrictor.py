from patients import PatientType
from menu import EntireMenu
from ingredient import Food 

# p1 = PatientType()
# selected_patient = p1.select_patient()

class Restriction:
    def __init__(self, selected_patient=None, selected_food=None):
        self.selected_patient = selected_patient
        self.selected_food = selected_food 


    def food_restriction(self):
        if (self.selected_patient == 'hypertension patient'):
            ingredient_to_avoid1 = 'salt'
            if ingredient_to_avoid1 in self.selected_food: 
                self.selected_food.remove(ingredient_to_avoid1)
            return self.selected_food
            
            
        elif (self.selected_patient == 'diabetic patient'):
            ingredient_to_avoid1 = 'white pasta'
            if ingredient_to_avoid1 in self.selected_food: 
                self.selected_food.remove(ingredient_to_avoid1)

            elif 'maple syrup' in self.selected_food: 
                self.selected_food.remove('maple syrup')
            
            elif 'dressing' in self.selected_food:
                self.selected_food.remove('dressing')

            return self.selected_food
           
        
        elif (self.selected_patient == 'kidney patient'):
            ingredient_to_avoid1 = 'spinach'
            if ingredient_to_avoid1 in self.selected_food: 
                self.selected_food.remove(ingredient_to_avoid1)
            elif 'tomato' in self.selected_food: 
                self.selected_food.remove('tomato')
            return self.selected_food
            
           

       

# r1 = Restriction()
# print(r1.food_restriction())