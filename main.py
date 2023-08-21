from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def create_conn():
    conn = mysql.connector.connect(
        host="rm-cn-lbj3crvpg000xg.rwlb.rds.aliyuncs.com",
        user="dfspoc",
        password="zaq12wsx!",
        database="DFS_POC"
    )
    return conn


def get_users():
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

@app.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete_user/<int:id>', methods=['GET','POST'])
def delete_user(id):
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update_user/', methods=['POST'])
def update_user():
    name = request.form['name']
    age = request.form['age']
    id = request.form['id']
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
