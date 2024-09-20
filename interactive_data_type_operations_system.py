# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice_one_counter = choice_two_counter = choice_three_counter = choice_four_counter = 0
while True:
    if choice_one_counter == 1 and choice_two_counter == 1 and choice_three_counter == 1 and choice_four_counter == 1:
        answer = input("You saw all four data types! Do you want to continue? Type Yes/No: ")
        if answer == "Yes":
            choice_one_counter = choice_two_counter = choice_three_counter = choice_four_counter = 0
            continue
        elif answer == "No":
            print("GOODBYE!")
            break
        else:
            print("INVALID ANSWER!")
            continue
    # Get the user's choice and store it in a variable
    choice = input("Enter the number of your choice (1-4): ")
    # If the user chooses Strings (choice == '1'):
    if choice == '1':
        choice_one_counter = 1
        print(f"You chose Strings!")
        # Declare a string variable, e.g., sentence = "Learning Python is fun!"
        sentence = "I am learning Python now!"
        print(f"Example sentence: {sentence}")
        # Extract and print a substring, such as the word "Python" from the sentence.
        print(f"Extracted word from index 14 to 19: {sentence[14:20]}")
        # Convert the entire sentence to uppercase and print it.
        print(f"Converted sentence to uppercase: {sentence.upper()}")
        # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
        replaced_word_in_sentence = sentence.replace("Python", "JS")
        print(f"Replaced word \"Python\": {replaced_word_in_sentence}")
        # Make a list from words in sentence:
        list_items_from_words = sentence.split()
        print(f"Words become list items: {list_items_from_words}")
        # Concatenate strings:
        first_word = "Python"
        second_word = "Fundamentals"
        print(f"Concatenate strings: \n* first word: {first_word}\n* second word: {second_word}"
              f"\n* first word + second word: "
              f"{first_word + second_word}")
    # If the user chooses Numbers (choice == '2'):
    elif choice == '2':
        choice_two_counter = 1
        print(f"You chose Numbers!")
        # Prompt the user to input two numbers, e.g., num1 and num2.
        first_num = int(input(f"Input first number: "))
        second_num = int(input(f"Input second number: "))
        # Perform and print the results of addition, subtraction, multiplication, and division.

        # Handle division by zero (e.g., print an error message if num2 is zero).

        # Perform a power operation, raising num1 to the power of num2, and print the result.

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        choice_three_counter = 1
        print(f"You chose Booleans!")
        # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
        is_python_easy = True
        is_python_difficult = False
        # Perform and print the results of logical operations: AND, OR, NOT.
        print(f"The result of NOT {is_python_difficult} is: {not is_python_difficult}")
        print(f"The result of NOT {is_python_easy} is: {not is_python_easy}")
        print(f"The result of {is_python_difficult} AND {is_python_difficult} is: "
              f"{is_python_difficult and is_python_difficult}")
        print(f"The result of {is_python_easy} AND {is_python_easy} is: {is_python_easy and is_python_easy}")
        print(f"The result of {is_python_difficult} AND {is_python_easy} is: {is_python_difficult and is_python_easy}")
        print(f"The result of {is_python_easy} AND {is_python_difficult} is: {is_python_easy and is_python_difficult}")
        print(f"The result of {is_python_difficult} OR {is_python_difficult} is: "
              f"{is_python_difficult or is_python_difficult}")
        print(f"The result of {is_python_easy} OR {is_python_easy} is: {is_python_easy or is_python_easy}")
        print(f"The result of {is_python_easy} OR {is_python_difficult} is: {is_python_easy or is_python_difficult}")
        print(f"The result of {is_python_difficult} OR {is_python_easy} is: {is_python_difficult or is_python_easy}")
        print(f"The result of NOT {is_python_difficult} AND {is_python_easy} OR {is_python_difficult}: "
              f"{not is_python_difficult and is_python_easy or is_python_difficult}")
        print(f"The result of NOT {is_python_difficult} AND {is_python_difficult} OR {is_python_difficult}: "
              f"{not is_python_difficult and is_python_difficult or is_python_difficult}")
        # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
        first_number = 10
        second_number = 5
        print(f"The result of {first_number} greater than {second_number} AND {second_number} equal to {second_number} "
              f"is: {first_number > second_number == second_number}")
        # {first_number > second_number and second_number == second_number}
        print(f"The result of {second_number} greater than {first_number} AND {second_number} equal to {second_number} "
              f"is: {first_number < second_number == second_number}")
        # {second_number > first_number and second_number == second_number}")
        print(f"Is {first_number} greater than {second_number}?: {first_number > second_number}")
        print(f"Is {second_number} greater than {first_number}?: {second_number > first_number}")
        print(f"Is {first_number} equal to {second_number}?: {first_number == second_number}")
        print(f"Is {first_number} not equal to {second_number}?: {first_number != second_number}")
        print(f"Is {second_number} greater than or equal to {first_number}?: {second_number >= first_number}")
        print(f"Is {first_number} greater than or equal to {second_number}?: {first_number >= second_number}")
    # If the user chooses Additional Data Types (choice == '4'):
    elif choice == '4':
        choice_four_counter = 1
        print(f"You chose Additional Data Types!")
        print("* List")
        print("* Tuple")
        print("* Dictionary")

    # ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans).

    # Append a new element to the list and print the updated list.

    # Access and print the 4th element in the list.

    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).

    # Print the length of the tuple.

    # Try to modify one element in the tuple and handle the resulting TypeError.

    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).

    # Access and print the value for one of the keys (e.g., "age").

    # Add a new key-value pair to the dictionary and print the updated dictionary.

    # If the user enters an invalid choice:
    else:
        # Print an error message indicating an invalid selection.
        print("INVALID SELECTION! Please choose a valid option between 1 and 5.")
        continue
