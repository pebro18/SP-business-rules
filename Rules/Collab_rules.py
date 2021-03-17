from Rules.reuseableSQL import ReuseSQL

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
    SQL_Commands = ["SELECT idvisitors, typevisitors FROM visitors WHERE idvisitors = {};",
                    "SELECT COUNT(idvisitors), typevisitors FROM visitors GROUP BY typevisitors ORDER BY typevisitors ASC;"
                    "SELECT visitors_idvisitors, sessions_idsessions FROM {};"
                    "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};",
                    "INSERT INTO content VALUES ({},{});"]
    
    def Collabritieve_Filter():
        
        buids_data = ReuseSQL.SQL_Select(SQL_Commands[2])

           
        for x in buids_data:
            
            tablename = ["orders",]
            order_data = ReuseSQL.SQL_Select(SQL_Commands[3].format(*tablename))
            tablename = ["events"]
            events = ReuseSQL.SQL_Select(SQL_Commands[3].format(*tablename))

            pass

        pass


    pass
