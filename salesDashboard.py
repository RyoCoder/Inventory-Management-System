from sqlite3.dbapi2 import DatabaseError
import flask
from flask import Flask, render_template, request
import sqlite3
import os
from datetime import datetime
"""
import - sqlite for database's
import flask micro web framework
import os for path exist testing and file exist testing
import datetime as it will be used for logging and record keeping
"""
# Check if database dir exist (returns: TRUE OR FALSE)
dirDBExist = os.path.isdir("databases")
# Check if the database file exist (returns: TRUE OR FALSE)
fileDbExist = os.path.isfile("databases/inventory.db")
# if directory does exist
if(dirDBExist == True):
    #Keep moving forward
    pass
else:
    #if not create the driectory
    os.mkdir("databases")
# Check if database file exist
if(fileDbExist == True):
        # if it does then keep moving forward
        pass
else:
    # if not create the database from scratch
    conn = sqlite3.connect('databases/inventory.db')
    conn.execute("CREATE TABLE items (barcode INTEGER, name TEXT, quantity INTEGER, price REAL, sales REAL, authorization TEXT)")
    conn.commit()
    conn.close()

# main appliction method
def main(app):
    # INDEX ROUTE (MAIN)
    @app.route('/')
    def index():
        return render_template('index.html', title="Sales Dashboard")
    # INVENTORY ROUTE (MENU)
    @app.route('/inventory')
    def inventory():
        return render_template('inventory.html', title="Inventory Menu")
    # VIEW INVENTORY DATABASE
    @app.route('/viewInv')
    def viewInv():
        con = sqlite3.connect("databases/inventory.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        rows = cur.fetchall()
        return render_template('viewInv.html', title="view inventory", rows=rows)
    
    # ADD ITEM TO INVENTORY
    @app.route('/newInvItem')
    def newInvItem():
        return render_template('newInvItem.html')
    # THIS GETS CALLED FROM FORM IN newInvItem.html
    @app.route('/addrec', methods=['POST', 'GET'])
    def addrec():
        if request.method == 'POST':
            try:
                barcode = request.form['barcode']
                name = request.form['name']
                quantity = request.form['quantity']
                price = request.form['price']
                salesPrice = request.form['sales_price']
                authorizedby = request.form['salesLeader']

                with sqlite3.connect("databases/inventory.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO items (barcode, name, quantity, price, sales, authorization) VALUES(?,?,?,?,?,?)", (barcode, name, quantity, price, salesPrice, authorizedby))
                    con.commit()
                    msg = "[+] Item added!"
            except:
                con.rollback()
                msg = "[-] Error adding item"
            finally:
                con.close()
                return render_template("result.html", msg=msg)
    # DELETE DATABASE RECORD - in inventory.html
    @app.route('/delrec', methods=['POST', 'GET'])
    def delrec():
        if request.method == 'POST':
            try:
                barcode = request.form['barcode']
                with sqlite3.connect("databases/inventory.db") as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM items WHERE barcode="+barcode)
                    con.commit()
                    msg = "[+] Item Deleted!"
            except:
                con.rollback()
                msg = "[-] Error deleting item"
            finally:
                con.close()
                return render_template("result.html", msg=msg)
    # MODIFY DATABASE RECORD - invetory.html
    @app.route('/modrec', methods=['POST', 'GET'])
    def modrec():
        if request.method == 'POST':
            try:
                barcode = request.form['barcode']
                name = request.form['name']
                quantity = request.form['quantity']
                price = request.form['price']
                salesPrice = request.form['sales_price']
                authorizedby = request.form['salesLeader']

                with sqlite3.connect("databases/inventory.db") as con:
                    cur = con.cursor()
                    cur.execute("UPDATE items SET name='"+name+"', quantity="+quantity+", price="+price+", sales="+salesPrice+", authorization='"+authorizedby+"' WHERE barcode="+barcode)
                    con.commit()
                    msg = "[+] Item Updated!"
            except:
                con.rollback()
                msg = "[-] Error updating item"
            finally:
                con.close()
                return render_template("result.html", msg=msg)

    # ADMIN PORTAL LOGIN - for adding user access in the future
    @app.route('/admin', methods=['POST', 'GET'])
    def admin():
        if request.method == 'POST':
            print("ADMIN POST TRUE")
        else: pass
        return render_template("admin.html", title="admin login")
    
    # SETTINGS TAB - used for adding UI Changes for users
    @app.route('/settings', methods=['POST', 'GET'])
    def settings():
        if request.method == 'POST':
            print("SETTINGS POST TRUE")
        else: 
            pass
        return render_template("settings.html", title="Settings Dashboard")
    
    # ABOUT TAB - used for version visualization - patch note changes
    @app.route('/about')
    def about():
        return render_template("about.html", title="About Sales")
    # START FLASK APP
    app.run()

#ENTRY POINT
if __name__  == '__main__':
    # setup instance of flask app
    app = Flask(__name__)
    # load flask config file
    app.config.from_pyfile('config.py')
    #run main()
    main(app)