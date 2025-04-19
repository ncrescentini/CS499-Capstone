import time
import sqlite3      # ENHANCEMENT 3 - import needed for save/load game functionality

# function showing Welcome text,  game instructions, and objective
# to be used in menu option 3
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

# function will display the dragon art when you find Trogdor
def trogdor():
    print()
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
    print()

def victory_knight():
    art = r"""
      / |
     |.|
     |.|
     |.|
     |:|      __
  ,_|:|_,   /  )
   (Oo     / _I_
    +\ \   || __|
       \ \ ||___|
         \ /.:.\-\
          |.:. /-----\
          |___|::oOo::|
          /   |:<_T_>:|
         |_____\ ::: /
          | |  \ \:/
          | |   | |
          \ /   | \___
          / |   \_____\
          `-'
    """
    print(art)
def start_menu():
    while True:
        print("=" * 50)
        print("\t\t   Welcome to Trogdor's Revenge")
        print("=" * 50)
        print("1. Start New Game")
        print("2. Load Game")
        print("3. How to Play")
        print("4. Exit")
        print()

        choice = input("Enter your selection (1-4): ")

        if choice == '1':
            print("\n>> Starting a new game...\n")
            return 'new'  # starts a new game
        elif choice == '2':
            print("\n>> Load game selected...\n")
            return 'load'  # enhancement 3
        elif choice == '3':
            show_instructions()
        elif choice == '4':
            print("\n>> Goodbye, brave adventurer!\n")
            exit()
        else:
            print("\n>> Invalid choice. Please enter 1, 2, 3, or 4.\n")

    # ENHANCEMENT 3
    # function to save the current game
    # saves current room and inventory to a SQLite Database
def save_game(currentRoom, inventory):
    conn = sqlite3.connect("trogdor_save.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS save_game")
    cursor.execute("CREATE TABLE save_game (current_room TEXT, inventory TEXT)")
    inventory_str = ",".join(inventory)
    cursor.execute("INSERT INTO save_game (current_room, inventory) VALUES (?, ?)", (currentRoom, inventory_str))
    conn.commit()
    conn.close()
    print(">> Game saved.\n")

    # ENHANCEMENT 3
    # function to load a saved game
    # loads save room and inventory from SQLite Database
def load_game():
    conn = sqlite3.connect("trogdor_save.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT current_room, inventory FROM save_game")
        row = cursor.fetchone()
        if row:
            currentRoom = row[0]
            inventory = row[1].split(",") if row[1] else []
            print(">> Game loaded.\n")
            return currentRoom, inventory
        else:
            print(">> No saved game found.\n")
            return None, None
    except sqlite3.OperationalError:
        print(">> No saved game found.\n")
        return None, None
    finally:
        conn.close()

def run_game(currentRoom = 'Gatehouse', inventory = None): # ENHANCEMENT 3 -- allow start from saved game
    if inventory is None:
        inventory= []

    # function that shows what room you are in and what is in your inventory
    def showStatus():
        print('You are in the {}'.format(currentRoom))
        print('Inventory: ', inventory)

    # The dictionary links a room to other rooms and the items contained within
    # ENHANCEMENT 2 cleanup - reformat dictionary for enhanced readability and maintainability
    rooms = {
        'Gatehouse': {
            'West': 'Grand Staircase',
            'item': ''
        },
        'Grand Staircase': {
            'East': 'Gatehouse',
            'South': 'Dining Hall',
            'item': 'Enchanted Armor'
        },
        'Dining Hall': {
            'North': 'Grand Staircase',
            'East': 'Barracks',
            'South': 'Library',
            'West': 'Living Quarters',
            'item': 'Shield'
        },
        'Living Quarters': {
            'East': 'Dining Hall',
            'item': "Hero's Bow"
        },
        'Library': {
            'North': 'Dining Hall',
            'East': 'Observatory',
            'item': 'Book of Dragons'
        },
        'Observatory': {
            'West': 'Library',
            'item': 'Arrows'
        },
        'Barracks': {
            'North': 'Hidden Dungeon',
            'West': 'Dining Hall',
            'item': "Knight's Longsword"
        },
        'Hidden Dungeon': {
            'South': 'Barracks'
        }
    }
    # define valid commands -- directions to move, or items available to pickup
    validDirections = ('North', 'East', 'South', 'West')
    validItems = ('Enchanted Armor', 'Shield', 'Hero\'s Bow', 'Book of Dragons', 'Arrows', 'Knight\'s Longsword')

    # game loop
    while currentRoom != 'exit':
        # call function to display current room and inventory
        showStatus()
        room_item = rooms[currentRoom].get('item')

        # Main feature of Enhancement #2 - new inventory management algorithm
        # Replaces long hardcoded if/else block
        # Displays what items are in the current room
        # If you've already picked up the item, it will no longer display in the room
        if room_item and room_item not in inventory:
            print(f'* You see the {room_item}')
            print()

        # Boss room. If you get here and your inventory has 6 items, you will win. If not 6, you will lose.
        # Game ends after either condition
        if currentRoom == 'Hidden Dungeon':
            # win
            if len(inventory) == 6:
                print('>> You\'ve found Trogdor!')
                print('>> With the help of the items you\'ve found in your travels, you are victorious in battle.')
                victory_knight() # You stand victorious with this glorious art!
                print('>> You win, congratulations!!')
                print('>> Game over')
                break
            # lose
            else:
                print('>> You\'ve found Trogdor!')
                trogdor()   # Reveals Trogdor art after finding the Hidden Dungeon. He kills you :(
                print('>> You fight valiantly, but you are no match and are eaten by the mighty dragon...')
                print('>> You lose')
                print('>> Game Over')
                break

        # Get user input for next move
        directionCommand = input('Choose your next move: ')


        # If user input is "exit", set currentRoom to exit which moves program to next while loop and ends the game
        if directionCommand == 'exit':
            currentRoom = 'exit'

        # ENHANCEMENT 3 - saves current game status if user types "save"
        elif directionCommand == 'save':
            save_game(currentRoom, inventory)

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
                # lets player know they have collected all the items and are ready to fight the Boss
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


# updated main function
def main():
    while True:
        choice = start_menu()

        if choice == 'new':
            run_game()
            break
        elif choice == 'load':      # ENHANCEMENT 3
            currentRoom, inventory = load_game()
            if currentRoom:
                run_game(currentRoom,inventory)
            else:
                print("Returning to main menu")
            time.sleep(3)
main()
