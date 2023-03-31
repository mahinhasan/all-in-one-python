import pickle
import Computer
import os

def get_int_input(prompt):
    num = -1
    while True:
        try:
            num = int(input(prompt))
            break
        except:
            print("Error: Enter an integer, try again...")
    return num

def clearScreen(clear):
    os.system('clear')
    proceed = True
    return proceed

def lookup(dictionary):
    computer_id = get_int_input('\tEnter the computer ID number: ')
    if computer_id in dictionary:
        print(dictionary.get(computer_id))
    else:
        print("\tThat ID number was not found.")

    proceed = True
    return proceed

def printAll(dictionary):
    for id in dictionary.keys():
        print(dictionary.get(id))
    proceed = True
    return proceed


def add(dictionary):
    computer_id = get_int_input('\tEnter the PC ID number: ')
    if computer_id in dictionary:
        print("\nPc is already in Database\n")
        proceed = True
        return proceed
    os_name = input('\tEnter the name of the OS: ')
    status = input('\tEnter the Status: ')
    problem = input('\tEnter the Problem: ')

    entry = Computer.Computer(computer_id, os_name, status, problem)
    dictionary[computer_id] = entry
    print('\tEmployee added succesfully')

    proceed = True
    return proceed


def change(dictionary):
    computer_id = get_int_input('\tEnter the Computer ID you would like to change: ')
    if computer_id in dictionary.keys():
        os_name = input('\tEnter new Computer OS: ')
        staus = input('\tEnter new Computer Status: ')
        problem = input('\tEnter problem: ')
        entry = Computer.Computer(computer_id, os_name, staus, problem)
        dictionary[computer_id] = entry
        print('\tDetails changed successfully.')
    else:
        print('That Computer ID was not found.')

    proceed = True
    return proceed


def delete(dictionary):
    computer_id = get_int_input('\tEnter the Computer ID you would like to remove: ')
    if computer_id in dictionary.keys():
        del dictionary[computer_id]
        print('\tComputer removed successfully')
    else:
        print('\tThat Computer ID was not found.')

    proceed = True
    return proceed


def save_quit(dictionary):
    output_file = open('computerDetails.txt', 'wb')
    pickle.dump(dictionary, output_file)
    output_file.close

    proceed = False
    return proceed


