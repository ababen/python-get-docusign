import requests

from flask import Flask, session
from flask_oauth import OAuth

# import docusign_authenticate.py

app = Flask(__name__)

# ----------------------------- KEYS GO HERE -------------------------------------------
# Once authorization_token is retrieved, get user_info: https://developers.docusign.com/esign-rest-api/guides/authentication/user-info-endpoints

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/authenticate')
def authenticate():
    # return requests.get('http://example.com').content
    # return requests.get("http://www.google.com")

@app.route("/proxy-example")
def proxy_example():
    r = requests.get("http://example.com/other-endpoint")
    return Response(
        r.text
        status = r.status_code,
        content_type = r.headers['content-type'],
    )

@app.route('/callback', code)
def callback():
    return code

oauth = OAuth()
    # Information on Flask-OAuth https://pythonhosted.org/Flask-OAuth/
    docusign = oauth.remote_app('docusign',
                                oauth_base_url = "account-d.docusign.com",
    )
    return None

# #https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-implicit
