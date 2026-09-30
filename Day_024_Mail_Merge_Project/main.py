# Day 24 - Mail Merge Project
PLACEHOLDER = "[name]"

# Read names
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()

        # Replace placeholder with actual name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create new personalized letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

print("Done! All letters created in Output/ReadyToSend/")