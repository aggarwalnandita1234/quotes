"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('index.html')

    def create(self):
        
        user_info = {
             "name" : request.form['form-first-name'],
             "alias": request.form['form-last-name'],
             "email": request.form['form-email'],
             "password":request.form['form-password'],
             "pw_confirmation" : request.form['form-conf-password']
        }


        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['name']  
            return redirect('/dashboard')
        else:

            for message in create_status['errors']:
                flash(message, 'regis_errors')

            return redirect('/')

    def login(self):

        user_info = {
            "email" : request.form['form-email'],
            "password" : request.form['form-password']
        }
        print "before calling create_status"
        create_status = self.models['User'].login(user_info)
        print "after calling create_status"
        if create_status['status'] == True:
            print "we are in create_status=True"
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            print session['id']
            return redirect('/dashboard')
        else:

            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def user_show(self, id):
        print "nandita is printing", id
        
        user_id={'user_id': id}
        print "user_id is:", user_id
        user_info=self.models['User'].user_info(user_id)[0]

        quotes=self.models['User'].quote_info(user_id)
        return self.load_view('user_show.html', quotes=quotes, user_info=user_info)

    def logout(self):
        if session:
            session.clear()
            return redirect('/')





