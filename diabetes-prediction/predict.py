import pickle

# Load the model
with open("logreg.pkl", "rb") as pickle_in:
    model = pickle.load(pickle_in)


# Function to get user input and make prediction
def get_user_input():
    try:
        # Prompt the user to enter values separated by comma
        input_string = input("Enter values for the features separated by spaces: ")

        # Split the input string into individual values
        input_values = list(map(float, input_string.split(',')))

        # Ensure that exactly 8 values are provided
        if len(input_values) != 8:
            print("Please enter exactly 8 values.")
            return

        # Make prediction
        prediction = model.predict([input_values])
        print(f"The prediction is: {prediction[0]}")

    except ValueError:
        print("Please enter valid numerical values.")


get_user_input()

