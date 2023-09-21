import random


class Board:

    class Square:
        def __init__(self,row,col):
            self.loc=str(row)+str(col)
            self.value='-'

    def __init__(self):
        self.board=[[None for x in range(3)] for y in range(3)]
        for i in range(3):
            for j in range(3):
                self.board[i][j]=self.Square(i,j)
        self.current_player = 'X'
        self.score = {'X':0,'O':0}


    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j].value,end=" ")
            print()

    def stringBoard(self):
        s=""
        for i in range(3):
            for j in range(3):
                s+=self.board[i][j].value
        return s

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]=self.Square(i,j)


    def get_x_score(self):
        return self.score['X']

    def get_o_score(self):
        return self.score['O']


    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def fill_square_check(self,row,col):

        if self.checkWinner():
            self.score[self.current_player]+=1
            return True
        return False


    def checkDraw(self):
        #print("checking draw)")
        if sum([[sqr.value for sqr in row].count('-') for row in self.board]) == 0:
            #print("draw true")
            return True
        return False

    def checkWinner(self):
        #Check Rows
        for row in self.board:
            if [item.value for item in row].count(self.current_player)==3:
                #print("row true")
                return True

        #Check Columns
        for i in range(3):
            temp = [row[i] for row in self.board]
            if [item.value for item in temp].count(self.current_player) == 3:
                #print("col true")
                return True

        #check Diagonal
        for i in range(3):
            temp = [self.board[i][i] for i in range(len(self.board))]
            if [item.value for item in temp].count(self.current_player)==3:
                #print("diag true")
                return True
        #Check other Diagonal
        for i in range(3):
            temp = [self.board[i][3-i-1] for i in range(len(self.board))]
            if [item.value for item in temp].count(self.current_player)==3:
                #print("other diag true")
                return True
        return False



class Board_Game:

    #make sure you dont let the other guy win
    def survive_or_win(self):
        # Check Rows
        board = self.board.board
        for i,row in enumerate(board):

            if [item.value for item in row].count('O') == 2 and [item.value for item in row].count('-') == 1:
                j = [item.value for item in row].index('-')

                #print("WIN this GUY row ")
                self.board.board[i][j].value = 'O'
                #print("o fills ", i, j)
                self.check_and_change(i, j)
                return True

            if [item.value for item in row].count('X') == 2 and [item.value for item in row].count('-') == 1 :
                j = [item.value for item in row].index('-')

                #print("Save this GUY row ")
                self.board.board[i][j].value = 'O'
                #print("o fills ", i, j)
                self.check_and_change(i, j)
                return True
            # Check Column
        for i in range(3):
            temp = [row[i] for row in board]
            if [item.value for item in temp].count('O') == 2 and [item.value for item in temp].count('-') == 1 :
                j = [item.value for item in temp].index('-')
                #print("win col true")
                self.board.board[j][i].value = 'O'
                #print("o fills ", j,i)
                self.check_and_change(j,i)
                return True

            if [item.value for item in temp].count('X') == 2 and [item.value for item in temp].count('-') == 1 :
                j = [item.value for item in temp].index('-')
                #print("save col true")
                self.board.board[j][i].value = 'O'
                #print("o fills ", j,i)
                self.check_and_change(j,i)
                return True

        # check Diagonal
        for i in range(3):
            temp = [board[i][i] for i in range(len(board))]

            if [item.value for item in temp].count('O') == 2 and [item.value for item in temp].count('-') == 1 :
                j = [item.value for item in temp].index('-')
                #print("win diagnoal true")
                self.board.board[j][j].value = 'O'
                #print("o fills ", j, j)
                self.check_and_change(j, j)
                return True

            if [item.value for item in temp].count('X') == 2 and [item.value for item in temp].count('-') == 1 :
                j = [item.value for item in temp].index('-')
                #print("save diagonal")
                self.board.board[j][j].value = 'O'
                #print("o fills ", j, j)
                self.check_and_change(j, j)
                return True

        # Check other Diagonal
        for i in range(3):
            temp = [board[i][3 - i - 1] for i in range(len(board))]
            if [item.value for item in temp].count('O') == 2 and [item.value for item in temp].count('-') == 1 :
                j = [item.value for item in temp].index('-')

                #print("win other diago true")
                self.board.board[j][2-j].value = 'O'
                #print("o fills ", j,2-j)
                self.check_and_change(j,2-j)
                return True

            if [item.value for item in temp].count('X') == 2 and [item.value for item in temp].count('-') == 1  :
                j = [item.value for item in temp].index('-')
                #print("save other diag true")
                self.board.board[j][2-j].value = 'O'
                #print("o fills ", j,2-j)
                self.check_and_change(j,2-j)
                return True


    def o_play(self):

        edge_list = [(1,0),(0,1),(2,1),(1,2)]
        random.shuffle(edge_list)
        #print(edge_list)
        #print("o is playing")
        # if middle square available fill it immediately
        if self.board.board[1][1].value == '-':
            self.board.board[1][1].value = 'O'
            self.check_and_change(1, 1)

        else:
            if self.survive_or_win():
                return
            for (row,col) in edge_list:
                if self.board.board[row][col].value =='-':
                    if row==1:
                        i=col
                    else:
                        i = row
                    if self.board.board[i][0].value == '-':
                        j=0
                    else:
                        j=2
                    if self.board.board[i][0].value == '-':
                        self.board.board[i][j].value = 'O'
                        #print("o fills ", i, j)
                        self.check_and_change(i, j)
                        return

            #print("i am in random")
            for i in range(3):
                for j in range(3):
                    if self.board.board[i][j].value == '-':
                        self.board.board[i][j].value = 'O'
                        #print("o fills ",i,j)
                        self.check_and_change(i, j)
                        return


    def printBoardArray(self):
        self.board.printBoard()

    def stringBoardArray(self):
        return self.board.stringBoard()

    def getBoardArray(self):
        return self.board.board

    def refresh_game(self):
        self.x_wins= self.board.get_x_score()
        self.o_wins = self.board.get_o_score()
        self.board.reset_game()

    def x_wins(self):
        return self.board.get_x_score()

    def o_wins(self):
        return self.board.get_o_score()

    def check_and_change(self,row,col):
        # Filling the matrix and checking winner
        if self.board.fill_square_check(row, col) or self.board.checkDraw():
            #print("refreshing game")
            self.refresh_game()
        self.board.change_player()
        if self.board.current_player == 'O':
            self.o_play()

    def x_play(self,row,col):
        #Filling the GUI. If not empty do nothing
        #print("x is filling",row,col)
        if self.board.board[row][col].value!='-' :
            return
        #filling the GUI
        self.board.board[row][col].value = 'X'
        self.check_and_change(row,col)

        #o plays
        if self.board.current_player == 'O':
            self.o_play()





    def __init__(self):
        self.board = Board()
        self.x_wins=0
        self.o_wins=0



