import pickle
from flask import Flask,render_template,request
from flask_cors import cross_origin
import sklearn


app=Flask(__name__)

model = pickle.load(open('model_upd.pkl','rb'))


@app.route("/")
@cross_origin()
def home():
    return render_template("basic.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        #gender
        sex=request.form['gn']
        if sex=='M':
            sex=1
        else:
            sex=0
        #sslc percentage
        sslc=float(request.form['sslcp'])

        #PUC percentage
        puc=float(request.form['pup'])

        #degree percentage
        degree=float(request.form['degp'])

        #enterance exam
        ent=float(request.form['etest'])

        #mba percentage
        mba=float(request.form['mbap'])

        #pucstream
        pucstream=request.form['pu_s']
        if pucstream=='Commerce':
            pucstream=2
        elif pucstream=='Science':
            pucstream=1
        else:
            pucstream=0


        #Dedree Stream
        degstream=request.form['deg_s']
        if degstream=='Comm&Mgmt':
            degstream=2
        elif degstream=='Sci&Tech':
            degstream=1
        else:
            degstream=0

        #Work Exp
        work_exp=request.form['w_exp']
        if work_exp=='Yes':
            work_exp=1
        else:
            work_exp=0

        #MBA specialisation
        mbas=request.form['mba_s']
        if mbas =='Mkt&HR':
            mbas=1
        else:
            mbas=0

        prediction=model.predict([[sslc,puc,degree,ent,mba,pucstream,degstream,sex,work_exp,mbas]])
        output=prediction[0]
        #print(output)

        #if output=='Placed':
    return render_template("basic.html",text="Congrats you are {}!!!!!".format(output))
        #else:
         #   return render_template("basic.html",text="Sorry your placement status is {}  ".format(output))
    #return render_template("basic.html")















