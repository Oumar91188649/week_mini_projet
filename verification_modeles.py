from db import get_connection
from models import lister_chambres
from models import lister_reservations
from models import creer_reservations
from models import supprimer_reservations
def verifier():
    conn = get_connection()
try:
  print("cmambres", lister_chambres(conn))
  print("reservation", lister_reservations(conn))
finally:
    conn.close