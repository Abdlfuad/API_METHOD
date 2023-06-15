from flask import Flask,jsonify,request
import psycopg2
from flask_sqlalchemy import SQLAlchemy

DB_URI = "postgresql+psycopg2://username:password@yourlocalhost:5432/postgres"

#define flask
app = Flask(__name__)
@app.route("/")
def index ():
    return "Test API"

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
   __table_args__ = {"schema": "public"}
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   telp = db.Column(db.String(14))


@app.route("/user", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    #connect 
    if request.method == 'GET':
        users = Users.query.all()
        results = [{"id": u.id, "name": u.name, "city": u.city, "telp": u.telp } for u in users]
        return jsonify(results)
    
    elif request.method == 'POST':
        user = Users(
        name=request.form['name'],
        city=request.form['city'],
        telp=request.form['telp']
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'POST ok'})
    
    elif request.method == 'PUT':
        user = Users.query.get(request.form['user_id'])
        user.name=request.form['name']
        user.city=request.form['city']
        user.telp=request.form['telp']
        db.session.commit()
        return jsonify({'status': 'PUT ok'})
    
    elif request.method == 'DELETE':
        user = Users.query.filter_by(id=request.form['user_id']).delete()
        db.session.commit()
        return jsonify({'status': 'DELETE ok'})

    else :
        return 'Method not allowed!'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

with app.app_context():
    db.create_all()