from Rules.reuseableSQL import ReuseSQL
"""
pseudocode for content filtering

1. Categorys gaan pakken
2. Orders/events pakken 
2a/ populaire producten pakken
2b/ genders pakken
2c/ prijzen pakken
2d/ brand pakken
2e/ product name pakken
2f/ variant pakken?
2g/ aanbieding pakken/folder actief
3. query analyseren
4. visitors en products aan linken in koppeltabel similars
5. recommendations geven

"""

class ContentRules():

    SQL_Commands = ["SELECT visitors_idvisitors, sessions_idsessions FROM {};",
                    "SELECT idproducts, name ,brand, category, price,doelgroep,target FROM products ORDER BY category ASC;",
                    "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};",
                    "INSERT INTO similars VALUES ({},{});"]

    def ContentFiltering(self):
         



        for command in SQL_Commands:
            
            
            
            pass



        pass
    pass



   






