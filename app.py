from flask import Flask,url_for,render_template, flash, request, redirect
from wtforms import Form
from gensim.models import word2vec
import gc
import os


app=Flask(__name__)

@app.route('/') 
def hello():
    return render_template('home.html');



@app.route('/output/' , methods=['GET','POST'])
def output():
    input1 = str(request.form['str'])   
    model = word2vec.Word2Vec.load_word2vec_format('static/text.model.bin', binary=True)
    res = model.most_similar(input1,topn=5)
    return render_template('output.html', input1=res)	
    
	
	
if __name__=='__main__':
    app.run()
