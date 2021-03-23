from reuseableSQL import ReuseSQL
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

class ContentRules:



    def ContentFiltering(self):

        SQL_Commands = ["SELECT idproducts, name ,brand, category, price,doelgroep,target FROM products ORDER BY category ASC;",
                        "SELECT category FROM products GROUP BY category;",
                        "SELECT products_idproducts FROM {} o JOIN sessions s on s.idsessions = o.sessions_idsessions WHERE s.idsessions = {};",
                        "INSERT INTO {} VALUES ({},{});"]

        SQLObj = ReuseSQL()
        product_data = SQLObj.SQL_Select(SQL_Commands[0])

        uniquecategorys = SQLObj.SQL_Select(SQL_Commands[1])
        
        for categorys in uniquecategorys:
            products = self.filter_products_using_categorys(categorys, product_data)
            for product in products:
                for product2 in products:
                    if product != product2:
                        additionals = ["similarsproduct",product[0],product2[0]]
                        SQLObj.SQL_Insert(SQL_Commands[3].format(*additionals))
                        print("Insert into table {} inserted {} and {}".format(*additionals))


    def filter_products_using_categorys(self,category, products):

        filtered_products = []
        for product in products:
            if product[3] in category:
                filtered_products.append(product)
        return filtered_products
    pass


ContentOBJ=ContentRules()
ContentOBJ.ContentFiltering()
   






