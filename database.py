import os
import pymysql
from datetime import datetime

class Database:
    def __init__(self):
        # Railway MySQL configuration
        self.host = os.environ.get('MYSQL_HOST', 'mysql.railway.internal')
        self.port = int(os.environ.get('MYSQL_PORT', 3306))
        self.user = os.environ.get('MYSQL_USER', 'root')
        self.password = os.environ.get('MYSQL_PASSWORD', 'GObSacAcQzjozmsxPixDRZSCfJGfTTQv')
        self.database = os.environ.get('MYSQL_DATABASE', 'railway')
        
    def get_connection(self):
        """Get MySQL database connection"""
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as e:
            print(f"Database connection error: {e}")
            return None
    
    def init_database(self):
        """Initialize database and create tables"""
        connection = self.get_connection()
        if not connection:
            return False
            
        try:
            with connection.cursor() as cursor:
                # Create contacts table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS contacts (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        message TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
                """)
                connection.commit()
                print("Database initialized successfully")
                return True
        except Exception as e:
            print(f"Database initialization error: {e}")
            return False
        finally:
            connection.close()
    
    def add_contact(self, name, email, message):
        """Add a new contact message to the database"""
        connection = self.get_connection()
        if not connection:
            return False
            
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, message))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error adding contact: {e}")
            return False
        finally:
            connection.close()
    
    def get_contacts(self, limit=50):
        """Get all contacts from the database"""
        connection = self.get_connection()
        if not connection:
            return []
            
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, name, email, message, created_at FROM contacts ORDER BY created_at DESC LIMIT %s"
                cursor.execute(sql, (limit,))
                return cursor.fetchall()
        except Exception as e:
            print(f"Error getting contacts: {e}")
            return []
        finally:
            connection.close()
    
    def get_contact_by_id(self, contact_id):
        """Get a specific contact by ID"""
        connection = self.get_connection()
        if not connection:
            return None
            
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, name, email, message, created_at FROM contacts WHERE id = %s"
                cursor.execute(sql, (contact_id,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error getting contact: {e}")
            return None
        finally:
            connection.close()
    
    def delete_contact(self, contact_id):
        """Delete a contact by ID"""
        connection = self.get_connection()
        if not connection:
            return False
            
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM contacts WHERE id = %s"
                cursor.execute(sql, (contact_id,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting contact: {e}")
            return False
        finally:
            connection.close()

# Global database instance
db = Database() 