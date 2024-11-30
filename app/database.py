import psycopg2

def get_job_data(conn_url, id):
    try:
        
        conn = psycopg2.connect(conn_url)
        
        cur = conn.cursor()
        
        cur.execute("SELECT id, job_title, description FROM Jobs WHERE id = %s LIMIT 1", (id,))
        
        row = cur.fetchone()

        #Return
        if row:
            id, job_title, description = row
            return job_title + " " + description
        else:
            return "No data found"   
    
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    
    finally:
        # Close the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()
