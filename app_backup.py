from flask import Flask,jsonify,request
import psycopg2




#define flask
app = Flask(__name__)

#endpoint pertama
@app.route("/")
def index ():
    return "Test API"


def get_connect():
    conn = psycopg2.connect(
        host= 'yourlocalhost',
        database= 'yourdatabases',
        user= 'youruser',
        password= 'yourpassword',
        port= 5432 
    )
    cur = conn.cursor()
    return conn,cur




@app.route("/health_check")
def health_check():
    #buat koneksi
    try:
        conn, cur = get_connect()
        status = 200
        info = 'Database connected'
    except Exception as e:
        status = 500
        info = str(e)
    return jsonify({"status": status, "info" : info})



@app.route("/user", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    #connect
    conn, cur = get_connect()

    if request.method == 'GET':
        query = '''
        SELECT * FROM public.users;
        '''
        cur.execute(query)
        #defined data
        data_user = cur.fetchall()

        #postgre to json (transform)
        results = []
        for row in data_user :
            row_dict = {}
            for i, col in enumerate(cur.description):
                row_dict[col.name] = row[i]
            results.append(row_dict)
        #output
        return jsonify(results)

    elif request.method == 'POST':
        name = request.form.get("name")
        city = request.form.get("city")
        telp = request.form.get("telp")

        query = f"""
        INSERT INTO public.users(name, city, telp)
        VALUES ('{name}', '{city}', '{telp}')
        """
        cur.execute(query)
        conn.commit()
        return jsonify({"status":"inserted"})

    elif request.method == 'PUT':
        name = request.form.get("name")
        city = request.form.get("city")
        telp = request.form.get("telp")
        user_id = request.form.get("user_id")
        
        query = f"""
        UPDATE public.users
        SET name='{name}', city='{city}', telp='{telp}'
        WHERE user_id='{user_id}';
        """
        cur.execute(query)
        conn.commit()
        return jsonify({"status":"ok update"})
    
    elif request.method == 'DELETE':
        user_id = request.form.get("user_id")

        query = f"""
        DELETE FROM public.users
        WHERE user_id='{user_id}';
        """

        cur.execute(query)
        conn.commit()
        return jsonify({"status":"ok delete"})

    else :
        return 'Method not allowed!'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")