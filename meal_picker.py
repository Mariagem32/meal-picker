import random

meals = ["Pasta", "Stir-fry", "Soup", "Tacos", "Omelette"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if len(meals) < 5:
    print("Add at least five meals to your list.")
else:
    weekly_meals = random.sample(meals, 5)

    print("Your meal plan:")
    for day, meal in zip(days, weekly_meals):
        print(day + ": " + meal)
