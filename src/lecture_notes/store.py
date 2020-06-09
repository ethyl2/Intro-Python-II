from category import Category

class Store:
    # attributes 
    # name
    # categories (departments)

    # constructor - the function that runs every time you create a new instance
    # self refers to the current instance of the class (in JS the word is "this")
    def __init__(self, name, categories):
        self.name = name    
        self.categories = categories
    
    def __str__(self):
        # return a string representing the store
        output = f"Welcome to {self.name}!"
        i = 1 
        for category in self.categories:
            output += f'\n {i}. {category.name}'
            i += 1
        return output

    def __repr__(self):
        # also returns a string which helps developers understand how your object is structured
        return f"self.name = {self.name} ; self.categories = {self.categories}" 
    


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Blue Jays Fans only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The american kind", [])
soccer_category = Category("Soccer", "The real football", [])


sports_store = Store("Gander Mountain", [running_category, baseball_category, basketball_category, football_category, soccer_category])
choice = -1
# REPL <- Read Evaluate Print Loop
print(sports_store)
print("type q to quit")
while True:
    # Read 
    choice = input("Please choose a category (#): ")
    try:
        # Evaluate 
        if (choice == 'q'):
            break
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
            # Print
            print(chosen_category)
        else:
            print("The number is out of range")

    except ValueError:
        print("Please enter a valid number")    


