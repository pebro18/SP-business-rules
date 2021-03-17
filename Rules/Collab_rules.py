from classes.send_data import DataSender

"""
pseudocode for collab filtering

1. visitors en sessions pakken of builds pakken
2a type visitor
2b/ events pakken
2c/ similars?
2d/ upselling duurdere variant verkopen
2e/ crossselling aan verwanten producten
2f/ deepselling meer verkopen aan soort gelijken producten
2g/ kijken naar sessions over de financieel situatie
3. linken in koppeltabel content
4. recommandaties geven
"""




class CollabRule():
    SQL_Commands = ["",
                    "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};",
                    "INSERT INTO content VALUES ({},{});"]
    
    def Collabritieve_Filter():
        pass


    pass
