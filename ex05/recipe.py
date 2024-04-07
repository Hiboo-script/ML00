cookbook = dict()
recipe = dict(ingredients = list(),meal = str(),prep_time = int())

sandwich = recipe.copy()
sandwich['ingredients'] = ['ham', 'bread', 'cheese', 'tomatoes']
sandwich['meal'] = 'lunch'
sandwich['prep_time'] = 10

cake = recipe.copy()
cake['ingredients'] = ['floor', 'sugar', 'eggs']
cake['meal'] = 'dessert'
cake['prep_time'] = 60

salad = recipe.copy()
salad['ingredients'] = ['avocado', 'arugula', 'tomatoes', 'spinach']
salad['meal'] = 'lunch'
salad['prep_time'] = 15 


cookbook['sandwich'] = sandwich
cookbook['cake'] = cake
cookbook['salad'] = salad

print(cookbook)
