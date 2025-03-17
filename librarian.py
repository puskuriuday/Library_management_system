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


    def cte_student(name,mail,password):
        
        ...
    



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
Librarian.Logout()