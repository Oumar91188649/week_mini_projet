from db import get_connection
from models import lister_reservations
from models import lister_chambres


def main ():
    conn = get_connection()
try:
    conn = lister_chambres()     
    print("===CHAMBRES===")
    for chambres in lister_chambres():
      print(chambres)
    
      print("//n===RESERVATIONS===")
    for reservations in lister_reservations(conn):
            print(reservations)
finally:
        conn.close()
            