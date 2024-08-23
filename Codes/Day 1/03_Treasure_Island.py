# Header
# this ascii art is from the site https://ascii.co.uk/art/treasureisland
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

#logic
while True:
    # First Question
    first_Q = input('Turn left or right? ').lower()
    if first_Q == 'right':
        print('Game over.')
        break
    elif first_Q == 'left':
        # Second Question
        second_Q = input('Swim or wait? ').lower()
        if second_Q == 'swim':
            print('Game over.')
            break
        elif second_Q == 'wait':
            # Third Question
            third_Q = input('Which door? (Red, Blue, Yellow) ').lower()
            if third_Q == 'red' or third_Q == 'blue':
                print('Game over.')
                break
            elif third_Q == 'yellow':
                print('You win!')
                break
            else:
                print("Invalid choice, please choose 'Red', 'Blue', or 'Yellow'.")
        else:
            print("Invalid choice, please choose 'Swim' or 'Wait'.")
    else:
        print("Invalid choice, please choose 'Left' or 'Right'.")
