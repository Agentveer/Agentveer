import csv

def about():
	return("hii   everyone")

table_rating=[[4000,2500, "World Class"],
[2400,2500 ,"Grandmaster"],
[2300,2400 ,"International Master"],
[2200,2300 ,"Master"],
[2100,2200 ,"National Master"],
[2000,2100 ,"Master Candidate"],
[1900,2000 ,"Authority"],
[1800,1900 ,"Professional"],
[1700,1800 ,"Expert"],
[1600,1700 ,"Experienced Intermediate"],
[1500,1600, "Intermediate"],
[1400,1500 ,"Experienced Learner"],
[1300,1400, "Learner"],
[1200,1300 ,"Scholar"],
[1100,1200 ,"Autodidact"],
[1000,1100, "Beginner"],
[0,1000 ,"Basic Knowledge"]]

def write(name,point,status,subject):
	with open("id.csv","w") as id:
		fieldname = ['name', 'point','status','subject']
		writer=csv.writer(id,fieldnames=fieldname)
		writer.writeheader()
		writer.writerow({'name': name, 'point': point,'status':status,'subject':subject})

class id():
	def __init__(self,name,subject,point=0,status="basic knowledge"):
		self.name=name
		self.point=point
		self.status=status
		self.subject=subject
		write(self.name,self.point,self.status,self.subject)
		
	def add_point(self,point):
		self.point+=point
		
	def subtract_point(self,point):
		self.point-=point
		
	def update_status(self):
		self.status=check_status(self.point)
		
	def information(self):
		return(self.name,self.point,self.status,self.subject)
		
	def history(self):
		pass

#check the status of the person		
def check_status(point,table=table_rating):
		x=table_rating
		for i in x:	
			if point in range(i[0],i[1]):
				y=i[2]
		return y
		
def write(user,passw):
	with open("login_detail.csv","w") as login_detail:
		fieldname = ['username', 'password']
		writer=csv.DictWriter(login_detail,fieldnames=fieldname)
		writer.writeheader()
		writer.writerow({'username': user, 'password': passw})

def reader(user,passw):
	with open("login_detail.csv") as login_detail:
		reader=csv.DictReader(login_detail)
		for row in reader:
			if user in row['username'] and passw in row['password']:
				return True
			else :
				return False		

def margin():
	for i in range(3):
		print()
	for i in range(20):
		print(":--",end="")
	for i in range(3):
		print()
		
def state_1():
	margin()
	print("login")
	print("about")
	print("create")
	margin()
	while True:
		x=input("value:--  ")
		if x.lower() in ["login","about","create"]:
			return(x)
			break

def state_2():
	margin()
	print("INFORMATION")
	print("UPDATE")
	print("LOGOUT")
	print("EXIT")
	margin()
	while True:
		x=input("value:--  ")
		if x.lower() in ["information","update","logout","exit"]:
			return(x)
			break

def state_3():
	margin()
	print("ADD")
	print("REMOVE")
	print("CHANGE")
	print("MORE")
	print("BACK")
	print("EXIT")
	margin()
	while True:
		x=input("value:--  ")
		if x.lower() in ["add","remove","change","more","back", "exit"]:
			return(x)
			break
	
def main():
	x=state_1()
	if x=="login":
		username=input("USERNAME :--  ")
		password=input("PASSWORD :--  ")
		if reader(username,password)==True:
			main2()
		else :
			print("INVALID USERNAME")
			main()
	elif x=="create":
		username=input("USERNAME :--  ")
		password=input("PASSWORD :--  ")
		name=input("NAME :--")
		write(username,password)
		id(username,name)
		main()
	else:
		print (about())
		main()

def main2():
			y=state_2()
			if y=="information":
				print(username.information())
				main2()
			elif y=="update":
				main3()
			elif y=="logout":
				main()
			elif y=="exit":
				main()

def main3():
		z=state_3()
		if z=="add":
			main3()
		elif z=="remove":
			main3()
		elif z=="change":
			main3()
		elif z=="more":
			main()
		elif z=="back":
			main2()
		elif z=="exit":
			main()

main()
