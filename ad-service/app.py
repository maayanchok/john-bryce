from flask import Flask, jsonify, Response
app = Flask(__name__)
import json

JSON = [
        {'image_url':"./1.jpg", "text":"text1", "link":"https://google.com"},
        {'image_url':"./2.jpg", "text":"text2", "link":"https://google.com"},
        {'image_url':"./3.jpg", "text":"text3", "link":"https://google.com"}
    ]


@app.route('/ads')
def ads():
    r=Response()
    r.headers["Content-type"]= "aaplication/json"
    return json.dumps(ads)

if __name__=="__main__":
    app.run(debug=True)