from ice_breacker import ice_brack 
from flask import Flask , request , jsonify , render_template


app = Flask(__name__)



@app.route("/" , methods = ["GET"])
def default():
    return render_template("index.html")


@app.route("/process" , methods = ["POST"])
def process():
    name = request.form['name']

    person_info,profile_pic_url = ice_brack(name=name)


    return jsonify (
        {
        'summary':person_info.summary,
        'facts':person_info.facts,
        'topic_of_instret':person_info.topic_of_instret,
        'ice_brackers':person_info.ice_brackers,
        'profile_pic_url':profile_pic_url
        }
    )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0" , debug = True)