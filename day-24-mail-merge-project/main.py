
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()

with open("./Input/Names/invited_names.txt") as list:
    names_list = list.readlines()

for line in names_list:
    name = line.strip("\n")
    with open(f"./Output/ReadyToSend/invitation_{name}", "w") as invitation:
        invitation.write(letter_template.replace("[name]", name))
        continue
