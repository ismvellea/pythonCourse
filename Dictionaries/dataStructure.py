import pprint

# Data Structure
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'gray'})
allCats

#Tic Tac Toe
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
pprint.pprint(theBoard)

def printBoard(board):
    print('-------------')
    print('| ' + board['top-L'] + ' | ' + board['top-L'] + ' | ' + board['top-L'] + ' |')
    print('-------------')
    print('| ' + board['top-L'] + ' | ' + board['top-L'] + ' | ' + board['top-L'] + ' |')
    print('-------------')
    print('| ' + board['top-L'] + ' | ' + board['top-L'] + ' | ' + board['top-L'] + ' |')
    print('-------------')

printBoard(theBoard)