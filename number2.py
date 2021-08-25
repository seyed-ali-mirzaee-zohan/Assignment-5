import time 
duration=time.time()
import random
print(" play with your friend : 1 ")
print(" play with pc : 2 ")
Game_format=input(" 1 or 2 : ")

game=[['_','_','_'],
      ['_','_','_'],
      ['_','_','_']]

# Function 1 : نمایش صفحه بازی
def monitor():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end="  ")
        print()


# Function 2 : کنترل برنده شدن
def control():
# برنده شدن بازیکن 1     
    # برنده شدن ردیفی
    if game[0][0]=="X" and game[0][1]=="X" and game[0][2]=="X":
        print("Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
    if game[1][0]=="X" and game[1][1]=="X" and game[1][2]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
    if game[2][0]=="X" and game[2][1]=="X" and game[2][2]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)   
        exit()
    # برنده شدن ستونی    
    if game[0][0]=="X" and game[1][0]=="X" and game[2][0]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
    if game[0][1]=="X" and game[1][1]=="X" and game[2][1]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
    if game[0][2]=="X" and game[1][2]=="X" and game[2][2]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
    # برنده شدن قطری
    if game[0][0]=="X" and game[1][1]=="X" and game[2][2]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)    
        exit() 
    if game[0][2]=="X" and game[1][1]=="X" and game[2][0]=="X":
        print( "Winner of the game : player 1 ")
        print("game duration : ",duration)
        exit()
# برنده شدن بازیکن 2     
    # برنده شدن ردیفی
    if game[0][0]=="O" and game[0][1]=="O" and game[0][2]=="O":
        print("Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
    if game[1][0]=="O" and game[1][1]=="O" and game[1][2]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
    if game[2][0]=="O" and game[2][1]=="O" and game[2][2]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)    
        exit()
    # برنده شدن ستونی    
    if game[0][0]=="O" and game[1][0]=="O" and game[2][0]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
    if game[0][1]=="O" and game[1][1]=="O" and game[2][1]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
    if game[0][2]=="O" and game[1][2]=="O" and game[2][2]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
    # برنده شدن قطری
    if game[0][0]=="O" and game[1][1]=="O" and game[2][2]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)    
        exit()    
    if game[0][2]=="O" and game[1][1]=="O" and game[2][0]=="O":
        print( "Winner of the game : player 2 ")
        print("game duration : ",duration)
        exit()
        

monitor()
# بازی 2 نفره
if Game_format=="1":
    while True:
        #  1 بازیکن شماره 
        print('player number 1 :')
        while True:
            print(" 0<= row and column <=2 ")
            row,column=input('Please specify the location of the nut : i,j : ').split(',')
            location=[int(row),int(column)]
            if 0<=int(row)<=2 and 0<=int(column)<=2:
                if game[location[0]][location[1]]=="_":
                    game[location[0]][location[1]]='X'
                    break
                else:
                    print()
                    print("!! The selected cell is full !! Try again ")
                    print()
            else:
                print()
                print("!! Input numbers are incorrect !! Try again ")
                print()
        monitor()
        control()

        #  2 بازیکن شماره 
        print('player number 2 :')    
        while True:        
            print(" 0<= row and column <=2 ")
            row,column=input('Please specify the location of the nut : i,j : ').split(',')
            location=[int(row),int(column)]
            if 0<=int(row)<=2 and 0<=int(column)<=2:
                if game[location[0]][location[1]]=="_":    
                    game[location[0]][location[1]]='O'
                    break
                else:
                    print()
                    print("!! The selected cell is full !! Try again ")
                    print()
            else:
                print()
                print("!! Input numbers are incorrect !! Try again ")
                print()
        monitor()
        control()
# بازی با رایانه
if Game_format=="2":
    while True: 
        #  1 بازیکن شماره 
        print('player number 1 :')
        while True:
            print(" 0<= row and column <=2 ")
            row,column=input('Please specify the location of the nut : i,j : ').split(',')
            location=[int(row),int(column)]
            if 0<=int(row)<=2 and 0<=int(column)<=2:
                if game[location[0]][location[1]]=="_":
                    game[location[0]][location[1]]='X'
                    break
                else:
                    print()
                    print("!! The selected cell is full !! Try again ")
                    print()
            else:
                print()
                print("!! Input numbers are incorrect !! Try again ")
                print()
        monitor()
        control()
        #  رایانه   
        print('PC :')    
        while True:        
            row=random.randint(0,2)
            column=random.randint(0,2)
            if game[row][column]=="_":    
                game[row][column]='O'
                break
            else:
                print()
                print("!! The selected cell is full !! Try again ")
                print()
        monitor()
        control()