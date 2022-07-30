import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='blog')

def addData(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into blog_details (name,username,password) values(%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

# create blog start

def addDataCreate(tc):
    con=getConnection()
    cur=con.cursor()
    query="insert into blog_post (title,content) values(%s,%s)"
    cur.execute(query,tc)
    con.commit()
    con.close()

# create blog end 

# update blog start

def addDataUpdate(tu):
    con=getConnection()
    cur=con.cursor()
    queryu="update blog_post set title=%s,content=%s where id=%s"
    cur.execute(queryu,tu)
    con.commit()
    con.close()

# update blog end 

def fetchData():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from blog_post")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist


def specificData(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from blog_post where id=%s",(id))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]
    

def deleteData(id):
    con=getConnection()                  
    cur=con.cursor()
    queryd="delete from blog_post where id=%s"
    cur.execute(queryd,(id))
    con.commit()
    con.close()
    