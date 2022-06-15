from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from Bd import Bd
app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'
bd = Bd()

@app.route('/')
def index():
    contacts = bd.selectAllData()
    # contacts = ({'id': '1', 'name': 'John', 'phone': '123', 'email': 'john@example.com'}, ) tambien se puede con diccionarios
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        bd.insert(name, phone, email)
        # print(name, phone, email)
        flash('Contact added successfully')
        return redirect(url_for('index'))
    # return '<h1>Add Contact</h1>'

@app.route('/get_contact/<id>', methods=['GET', 'POST'])
def get_contact(id):
    contact = bd.select(id)
    return render_template('edit.html', contact=contact)

@app.route('/update_contact/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        bd.update(id, name, phone, email)
        flash('Contact updated successfully')
        return redirect(url_for('index'))
    # return '<h1>Update Contact</h1>'

@app.route('/delete_contact/<id>', methods=[ 'POST', 'GET' ])
def delete_contact(id):
    bd.delete(id)
    flash('Contact deleted successfully')
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(port=5000, debug=True)

bd.closeConnection()
