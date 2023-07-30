from datetime import date,time,datetime,timedelta
import numpy as np
#import matploitlib.pyplot as pl
import mysql.connector as sq
con = sq.connect(host="localhost",user="root",passwd="vineet3012",database="manage")
cur = con.cursor()
if con.is_connected() :
    print("sucessfully conected")
else:
    print("Not conected sussesfully")
#cur.execute("CREATE DATABASE manage")
#cur.execute("SHOW DATABASES ")
#cur.execute("SHOW TABLES detail")
#cur.execute("CREATE TABLE coustomer(name nchar,adharcard nchar,phone nchar,date DATE,room int)")
#cur.execute("ALTER TABLE coustomer ADD checkout DATE")
#cur.execute("SELECT  * FROM rooms")
#field = [i[0]for i in cur.description]
#r = cur.fetchall()
#print(r)
#print(field)
def out():
     serch = ("SELECT room FROM rooms WHERE avalable=1")
     cur.execute(serch)
     d = cur.fetchall()
     f = [item for t in d for item in t]
     return(f)
def serc(ca):
     serch = ("SELECT room FROM rooms WHERE catagory=%s AND avalable=%s ")
     val = (ca,0)
     cur.execute(serch,val)
     d = cur.fetchall()
     f = [item for t in d for item in t]
     return(f)
def getdata(a):
    if a == 1 :
        inn = str(input("enter coustomer name or phone number to show history:- "))
        if inn == "all" :
             cur.execute("SELECT * FROM coustomer")
             g = cur.fetchall()
             print("here is the data")
             for row in g:
              print(row)
        else: 
          ge = "SELECT * FROM coustomer ORDER BY name = %s or phone = %s or room = %s"
          ro = int(inn)
          val = (inn,inn,ro)
          cur.execute(ge,val)
          g = cur.fetchall()
          fe = [item for t in g for item in t]
          if len(fe) == 0 :
            print("we dont have any coustomer name",inn)
          else :
            print(g)
    elif a == 3 :
         con = str(input("enter employ name or phone number :-  ")).lower()
         if con == "y" :
             cur.execute("SELECT * FROM employ")
             g = cur.fetchall()
             print("here is the data")
             for row in g:
              print(row)
         else:
             get = "SELECT * FROM employ ORDER BY name = %s or phone = %s"
             val = (con,con)
             cur.execute(get,val)
             g = cur.fetchall()
             fe = [item for t in g for item in t]
             if len(fe) == 0 :
                print("we dont have any coustomer name",inn)
             else :
                print(g)
        
        
while True  :
    date = date.today()
    #cur.execute("SELECT  * FROM coustomer")
    #field = [i[0]for i in cur.description]
    #r = cur.fetchall()
    #print(r)
    #print(field)
    cur.execute("SELECT code FROM employ")
    c = cur.fetchall()
    f = [item for t in c for item in t]
    #print(f)
    #print(c)
    log = int(input("please enter your login ID :- "))
    if log == 2280 :
        n = str(input("enter what to add employ or room:- "))
        if n == "employ":
            na = str(input("please enter employ name:- "))
            d = str(input("please enter detail of employ:- "))
            p = str(input("enter phone number of employ:- "))
            c = int(input("enter code to login in system:- "))
            insert = "INSERT INTO manage.employ(NAME,detail,phone,code,date) VALUES(%s,%s,%s,%s,%s)"
            val = (na,d,p,c,date)
            cur.execute(insert,val)
        elif n == "room":
             nu = int (input("enter room number to add:- "))
             ca = str(input("enter catagory of the room:- "))
             insert = "INSERT INTO rooms(room,catagory,avalable) VALUES(%s,%s,0)"
             val = (nu,ca)
             cur.execute(insert,val)
    elif log in f :
      check = str(input("enter check in or check out:- ")).lower()
      if check == "i":
        ca = str(input("enter room catagory:- "))
        f = serc(ca)
        if len(f) != 0 :
            c = str(input("do you want to book this room y or n :-  ")).lower()
            if c == "y":
                na = str(input("please enter customer name:- ")).lower()
                p = int(input("enter coustomer phone number:- "))
                ad = int(input("enter coustomer adhar number number:- "))
                choo = int(input("enter for how many day :- "))
                co = str(input("are you conform y or n :- ")).lower()
                if co == "y" :
                    r = [f[0]]
                    room = r[0]
                    print(na,"room number is",room)
                    insert = "UPDATE rooms SET avalable=%s WHERE room=%s"
                    val = (1,room)
                    cur.execute(insert,val)
                    inst = "INSERT INTO coustomer(name,adharcard,phone,room,date,checkout) VALUE(%s,%s,%s,%s,%s,%s)"
                    outt= date.today() + timedelta(days=choo)
                    value = (na,p,ad,room,date,outt)
                    cur.execute(inst,value)
                else:
                    continue
        else:
            print("soory room is not avalable")
      elif check == "o" :
          ra = int(input("enter room number to check out:- "))
          roo = ra
          ch = out()
          if roo in ch :
           su = str(input("are you sure y or n :- ")).lower()
           if su == 'y':
            insert = "UPDATE rooms SET avalable=%s WHERE room=%s"
            val = (0,roo)
            cur.execute(insert,val)
            it = "UPDATE coustomer SET checkout=%s WHERE room=%s"
            vv = (date,roo)
            cur.execute(it,vv)
            print("check out sucessfully")
            
           else:
              continue
          else:
              print("please check room number")
              continue
    elif log == 1110:
     print("enter 1 for detail of one person")
     print("enter 2 for seeing how many person come more than one")
     print("enter 3 for detail of employ")
     print("enter 4 for total revenue")
     n = int(input("enter number what you want to see:- "))
     getdata(n)
    elif log == 000 :
        chout = "SELECT * FROM coustomer WHERE checkout=%s or room=%s" 
        vval = (date,0)
        cur.execute(chout,vval)
        oo = cur.fetchall()
        for row in oo:
              print(row)
    else:
       continue
     
        
    
cur.close()
            
            

     
 
     
     
      
  
        

