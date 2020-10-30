import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',
                               user='root',
                               port="3306",
                               password='root',
                               auth_plugin="mysql_native_password",
                               database='BloodBank')
mc = mydb.cursor()
data1=('Ganga Balan',28,'Female','27/02/1992',8829109827,'gangabalan12@gmail.com','B+','TC 85(61)1','Palkulanghara','Thiruvanathapuram','Kerala')
data2=('RJ Lupin',36,'Male','15/05/1984',7773920288,'moonylupin@gmail.com','B+','24/E,Juhu Rd','Hasmukh Nagar','Mumbai','Maharashtra')
data3=('Sachin S',29,'Male','21/12/1991',9188130360,'darklordsachin12@gmail.com','O+','TC 39/155(1)','Killipalam','Thiruvanathapuram','Kerala')
data4=('Ginny Granger',31,'Female','19/08/1989',6372990027 ,'ginnygin@gmail.com','O+','B-21','BJB Nagar','Bhuubaneswar','Orissa')
data5=('Molly Carter',35,'Female','09/08/1985',8790542618,'cartermolly@gmail.com','A+','191','The Mall','Agra','Uttar Pradesh')
data6=('Johnny Rokeby',32,'Male','27/11/1988',2589027789,'johnnyrock@gmail.com','A+','Sec-133','Sobhaganj','Alipurduar','West Bengal')
data7=('Robin Cunliffe',37,'Female','16/10/1983',6372990027,'robinrobs@gmail.com','A-','3/687','Edappally','Kochi','Kerala')
data8=('Shameer Sha',40,'Male','30/01/1980',8956782346,'shameershaz@gmail.com','A-','Sec-144','Noida','Gautam Buddh Nagar','Uttar Pradesh')
data9=('Jyothi Krishna',38,'Female','05/07/1982',7788390038,'jyothikrishz@gmail.com','B-','12A','Ponnappanadar Colony','Nagarcoil','Tamilnadu')
data10=('Shankar Raj',27,'Male','16/03/1993',7822569827,'rajashankar34@gmail.com','B-','4th Stage','Bannur','Mysore','Karnataka')
data11=('Sarah Shadlock',30,'Female','26/04/1990',9876524411,'shadlockzz@gmail.com','O-','39/61','Vijyapuram','Chittoor','Andhra Pradesh')
data12=('Amardeep Singh',35,'Male','29/09/1985',6883002772,'amarsingh@gmail.com','O-','26/15','Biassu','Jhunjhunu','Rajasthan')
data13=('Charlotte Strike',29,'Female','18/01/1991',2234091178,'charlstrike@gmail.com','AB+','17/1','Hisar city','Hisar','Haryana')
data14=('Amir Malik',34,'Male','25/08/1986',6658974321,'malikmalik@gmail.com','AB+','B-17','Pushkar Nagar','Budgam','Jammu&Kashmir')
data15=('Brittany Johnson',36,'Female','30/11/1984',9856174235,'brittanybrit@gmail.com','AB-','14/2','Chanderi','Gwalior','Madhya Pradesh')
data16=('Tobias Snape',39,'Male','05/07/1981',7489654682,'halfbloodprince@gmail.com','AB-','55C','Kodungallur','Thrissur','Kerala')
cmd="select count(*) from donor"
mc.execute(cmd)
res=mc.fetchone()
row=res[0]
cmd="""INSERT INTO donor(Name,Age,Gender,Date_Of_Birth,Contact_no,Email,Blood_Group,Address,City,District,state)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
if row==0:

    mc.execute(cmd,data1)   
    mc.execute(cmd,data2)
    mc.execute(cmd,data3)
    mc.execute(cmd,data4)
    mc.execute(cmd,data5)
    mc.execute(cmd,data6)
    mc.execute(cmd,data7)
    mc.execute(cmd,data8)
    mc.execute(cmd,data9)
    mc.execute(cmd,data10)
    mc.execute(cmd,data11)
    mc.execute(cmd,data12)
    mc.execute(cmd,data13)
    mc.execute(cmd,data14)
    mc.execute(cmd,data15)
    mc.execute(cmd,data16)
    mydb.commit()
cmd="select count(*) from donor"
mc.execute(cmd)
res=mc.fetchone()
row=res[0]

