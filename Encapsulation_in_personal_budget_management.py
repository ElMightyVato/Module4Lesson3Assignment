class Budget:
    def __init__(self, category_name, allocated_budget): # Function to initialize category name and allocated budget
        self.__category_name = category_name  # private attribute for category name
        self.__allocated_budget = allocated_budget  # private attribute for allocated budget
        self.__remaining_budget = allocated_budget  # private attribute to track remaining budget

    def get_category_name(self): # our getter for category name
        return self.__category_name

    def set_category_name(self, name): # Our setter for category name
        self.__category_name = name

    def get_allocated_budget(self): # Getter for allocated budget
        return self.__allocated_budget

    def set_allocated_budget(self, budget): # Setter for allocated budget
        if budget > 0: # we want to make sure the number is positive
            self.__allocated_budget = budget
            self.__remaining_budget = budget  
        else:
            print("Budget must be a positive number.")

    def get_remaining_budget(self): # Getter for the remaining budget I didn't create a setter since the code doesn't directly modify it.
        return self.__remaining_budget

    def add_expense(self, amount): # method to add an expense to the category
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            print("Invalid expense amount. Make sure it's positive and within the remaining budget.")

    def display_category_summary(self): # our method to display our details
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")
    

# Examples of code being utilized
Game_collection = Budget("Devil May Cry ", 500)
Game_collection.add_expense(32)
Game_collection.display_category_summary()

# Attempting to get an invalid response
Game_collection.add_expense(600)

# Updating the budget and displaying the updated one
Game_collection.set_allocated_budget(600)
Game_collection.display_category_summary()
