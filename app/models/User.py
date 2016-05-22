""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re


class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['name']:
            errors.append('First Name cannot be blank')

        elif len(info['name']) < 2:
            errors.append('First Name must be at least 2 characters long')
        
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:

            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
   
            query_insert="INSERT INTO users (name, alias, email, password) VALUES (:name, :alias, :email, :password)"
            data={'name':info['name'],'alias':info['alias'], 'email':info['email'],'password':pw_hash}
            self.db.query_db(query_insert, data)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
    
            status = { "status": True, "user": users[0] }
            return status

    def login(self, info):

        errors = []

        query_login = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }

        user = self.db.query_db(query_login, data)

        if user == []:
            print "no user"
            errors.append('Invalid login!')
            return{"status": False, "errors": errors}
        else:
            if self.bcrypt.check_password_hash(user[0]['password'], info['password']):
                print "password matched"
                return {"status": True, "user": user[0] }
            else:
                print "password not matched"
                errors.append('Invalid login!')
                return{"status": False, "errors": errors}

    def quote_info(self, user_id):
        query= "select quotes.quote, quotes.author FROM quotes WHERE quotes.user_id=:id"
        data={'id':user_id['user_id']}
        return self.db.query_db(query, data)

    def user_info(self, user_id):
        query="select users.name as name,  count(quotes.author) as count from quotes JOIN users on quotes.user_id=users.id where users.id=:id "
        data={'id':user_id['user_id']}
        print "data in model is", data
        return self.db.query_db(query, data)



