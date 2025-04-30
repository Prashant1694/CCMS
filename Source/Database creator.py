import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password ='1694')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
c1.execute('create database ccms')
print("DATABASE CREATED")
c1.execute('use ccms')
c1.execute('create table Entry(CGID int not null,Date varchar(20),Time varchar(25))')
c1.execute('create table Members(CGID int not null,Name varchar(20) not null,Age int(3)not null,Address varchar(100) not null,Phone_no int(10) not null,Email_ID varchar(30) not null,Plan varchar(8),Date_of_issuing_membership varchar(25),primary key(Phone_no))')
c1.execute('insert into Members(CGID ,Name,Age,Address,Phone_no,Email_id,Plan,Date_of_issuing_membership) values("9120","Divyang","17","Luckhnow","98989810","divyangparmar01@gmail.com","1","23/2/2022"),("3284","Prashant","17","Kudasan","90234591","pkbhatt@gmail.com","2","23/2/2022"),("7678","DhruvR","18","Gandhinagar","78456712","dhruvr@gmail.com","3","23/2/2022"),("4215","Kahan","21","Gandhinagar","63533524","kahandesia@gmail.com","1","24/2/2022"),("5785","Priya","19","Ahmedabad","90909012","priya21@gmail.com","2","24/2/2022"),("4444","Khushi","21","Kalol","98983361","khushi23@gmail.com","1","24/2/2022"),("5122","Jiya","23","Pune","98237600","jiya01@gmail.com","2","24/2/2022"),("3879","Parul","25","Himmatnagar","98765430","parul@gmail.com","2","24/2/2022"),("1948","Shrey","26","Vavol","78965210","shrey@gmail.com","3","25/2/2022"),("5315","Rushi","17","Bapunagar","93045626","rushisvyas@gmail.com","1","25/2/2022"),("7519","Visheg","21","Sargasan","867452310","visheg@gmail.com","2","26/2/2022"),("3482","Dwija","23","Gandhinagar","76542631","dwija@gmail.com","1","26/2/2022"),("4485","Ishani","24","Bhopal","97312580","ishu@gmail.com","2","27/2/2022"),("4317","Dhara","27","Ahmedabad","91736405","dh21@gmail.com","1","27/2/2022"),("7745","Vishal","18","Gandhinagar","92736405","vishal21@gmail.com","2","28/2/2022"),("5512","Viraj","21","Bhopal","98765230","vj123@gmail.com","3","1/3/2022"),("7179","Chintu","28","Gandhinagar","62417890","chintu12@gmail.com","1","2/3/2022"),("8623","Kunjal","24","Ahmdabad","89763210","kunj12@gmail.com","1","3/3/2022"),("4928","Mili","26","Sarghasan","78943210","mili23@gmail.com","2","3/3/2022"),("5695","Harsh","28","Gandhinagar","79543210","gamingbhai@gmail.com","3","4/3/2022")')
c1.execute('create table Not_Members(CGID int ,Name varchar(20) not null,Age int(3)not null,Address varchar(100) not null,Phone_no int(10) not null,Email_ID varchar(30),Date_of_Registration varchar(25) not null,primary key(Phone_no))')
c1.execute('insert into Not_members(CGID,Name,Age,Address,Phone_no,Email_id,Date_of_Registration)values("4852" ,"Arya","18","Ahmedabad","75432101","arya12@gmail.com","5/3/2022"),("2440" ,"Darshana","28","Ahmdabad","69875432","darshu@gmail.com","5/3/2022"),("7180","Darshan","27","Gandhinagar","78910021","dk@gmail.com","6/3/2022"),("7432","Abhi","18","Lucknow","939939310","apppp@gmail.com","7/3/2022"),("2340","Abhinav","17","Bopal","45637600","abh@gmail.com","8/3/2022"),("2829","Vikram","21","Bapunagar","54637281","viki@gmail.com","8/3/2022"),("9058","Vivek","28","Gandhinagar","65784000","vicky@gmail.com","9/3/2022"),("9103","Ishita","29","Ahmedabad","11223344","ishu@gmail.com","9/3/2022"),("5976","Dhanvi","21","Gandhinagar","43526187","dhaaa@gmail.com","10/3/2022"),("7862","Dhruvi","24","Gandhinagar","76500000","pdhruvi@gmail.com","11/3/2022"),("4815","Heer","28","Kudasan","85458858","chomi@gmail.com","12/3/2022"),("6744","Hetvi","25","Bopal","45362010","hetvi@gmail.com","13/3/2022"),("5499","Hami","17","Gandhinagar","67540011","hamipatel@gmail.com","13/3/2022"),("7077","Aayushi","18","Ahmedabad","10101010","Aayu@gmail.com","14/3/2022"),("6529","Rishita","18","Sargasan","20202020","jrishita@gmail.com","14/3/2022"),("1607","Malaya","19","Gandhinagar","25252525","malaya@gmail.com","15/3/2022"),("4196","Prana","20","Bopal","34343434","prana@gmail.com","16/3/2022"),("1716","Smith","18","Gandhinagar","678439843","preyu@gmail.com","17/3/2022"),("5952","Pooja","21","Gandhinagar","38564935","pooja@gmail.com","18/2/2022")')  
c1.execute('create table Bill(Phone_no int(10) not null,Time_accessed_in_min int,Total_charges int)')
c1.execute('create table Time_charges(Time varchar(30),Amount_charged int)')

print("Data Copied")
print("Ready to use.........")

anykey=input("Press any key to exit")
exit()

