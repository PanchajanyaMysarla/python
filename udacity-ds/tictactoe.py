class TicTacToe():
    
    def __init__(self):
        self.theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        self.turn = 'X'
        self.win_strategy = (
            ('top-L','top-M','top-R'),
            ('mid-L','mid-M','mid-R'),
            ('low-L','low-M','low-L'),
            ('top-L','mid-L','low-L'),
            ('top-M','mid-M','low-M'),
            ('top-R','mid-R','low-R'),
            ('top-L','mid-M','low-R'),
            ('top-R','mid-M','low-L')
        )
        
        
    def printBoard(self):
        print(self.theBoard['top-L'] + '|' + self.theBoard['top-M'] + '|' + self.theBoard['top-R'])
        print('-+-+-')
        print(self.theBoard['mid-L'] + '|' + self.theBoard['mid-M'] + '|' + self.theBoard['mid-R'])
        print('-+-+-')
        print(self.theBoard['low-L'] + '|' + self.theBoard['low-M'] + '|' + self.theBoard['low-R'])
    
    def next_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
        
    def setMove(self,move):
        self.theBoard[move] = self.turn
        
    def game_over(self):
        win = False;
        for strategy in self.win_strategy:
            if ' ' not in [self.theBoard[strategy[0]],self.theBoard[strategy[1]],self.theBoard[strategy[2]]] and self.theBoard[strategy[0]] == self.theBoard[strategy[1]] == self.theBoard[strategy[2]]:
                win = True
                break
        return win    
        
    
game = TicTacToe()
    
for i in range(9):
    game.printBoard()
    print('Turn for '+game.turn+'. Move on which space?')
    move = input()
    
    if game.theBoard[move] == ' ':
        game.setMove(move)
        if game.game_over():
            print(game.turn + ' You won the game')
            game.printBoard()
            break;
        else:
            game.next_turn() 
    else:
        print('Move already made. please select a valid move')


