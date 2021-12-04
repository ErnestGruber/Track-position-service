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

  def getpoweroneGS(self,id_phone): # {id :[latitude,logitude,power]}
    self.id_phone=id_phone
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"SELECT id,power  from transfer_gps where id in (select max(id) from transfer_gps)")
      rows = cur.fetchall()
    return rows[0][1]


  def getMac(self,id): # 'mac'
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select id,mac from transfer_wifi where id in (select max(id) from transfer_wifi)")
      rows=cur.fetchall()
      a=rows[0]
    return a[1]


  def getAccelerometr(self,id):  # {id:[x,y,z]}
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select id,x,y,z from (select id,x,y,z from transfer_accelerometr order by id_req desc) as foo where id={id} Limit 1")
      rows=cur.fetchall()
    return {rows[0][0]:[rows[0][1],rows[0][2]]}


  def getGyroscop(self,id): # {id : [x,y,z]}
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select id,x,y,z from (select id,x,y,z from transfer_gyro order by id_req desc) as foo where id={id} Limit 1")
      rows=cur.fetchall()
    return {rows[0][0]: [rows[0][1], rows[0][2]]}


  def getMeta (self,id): # return {id:power}
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select id,volt from (select id,volt from transfer_meta order by id_req desc) as foo where id={id} Limit 1")
      rows=cur.fetchall()
    return {rows[0][0]:rows[0][1]}


  def getGSM (self,id): # return {id:[id_tower,power]}
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select mcc,mnc,cell_id,lac from transfer_gsm where id in (select max(id)  from transfer_gsm ) ")
      rows = cur.fetchall()
      a=rows[0]
      b=[];b.append(a[0]);b.append(a[1]);b.append(a[2]);b.append(a[3])
    return b

  def getoneGPS(self,id_phone): # {id :[latitude,logitude,power]}
    self.id_phone=id_phone
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"SELECT lat,lon  from transfer_gps where id in (select max(id) from transfer_gps )")
      rows = cur.fetchall()
      a=[]
      a.append(rows[0][0]); a.append(rows[0][1])
    return a



  def getmanyGPS(self,id_phone): # {id :[latitude,logitude,power]}
    self.id_phone=id_phone
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"SELECT lat,lon  from transfer_gps")
      rows = cur.fetchall()
    return rows



  def getpowerwifi(self,id): # 'mac'
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select power from transfer_wifi where id in (select max(id) from transfer_wifi)")
      rows=cur.fetchall()
      a=rows[0]
    return a[0]


  def getGSM (self,id): # return {id:[id_tower,power]}
    with DataConn() as con:
      cur = con.cursor()
      cur.execute(f"select mcc,mnc,cell_id,lac"
                  f" from (select id, mcc,mnc,cell_id,lac  from transfer_gsm order by id_req desc) as foo where id={id} Limit 1")
      rows = cur.fetchall()
      a=rows[0]
      b=[];b.append(a[0]);b.append(a[1]);b.append(a[2]);b.append(a[3])
    return b
