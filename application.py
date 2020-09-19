from flask import Flask, render_template,request,make_response
from flask_compress import Compress
from flask_caching import Cache

config= {
    "DEBUG" : True,
    "CACHE_TYPE" : "simple",
    "CACHE_DEFAULT-TIMEOUT" : 300,
    "SEND_FILE_MAX_AGE_DEFAULT" : 31536000
}

application = Flask(__name__)
application.config.from_mapping(config)
COMPRESS_MIMETYPES=['text/html','text/css','text/javascript']
COMPRESS_LEVEL=6
COMPRESS_MIN_SIZE=500
Compress(application)
cache=Cache(application)


@application.route('/')
@cache.cached(timeout=5185000)
def Home():
    res=make_response(render_template("index.html"))
    res.cache_control.max_age=31536000
    return res

@application.route('/team')
def Team():
    return render_template("team.html")

@application.route('/journey')
def Journey():
    return render_template("journey.html")

@application.route('/solution')
def solution():
    return render_template("solutions.html")

@application.route('/donate')
def donate():
    return render_template("donate.html")

@application.route('/govtAlliance')
def Alliances():
    return render_template("govAlliances.html")

@application.route('/donors')
def Donors():
    return render_template("donors.html")

@application.route('/knowledgePartners')
def knowledgePartners():
    return render_template("knowledgePartners.html")

@application.route('/partners')
def Partners():
    return render_template("partners.html")

if __name__=='__main__':
    application.run(debug=True)
