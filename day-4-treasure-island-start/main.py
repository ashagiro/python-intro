print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\\n \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\\n \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
print("You arrived at the entrance of an island and found a mysterious map.")
print(
    "You decided to follow the map and you came across a fork in the road.\nTurn left to choose faster but dangerous route, turn right to choose slower but steady route."
)
choice1 = input('Where do you want to go?\nType left or right\n')
if choice1.lower() == "left":
    print("You continued walking and found a river.")
    choice2 = input(
        "Do you want to swim across or wait for a boat?\nType swim or wait.\n")
    if choice2.lower() == "wait":
        print(
            "You successfully arrived at the bank of the river and continued to follow the map"
        )
        choice3 = input(
            "You found a house with three doors. One red, one yellow and one blue. Which color do you choose?\nType red, yellow or blue.\n"
        )
        if choice3.lower() == "red":
            print("You entered a room full of snakes.\nGame Over")
        elif choice3.lower() == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("You entered a room full of insects.\nGame Over")
    else:
        print("You were attacked by a tout.\nGame Over.")
else:
    print("You fell off the cliff and died.\nGame Over.")
