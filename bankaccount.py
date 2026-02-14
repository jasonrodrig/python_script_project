class bankaccount:

	def __init__( self , name , number , balance = 0 ):
		self.name     =  name
		self.number   =  number
		self.balance  =  balance
		self.transactions = []

	def deposit( self , amount ):
		if( amount < 0 ):
			print("invalid deposit amount entered:" , amount , "\n please enter positive deposit value and retry again \n") 
		else:
			self.balance = self.balance + amount
			self.record_transaction( "Deposit" , amount , None )
			print(self)

	def withdraw( self , amount ):
		if( amount > self.balance or amount < 0 ):
			print("invalid withdraw amount entered:" , amount , "\n please enter withdraw amount less than the current balance and retry again \n") 
			print(self)
		else:
			self.balance = self.balance - amount
			self.record_transaction( "Withdraw" , amount , None )
			print(self)

	def transfer(self, target_account , amount ):
		if( amount > self.balance or amount < 0 ):
			print("invalid transfer amount entered:" , amount , "\n please enter transfer amount less than the current balance and retry again \n") 
			print(self)
		else:
			self.balance = self.balance - amount;
			target_account.balance = target_account.balance + amount
			self.record_transaction( "Transfer" , amount , f" To {target_account.name}" ) 
			target_account.record_transaction( "Transfer" , amount , f" From {self.name}" )
			print(self)
			print(target_account)

	def get_balance(self):
		print(f" current balance in {self.name}'s account : {self.balance}\n")

	def __str__(self):
		return( 
			"=========================================================\n"
			f"{'Name':<20}{'Account Number':<20}{'Balance (₹)':>15}\n"
			"---------------------------------------------------------\n"
			f"{self.name:<20}{self.number:<22}{self.balance:>15.2f}\n"
			"=========================================================\n"
		)

	def record_transaction( self , transaction_type , amount , to ):
		self.transactions.append( { "type" : transaction_type , "amount" : amount , "details" : to } )		

	def transaction_log(self):
		print(f" \nTransaction History on {self.name}'s bank account\n")
		print("--------------------------------------------------")
		for i, txn in enumerate(self.transactions, 1):
			print(f"{i}. {txn}")
		print("--------------------------------------------------\n")


p1 = bankaccount("Mr.Walter White",1111111111,150)
p2 = bankaccount("Mr.Jesse Pinkman",2222222222,150)
p3 = bankaccount("Mr.Gustav Fring",3333333333,150)

print("#############################################################")
print( " \n initial balance on bank account holders \n " )
print(p1)
print(p2)
print(p3)
print("#############################################################")

print("#############################################################")
print( " \n display get_balance on each bank account holders \n " )
p1.get_balance()
p2.get_balance()
p3.get_balance()
print("#############################################################")

print("#############################################################")
print( " \n display deposit of ₹100 each on bank account holders \n " )
p1.deposit(100)
p2.deposit(100)
p3.deposit(100)
p1.deposit(-1)
print("#############################################################")

print("#############################################################")
print( " \n display withdraw amount of ₹50 each on bank account holders \n " )
p1.withdraw(50)
p2.withdraw(50)
p3.withdraw(50)
p1.withdraw(100)
print("#############################################################")

print("#############################################################")
print( " \n transferring amount of ₹50 from p3 to p1 \n " )
p3.transfer(p1,50)
print( " \n transferring amount of ₹50 from p3 to p2 \n " )
p3.transfer(p2,50)
print( " \n transferring amount of ₹50 from p3 to p1 \n " )
p3.transfer(p1,50)
p3.transfer(p2,60)
print("#############################################################")

print("#############################################################")
print( " \n display transaction log on p1 \n " )
p1.transaction_log()
print( " \n display transaction log on p2 \n " )
p2.transaction_log()
print( " \n display transaction log on p3 \n " )
p3.transaction_log()
print("#############################################################")




