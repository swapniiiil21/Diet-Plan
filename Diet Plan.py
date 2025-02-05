def load_data():
    print("Data loaded successfully!")

def main():
    load_data()
    print("👋 Welcome to the Advanced Calorie Tracker!")

    while True:
        print("\n📋 Choose an option:")
        print("1. Add a Meal")
        print("2. Edit a Meal")
        print("3. Delete a Meal")
        print("4. View Meals for a Date")
        print("5. Display Summary for a Date")
        print("6. Generate Weekly Calorie Trend")
        print("7. Create a Diet Plan")
        print("8. View Diet Plans")
        print("9. Recommend Calories for a Date")
        print("10. Calculate Calories for Weight Maintenance/Deficit")
        print("11. Save and Exit")
        
        choice = input("🔢 Enter your choice (1-11): ")

        if choice == "1":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            meal_name = input("🍴 Enter the meal name: ")
            try:
                calories = int(input("🔥 Enter the calories: "))
                add_meal(date, meal_name, calories)
            except ValueError:
                print("⚠️ Invalid calorie input. Please enter a valid number.")
        elif choice == "2":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            meal_name = input("🍴 Enter the meal name to edit: ")
            try:
                new_calories = int(input("🔥 Enter the new calorie value: "))
                edit_meal(date, meal_name, new_calories)
            except ValueError:
                print("⚠️ Invalid calorie input. Please enter a valid number.")
        elif choice == "3":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            meal_name = input("🍴 Enter the meal name to delete: ")
            delete_meal(date, meal_name)
        elif choice == "4":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            view_meals(date)
        elif choice == "5":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            display_summary(date)
        elif choice == "6":
            start_date = input("📅 Enter the start date (YYYY-MM-DD): ")
            end_date = input("📅 Enter the end date (YYYY-MM-DD): ")
            weekly_trend(start_date, end_date)
        elif choice == "7":
            name = input("📝 Enter the diet plan name: ")
            goal = input("🎯 Enter the goal (e.g., Weight Loss, Maintenance, Weight Gain): ")
            try:
                daily_calories = int(input("🔥 Enter daily calorie goal: "))
                create_diet_plan(name, goal, daily_calories)
            except ValueError:
                print("⚠️ Invalid calorie input. Please enter a valid number.")
        elif choice == "8":
            view_diet_plan()
        elif choice == "9":
            date = input("📅 Enter the date (YYYY-MM-DD): ")
            diet_plan_name = input("🍽️ Enter your diet plan name: ")
            recommend_calories(diet_plan_name, date)
        elif choice == "10":
            height = float(input("📏 Enter your height in cm: "))
            weight = float(input("⚖️ Enter your weight in kg: "))
            age = int(input("🎂 Enter your age: "))
            gender = input("♂️♀️ Enter your gender (male/female): ")
            activity_level = input("🏃 Enter your activity level (sedentary, light, moderate, active, very_active): ")
            calculate_calories(height, weight, age, gender, activity_level)
        elif choice == "11":
            save_data()
            print("🔒 Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Please choose a valid option (1-11).")

if __name__ == "__main__":
    main()
