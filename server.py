from flask import Flask, url_for
from flask import request

app = Flask(__name__)


from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        f.required_methods = ['OPTIONS']
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/")
def index():
    return "Index Page"

@app.route("/add", methods=['GET'])
def add_page():
    return "added"

@app.route("/addmore", methods=['POST'])
@crossdomain(origin='*')
def add_more_page():
    print(request)
    xx = request.form['param2']
    print(xx)
    #a = request
    #b = a.args
    return "added more2:"+xx


@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/user/<username>")
def show_user_profile(username):
    return "User {0}".format(username)

@app.route("/post/<int:postid>")
def show_post(postid):
    return "Post ID: {0}".format(postid)

@app.route("/projects/")
def projects():
    return "Projects Page"

@app.route("/about")
def about():
    return "About page"

if __name__ == "__main__":
    app.debug = True
    app.run()