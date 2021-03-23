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
                        "SELECT COUNT(idvisitors), typevisitors FROM visitors GROUP BY typevisitors ORDER BY typevisitors ASC;"
                        "SELECT visitors_idvisitors, sessions_idsessions FROM {};"
                        "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};",
                        "INSERT INTO {} VALUES ({},{});"]        
        
        SQLObj = ReuseSQL()
        visitor_data = SQLObj.SQL_Select(SQL_Commands[0])

        
        products = []
        for data in visitor_data:
            
            additional = ["orders"]
            order_data = SQLObj.SQL_Select(SQL_Commands[2].format(*additional))
            pass

        for data in visitor_data:
            for product in []:
                pass
            additional = ["content",visitor_data[0],]
            ReuseSQL.SQL_Insert(SQL_Commands[4].format)
            pass


        pass

CollabObj=CollabRule()
CollabObj.Collabritieve_Filter()
