from flask import Flask , render_template
application = Flask(__name__, static_folder = 'frontend' , template_folder = 'frontend')

@application.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
