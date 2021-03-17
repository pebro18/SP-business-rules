import psycopg2
from _functions.config import config



class ReuseSQL():
    

    def OpenConnection(self):
        db = config()
        con = psycopg2.connect(**db)
        return con

    def CloseConnection(self, con, cur):
        cur.close()
        con.close()

    def SQL_Select(self,columm, table):

        sqlstring = "SELECT {} ".format()
        con = OpenConnection()
        cur = con.cursor()
        cur.execute(sqlstring)

        rows = cur.fetchall()
        return rows

    def SQL_Insert(self,table,data):
        sqlstring = "".format()
        con = OpenConnection()
        cur = con.cursor()
        cur.execute(sqlstring)
        con.commit()
        CloseConnection(con,cur)
        pass
    
    
    pass