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

@app.route('/output1/' , methods=['GET','POST'])
def output1():
    input2 = str(request.form['str2']);  
    input3 = str(request.form['str3']); 
    input4 = str(request.form['str4']);  
    model = word2vec.Word2Vec.load_word2vec_format('static/text.model.bin', binary=True)
    #res1 = model.most_similar((input2,input3),input4,topn=5);
    res1 = model.most_similar(positive=[input2, input3], negative=[input4],topn=5);
    return render_template('output1.html', input1=res1)

@app.route('/output2/' , methods=['GET','POST'])
def output2():
    input5 = str(request.form['str5']);  
    input6 = str(request.form['str6']);  
    input7 = str(request.form['str7']);
    input8 = str(request.form['str8']); 
    model = word2vec.Word2Vec.load_word2vec_format('static/text.model.bin', binary=True)
    res2 = model.doesnt_match((input5,input6,input7,input8));
    return render_template('output2.html', input1=res2)	
	
	
if __name__=='__main__':
    app.run()
