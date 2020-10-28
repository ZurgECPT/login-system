#Ask if user is a new user or a returning user
#Based on response, either prompt for account creation
#or login
#When user is created, their username/PW
#will be stored in a different text file



def begin():
	#This function starts the program, gives the welcome message
	#and the option to login or register
	global option
	#global allows the variable 'option' to be used outside of the function 'begin'
	print('Welcome to ZurgLogistics')
	option = input('Login or Register (login, register)' )
	if (option != 'login' and option != 'register'):
		begin()

granted = False

#Granted variable turns true if user logs in or registers, grants user access to
#the program ('They get the welcome message')

def grant():
	global granted
	granted = True

def login(name,password):
	global username
	success = False
	file = open('userData.txt', 'r')
	for i in file:
		a, b = i.split(',')
		#The for loop runs the code for each line(i) in the file
		#This splits each line in the text file into two variables
		#with the comma being the separator
		b = b.strip()
		if (a == name and b == password):
			success = True
			break

	file.close()

	if (success):
		username = name
		print('You have logged in successfully')
		grant()
	else:
		print('Invalid username/password')
			

	
def register(name,password):
	global username
	#the global username variable is used in order to give access
	#to the final print statement of the program
	file = open('userData.txt', 'r')
	#Opens the userData file in Notepad in append mode(a)
	for i in file:
		a, b = i.split(',')
		b = b.strip()
		
		while a == name:		     
			print('Username taken, try again \n')
			name = input('Enter a username: ')
			password = input('Enter a password: ')

			
	username = name	
	file.close()		
	file = open('userData.txt', 'a')
	file.write('\n' + name + ',' + password)
	file.close()
	grant()	
	

	
		
			
	#Adds the username and password provided to the userData file


def access(option):
	#This function takes the users choice of logging in or registering
	#and gives presents them with the login or register process
	global name
	if(option=='login'):
		name = input('Enter your username: ')
		password = input('Enter your password: ' )
		login(name, password)
	else:
		print('Enter your name and password to register: ')
		name = input('Enter your username: ')
		password = input('Enter your password :' )
		register(name, password)



begin()
access(option)
if(granted):
	print('Welcome to the program, ', username)
