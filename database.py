import psycopg2


class DataConn:

    def __enter__(self):
        self.con = psycopg2.connect(
            database="GPS",
            user="Markues",
            password="nerotex_201",
            host="rc1c-2opxo7cwlxs6ftj3.mdb.yandexcloud.net",
            port="6432")

        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


class Postgres:

    def getGPS(self, id_phone):  # {id :[latitude,logitude,power]}
        self.id_phone = id_phone
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(
                f"SELECT id,latitude,longitude,power  from transfer_gps where id_req in (select id_req from transfer_gps order by id_req desc Limit 10) and id={id_phone}")
            rows = cur.fetchall()
        return {rows[0][0]: [rows[0][1], rows[0][2]]}

    def getMac(self, id):  # 'mac'
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(f"select id,mac from wifi where id={id}")
            rows = cur.fetchall()
            a = rows[0]
        return a[1]

    def getAccelerometr(self, id):  # {id:[x,y,z]}
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(
                f"select id,x,y,z from (select id,x,y,z from accelerometr order by id_req desc) as foo where id={id} Limit 1")
            rows = cur.fetchall()
        return {rows[0][0]: [rows[0][1], rows[0][2]]}

    def getGyroscop(self, id):  # {id : [x,y,z]}
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(
                f"select id,x,y,z from (select id,x,y,z from gyroscop order by id_req desc) as foo where id={id} Limit 1")
            rows = cur.fetchall()
        return {rows[0][0]: [rows[0][1], rows[0][2]]}

    def getMeta(self, id):  # return {id:power}
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(
                f"select id,volt from (select id,volt from meta order by id_req desc) as foo where id={id} Limit 1")
            rows = cur.fetchall()
        return {rows[0][0]: rows[0][1]}

    def getGSM(self, id):  # return {id:[id_tower,power]}
        with DataConn() as con:
            cur = con.cursor()
            cur.execute(
                f"select id,id_tower,power from (select id,id_tower,power from gsm order by id_req desc) as foo where id={id} Limit 1")
            rows = cur.fetchall()
        return {rows[0][0]: [rows[0][1], rows[0][2]]}


a = Postgres()
a.getGPS(1)
