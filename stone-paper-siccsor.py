import random
from  colorama  import Fore , Back
class game:
    def __init__(self):
        pass       
# here user = user entered number
# here mac is the number generated from the machine
    
    def get_data(self,user,mac):
        self.user = user
        self.mac = mac   

    def log(self):
        print(f"User choice is : {self.user} \nMachine choice is : {self.mac}")


        if(self.user==self.mac):
            print(Fore.GREEN +"-->▶️▶️ITS AN TIE")
            print(Fore.WHITE + " ")


        elif((self.user==1 and self.mac==2) or(self.user==3 and self.mac==2) or(self.user==2 and self.mac==1) or(self.user==1 and self.mac==3) ):
            print(f"-->👍YOU WON THE GAME👍")
        else:
            print(Fore.RED +"-->😒YOU LOST THE GAME😒")
            print(Fore.WHITE + " ")

        




info = '''
RULE OF THE GAME :
Enter the number 1 for stone
Enter the number 2 for paper
Enter the number 3 for siccor

'''

print(info)
ran = random.randint(1,3)


user = int(input("Enter your choice in number : "))

if(user>3 or user<1):
    print("ENTER NUMBER BETWEEN 1 - 3")
else:


    print('''
    1->stone
    2->paper
    3->sisscor
    ''')
    g1 = game()
    g1.get_data(user,ran)
    g1.log()