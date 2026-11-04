# Run the Workout Assistant command-line application.

from workout_logger import prompt_for_workout, display_workout

# Keep the main menu open until the user exits.

while True:
    # Show the main menu.
    print("\nMain Menu\n")
    print("1. Start Workout")
    print("2. Exit")

    main_choice = input("\nChoose an option: ").strip()
    if main_choice == "1":

        # Collect details and create a workout.
        workout = prompt_for_workout()

        while True:

            # Show actions for the current workout.
            print("\nWorkout Menu\n")
            print("1. Add Exercise")
            print("2. View Workout")
            print("3. Finish Workout")

            workout_choice = input("\nChoose an option: ").strip()
            if workout_choice == "1":
                
                # Keep the exercise menu open until the exercise is finished.
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
                display_workout(workout)

            elif workout_choice == "3":
                print("Finishing Workout...")
                display_workout(workout)
                break

            else:
                print("\nInvalid option. Please enter a number from 1 to 3.\n")            



    elif main_choice == "2":
        break

    else:
        print("\nInvalid option. Please enter a number from 1 to 2.\n")
