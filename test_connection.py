import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="db_analyst_project",  
        user="postgres",       
        password="300704"   
    )
    print("Koneksi berhasil!")
    
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("Versi PostgreSQL:", db_version)
    
    cur.close()
    conn.close()

except Exception as e:
    print("Koneksi gagal:", e)