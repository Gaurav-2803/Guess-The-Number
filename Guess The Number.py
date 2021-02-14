import random,os,sys

clear=lambda:os.system("cls")                #Clear_Fn
clear()                                      #Clear_Fn_Call

color_blue=lambda:os.system("color 0d")      #Blue_Color_Fn

color_red=lambda:os.system("color 0c")       #Red_Color_Fn

color_brwhite=lambda:os.system("color 0f")   #Bright_White_Color_Fn
color_brwhite()                              #Bright_White_Color_Fn_Call

print("\t\t<|Guess The Number|>\n")
name=input("Enter You Name : ")
print("===============================\nWelcome",name,"\n===============================\n# Here Are The Rules Of The Game\n1]Guess Number Between 1-100\n2]No Use Of Decimal Number\n3]To Exit Game Press(exit)\n===============================\n",name,end=" ")
diff=input("Choose The Difficulty\n\n1]Easy(8 Guess's)\n2]Medium(6 Guess's)\n3]Hard (5 Guess's)\n\nYour Choice (1~3) : ")
print("===============================")
close_0=diff.upper()
if diff=='1':
    trial=8
    print("Difficulty => Easy\nTotal Guess's => ",trial)
elif diff=='2':
    trial=6
    print("Difficulty => Medium\nTotal Guess's => ",trial)
elif diff=='3':
    trial=5
    print("Difficulty => Hard\nTotal Guess's => ",trial)
elif close_0=="EXIT":
    clear()
    color_red()
    print("==============================================\n   Sry For That, But You Just Exit The Game\n==============================================")
    sys.exit(0)
else:
    clear()                                   #Clear_Fn_Call
    color_red()                               #Red_Color_Fn_Call
    print("=========================================================================================\nVariable Type Error : Invalid Input : Only Numeric Types Of Value Accepted Between 1 to 3\n=========================================================================================")                 
    sys.exit(0)

choice=input("Hit Enter To Begin The Game : ")
close_3=choice.upper()
if close_3=="EXIT":
    clear()
    color_red()
    print("==============================================\n  Sry For That, But You Just Exit The Game\n==============================================")
    sys.exit(0)

clear()                                       #Clear_Fn_Call

print("==============================================")
x=int(random.randint(0,100))
i=trial
while trial>0:    
    color_blue()                              #Blue_Color_Fn_Call
    print(name,end=" ")
    a=input("Guess The Number Between 1 to 100 : ")
    close_2=a.upper()
    if a=="":
        print("You Entered Nothing, Try Again!!!\nChances Reamining :",trial,"\n==============================================") 
    elif close_2=="EXIT":
        clear()
        color_red()
        print("==============================================\n  Sry For That, But You Just Exit The Game\n==============================================")
        sys.exit(0)

    elif a.isalpha()==True:
        color_red()                           #Red_Color_Fn_Call
        print("===============================================================\nVariable Type Error : Invalid Input : Only Numeric Types Of Value Accepted Between 1 to 3\nChances Reamining :",trial)
        input("Hit Enter To Continue!!!")
        print("===============================================================")
    elif int(a)>100 or int(a)<0:
        color_red()                           #Red_Color_Fn_Call
        print("===============================================================\nLimit Error : Invalid Input : Number should be between 1 to 100\nChances Reamining :",trial)
        input("Hit Enter To Continue!!!")
        print("===============================================================")
    elif int(a)==x: 
        if trial==1:
            print("==============================================\n\t",name,"It Is Time Consuming But Nice One\n\t\t||You Won||\n==============================================")
        elif trial==2:            
            print("==============================================\n\t",name,"Thats A Good One\n\t||You Won||\n==============================================")
        elif trial==3:            
            print("==============================================\n\t",name,"You're Nothing But A Perfect Guesser\n\t\t||You Won||\n==============================================")
        elif trial==4:
            print("==============================================\n\t",name,"You're A Perfect Player\n\t\t||You Won||\n==============================================")
        elif trial==5:
            print("==============================================\n\t",name,"Excellent Guessing Skills \n\t\t||You Won||\n==============================================")
        elif trial==6:
            print("==============================================\n\t",name,"Your Guessing Is Awesome\n\t\t||You Won||\n==============================================")
        elif trial==7:
            print("==============================================\n\t",name,"You're Guessing Expert\n\t\t||You Won||\n==============================================")
        elif trial==8:
            print("======================================================\n",name,"Its Nothing But a Extraorinary 'LUCK'; HA HA!\n\t\t  ||You Won||\n======================================================")
        break
    elif int(a)<x:
        trial-=1
        print("Chances Reamining :",trial)
        if a!=x and trial!=0:
            print("You Entered Smaller Number Try Again\n==============================================")              
        elif a!=x and trial==0:
            print("You Entered Smaller Number, Better Luck next Time")
    elif int(a)>x:
        trial-=1
        print("Chances Reamining :",trial)
        if a!=x and trial!=0:
            print("You Entered Greater Number Try Again\n==============================================")       
        elif a!=x and trial==0:
            print("You Entered Greater Number, Better Luck Next Time")                   
if trial==0:
    clear()                                   #Clear_Fn_Call
    color_red()                               #Red_Color_Fn_Call
    print("=======================================================\nYou Lost, Number of Trial Exhausted")        
    a=int(a)
    if (a-x>0 and a-x<=5) or (x-a>0 and x-a<=5) :
        print(name,"You Almost Killed It")
    elif (a-x>5 and a-x<10) or (x-a>5 and x-a<=10):
        print(name,"You're So Close")
    else:
        print(name,"You Must Improve Your Gameplay,Need For Practice")       
    print("Number Is :",x,"\n=======================================================")
                