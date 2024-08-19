from flask import Flask, render_template, request, redirect, url_for
from db import DB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biodata', methods=['GET','POST'])
def biodata():

    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        umur = request.form["umur"]
        jenis_kelamin = request.form["jenis_kelamin"]
        nik = request.form["nik"]
        pendidikan = request.form["pendidikan"]
        posisi = request.form["posisi"]
        alasan_posisi = request.form["alasan_posisi"]
        
        db = DB()
        cursor = db.connection.cursor()
        query = "INSERT registrant (name, date, umur, jenis_kelamin, nik, pendidikan, posisi, alasan_posisi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, date, umur, jenis_kelamin, nik, pendidikan, posisi, alasan_posisi))
        db.connection.commit()

        return redirect(url_for('thanks'))
    

    return render_template('biodata_form.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
  app.run()