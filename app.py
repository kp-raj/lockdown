import os, json, requests, hashlib
import psycopg2
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
'''
DATABASE_URL = 'postgres://muzdyqyc:FFhyjH8odvCSIpj8tlj-ZCopCknLjJEt@queenie.db.elephantsql.com:5432/muzdyqyc'
'''
DATABASE_URL='postgres://ldifxbgmuxhhyi:84ac0f3dd8a0145c59e55de4d4e63f42a4ab57f4b0c249a0d6343f00f405d2dc@ec2-3-234-85-177.compute-1.amazonaws.com:5432/d639pt0rh5buqn'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def display(type):
    if type=='movies':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("Select * from movies;")
                movies=cursor.fetchall()
                movies=sorted(movies,key=lambda x:x[4],reverse=True)
                return movies
    if type=='books':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("Select * from books;")
                books=cursor.fetchall()
                books=sorted(books,key=lambda x:x[4],reverse=True)
                return books
    if type=='shows':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("Select * from shows;")
                shows=cursor.fetchall()
                shows=sorted(shows,key=lambda x:x[4],reverse=True)
                return shows

@app.route('/', methods=['GET'])
def index():
    movies=display('movies')
    return render_template('home.html',display=movies,type='movies',base='home')
@app.route('/books', methods=['GET'])
def books():
    books=display('books')
    return render_template('home.html',display=books,type='books',base='home')
@app.route('/shows', methods=['GET'])
def shows():
    shows=display('shows')
    return render_template('home.html',display=shows,type='shows',base='home')

@app.route('/email', methods=['GET'])
def email():
    return render_template('email.html',message='',base='email')

@app.route('/add',methods=['GET'])
def add():
    email_hash=request.args.get('email')
    type=request.args.get('type')
    name1=(request.args.get('name1').lower()).replace("'","")
    name2=request.args.get('name2').lower().replace("'","")
    name3=request.args.get('name3').lower().replace("'","")
    name4=(request.args.get('name4').lower()).replace("'","")
    name5=request.args.get('name5').lower().replace("'","")
    if name1!='':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("select * from "+type+" where name like '%"+name1+"%';")
                count=1
                results=cursor.fetchone()
                if results==None: length=0
                else:
                    length=len(results)
                if length!=0:
                    count=(results[4])+1
                    cursor.execute("update "+type+" set count="+str(count)+" where id=(select id from "+type+" where name like '%"+name1+"%' order by id limit 1);")
                    conn.commit()
                else:
                    year1=request.args.get('year1').lower()
                    language1=(request.args.get('language1')).lower()
                    cursor.execute("insert into "+type+" (name,year,language,count) values(%s,%s,%s,'1');",(name1,str(year1),language1))
            conn.commit()
    if name2!='':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("select * from "+type+" where name like '%"+name2+"%';")
                count=1
                results=cursor.fetchone()
                if results==None: length=0
                else:
                    length=len(results)
                
                if length!=0:
                    count=(results[4])+1
                    cursor.execute("update "+type+" set count="+str(count)+" where id=(select id from "+type+" where name like '%"+name2+"%' order by id limit 1);")
                    conn.commit()
                else:
                    year2=(request.args.get('year2')).lower()
                    language2=(request.args.get('language2')).lower()
                    cursor.execute("insert into "+type+" (name,year,language,count) values(%s,%s,%s,'1');",(name2,str(year2),language2))
            conn.commit()
    if name3!='':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("select * from "+type+" where name like '%"+name3+"%';")
                count=1
                results=cursor.fetchone()
                if results==None: length=0
                else:
                    length=len(results)
                
                if length!=0:
                    count=(results[4])+1
                    cursor.execute("update "+type+" set count="+str(count)+" where id=(select id from "+type+" where name like '%"+name3+"%' order by id limit 1);")
                    conn.commit()
                else:
                    year3=(request.args.get('year3')).lower()
                    language3=(request.args.get('language3')).lower()
                    cursor.execute("insert into "+type+" (name,year,language,count) values(%s,%s,%s,'1');",(name3,year3,language3))
            conn.commit()
    if name4!='':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("select * from "+type+" where name like '%"+name4+"%';")
                count=1
                results=cursor.fetchone()
                if results==None: length=0
                else:
                    length=len(results)
                
                if length!=0:
                    count=(results[4])+1
                    cursor.execute("update "+type+" set count="+str(count)+" where id=(select id from "+type+" where name like '%"+name4+"%' order by id limit 1);")
                    conn.commit()
                else:
                    year4=(request.args.get('year4')).lower()
                    language4=(request.args.get('language4')).lower()
                    cursor.execute("insert into "+type+" (name,year,language,count) values(%s,%s,%s,'1');",(name4,str(year4),language4))
            conn.commit()
    if name5!='':
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("select * from "+type+" where name like '%"+name5+"%';")
                count=1
                results=cursor.fetchone()
                if results==None: length=0
                else:
                    length=len(results)
                
                if length!=0:
                    count=(results[4])+1
                    cursor.execute("update "+type+" set count="+str(count)+" where id=(select id from "+type+" where name like '%"+name5+"%' order by id limit 1);")
                    conn.commit()
                else:
                    year5=(request.args.get('year5')).lower()
                    language5=(request.args.get('language5')).lower()
                    cursor.execute("insert into "+type+" (name,year,language,count) values(%s,%s,%s,'1');",(name5,str(year5),language5))     
            conn.commit()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("select * from email where email_hash='"+email_hash+"';")
            if len(cursor.fetchall())!=0:
                cursor.execute("update email set "+type+"='1' where email_hash='"+email_hash+"';")
            else:
                cursor.execute("insert into email (email_hash,"+type+") values ('"+email_hash+"','1');")
        conn.commit()

    update=display(type)       
    return render_template('home.html',display=update,type=type,base='home')

@app.route('/verify_email',methods=['GET'])
def verify_mail():
    email_address = request.args.get('email')
    type= request.args.get('type')
    email_hash=(hashlib.sha256(email_address.encode())).hexdigest()

    with conn:
        with conn.cursor() as cursor:
            if type=='movies':
                cursor.execute("select * from email where email_hash='"+email_hash+"' and movies='1';")
            elif type=='books':
                cursor.execute("select * from email where email_hash='"+email_hash+"' and books='1';")
            elif type=='shows':
                cursor.execute("select * from email where email_hash='"+email_hash+"' and shows='1';")
            if len(cursor.fetchall())!=0:
                message='Sorry! We already have a list of '+type+' suggested by "'+ email_address+'".'
                return render_template('email.html', message=message, base='email')
            else:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute("select * from email where email_hash='"+email_hash+"';")
                        result=cursor.fetchone()
                        if result==None: length=0
                        else: length=len(result)
                        if length==0:
                            response = requests.get("http://apilayer.net/api/check?access_key=852b4119fd0c195be7eb0adf408597a2", params={'email':email_address})
                            status = response.json()['smtp_check']
                            if status == True:
                                return render_template('suggest.html',email=email_hash,type=type, base='suggest')
                            else:
                                message="Sorry! The provided email id '" +email_address+"' is invalid."
                                return render_template('email.html', message=message,base='email')
                        else:
                            return render_template('suggest.html',email=email_hash,type=type, base='suggest')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',base='error')


if __name__=='__main__':
    app.run(debug=True)
