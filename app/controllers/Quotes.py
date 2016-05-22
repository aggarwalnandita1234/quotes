
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)

        self.load_model('Quote')
        self.db = self._app.db

   
    def dashboard(self):
        quotes=self.models['Quote'].get_quotes()
        info={'user_id': session['id']}
        favs=self.models['Quote'].show_favorites(info)
        print "lets see what favs is", favs
        return self.load_view('dashboard.html', quotes=quotes, favs=favs)


    def create_quote(self):
        quote_info={
            'author': request.form['author'],
            'message':request.form['message'],
            'user_id':session['id']
        }
        print session['id']
        create_status=self.models['Quote'].insert_quote(quote_info)
        if create_status['status'] == True:
 
            return redirect('/dashboard')
        else:
            for message in create_status['errors']:
                flash(message, 'quote_errors')
                return redirect('/dashboard')

    def favorites(self):

        quote_info={
            'quote':request.form['quote']
        }
        quote_id=self.models['Quote'].get_quote_id(quote_info)[0]['id']

        fav_info={
            'user_id':request.form['user_id'],
            'quote_id':quote_id,
            'favorites_of':session['id']
        }

        insert_fav=self.models['Quote'].insert_favorites(fav_info)
       

        return redirect('/dashboard')

    def delete(self):
        delete_info={'author':request.form['author']}
        self.models['Quote'].delete_favorites(delete_info)
        return redirect('/dashboard')





