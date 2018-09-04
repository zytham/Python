import cx_Oracle
import db_constant
from contextlib import closing

def get_oracle_db_config():
    db_url = db_constant.USERNAME+"/"+db_constant.PASSWORD+"@"+\
        db_constant.DATABASE_URL+":"+db_constant.PORT+"/"+db_constant.SERVICE_POINT
    connection = cx_Oracle.connect(db_url)
    return connection

def get_address_details(conn):
    try:
           with closing(conn.cursor()) as cur:
               # Execute the SQL command
               cur.execute(db_constant.SELECT_ADDRESS)
               # Fetch all the rows in a list of lists.
               results = cur.fetchall()
               if len(results) > 0:
                   for row in results:
                      print("------ Customer address -------")
                      address = row[1]
                      landmark = row[2]
                      zip_code = row[3]
                      email = row[4]
                      phone = row[5]
                      print("Address: "+ str(address) +" Landmark: "
                            + str(landmark) + " ZipCode: "+str(zip_code))
                      print("Email: " + str(email) + " Phone: " + str(phone))
                      print("\n")
    except Exception as e:
           print("Exception occured in execution.... : ")
           print(e)
           exit()
    finally:
          conn.close()
#starts here.....
if __name__=="__main__":
    print ("**************Start DB Operation****************")
    conn = get_oracle_db_config()
    get_address_details(conn)
    print ("**************Finished DB Operation****************")
