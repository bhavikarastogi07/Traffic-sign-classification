from flask import Flask,render_template,redirect,request
import signPredictor

app= Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/',methods=['POST'])
def getp():
    if request.method=='POST':
        f=request.files['userfile']
        path="./static/{}".format(f.filename)
        f.save(path)
        
        sign=signPredictor.predict_sign(path)
        


        result_dict={
            'image': path,
            'sign' : sign

        }

        return render_template("index.html", trafficPred=result_dict)


    
if __name__=='__main__' :
    app.run(debug=True)