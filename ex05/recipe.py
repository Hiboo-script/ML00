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
			print(f"Recipe {name} has been deleted !")
		else:
			print(f"There aren't {name} in this book.")
		
	def inputRecipe(self):
		name = ""
		ingredient = "cardamona"
		meal = ""
		prep_time = 0
		
		ingredients = []
		
		print("Insert your new recipe :")
		name = input("\nName of your recipe : \n")
		if not name:
			print("voidError : your recipe must be had a name !")
			return None
		
		print("\nIngredients of your recipe : ")
		while not not ingredient:
			ingredient=input("- ")
			if not not ingredient:
				ingredients.append(ingredient)
		if not ingredients:
			print("voidError : number of ingredients must be minimal 1 !")
			return None

		meal = input("\nWhat are your recipe meal type ? \n")
		if not meal:
			print("voidError : your recipe must had a meal type !")
			return None
		
		prep_time = input("\nHow long take your recipe (in minutes) ?\n")
		if not prep_time:
			print("voidError : your recipe must had a preparation time !")
			return None
		try:
			prep_time = int(prep_time)
		except:
			print("typeError : the preparation time must be a int !")
			return None

		newRecipe = Recipe(name,ingredients,meal,prep_time)
		self.addRecipe(newRecipe)
		
		print(f"Your new recipe {name} has been added : ")
		self.recipeDetails(name)

cookbook = Book()

sandwich = Recipe('sandwich',['ham', 'bread', 'cheese', 'tomatoes'],'lunch',10)
cake = Recipe('cake',['floor', 'sugar', 'eggs'],'dessert',60)
salad = Recipe('salad',['avocado', 'arugula', 'tomatoes', 'spinach'],'lunch', 15)

cookbook.addRecipe(sandwich)
cookbook.addRecipe(cake)
cookbook.addRecipe(salad)

str_start = "Welcome in cookbook python !"
str_menu = """\nList of available options :
	1 : Add a recipe
	2 : Delete a recipe 
	3 : Print a recipe
	4 : Print cookbook
	5 : Quit\n"""
str_invite = ">> "
str_errChoice = "errorOption : This option do not exist !"
str_nameRecipeGet = "Please enter a name of the recipe you want see :"
str_nameRecipeDel = "Please enter a name of the recipe you want delete :"
str_close = "\nGood bye !"
choice = 0
str_option = ""

print(str_start)
print(str_menu)
while choice!=5:
	choice = input(str_invite)
	try:
		choice = int(choice)
		if not (choice in set(range(1,6))):
			print(str_errChoice)
	except:
		print(str_errChoice)
	
	
	if choice==1:
		cookbook.inputRecipe()
		print(str_menu)
	elif choice==2:
		print(str_nameRecipeDel)
		str_option = input(str_invite)
		cookbook.deleteRecipe(str_option)
		print(str_menu)
	elif choice==3:
		print(str_nameRecipeGet)
		str_option = input(str_invite)
		cookbook.recipeDetails(str_option)
		print(str_menu)
	elif choice==4:
		cookbook.printNames()
		print(str_menu)
	elif choice==5:
		print(str_close)
