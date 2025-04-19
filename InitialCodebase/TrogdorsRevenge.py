# define player starting room and variable to store inventory, starts off empty
currentRoom = 'Gatehouse'
inventory = []

# function  showing Welcome text,  game instructions, and objective
def show_instructions():
    print('-+-+-+-+- Welcome to Trogdor\'s Revenge! -+-+-+-+-')
    print()
    print('Trogdor, the mighty dragon, lurks somewhere in the castle. You will need the aid of six powerful items to defeat him!')
    print('Find all six items before you encounter Trogdor to win')
    print('If you find Trogdor before you find all six items, you will surely perish...')
    print()
    print('Move between rooms by entering one of the following directions: North, South, East, West')
    print('If you see an item, enter the item name to add it to your inventory')
    print('Type exit to leave the game')
    print()
    print('-' * 50)
    print()

# function will display the dragon when you find Trogdor
# found this ASCII dragon online and converted it to print statements
def trogdor():
    print('             |\___/|')
    print("            (,\  /,)\\")
    print('            /     /  \\')
    print('           (@_^_@)/   \\')
    print('            W//W_/     \\')
    print('          (//) |        \\')
    print('        (/ /) _|_ /   )  \\')
    print('      (// /) \'/,_ _ _/  (~^-.')
    print('    (( // )) ,-{        _    `.')
    print('   (( /// ))  \'/\      /      |')
    print('   (( ///))     `.   {       }')
    print('    ((/ ))    .----~-.\   \-''')
    print('             ///.----..>   \\')
    print('              ///-._ _  _ _}')


# main function
def main():

    # function that shows what room you are in and what is in your inventory
    def showStatus():
        print('You are in the {}'.format(currentRoom))
        print('Inventory: ', inventory)

    # The dictionary links a room to other rooms, based on my map from previous assignment.
    rooms = {

        'Gatehouse': {'West': 'Grand Staircase', 'item': ''},
        'Grand Staircase': {'East': 'Gatehouse', 'South': 'Dining Hall', 'item': 'Enchanted Armor'},
        'Dining Hall': {'North': 'Grand Staircase', 'East': 'Barracks', 'South': 'Library', 'West': 'Living Quarters', 'item': 'Shield'},
        'Living Quarters': {'East': 'Dining Hall', 'item': 'Hero\'s Bow'},
        'Library': {'North': 'Dining Hall', 'East': 'Observatory', 'item': 'Book of Dragons'},
        'Observatory': {'West': 'Library', 'item': 'Arrows'},
        'Barracks': {'North': 'Hidden Dungeon', 'West': 'Dining Hall', 'item': 'Knight\'s Longsword'},
        'Hidden Dungeon': {'South': 'Barracks'},
    }

    currentRoom = 'Gatehouse'
    inventory = []

    # define valid commands -- directions to move, or items available to pickup
    validDirections = ('North', 'East', 'South', 'West')
    validItems = ('Enchanted Armor', 'Shield', 'Hero\'s Bow', 'Book of Dragons', 'Arrows', 'Knight\'s Longsword')

    # call function to show player the instructions when the game starts
    show_instructions()

    # game loop
    while currentRoom != 'exit':
        # call function to display current room and inventory
        showStatus()
        # displays what items are in the current room
        # if you've already picked up the item, it will no longer display in the room
        if currentRoom == "Grand Staircase" and 'Enchanted Armor' not in inventory:
            print('* You see the Enchanted Armor')
            print()
        elif currentRoom == 'Dining Hall' and 'Shield' not in inventory:
            print('* You see the Shield')
            print()
        elif currentRoom == 'Living Quarters' and 'Hero\'s Bow' not in inventory:
            print('* You see the Hero\'s Bow')
            print()
        elif currentRoom == 'Barracks' and 'Knight\'s Longsword' not in inventory:
            print('* You see the Knight\'s Longsword')
            print()
        elif currentRoom == 'Library' and 'Book of Dragons' not in inventory:
            print('* You see the Book of Dragons')
            print()
        elif currentRoom == 'Observatory' and 'Arrows' not in inventory:
            print('* You see the Arrows')
            print()
        # Boss room. If you get here and your inventory has 6 items, you will win. If not 6, you will lose.
        # Game ends after either condition
        elif currentRoom == 'Hidden Dungeon':
            # win
            if len(inventory) == 6:
                print('>> You\'ve found Trogdor!')
                print()
                # call function to display the dragon!
                trogdor()
                print()
                print('>> With the help of the items you\'ve found in your travels, you are victorious in battle.')
                print('>> You win, congratulations!!')
                print('>> Game over')
                break
            # lose
            else:
                print('>> You\'ve found Trogdor!')
                print()
                # call function to display the dragon!
                trogdor()
                print()
                print('>> You fight valiantly, but you are no match and are eaten by the mighty dragon...')
                print('>> You lose')
                print('>> Game Over')
                break


        # Get user input for next move
        directionCommand = input('Choose your next move: ')

        # If user input is "exit", set currentRoom to exit which moves program to next while loop and ends the game
        if directionCommand == 'exit':
            currentRoom = 'exit'

        # if user input is anything other than a valid direction or valid item, shows "invalid command"
        elif directionCommand not in validDirections and directionCommand not in validItems:
            print('>> Invalid command')
            print()

        # If the input is a valid direction from the current room based on the dictionary, move to the new room and update currentRoom
        elif directionCommand in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][directionCommand]
            print()
            print('>> Traveling to the {}'.format(currentRoom))
            print()
            print('-' * 50)
            print()
        # user enters a valid direction, but it is not accessible from the current room
        elif directionCommand in validDirections:
            if directionCommand not in rooms[currentRoom]:
                print()
                print('>> Ouch! You hit a wall. Try another direction.')
                print()
        # user tries to enter an item already in their inventory from the current room
        elif directionCommand in rooms[currentRoom]['item']:
            if rooms[currentRoom]['item'] in inventory:
                print('>> You already picked up this item!')
            # if not in inventory, player picks up item and adds to inventory
            else:
                inventory.append(rooms[currentRoom]['item'])
                print('>> You picked up the {}'.format(rooms[currentRoom]['item']))
                # lets player know they have collected all of the items and are ready to fight the Boss
                if len(inventory) == 6:
                    print('>> You have found all of the items.')
                    print('>> You now have the strength to defeat Trogdor!')
            print()
            print('-' * 50)
            print()
        # user tries to pickup a valid item from another room
        elif directionCommand in validItems:
            if directionCommand not in rooms[currentRoom]['item']:
                print()
                print('>> You cannot pick this item up. Perhaps it is in another room...')
                print()
                print('-' * 50)
        else:
            print()
            print(">> Invalid move or command")
            print()
            print('-' * 50)
            print()
        # Loops until player inputs "exit", which sets currentRoom to 'exit' and goes to next while loop below

    # Ends the game when currentRoom is the 'exit' room, with a goodbye message
    while currentRoom == 'exit':
        print('>> Goodbye and thanks for playing!')
        break

main()
