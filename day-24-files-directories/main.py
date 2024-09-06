# file = open("my.txt")
# content = file.read()
# print(content)
# file.close()


# here file automatically closes at the end of the indent
with open("my.txt", mode="a") as file:
    file.write("New text.")
    contents = file.read()
    print(contents)