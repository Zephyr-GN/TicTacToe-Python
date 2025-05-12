
import random
import math
import os

#X is max = 1
#O in min = -1

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.humanPLayer = 'X'
            self.botPlayer = "O"
        else:
            self.humanPLayer = "O"
            self.botPlayer = "X"

    def show_board(self):
        print("")
        for i in range(3):
            print("  ",self.board[0+(i*3)]," | ",self.board[1+(i*3)]," | ",self.board[2+(i*3)])
            print("")
            
    def is_board_filled(self,state):
        return not "-" in state

    def is_player_win(self,state,player):
        if state[0]==state[1]==state[2] == player: return True
        if state[3]==state[4]==state[5] == player: return True
        if state[6]==state[7]==state[8] == player: return True
        if state[0]==state[3]==state[6] == player: return True
        if state[1]==state[4]==state[7] == player: return True
        if state[2]==state[5]==state[8] == player: return True
        if state[0]==state[4]==state[8] == player: return True
        if state[2]==state[4]==state[6] == player: return True

        return False

    def checkWinner(self):
        if self.is_player_win(self.board,self.humanPLayer):
            os.system("cls")
            print(f"   Jugador {self.humanPLayer} ha ganado el juego!")
            return True
            
        if self.is_player_win(self.board,self.botPlayer):
            os.system("cls")
            print(f"   Jugador {self.botPlayer} ha ganado el juego!")
            return True

        # comprobar si el juego es empate o no
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Empate!")
            return True
        return False

    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = humanPLayer(self.humanPLayer)
        while True:
            os.system("cls")
            print(f"   Turno del juegador {self.humanPLayer} ")
            self.show_board()
            
            #Human
            square = human.human_move(self.board)
            self.board[square] = self.humanPLayer
            if self.checkWinner():
                break
            
            #Bot
            square = bot.machine_move(self.board)
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break

        # mostrando la vista final del tablero
        print()
        self.show_board()

class humanPLayer:
    def __init__(self,letter):
        self.letter = letter
    
    def human_move(self,state):
        # tomando la entrada del jugador
        while True:
            square =  int(input("Ingrese un numero para seleccionar en el cuadro (1-9): "))
            print()
            if state[square-1] == "-":
                break
        return square-1

class ComputerPlayer(TicTacToe):
    def __init__(self,letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"

    def players(self,state):
        n = len(state)
        x = 0
        o = 0
        for i in range(9):
            if(state[i] == "X"):
                x = x+1
            if(state[i] == "O"):
                o = o+1
        
        if(self.humanPlayer == "X"):
            return "X" if x==o else "O"
        if(self.humanPlayer == "O"):
            return "O" if x==o else "X"
    
    def actions(self,state):
        return [i for i, x in enumerate(state) if x == "-"]
    
    def result(self,state,action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState
    
    def terminal(self,state):
        if(self.is_player_win(state,"X")):
            return True
        if(self.is_player_win(state,"O")):
            return True
        return False

    def minimax(self, state, player):
        max_player = self.humanPlayer  # El juegador
        other_player = 'O' if player == 'X' else 'X'

        # Primero queremos comprobar si el movimiento anterior es ganador
        if self.terminal(state):
            return {'position': None, 'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
                        len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # cada puntaje debe maximizar
        else:
            best = {'position': None, 'score': math.inf}  # cada puntaje debe minimizar
        for possible_move in self.actions(state):
            newState = self.result(state,possible_move)
            sim_score = self.minimax(newState, other_player)  # Simular un juego después de hacer ese movimiento

            sim_score['position'] = possible_move  # Esto representa el siguiente movimiento óptimo.

            if player == max_player:  # X es el jugador mayor
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def machine_move(self,state):
        square = self.minimax(state,self.botPlayer)['position']
        return square

# comienza el juego
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
