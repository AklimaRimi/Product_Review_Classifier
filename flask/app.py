from flask import Flask ,render_template, request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def page():

    if request.method == "POST":
        text = request.form['text']
        response = requests.post("https://rimi98-reviewclassifier.hf.space/run/predict", json={
            "data": [
                text
            ]
        }).json()

        data = response["data"]
        result = data[0]['label']
        print(result+'\n\n\n\n\n\n')
        return render_template('review-detect.html',text = text,result = result)
    else:
    
        return render_template('review-detect.html',text='',result='')


if __name__=='__main__':
    app.run()
