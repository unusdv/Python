from os import system
from random import choice
from time import sleep

class TTT:
	def __init__(self):
		print('Modes:\nEasy - 1\nMedium - 2\nHard - 3')
		self.mode = input('Choose: ')
		self.sign = input('X or O:')
		self.sign = 'X' if self.sign.lower()=='x' else 'O'
		self.laptop = 'O' if self.sign == 'X' else 'X'
		self.spaces = list(range(9))
		self.desk = [str(i) for i in range(1,10)]
		self.step = 0
		if self.mode == '1':
			self.start(self.put)

	def start(self,f):
		self.step = 1
		while self.step<=9:
			system("clear")
			self.show()
			if self.step%2:
				if f(int(input('Choose a number: '))-1):
					self.step+= 1
			else:
				f(choice(self.spaces))
				self.step+= 1
			res = self.finished()
			if res[0]:
				system('clear')
				self.show()
				#print('You win!' if list(res[1])[0]==self.sign else 'AI win!')
				print('You win!' if self.sign in res[1] else 'AI win!')
				break
		if not self.finished()[0]:
			system("clear")
			self.show()
			print('Draw!')
	def finished(self):
		for i in range(0,7,3):
			s = set(self.desk[i:i+3])
			if len(s) == 1:
				return [True,s]
		for i in range(3):
			s = set(self.desk[i::3])
			if len(s) == 1:
				return [True,s]
		s = set(self.desk[::4])
		if len(s) == 1:
			return [True,s]
		s = set(self.desk[2:7:2])
		if len(s) == 1:
			return [True,s]
		return [False,{''}]

	def put(self,i):
		if self.desk[i] not in 'OX':
			self.desk[i] = self.sign if self.step%2 else self.laptop
			self.spaces.remove(i)
			return True
		return False

	def show(self):
		line = '+---'*3+'+'
		print(line)
		for i in range(9):
			l = len(self.desk[i])
			print(f"|{' '*(2-l)}{self.desk[i]}",end=' ')
			if i%3 == 2:
				print(f"|\n{line}")

class TTTMedium(TTT):
	def __init__(self):
		super().__init__()
		if self.mode == '2':
			print('MEDIUM')
			sleep(5)
			self.start(self.put2)
	def put2(self,i):
		pass

class TTTHard(TTTMedium):
	def __init__(self):
		super().__init__()
		if self.mode == '3':
			print('HARD')
			sleep(5)
			self.start(self.put3)
	def put3(self,i):
		pass

if __name__ == "__main__":
	TTTHard()
