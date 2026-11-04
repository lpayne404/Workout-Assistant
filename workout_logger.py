from datetime import datetime


# Collect and validate workout details from the user.
def prompt_for_workout():

    while True:
        date = input("Enter workout date (YYYY-MM-DD): ").strip()

        # Parse the input to check that it is a valid date.
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        # Ask again if the date is invalid.
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
            continue

        if parsed_date.strftime("%Y-%m-%d") == date:
            break

        # Ask for leading zeros when the date format is incorrect.
        print("Please use YYYY-MM-DD format, including leading zeros.")

    while True:
        day_type = input("Enter training day type: ").strip().upper()

        # Accept the day type only when it is not empty.
        if day_type:
            break
        
        print("Please enter a training day type.")

    while True:
        length = input("Enter workout length (in minutes): ")

        # Convert the input to a whole number.
        try:
            length = int(length)
        # Ask again if the input is not a whole number.
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length > 0:
            break

        # Ask again if the length is zero or negative.
        print("Workout length must be greater than 0.")

    while True:
        energy = input("Enter energy level (from 1 to 10): ")

        # Convert the input to a whole number.
        try:
            energy = int(energy)
        # Ask again if the input is not a whole number.
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 1 <= energy <= 10:
            break

        print("Energy level must be between 1 and 10.")

    return create_workout(date, day_type, length, energy)

def create_workout(date, day_type, length, energy):

    # Validate values here too, so calls outside the input prompts are checked.
    # Raising ValueError stops the function and reports an invalid value to the caller.
    if not 1 <= energy <= 10:
        raise ValueError("Energy level must be between 1 and 10.")

    if length <= 0:
        raise ValueError("Length must be greater than 0.")

    # Parse the date to check that it exists; strptime raises ValueError if it doesn't.
    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    # Convert the date back to text to check the format and leading zeros.
    if parsed_date.strftime("%Y-%m-%d") != date:
        raise ValueError("Date must be in YYYY-MM-DD format.")    

    # Remove surrounding whitespace and use consistent capitalization.
    day_type = day_type.strip().upper()
    if not day_type:
        raise ValueError("Day type must be provided.")

    # Group the validated values in a dictionary with descriptive keys.
    workout = {
            "date": date,
            "day_type": day_type,
            "duration_minutes": length,
            "energy": energy
        }

    # Give the completed dictionary back to the code that called this function.
    return workout

# Display each workout detail using its dictionary key as a label.
def display_workout(workout):
    for key, value in workout.items():
        print(f"{key}: {value}")
