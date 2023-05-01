import uuid
from datetime import timedelta
from flask import *
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from sql_connection import connection
from flask import send_file


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


# encryption
# L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
#      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
     "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# M = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
#      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

##########################-Functions
def split1(e):
    return [char for char in e]

def convert(f):
    str1 = ""
    return(str1.join(f))

def convert1(g):
    str1 = " "
    return(str1.join(g))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    if request.method == 'POST':
        file = request.files['file']
        f1 = open("encrypted.txt", "w")
        f2 = file.read().decode('utf-8')
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for line in f2:
            # line = line.decode('utf-8')
            word1 = line.split(" ")
        #   print("word split",word1)
            for word in word1:
                letter1 = split1(word)
        #        print("letter split", letter1)
                for i in range(len(letter1)):
                    for j in range(len(L)):
                        if letter1[i] == L[j]:
                            list1.append(L[(j+2) % len(L)])
                            print(list1)
                            break
                    else:
                        list1.append(letter1[i])
                list2 = convert(list1)
                list3.append(list2)
                list1 = []
                print("word list", list3)
            list4 = convert1(list3)
            list3 = []
            f1.write(list4)
            print(list4)
        f1.close()
        return send_file('encrypted.txt', as_attachment=True)
    return render_template("dashboard.html")


@app.route('/decrypt', methods=['POST', 'GET'])
def decrypt():
    if request.method == 'POST':
        file = request.files['file']
        f1 = open("decrypted.txt", "w")
        f2 = file.read().decode('utf-8')
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for line in f2:
            # line = line.decode('utf-8')
            word1 = line.split(" ")
        #   print("word split",word1)
            for word in word1:
                letter1 = split1(word)
        #        print("letter split", letter1)
                for i in range(len(letter1)):
                    for j in range(len(L)):
                        if letter1[i] == L[j]:
                            list1.append(L[(j-2) % len(L)])
                            print(list1)
                            break
                    else:
                        list1.append(letter1[i])
                list2 = convert(list1)
                list3.append(list2)
                list1 = []
                print("word list", list3)
            list4 = convert1(list3)
            list3 = []
            f1.write(list4)
            print(list4)
        f1.close()
        return send_file('decrypted.txt', as_attachment=True)
    return render_template("dashboard.html")


users_dict = {}
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = connection()
        mycursor = db.cursor()
        sql = "SELECT * FROM info WHERE email='%s';"
        mycursor.execute(sql % email)
        user = mycursor.fetchone()
        print("This is user: ",user)
        mycursor.close()


        if user:
            if email == user[3] and password == user[2]:
                session_id = str(uuid.uuid4())  # generate a unique session id
                users_dict[session_id] = user[0]  # store the username in the users dictionary
                print(users_dict)
                session["session_id"] = session_id  # store the session id in the session cookie
                session["user"] = user[1]
                return redirect(url_for("dashboard"))
            error = "Username or Password Doesn't match. Please try again1"
            return render_template('login.html', error=error)
        error1 = "Username or Password Doesn't match. Please try again2"
        return render_template('login.html', error=error1)
    error3 = "fill all the required fields"
    return render_template('login.html', error=error3)


@app.context_processor
def inject_user():
    current_user = session.get("user")
    return dict(current_user=current_user)


@app.route('/')
def index1():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 == password2:
            db = connection()
            cur = db.cursor()
            sql = "SELECT * FROM info WHERE email='%s';"
            cur.execute(sql, {'email': email})
            existing_user = cur.fetchone()
            if existing_user:
                error = "This username is already taken. Please choose another."
                return render_template('register.html', error=error)
            sql = "INSERT INTO info(username,password,email) VALUES(%s,%s,%s);"
            cur.execute(sql, (username, password1, email))
            db.commit()
            session['user'] = username
            return redirect(url_for('dashboard'))
        err = "password doesn't match"
        return redirect(url_for('register.html'), err=err)
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('session_id', None)
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    return render_template("reset.html")

if __name__ == '__main__':
    app.run(debug=True)