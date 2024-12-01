import psycopg2
import os
from dotenv import load_dotenv

def get_job_data(conn_url):
    try:
        
        conn = psycopg2.connect(conn_url)
        
        cur = conn.cursor()

        cur.execute('SELECT resume FROM "User" LIMIT 5 WHERE id=%s;'(user_id,))
        resume = cur.fetchone()
        
        #get job id from relevant jobs table
        cur.execute('SELECT "jobId" FROM "RelevantJob" LIMIT 1;')
        job = cur.fetchone()

        #get job data from jobs table
        cur.execute('SELECT position, description FROM "Job" WHERE id = %s', (job[0],))

        details = cur.fetchone()

        position, description = details
        if len(description) > 1000:
            description = description[:1000] + "..."
        return position + " " + description 
    
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    
    finally:
        # Close the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()

def save_resume(resume):
    try:
        conn = psycopg2.connect(conn_url)
        cur = conn.cursor()
        cur.execute('INSERT INTO "Resume" (resume) VALUES (%s)', (resume,))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    load_dotenv()
    conn_url = os.getenv("CONN_URL")
    print(get_job_data(conn_url))
   