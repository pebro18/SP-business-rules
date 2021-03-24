from reuseableSQL import ReuseSQL


"""
pseudocode for collab filtering

1. visitors en sessions pakken of builds pakken
2a type visitor
2b/ events pakken
2c/ similars?
2d/ upselling duurdere variant verkopen
2e/ crossselling aan verwanten producten
2f/ deepselling meer verkopen aan soort gelijken producten
2g/ kijken naar sessions over de financieel situatie <- misschien niet echt ethics
3. linken in koppeltabel content
4. recommandaties geven
"""


class CollabRule():
   
    def Collabritieve_Filter():
        SQL_Commands = ["SELECT idvisitors, typevisitors FROM visitors;",
                        "SELECT idsessions,identifier FROM sessions;"
                        "SELECT COUNT(idvisitors), typevisitors FROM visitors GROUP BY typevisitors ORDER BY typevisitors ASC;"
                        "SELECT visitors_idvisitors, sessions_idsessions FROM {} WHERE visitors_idvisitors = {};",
                        "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};"]        
        
        SQLObj = ReuseSQL()
        visitor_data = SQLObj.SQL_Select(SQL_Commands[0])
        session_data = SQLObj.SQL_Select(SQL_Commands[1])
        
        for session in session_data:           
            additional = ["events",session[0]]
            event_data += SQLObj.SQL_Select(SQL_Commands[4].format(*additional))
            self.Send_Data(event_data)
            pass
        pass

    def Send_Data(self,events,):

        Send_Command = "INSERT INTO {} VALUES ({},{});"
        products = self.get_products_based_on_type()
        for product in products:
            additional = ["content",visitor, product]
            ReuseSQL.SQL_Insert(Send_Command.format(*additional))
            pass

    def get_products_based_on_type(self,type,events):

        SQL_Command = ""
        additional = ["events",session[0]]
        SQLObj.SQL_Select(SQL_Commands[4].format(*additional))
        return None

CollabObj=CollabRule()
CollabObj.Collabritieve_Filter()
