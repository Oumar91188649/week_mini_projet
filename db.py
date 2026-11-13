from pathlib import Path
import sqlite3
DB_path = Path(__file__).resolve().parent / "hotel.db"
def get_connection():
 conn = sqlite3.connect("DB_path")
 conn. execute("PRAGMA  foreign_key = ON")
 return conn
  
 
      
