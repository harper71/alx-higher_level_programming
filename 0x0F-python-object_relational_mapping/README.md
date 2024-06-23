To connect to a MySQL database running on a specific port, you need to specify the port number in the `MySQLdb.connect` method. Here's how you can modify the example script to include a specific port:

### Example Python Script with Specific Port

```python
import MySQLdb

# Database connection details
db_host = "localhost"
db_user = "your_username"
db_password = "your_password"
db_name = "your_database_name"
db_port = 3306  # Replace with your specific port number

try:
    # Establish a database connection
    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, port=db_port)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute an SQL query
    cursor.execute("SELECT VERSION()")

    # Fetch one result
    data = cursor.fetchone()

    # Print the result
    print(f"Database version: {data[0]}")

except MySQLdb.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the database connection
    if db:
        db.close()
```

### Explanation
1. **Add the `db_port` variable** to specify the port number:
   ```python
   db_port = 3306  # Replace with your specific port number
   ```

2. **Include the `port` parameter** in the `MySQLdb.connect` method:
   ```python
   db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, port=db_port)
   ```

### Running the Script
- Replace `your_username`, `your_password`, `your_database_name`, and `3306` with your actual MySQL database credentials and port number.
- Save the script to a file, for example, `mysql_connect.py`.
- Run the script using:
  ```bash
  python3 mysql_connect.py
  ```

This script will connect to your MySQL database on the specified port, execute a query to get the database version, and print the result. You can modify the script to perform other database operations as needed.