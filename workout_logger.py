from datetime import datetime


#Workout creation function.
def prompt_for_workout():

    while True:
        date = input("Enter workout date (YYYY-MM-DD): ").strip()

        # Validate input.
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
        # Handle invalid dates.
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
            continue

        if parsed_date.strftime("%Y-%m-%d") == date:
            break

        # Handle invalid formatting.
        print("Please use YYYY-MM-DD format, including leading zeros.")

    while True:
        day_type = input("Enter training day type: ").strip().upper()

        #Handle empty input.
        if day_type:
            break
        
        print("Please enter a training day type.")

    while True:
        length = input("Enter workout length (in minutes): ")

        # Validate input.
        try:
            length = int(length)
        # Handle input that is not a whole number.
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length > 0:
            break

        # Handle zero or negative values.
        print("Workout length must be greater than 0.")

    while True:
        energy = input("Enter energy level (from 1 to 10): ")

        # Validate input.
        try:
            energy = int(energy)
        # Handle input that is not a whole number.
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 1 <= energy <= 10:
            break

        print("Energy level must be between 1 and 10.")

    return create_workout(date, day_type, length, energy)

def create_workout(date, day_type, length, energy):

    if not 1 <= energy <= 10:
        raise ValueError("Energy level must be between 1 and 10.")

    if length <= 0:
        raise ValueError("Length must be greater than 0.")

    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    if parsed_date.strftime("%Y-%m-%d") != date:
        raise ValueError("Date must be in YYYY-MM-DD format.")    

    day_type = day_type.strip().upper()
    if not day_type:
        raise ValueError("Day type must be provided.")

    workout = {
            "Date": date,
            "Day Type": day_type,
            "Workout Length": length,
            "Energy": energy
        }

    return workout

# View workout function.
def display_workout(workout):
    for key, value in workout.items():
        print(f"{key}: {value}")
