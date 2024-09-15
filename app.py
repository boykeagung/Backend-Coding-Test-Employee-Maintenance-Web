from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM pekerja")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', pekerja=data )

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Employee Berhasil Ditambahkan")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gaji = request.form['gaji']
        jabatan = request.form['jabatan']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pekerja (name, email, phone, gaji, jabatan, alamat) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (name, email, phone, gaji, jabatan, alamat))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Data Employee Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pekerja WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gaji = request.form['gaji']
        jabatan = request.form['jabatan']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE pekerja
               SET name=%s, email=%s, phone=%s, gaji=%s, jabatan=%s, alamat=%s
               WHERE id=%s
            """, (name, email, phone, gaji, jabatan, alamat, id_data))
        flash("Data Employee Berhasil Diubah")
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
