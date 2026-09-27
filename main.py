# Workout Assistant

# Main Menu Loop

while True:
    # Main Menu
    print("\nMain Menu\n")
    print("1. Start Workout")
    print("2. Exit")

    main_choice = input("\nChoose an option: ").strip()
    if main_choice == "1":

        while True:

            # Workout Menu
            print("\nWorkout Menu\n")
            print("1. Add Exercise")
            print("2. View Workout")
            print("3. Finish Workout")

            workout_choice = input("\nChoose an option: ").strip()
            if workout_choice == "1":
                
                # Exercise Menu
                while True:

                    print("\nExercise Menu")
                    print("1. Add Set")
                    print("2. Finish Exercise")

                    exercise_choice = input("\nChoose an option: ").strip()
                    if exercise_choice == "1":
                        print("Adding Set...")

                    elif exercise_choice == "2":
                        break

                    else:
                        print("\nInvalid option. Please enter a number from 1 to 2.\n")


            elif workout_choice == "2":
                print("Viewing Workout...")

            elif workout_choice == "3":
                print("Finishing Workout...")
                break

            else:
                print("\nInvalid option. Please enter a number from 1 to 3.\n")            



    elif main_choice == "2":
        break

    else:
        print("\nInvalid option. Please enter a number from 1 to 2.\n")
