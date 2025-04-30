import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password ='1694', database  ='ccms')
c1=conn.cursor()
print("                                       +-----------------WELCOME--------------------+        ")
print("                                               CYBER CAFE MANAGEMENT SYSTEM            ")


#==============================================================================#
# Function to draw line on screen for presentation
#==============================================================================#
def drawLine(n=55):
     print("="*n)


#==============================================================================#
# Function to display uniform title for each option
#==============================================================================#
def reportTitle(string,n=55):
     drawLine(n)
     print("\t",string)
     drawLine(n)

#==============================================================================#
#  FUNCTION TO ADD ENTRY
#==============================================================================#
def Entry():
     reportTitle("Make an Entry")
     CGID=input("Enter your CGID")
     from datetime import date
     today=date.today()
     d1=today.strftime("%d/%m/%Y")
     date=d1
     from datetime import datetime
     now = datetime.now()
     current_time = now.strftime("%H:%M:%S")
     Time=current_time
     et="insert into entry values('{}',{},'{}')".format(CGID,date,Time)
     c1.execute(et)
     conn.commit()
     print("Entry successfull")
     backtomenu=input("Press any key to return to Menu")
     MainMenu()

#==============================================================================#
#  FUNCTION TO ADD MEMBER
#==============================================================================#
def AddMember():
    reportTitle("Add Member")
    print("Membership enables you to surf the internet at speeds higher than the normal")
    print("You will have to pay a small amount of money. You are at the right place if you need computer daily at low costs.")
    print("You don't need to look for anything else when you have a Membership.")
    print("Do you want to continue???")
    yn=int(input("Press 1 to Continue 0 to go back to Menu"))
    if yn==1:
         Yes()
    elif yn==0:
         No()
    else:
         print("Invalid Choice")
         MainMenu()
         
#==============================================================================#
#  SUBFUNCTION NO
#==============================================================================#
def No():
     backtomenu=input("Press any key to return to Menu")
     MainMenu()
         
#==============================================================================#
#  SUBFUNCTION YES
#==============================================================================#
def Yes():
     import random
     ID=random.randint(1000,9999)
     print("Your CGID is",ID)
     CGID=ID
     name=input("Enter your name :")
     age=int(input("Enter your age :"))
     address=input("Enter your residential address :")
     phone_no=int(float(input("Enter your phone number :")))
     email_id=input("Enter your Email ID :")
     print("1 YEAR")
     print("2 YEARS")
     print("3 YEARS")
     plan=int(input("Enter the plan you want(in years)"))
     if plan==1:
          print("Please pay Rs.700")
     elif plan==2:
          print("Please pay Rs.1300")
     elif plan==3:
          print("Please pay Rs.2000")
     else:
          print("Please choose a valid plan")
     from datetime import date
     today=date.today()
     d1=today.strftime("%d/%m/%Y")
     date_issued=d1
     ty="insert into Members values({},'{}',{},'{}',{},'{}',{},'{}')".format(CGID,name,age,address,phone_no,email_id,plan,date_issued)
     c1.execute(ty)
     conn.commit()
     print("                                                MEMBER ADDED               ")
     MainMenu()

#==============================================================================#
#  FUNCTION TO REGISTER LOCALS
#==============================================================================#
def Registerlocals():
    reportTitle("REGSTER")
    import random
    ID=random.randint(1000,9999)
    print("Your CGID is",ID)
    CGID=ID
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    address=input("Enter your residential address :")
    phone_no=int(float(input("Enter your phone number :")))
    email_id=input("Enter your Email ID :")
    from datetime import date
    today=date.today()
    d1=today.strftime("%d/%m/%Y")
    date=d1
    ty="insert into not_members values({},'{}',{},'{}',{},'{}',{})".format(CGID,name,age,address,phone_no,email_id,date)
    c1.execute(ty)
    conn.commit()
    print("                                                REGISTERED                ")
    MainMenu()
    
#==============================================================================#
#  FUNCTION TO REMOVE MEMBERS
#==============================================================================#
def RemoveMember():
    reportTitle("ADD CUSTOMER")
    CGID = input("Enter the CGID of the user you want to delete")
    ty=("delete from Members where CGID=" + str(CGID))
    mr=c1.execute(ty)
    conn.commit()
    print("MEMBER REMOVED")
    backtomenu=input("Press any key to return to Menu")
    MainMenu()
#==============================================================================#
#  FUNCTION FOR TIME CHARGES
#==============================================================================#
def TimeCharges():
      reportTitle("TIME CHARGES")
      time=input("Enter the time :") 
      amount=int(input("Enter the amount :"))
      ss="insert into Time_charges values('{}',{})".format(time,amount)
      c1.execute(ss)
      conn.commit()
      backtomenu=input("Press any key to return to Menu")
      MainMenu()

#==============================================================================#
#  FUNCTION FOR BILLING
#==============================================================================#
def Billing():
     reportTitle("BILL")
     CGID=input("Enter your CGID :")
     time=int(input("Enter the time you accessed cyber cafe in minutes :"))
     total=time*2
     qw="insert into Bill values('{}',{},{})".format(CGID,time,total)
     c1.execute(qw)
     conn.commit()
     print("Please pay Rs.",total)
     print("Type YES to pay your bill or NO to pay it later")
     b=input("Type YES or NO:")
     if b=="YES":
         print("Bill paid successfully")
     else:
         print("Bill not paid,pay the bill to leave the place")
         backtomenu=input("Press any key to return to Menu")
         MainMenu()

#==============================================================================#
#  FUNCTION TO VIEW MEMBERS DETAILS
#==============================================================================#
def MemberDetails():
     CGID=input("Enter the CGID of the customer you want to search :")
     ea="select * from Members where CGID=" + str(CGID)
     c1.execute(ea)
     data=c1.fetchall()
     if (not data):
          print("user not found")
     else:
          reportTitle("CUSTOMER DETIALS")
     for row in data:
          print("CGID:",row[0])
          print("Name:",row[1])
          print("Age:",row[2])
          print("Address:",row[3])
          print("Phone number:",row[4])
          print("Email ID:",row[5])
          print("Plan(in Years:)",row[6])
          print("Date Issued:",row[7])
          backtomenu=input("Press any key to return to Menu")
          MainMenu()

#==============================================================================#
#  FUNCTION TO VIEW LOCALS DETAILS
#==============================================================================#
def LocalDetails():
     CGID=input("Enter the CGID of the customer you want to search :")
     ea="select * from not_members where CGID=" + str(CGID)
     c1.execute(ea)
     data=c1.fetchall()
     if (not data):
          print("user not found")
     else:
          reportTitle("CUSTOMER DETIALS")
     for row in data:
          print("CGID:",row[0])
          print("Name:",row[1])
          print("Age:",row[2])
          print("Address:",row[3])
          print("Phone number:",row[4])
          print("Email ID:",row[5])
          print("Date:",row[6])
          backtomenu=input("Press any key to return to Menu")
          MainMenu()

#==============================================================================#
#  FUNCTION TO VIEW ALL MEMBERS
#==============================================================================#
def AllMembers():
     ea="select * from Members "
     c1.execute(ea)
     data=c1.fetchall()
     reportTitle("\tALL STUDENTS REPORT",150)
     print("CGID    Name        Age   Address             Phone.no          Email                        Plan   Date of issuing membership              ")
     drawLine(150)
     for row in data:
          print(row)
          print("/n")
          backtomenu=input("Press any key to return to Menu")
          MainMenu()

#==============================================================================#
#  FUNCTION TO VIEW ALL LOCALS
#==============================================================================#
def AllLocals():
     ea="select * from not_members "
     c1.execute(ea)
     data=c1.fetchall()
     reportTitle("\tALL STUDENTS REPORT",150)
     print("CGID    Name        Age   Address             Phone.no          Email                        Date Of Resgistration                            ")
     drawLine(150)
     for row in data:
          print(row)
          print("/n")
          backtomenu=input("Press any key to return to Menu")
          MainMenu()

          

#==============================================================================#
#  FUNCTION TO VIEW ALL ENTRIES
#==============================================================================#
def AllEntries():
     ea="select * from entry "
     c1.execute(ea)
     data=c1.fetchall()
     reportTitle("\tALL STUDENTS REPORT",59)
     print("CGID                Date                 Time") 
     drawLine(59)
     for row in data:
          print(row)
          print(   )
          backtomenu=input("Press any key to return to Menu")
          MainMenu()

#==============================================================================#
#  FUNCTION TO EXIT
#==============================================================================#
def Exit():
     print("                                                THANK YOU VISIT AGAIN               ")
     exit()


#==============================================================================#     
#MENU
#==============================================================================#     
def MainMenu():
      print("1.Add Member")
      print("2.Remove Member")
      print("3.Member Details")
      print("4.Register Locals" )
      print("5.Local Details")
      print("6.Entry")
      print("7.Entry Details")
      print("8.Time Charges")
      print("9.Billing")
      print("0.Exit")
while True:
     print("Enter 00 to Load Menu")

     try:
          
          x=int(input("Enter Your Choice :"))
          if x==00:
               MainMenu()
               
          elif x==0:
               Exit()

          elif x==1:
               AddMember()

          elif x==2:
               RemoveMember()

          elif x==3:
               MemberDetails()

          elif x==4:
               AllMembers()
               
          elif x==5:
               Registerlocals()
          
          elif x==6:
               LocalDetails()

          elif x==7:
               AllLocals()
          
          elif x==8:
               Entry()
          
          elif x==9:
               AllEntries()
     
          elif x==10:
               TimeCharges()

          elif x==11:
               Billing()
          
          else :
                     print("Invalid choice")
                     MainMenu()
     except ValueError:
          
          print("Invalid Choice, Select from 1-5")
exit
