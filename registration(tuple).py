from PIL import Image
import time
import secrets


action = input("sign up(1) or sign in(2)?")


password_length = 13
random_password = secrets.token_urlsafe(password_length)

 	
 
reg_f = (["sveta","sveta1434"],['vegetable','vegetable123'])
reg_f2 = []
loop = "Yes"
def sign_in():
	username = input("Enter userame : ") 
	for i in reg_f :
		if username in i :
			print("U'r welcome")
			password = input("Enter password : ")
			if password in i :
				print("welcome")
				print("opening photo...")
				time.sleep(1)
				im = Image.open(r"code.jpeg") 
				im.show()
				print("done")
			else:
				print("go away")
		elif reg_f[len(reg_f)-1] != 1:
			continue
		else:
			print("username incorrect")


def sign_up():
	global reg_f
	global reg_f2 
	print("wait")
	time.sleep(2)
	print("Welcome to wokiak's code\nCreate new login and password\nLogin:")
	new_login = input()
	print("login :"+ new_login)
	print("Now create new password :")
	new_password = input("if u can't create password by urself u can use Random. type \"Random\" or \'r\' to use random generation : ")
	if new_password == "Random" or new_password=="r":
		global password_length
		global random_password
		print(f'''\nlogin :  {new_login}
password : {random_password}
			''')
		# print(random_password + "\nIt's u'r safety password, don't forget it")
		reg_f=list(reg_f)
		reg_f2.append(new_login)
		reg_f2.append(random_password)
		reg_f.append(reg_f2)
		reg_f=tuple(reg_f)
		print("Done" + str(reg_f))
	else:
		print("confirm password :")
		repeat_password = input()
		if new_password == repeat_password :

			reg_f=list(reg_f)
			reg_f2.append(new_login)
			reg_f2.append(new_password)
			reg_f.append(reg_f2)
			reg_f=tuple(reg_f)
			print("Done" + str(reg_f))


while loop == "Yes":
	if action == "2" or action == "sign in":
		sign_in()

	if action =="1" or action =="sign up":
		sign_up()
	loop = input("do u wanna log in?(Yes or No)")

	if loop == "No" or loop == "N" or loop =="no" or loop =="n" :
		print ("see u later")
		break
	if loop == "Yes" or loop== "Y" or loop =="yes" or loop =="y":
		sign_in()