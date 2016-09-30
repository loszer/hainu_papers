import web
import sqlite3

# use sqlite instead of mysql
# db = web.Database.open()

def getPapersByPages(limit, page_num):
    conn = sqlite3.connect('./mock/data.db')
    c = conn.cursor()
    # query data by pages
    res = c.query("select * form papers where 1 order by create_time DES limit "+page_num+"")
    conn.commit()
    conn.close()
    pass

def createUser():
    pass

def getUser():
    pass

def updateUser():
    # update some existed property
    pass

def login(username, passwd):
    # the better method is using the token instead of username and password
    conn = sqlite3.connect('./mock/data.db')
    c = conn.cursor()
    res = c.query("select * from users where username = '"+username+"' and password = '"+passwd+"' ")
    conn.close()
    pass

def logout():
    # delete the session: 
    pass