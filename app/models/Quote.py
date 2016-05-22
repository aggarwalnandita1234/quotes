""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()
    

    def get_quotes(self):
        query = "SELECT quotes.*, users.name as name from quotes JOIN users ON quotes.user_id=users.id"
        return self.db.query_db(query)

    def insert_quote(self, quote_info):
        errors = []
        if len(quote_info['author']) < 3:
            errors.append('Author name cannot be that short, dont know why')
        elif len(quote_info['message'])<10:
            errors.append('Quote cannot be that short')
        if errors:
            return {"status": False, "errors": errors}

        else:

            query="INSERT INTO quotes (author, quote, user_id) VALUES (:author, :quote, :user_id)"
            data2={
                'author':quote_info['author'],
                'quote':quote_info['message'],
                'user_id':quote_info['user_id']
            }
            
            inserted=self.db.query_db(query, data2)
            return { "status": True}

    def get_quote_id(self, quote_info):
        query="SELECT id FROM quotes WHERE quote=:quote"
        data={'quote': quote_info['quote']}
        return self.db.query_db(query, data)



    def insert_favorites(self, fav_info):
        query="INSERT INTO favorites (user_id, quote_id, favorites_of) VALUES (:user_id, :quote_id, :favorites_of)"
        data={
            'user_id':fav_info['user_id'],
            'quote_id':fav_info['quote_id'],
            'favorites_of':fav_info['favorites_of']
        }
        print data
        return self.db.query_db(query, data)

    def show_favorites(self, info):
        query="SELECT * FROM favorites WHERE favorites_of=:id"
        data={'id': info['user_id']}
        result=self.db.query_db(query, data)
        if result:
            query1="SELECT users.name, users.id as user_id, quotes.quote, quotes.author FROM favorites JOIN quotes ON favorites.quote_id=quotes.id JOIN users ON quotes.user_id=users.id WHERE favorites.favorites_of=:id"
            return self.db.query_db(query1, data)
        else:
            return None


    def delete_favorites(self, delete_info):
        print delete_info
        query1="select quotes.id from quotes where quotes.author=:author"
        data1={'author':delete_info['author']}
        quote_id=self.db.query_db(query1, data1)[0]
        print "is this quote_id", quote_id

        query2="DELETE FROM favorites WHERE favorites.quote_id=:quote_id"
        data2={'quote_id':quote_id['id']}
        return self.db.query_db(query2, data2)












