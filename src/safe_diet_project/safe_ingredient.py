from patients import PatientType
from menu import EntireMenu
from ingredient import Food 
from restrictor import Restriction



p1 = PatientType()
patient = p1.select_patient()
print(patient)


f1 = Food()
food = f1.food_ingredeients()
food1 = food[:]


r1 = Restriction(patient, food1)
safe_ingredients = r1.food_restriction()


ommited_ingredient = '' 
for unwanted_ingrid in food:
    if unwanted_ingrid not in safe_ingredients:
        ommited_ingredient = unwanted_ingrid
         
       
        
if len(ommited_ingredient) == 0:
    ommited_ingredient = "nothing is ommited from your food. Your ingriedients are safe to eat"



print("--------------------------------------------------------------------------------------------")
print(f'Since you are {patient}, please avoid adding: {ommited_ingredient}') 
print("--------------------------------------------------------------------------------------------")
print(f'Your safe ingriedient list is: {safe_ingredients}')
print("--------------------------------------------------------------------------------------------")
print(f'Omitted ingredient: {ommited_ingredient}')
print("--------------------------------------------------------------------------------------------")
print(f'(Original ingredient list: {food})')
print("--------------------------------------------------------------------------------------------")

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'white pasta':
        safe_ingredients.append('whole-grain pasta')
        print('Suggestion:\n White pasta is high in carb.\n Substitute white pasta with whole-grain pasta. \n Your updated ingredient list is: ', safe_ingredients)

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'maple syrup':
        safe_ingredients.append('Raw honey')
        print('Suggestion:\n Maple syrup is high in carb.\n Substitute maple syrup with Raw honey. \n Your updated ingredient list is: ', safe_ingredients)

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'dressing':
        safe_ingredients.append('olive oil and vinegar dressing')
        print('Suggestion:\n Dressing is high in carb.\n Substitute dressing with olive oil and vinegar dressing. \n Your updated ingredient list is: ', safe_ingredients)

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'salt':
        safe_ingredients.append('Mrs Dash')
        print('Suggestion:\n Salt will increase your blood presssure.\n Substitute salt with Mrs Dash.\n Your updated ingredient list is: ', safe_ingredients)

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'spinach':
        safe_ingredients.append('Arugula')
        print('Suggestion:\n Spinach is high in potassium.\n Substitute spinach with arugula.\n Your updated ingredient list is: ', safe_ingredients)

if len(ommited_ingredient) > 1: 
    if ommited_ingredient == 'tomato':
        safe_ingredients.append('broccoli')
        print('Suggestion:\n Tomato is high in potassium.\n Substitute tomato with broccoli.\n Your updated ingredient list is: ', safe_ingredients)

print("----------    ----------    ----------      //      ----------    ----------     ---------- ")
print("--------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------")
