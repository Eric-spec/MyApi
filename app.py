from flask import *
import pymysql
app = Flask(__name__)
#routes
@app.route('/api/all')
def all():
    con = pymysql.connect(host='localhost', user='root', password='',database='api')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    sql = "select * from locations"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

#test
#http://127.0.0.1:5000/


#create a database named api
#create a table named locations
#location_id INT PK,
# lat VARCHAR 50,
# lon VARCHAR 50,
# name VARCHAR 50,
# phone VARCHAR 50,
# desc VARCHAR 50

if __name__ == '__main__':
    app.run(port=8080)

    # Database hostaddress:
    # eric.mysql.pythonanywhere - services.com
    # Username:
    # eric

# https://classroom.google.com/c/MzY4MTQxMTM5NzQz/m/NDExODc4ODc5ODQz/details