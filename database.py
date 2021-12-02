import psycopg2

class DataConn:

  def __enter__(self):
    self.con = psycopg2.connect(
      database="GPS",
      user="Markues",
      password="nerotex_201",
      host="rc1c-2opxo7cwlxs6ftj3.mdb.yandexcloud.net",
      port="6432" )

    return self.con

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.con.close()



class Postgres:
  def getGPS(self,id_phone):
    self.id_phone=id_phone
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"SELECT id,latitude,longitude  from gps where req_id in (select req_id from gps order by req_id desc Limit 4)")
      rows = cur.fetchall()
      print(rows)
a=Postgres()


a.getGPS(1)