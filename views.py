from flask import Flask , render_template , request , make_response

from myproject import application ,db
from models import User

@application.route("/")
def main():
    return render_template('index.html')

@application.route('/user/create/' , methods = ['POST'])
def create_agent():
    '''
        User registeration
    '''
    try:
        # import pdb; pdb.set_trace()
        user = User.query.filter(User.email == request.form['email']).first()
        if not user:
            user = User(name= request.form['name'],
                        email = request.form['email'],
                        password = request.form['password'])
            db.session.add(user)
            db.session.commit()
            response = make_response('' , 200)
        else:
            response = make_response('',503)
            response.headers['message'] = 'User exist'
        return response
    except Exception,e:
        print e
        response = make_response('',500)
        response.headers['message'] = 'Something went wrong'
        return response


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
