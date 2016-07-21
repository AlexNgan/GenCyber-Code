# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost',user='root',passwd='password',db='gencybercs4cs')      #Establishes a connection.
cur = conn.cursor()       #Makes a cursor.

@app.route("/")           #Creates URL.
def home():
    sql = 'SELECT candy_name FROM candy'        #Defines a query.
    cur.execute(sql)
    results = []                                #Empty list to store the candies.

    #Returns all the rows returned after the query is executed.
    for row in cur.fetchall():
        results.append(str(row[0]))
    
    #Renders a page using an HTML file and the results.
    return render_template('index.html', results = results) 

#-----------------------------------------------------------------------------------------------------    
@app.route("/favecandy", methods=['get'])
def favorite_candy():
    searchword = request.args.get('candy','NULL')
    cur.execute('select name from students natural join likes where candy_name = %s', searchword)
    results = []
    
    for row in cur.fetchall():
        results.append(str(row[0]))
                    
    return render_template('favecandy.html', results = results, searchword = searchword)
    
#-----------------------------------------------------------------------------------------------------
@app.route("/tables")
def tables():
    sql = 'SELECT * FROM students'
    cur.execute(sql)
    results = []
    
    for row in cur.fetchall():
        currRow = []
        results.append(currRow)
        for column in row:
                currRow.append(str(column))
                    
    sql2 = 'SELECT * FROM likes'
    cur.execute(sql2)
    results2 = []
    
    for row in cur.fetchall():
        currRow = []
        results2.append(currRow)
        for column in row:
                currRow.append(str(column))
                    
    sql3 = 'SELECT * FROM candy'
    cur.execute(sql3)
    results3 = []
    
    for row in cur.fetchall():
        currRow = []
        results3.append(currRow)
        for column in row:
                currRow.append(str(column))
                
# Write a query to join the students table and the likes table together!                   
    sql4 = 'SELECT students * FROM '
    cur.execute(slq4)
    

    joinresults = []
    for row in cur.fetchall():
            currRow = []
            joinresults.append(currRow)
            for column in row:
                    currRow.append(str(column))
                    
# Write a query to join the students table, the likes table, and the candy table together!                   






    joinresults2 = []
    for row in cur.fetchall():
            currRow = []
            joinresults2.append(currRow)
            for column in row:
                    currRow.append(str(column))
             
    return render_template('tables.html', results = results, results2 = results2, results3 = results3, joinresults = joinresults, joinresults2 = joinresults2)

#-------------------------------------------------------------------------------------------------------------------    
@app.route("/ordercandy")
def order():
    
    sql = 'SELECT * FROM candy'
    cur.execute(sql)
    results0 = []
    
    for row in cur.fetchall():
        currRow = []
        results0.append(currRow)
        for column in row:
                currRow.append(str(column))
                
# Write and execute a query that finds everyone’s name, the candy they ordered, and the amount 
# of each candy they ordered. 
    
    
    

    results = []
    for row in cur.fetchall():
            currRow = []
            results.append(currRow)
            for column in row:
                    currRow.append(str(column))
    
#----------------------------------------------------------------------------------------------------------------
# Write and execute a query to calculate the total cost of each student's order!
   
   
   


    results2 = []
    for row in cur.fetchall():
            currRow = []
            results2.append(currRow)
            for column in row:
                    currRow.append(str(column))
    
    
#-------------------------------------------------------------------------------------------------------------------------
# Write and execute a query to find the total cost of each candy order!
# Hint: Creating a view may help   


    
  
  

    results3 = []
    for row in cur.fetchall():
            currRow = []
            results3.append(currRow)
            for column in row:
                    currRow.append(str(column))
                    
    return render_template('ordercandy.html', results0 = results0, results = results, results2 = results2, results3 = results3)

    
if __name__ == "__main__":
    app.run(debug = True)