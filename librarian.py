from database import *
class Librarian:

    crt_incharge = None

    @classmethod
    def Login(cls,mail,password):
        try:
            conn , cur = dbconn()
            query = 'select * from librarian where mail = %s'
            cur.execute(query,(mail,))
            member = cur.fetchone()
            if member:
                if password == member[3]:
                    cls.crt_incharge = member[1]
                    print("login " , member[1])
                else:
                    print("invalid Password")
            else:
                print("Ivalild E-mail")
            clscur(cur)
            clsconn(conn)
        except Exception as error:          
            print(error)

    @classmethod
    def cte_student(cls,roll_no,name,mail,password = None):
        try:
            if not cls.crt_incharge:
                print("Login first..")
            else:
                conn , cur = dbconn()
                query = 'select * from students where roll_no = %s'
                cur.execute(query,(roll_no,))
                member = cur.fetchone()
                if member:
                    print("Roll Number already exits!!")
                else:
                    query = 'select * from students where mail = %s'
                    cur.execute(query,(mail,))
                    member = cur.fetchone()
                    if member:
                        print("Mail already exits!!")
                    else:
                        if not password:
                            password = roll_no
                        query = 'insert into students(roll_no,name,mail,password) values(%s,%s,%s,%s)'
                        cur.execute(query,(roll_no,name,mail,password,))
                        comm(conn)
                        clscur(cur)
                        clsconn(conn)
                        print("created student successfully!!!")
        except Exception as e:
            print(e)
    
    @classmethod
    def upd_stu(cls,roll_no,attr,value):
        try:
            if not cls.crt_incharge:
                print('login first')
            else:
                conn , cur = dbconn()
                query = 'select * from students where roll_no = %s'
                cur.execute(query,(roll_no,))
                mem = cur.fetchone()
                if not mem:
                    print("Invalid Roll Number")
                else:
                    query = f'update students set {attr} = %s where roll_no = %s'
                    cur.execute(query,(value,roll_no,))
                    print("updated successfully !!!")
                    comm(conn)
                    clscur(cur)
                    clsconn(conn)
        except Exception as e:
            print(e)




    @classmethod
    def Logout(cls):
        if cls.crt_incharge != None:
            cls.crt_incharge = None
            print("logout successfully")
        else:
            print('no login so no logout')




mail = "raju123@gmail.com"
password = 'RajuXgw'
Librarian.Login(mail,password)
print()
print()
print()
Librarian.upd_stu('22X01A6245','mail','22x01a6245@gmail.com')
print()
print()
print()
Librarian.Logout()