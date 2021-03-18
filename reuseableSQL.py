from _functions.config import config
import psycopg2

class ReuseSQL:
    
    def __init__(self):
        pass

    def openconnection(self):
        db = config()
        con = psycopg2.connect(**db)
        return con

    def CloseConnection(self, con, cur):
        cur.close()
        con.close()

    def SQL_Select(self,sqlstring):
        con = self.openconnection()
        cur = con.cursor()
        cur.execute(sqlstring)
        rows = cur.fetchall()
        self.CloseConnection
        return rows

    def SQL_Insert(self,sqlstring):
        con = self.openconnection()
        cur = con.cursor()
        try:
            cur.execute(sqlstring)
        except:
            pass
        con.commit()
        self.CloseConnection(con,cur)
        pass
       
    pass