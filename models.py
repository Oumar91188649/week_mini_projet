from datetime import date 
def verifier_dates(date_debut, date_fin) :
 try:
    debut = date.fromisoformat(date_debut)
    fin = date.fromisoformat(date_fin)
 except(TypeError, ValueError) :
     raise ValueError("les dates doivent etre au format AAAA-MM-jj")
 if debut.isoformat() != date_debut or fin.isoformat() != date_fin :
     raise ValueError("les dates doivent etre au formatr AAAA_MM_jj")
 if fin <= debut:
     raise ValueError ("La date du fin doit etre apres la date du debut")
def lister_chambres(conn):
     cur = conn.cursor()
     cur.execute(""" SELECT id, numero, prix_nuit
                 FROM chambres ORDER BY numero""")
     return cur.fetchall()
def lister_reservations(conn) :
     cur = conn.cursor() 
     cur.execute(
         """SELECT reservation id, clients.nom ,chambres.numero
         reservations.date_debut , date_fin
         FROM reservations
         JOIN clients ON reservation.client_id = client_id
         JOIN chambres ON reservations.chambres_id = chambres.id
         ORDER BY reservations.id """
     )
     return cur.fetchall()
def creer_reservations(conn, client_id, chambre_id, date_debut,date_fin):
     verifier_dates(date_debut, date_fin)
     with conn :
         cur = conn.cursor()
         cur.execute("""
 INSERT INTO reservations
 (client_id, chambre.id,date_debut,date_fin)
 VALUES(?,?, ?,?)
 """ , (client_id,chambre_id, date_debut, date_fin)
                     )
         return cur.lastrowid
def modifier_reservation(conn, reservation_id , date_debut,date_fin ) :
    verifier_dates(date_debut, date_fin)
    with conn :
        cur = conn.cursor()
        cur.execute(""" UPDATE reservations
            SET date_debut = ?, date_fin = ?
            where id = ?
    """,(date_debut, date_fin, reservation_id)
    
          )
        return cur.rowcount
def supprimer_reservations(conn, reservation_id):
    with conn:
     cur = conn.cursor()
     cur.execute("""
        DELETE FROM resrevation 
        WHERE id = ?
        """, (reservation_id)
        
    )
    return cur.rowcount
    
    
    