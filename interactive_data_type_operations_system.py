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
        elif answer == "No":
            print("GOODBYE!")
            break
        else:
            print("INVALID ANSWER! Type only Yes or No.")
            continue
    # Get the user's choice and store it in a variable
    choice = input("Enter the number of your choice (1-4): ")
    # If the user chooses Strings (choice == '1'):
    if choice == '1':
        choice_one_counter = 1
        print("****** You chose Strings! ******")
        print()
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
        print("****** You chose Numbers! ******")
        print()
        # Prompt the user to input two numbers, e.g., num1 and num2.
        while True:
            try:
                first_num = int(input(f"Input first number: "))
                second_num = int(input(f"Input second number: "))
                # Perform and print the results of addition, subtraction, multiplication, division and modular division.
                print(f"Addition: {(first_num + second_num):.1f}")
                print(f"Subtraction: {(first_num - second_num):.1f}")
                print(f"Multiplication: {(first_num * second_num):.1f}")
                # # Handle division by zero (e.g., print an error message if num2 is zero).
                # try:
                #     print(f"Division: {(first_num / second_num):.1f}")
                #     break
                # except ZeroDivisionError:
                #     print("ERROR! You cannot divide by zero!")
                #     # Perform a power operation, raising num1 to the power of num2, and print the result.
                #     print(f"{first_num} raised to the power of {second_num} is: {(first_num ** second_num):.1f}")
                # Handle division by zero (e.g., print an error message if num2 is zero).
                if second_num != 0:
                    print(f"Subtraction: {(first_num / second_num):.1f}")
                    print(f"Modular divisions: {(first_num % second_num):.1f}")
                    break
                elif second_num == 0:
                    print(f"INVALID SECOND NUMBER! You cannot divide by zero!")
                    # Perform a power operation, raising num1 to the power of num2, and print the result.
                    print(f"{first_num} raised to the power of {second_num} is: {(first_num ** second_num):.1f}")
            except ValueError:
                print("ERROR! Please enter valid numeric values.")
        # Perform a power operation, raising num1 to the power of num2, and print the result.
        print(f"{first_num} raised to the power of {second_num} is: {(first_num ** second_num):.1f}")
    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        choice_three_counter = 1
        print("****** You chose Booleans! ******")
        print()
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
        print("****** You chose Additional Data Types! ******")
        print()
        print("****** List ******")
        # Create a list with mixed data types (e.g., numbers, strings, booleans).
        list_of_mixed_data_types = [1, "Python", True, 2, False, 3]
        print(f"Example List: {list_of_mixed_data_types}")
        # Append a new element to the list and print the updated list.
        list_of_mixed_data_types.append("JS")
        print(f"Updated List with a new added element: {list_of_mixed_data_types}")
        # Access and print the 4th element in the list.
        print(f"The 4th element in the new List is: {list_of_mixed_data_types[3]}")
        # Print the index of element True and False.
        index_of_true = next(i for i, x in enumerate(list_of_mixed_data_types) if x is True and type(x) is bool)
        index_of_false = next(i for i, x in enumerate(list_of_mixed_data_types) if x is False and type(x) is bool)
        print(f"The index of element True is: {index_of_true}")
        print(f"The index of element False is: {index_of_false}")
        # Print the index of element 2 and "Python".
        print(f"The index of element 2 is: {list_of_mixed_data_types.index(2)}")
        index_of_python = list_of_mixed_data_types.index("Python")
        print(f"The index of element \"Python\" is: {index_of_python}")
        # Change the last item and fifth item:
        list_of_mixed_data_types[-1] = "C#"
        print(f"Updated List with replaced \"JS\" element to \"C#\" is: {list_of_mixed_data_types}")
        list_of_mixed_data_types[4] = True
        print(f"Updated List with replaced False element to True is: {list_of_mixed_data_types}")
        # Remove C# and True:
        list_of_mixed_data_types.remove("C#")
        # list_of_mixed_data_types = [1, "Python", True, 2, True, 3]
        list_of_mixed_data_types.pop(2)
        # list_of_mixed_data_types = [1, "Python", 2, True, 3]
        list_of_mixed_data_types.pop(3)
        print(f"Updated List with removed elements \"C#\" and True is: {list_of_mixed_data_types}")
        print()
        print("****** Tuple ******")
        # Create a tuple with some string elements (e.g., fruits).

        # Print the length of the tuple.

        # Try to modify one element in the tuple and handle the resulting TypeError.

        print("****** Dictionary ******")
        print()
    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).

    # Access and print the value for one of the keys (e.g., "age").

    # Add a new key-value pair to the dictionary and print the updated dictionary.

    # If the user enters an invalid choice:
    else:
        # Print an error message indicating an invalid selection.
        print("INVALID SELECTION! Please choose a valid option between 1 and 5.")
        continue
