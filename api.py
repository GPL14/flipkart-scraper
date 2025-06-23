from flask import Flask, jsonify, request, Response
from db_config import connect_db
import csv
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "📦 Flipkart Scraper API is running!"

@app.route("/products", methods=["GET"])
def get_products():
    query = request.args.get('q', '')  # Get query string from URL

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    if query:
        cursor.execute("SELECT * FROM products WHERE name LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(rows)

@app.route("/export", methods=["GET"])
def export_products():
    query = request.args.get('q', '')
    conn = connect_db()
    cursor = conn.cursor()

    if query:
        cursor.execute("SELECT id, name, price, rating FROM products WHERE name LIKE %s", (f"%{query}%",))
    else:
        cursor.execute("SELECT id, name, price, rating FROM products")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    def generate():
        yield 'id,name,price,rating\n'
        for row in rows:
            yield f'{row[0]},"{row[1]}",{row[2]},{row[3]}\n'

    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment; filename=products.csv"})



@app.route("/view", methods=["GET"])
def view_products():
    query = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    per_page = 10
    offset = (page - 1) * per_page

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    if query:
        cursor.execute("SELECT COUNT(*) as total FROM products WHERE name LIKE %s", (f"%{query}%",))
        total = cursor.fetchone()['total']
        cursor.execute("SELECT * FROM products WHERE name LIKE %s LIMIT %s OFFSET %s", (f"%{query}%", per_page, offset))
    else:
        cursor.execute("SELECT COUNT(*) as total FROM products")
        total = cursor.fetchone()['total']
        cursor.execute("SELECT * FROM products LIMIT %s OFFSET %s", (per_page, offset))

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    total_pages = (total + per_page - 1) // per_page

    return render_template("products.html", products=rows, query=query, page=page, total_pages=total_pages)



if __name__ == "__main__":
    app.run(debug=True)
    
