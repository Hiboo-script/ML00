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
	
	def printNames(self):
		for recipe in self.book:
			print(f"- {recipe}")		
	
	def recipeDetails(self, name):
		if name in self.book:
			print(f"details of {name}'s recipe :")
			recipe = self.book[name]
			for key, value in recipe.items():
				print(f"- {key} : {value}")
		else:
			print(f"There aren't {name} in this book.")
	
	def deleteRecipe(self, name):
		if name in self.book:
			del self.book[name]
		else:
			print(f"There aren't {name} in this book.")


cookbook = Book()

sandwich = Recipe('sandwich',['ham', 'bread', 'cheese', 'tomatoes'],'lunch',10)
cake = Recipe('cake',['floor', 'sugar', 'eggs'],'dessert',60)
salad = Recipe('salad',['avocado', 'arugula', 'tomatoes', 'spinach'],'lunch', 15)


cookbook.addRecipe(sandwich)
cookbook.addRecipe(cake)
cookbook.addRecipe(salad)

cookbook.printNames()
cookbook.deleteRecipe('salad')
cookbook.recipeDetails('salad')
