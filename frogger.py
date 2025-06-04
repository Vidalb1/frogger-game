"""
File:    frogger.py
Author:  Vidal Bickersteth
Date:    11/22/2024
Description: This program simulates the real frogger game on a more basic scale.
"""
import os
root, directories, files = next(os.walk('.'))
FROG = '\U0001F438' # the emoji one
FIRST_LINE = 0
SECOND_LINE = 1
THIRD_LINE = 2


   

def open_file(frog_file):
    """    A function to access the game files and convert them into manipulative lists. 
            :param frog_file: The file that the user selected.
            :return: 2D that contains the first, second, and rest of the lines. 
    """
    big_list = []
    list = []
    list2 = []
    with open(frog_file) as file:
        lines = file.readlines()
    first = lines[FIRST_LINE].split()
    for i in range(len(first)):
        if(first[i] != " "):
            list.append(first[i])
    second = lines[SECOND_LINE].split()
    for j in range(len(second)):
        if(second[j] != " "):
            list2.append(second[j])
    third = lines[THIRD_LINE:]
    for i in range(len(third)):
        third[i] = third[i].strip()
    big_list = [list, second, third]
    return big_list
    



def select_game_file():
    """    A function to ask what file does the user wants to play frogger with. 
            :return: The file that the user wants to play.
    """
    print("[1]  game1.frog" + "\n[2]  game2.frog" + "\n[3]  game3.frog")
    selection = str(input("Enter an option or filename:"))
    if(selection == "1"):
        return "game1.frog"
    elif(selection == "2"):
        return "game2.frog"
    elif(selection == "3"):
        return "game3.frog"
    return selection 

def get_game(rows):
    """    A function to create the initial gameboard including the frog in a 2D list.
            :param rows: A list that contains the gameboard from the game files
            :return: The initialized frogger gameboard.
    """
    list = []
    frog_list = []
    blank_list = []
    blank_list2 = []
    for lasts in range(len(rows[0])):
        blank_list2.append(" ")
    list.append(blank_list2)
    for i in range(len(rows)):
        new_list = []
        for j in range(len(rows[i])):
            new_list.append(rows[i][j])
        list.append(new_list)
    
    for first in range(len(list[0])):
        frog_pos = len(list[0])// 2 + 1
        if(first == frog_pos):
            frog_list.append(FROG)
        else:
            frog_list.append(" ")

    for last in range(len(rows[0])):
        blank_list.append(" ")

    list.append(blank_list)    
    mega_list = [list, frog_list]
    return mega_list


def display_frog(boards,frog):
    """    A function to display the gameboard, place the frog onto the road, 
                and determine if the frog been hit by a car or not.
            :param boards: The gameboard
            :param frog: The frog's positions for row and col. 
            :return: Boolean value of True or False depending if the frog had collided with a car or not. 
    """    
    boolean = True
    for row in range(len(boards)):
        for col in range(len(boards[row])):
            original = boards[row][col]
            if(row == frog[0] and col == frog[1]):
               boards[row][col] = FROG
               print(boards[row][col], end=" ")
               if(original == "X" and boards[row][col] == FROG):
                   boolean = False
               boards[row][col] = original
            else:
               print(boards[row][col], end=" ")
        print()
    return boolean
   
    
def move_frog(input, frog_pos, gameboard, jumps):
    """    A function to allow the frog to move and cross over the road.
                :param input: The movement that the user wants to frog to make.
                :param frog_pos: The row and col coordinates of the frog.
                :param gameboard: The road or the board of the game. 
                :param jumps: the number of jumps that can be used in the entire game.
                :return: Updated row and col positions of the frog. 
    """
    frog_row = frog_pos[0]
    frog_col = frog_pos[1]
    if input.upper() == "W":
        if(frog_row - 1 >= 0):
            frog_row -= 1
    if input.upper() == "S":
        if(frog_row + 1 < len(gameboard)):
            frog_row += 1
    if input.upper() == "D":
        if(frog_col + 1 < len(gameboard[0])):
            frog_col += 1
    if input.upper() == "A":
        if(frog_col - 1 >= 0):
            frog_col -= 1
    if "J" in input.upper():
        if(jumps >= 0):
            new_list = input.split()
            jumps = []
            for i in range(len(new_list)):
                if(new_list[i] != " "):
                    jumps.append(new_list[i])
            if(frog_row - int(jumps[1]) <= 1 and int(jumps[1]) - frog_row <= 1):
                if(int(jumps[1]) < len(gameboard) and int(jumps[1]) > 0 and int(jumps[2]) < len(gameboard[0]) and int(jumps[2]) > 0):
                    frog_row = int(jumps[1])
                    frog_col = int(jumps[2]) - 1
                    frog_pos = [frog_row, frog_col]
                    return frog_pos
    frog_pos = [frog_row, frog_col]
    return frog_pos

            






def frogger_game(file):
        """    A function of the frogger game and determines if the frog crosses the road 
                    safely or not. 
                :param file: The selected game file that the user wants to pick. 
                :return: NONE
        """
        round = 1
        i = 0
        info = open_file(file)
        jump = info[0]
        jumps = int(jump[2])
        speed = info[1]
        rows = info[2]
        list = get_game(rows)
        board = list[0]
        frog_list = list[1]
        frog_pos = [0,len(board[0])//2]
        print(round)
        dis = display_frog(board, frog_pos)
       
        while(dis != False and frog_pos[0] != len(board) - 1):
            movement = str(input("WASDJ >> "))
            round += 1
            print(round)
            if("J" in movement.upper()):
                jumps -= 1
            move = move_frog(movement, frog_pos, board, jumps)
            frog_pos = move
            
            for i in range(1, len(board) - 1):
                board[i] = board[i][-(int(speed[i-1])):] + board[i][:-(int(speed[i-1]))]
            dis = display_frog(board, frog_pos)
            if(dis == False):
                print("You Lost, Sorry Frog")
        if(dis == True):
            print("You won, Frog lives to cross another day.")
            
            


    

if __name__ == '__main__':
    # The access to file and the simulation of the frogger game. 
    selected_game_file = select_game_file()
    frogger_game(selected_game_file)
