import addComputer
import pickle
from addComputer import lookup,add,change,delete,printAll,save_quit,clearScreen,get_int_input
def main():
    try:
        input_file = open('computerDetails.txt', 'rb')
        computer_dictionary = pickle.load(input_file)
        input_file.close()

    except:
        computer_dictionary = {}

    proceed = True
    while proceed:
        
        print('\t\tLAB MANAGEMENT SYSTEM')
        print("\t************************************")
        
        print('\t| 1. Lookup an Computer            |')
        print('\t| 2. Add a new Computer            |')
        print('\t| 3. Edit an existing Computer   |')
        print('\t| 4. Delete an existing Computer   |')
        print('\t| 5. Display All                   |')
        print('\t| 6. Save and Quit                 |')
        print('\t| 7. Clear Screen                  |')
        print("\t************************************")

        option_choice = get_int_input('\n\tEnter an option to continue:')

        options = {
            1: lookup,
            2: add,
            3: change,
            4: delete,
            5: printAll,
            6: save_quit,
            7: clearScreen,
        }
        proceed = options[option_choice](computer_dictionary)


if __name__ == "__main__":
    main()