app = Flask(__name__)
CORS(app)

# Add your Database connection details in the below three lines
db_config = {
    "host": "mysql",
    "user": "root",
    "password": "rootpassword",
    "database": "ytdb"
}

@app.route('/login', methods=['GET'])
def login():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users LIMIT 1;")  # Adjust query as needed
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "No users found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
