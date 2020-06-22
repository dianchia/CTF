from flask import Flask, flash, request, redirect, url_for, send_from_directory
import subprocess
import os
from werkzeug.utils import secure_filename

upload_folder = '/home/flask/uploads'
allowed_extensions = {'hs'}
app = Flask(__name__)
app.config['upload_folder'] = upload_folder

if __name__ == "__main__":
    app.run(host='0.0.0.0')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/submit', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload_folder'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Submit homework</title>
    <h1>Submit your assignment here</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    results = open("/home/flask/uploads/" + filename + "_results.txt","w")
    for i in filename:
        if not i.isalpha() and i != ".":
            return '''
            <!doctype html>
            <title>Error</title>
            <h1>Internal Server Error. Please try again.
            '''

    subprocess.run(["ghc","--make","/home/flask/uploads/"+filename],stdout=results,stderr=results,stdin=results)
    subprocess.run(["/home/flask/uploads/"+filename.split(".")[0]],stdout=results,stderr=results,stdin=results)
    return send_from_directory(app.config['upload_folder'],filename+"_results.txt")

@app.route('/')
def home():

    return '''
    <!doctype html>
    <title>Homepage</title>
    <h1>Welcome to Functional Programming 220!</h1> 
    <p>During this semester we're going to learn the ins and outs of functional programming languages using Haskell</p>
    <p>Why use a functional language? Because everything is a function! Functions can take other functions as inputs and return them as output.</p>
    <p>This is known as a "higher order function". Through the semester we're going to learn about Functors, Applicatives, and Monads. These are all abstractions that allow us to work better with higher order functions. However, these are all down the road.</p>
    <p>For now we're just going to start with the basics of arithmetic and function declaration. You can find your first <a href="/homework1">homework here.</a></p>
    <p>As we discussed in class, your submissions will be automatically graded because I'm lazy. The homework instructions will specify the exact output that is expected. If you try to cheat this with putStrLn statements then you will receive a zero. You can find the submission link on the homework 1 page.</p>
    
    <h1>Resources</h1>
    <p>Here are some resources that you may find helpful in completing your assignments.</p>
    <p>Our book for the course (free!): http://learnyouahaskell.com/chapters</p>
    <p>The complete Haskell package repository. You can expect any necessary packages to be on the grading system: https://hackage.haskell.org/</p>
    <p>
    '''
@app.route('/homework1')
def homework1():
    return '''
    <!doctype html>
    <title>Homework 1</title>
    <p>Welcome to your first homework assignment! Your problems are as follows.</p>
    <p>1) A function called "fib" that outputs the Fibonacci sequence. I will be checking for the first 100 numbers formatted as "1 1 3 ...".</p>
    <p>2) A function called "range" that takes 2 numbers and returns a flat list containing all the integers in that range. Example: range 1 5 outputs [1,2,3,4,5]</p>
    <p>3) A function called "grey" that takes a number as input and returns all of the codes for that n-bit number. Ex: grey 3 outputs ['000','001','011','010',110,111,101,100]. You can find more information about grey codes here: https://en.wikipedia.org/wiki/Gray_code"
    <p>All of your functions must have the types correctly declared. I'll give you number one for free, as an example: fib :: Int -> Int -> [Int]</p>
    <h2>You can submit your homework <a href="/upload">here.</a></h2>
    <p>Only Haskell files are accepted for uploads. Learned that one the hard way last semester...</p>
    <p>Your file will be compiled and ran and all output will be piped to a file under the uploads directory.</p>
    '''
