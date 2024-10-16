from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "DB Reader API is kicking!"})



@app.route('/api/schema/postgres', methods=['POST'])
def get_postgres_schema():
    data = request.json
    db_name = data.get('db_name')
    user = data.get('user')
    password = data.get('password')
    host = data.get('host')
    port = data.get('port', 5432)

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Create a cursor object
        cur = conn.cursor()

        # Query to get table names
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cur.fetchall()

        schema = {"tables": []}

        # For each table, get column information
        for table in tables:
            table_name = table[0]
            cur.execute(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = '{table_name}'
            """)
            columns = cur.fetchall()
            
            table_schema = {
                "name": table_name,
                "columns": [{"name": col[0], "type": col[1]} for col in columns]
            }
            schema["tables"].append(table_schema)

        cur.close()
        conn.close()

        return jsonify({"db_type": "postgres", "schema": schema})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/schema/test', methods=['GET'])
def get_schema(test):
    # This is a placeholder. In a real application, you'd fetch the actual schema.
    sample_schema = {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "username", "type": "VARCHAR(50)"},
                    {"name": "email", "type": "VARCHAR(100)"}
                ]
            },
            {
                "name": "products",
                "columns": [
                    {"name": "id", "type": "INTEGER"},
                    {"name": "name", "type": "VARCHAR(100)"},
                    {"name": "price", "type": "DECIMAL(10,2)"}
                ]
            }
        ]
    }
    return jsonify({"db_type": "test", "schema": sample_schema})

if __name__ == '__main__':
    app.run(debug=True)
