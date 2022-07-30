from flask import Flask,request,redirect,render_template,session
from dbms import *
import pymysql as p

app=Flask(__name__)

app.secret_key="abc"

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='blog')


#First Routing
@app.route("/")
def home_func():
    return render_template('login.html')


@app.route("/register")
def register_func():
    return render_template("register.html")


@app.route("/savelink",methods=["POST", "GET"])
def save_func():
    n=request.form['name']
    u=request.form['username']
    p=request.form['password']
    t=(n,u,p)
    addData(t)
    return redirect("/login")


@app.route("/login")
def login_func():
    return render_template("login.html")


@app.route("/savelink1",methods=["POST"])
def login_save():
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password=request.form['password']
        con=getConnection()
        cur=con.cursor()
        cur.execute("select * from blog_details where username=% s AND password=% s",(username,password))
        result=cur.fetchone()
        if result:
            session['k']=True
            return redirect('/home')
        else:
            return render_template('login.html') 
    
    return redirect("/home")


@app.route('/home')
def home():
    datalist=fetchData()
    return render_template('home.html',data=datalist)


@app.route('/category')
def category():
    return render_template('category.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route("/savecreate",methods=["POST", "GET"])
def save_create():
    t=request.form['title']
    c=request.form['content']
    tc=(t,c)
    addDataCreate(tc)
    return render_template("blog.html")


@app.route("/show")
def allpost():
    return render_template('allpost.html')


@app.route('/allpost')
def show_func():
    datalist=fetchData()
    return render_template("allpost.html",data=datalist)
    

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/logout')
def logout_func():
    session.pop('username',None)
    session.pop('password',None)
    return render_template('login.html')


@app.route("/edit/<int:id>")
def displayforupdate(id):
    datalist=specificData(id)
    return render_template("edit.html",data=datalist)


@app.route("/update/<int:id>",methods=["POST"])
def updatefun(id):
    n=request.form['name']
    u=request.form['username']
    tu=(n,u,id)
    addDataUpdate(tu)
    return redirect("/allpost")


@app.route("/delete/<int:id>")
def deletefun(id):
    deleteData(id)
    return redirect("/allpost") 

# image click start

@app.route("/ganesh")
def ganesh():
    datalist=fetchData()
    return render_template("ganesh.html",data=datalist)

# image click end  

# user post 1 start

@app.route("/userpost1")
def userpost1():
    datalist=fetchData()
    return render_template("userpost1.html",data=datalist)

# user post 1 end 

# user post 2 start

@app.route("/userpost2")
def userpost2():
    datalist=fetchData()
    return render_template("userpost2.html",data=datalist)

# user post 2 end 


if __name__=='__main__':
     app.run(debug=True)
