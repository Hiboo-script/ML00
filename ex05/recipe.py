class Recipe:
	def __init__(self, name, ingredients, meal, prep_time):
		self.name = name
		self.recipe = dict(ingredients = ingredients, meal = meal,prep_time = prep_time)
	
	def getName(self):
		return self.name
	
	def get(self):
		return self.recipe


class Book:
	def __init__(self):
		self.book = dict()

	def addRecipe(self, recipe):
		self.book[recipe.getName()] = recipe.get()

	def print(self):
		print(self.book)		


cookbook = Book()

sandwich = Recipe('sandwich',['ham', 'bread', 'cheese', 'tomatoes'],'lunch',10)
cake = Recipe('cake',['floor', 'sugar', 'eggs'],'dessert',60)
salad = Recipe('salad',['avocado', 'arugula', 'tomatoes', 'spinach'],'lunch', 15)


cookbook.addRecipe(sandwich)
cookbook.addRecipe(cake)
cookbook.addRecipe(salad)

cookbook.print()
