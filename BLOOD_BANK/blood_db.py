import mysql.connector

class bloodbank:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='hidar',host='localhost',database='blooddb')
        self.c=self.con.cursor()
        print('connection success')

    def create(self,name,bloodgroup,phone,city,last_donation):
        query='insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)'
        data=(name,bloodgroup,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        print('inserted successfully')

    def list(self):
        query='select * from donor'
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            return record
        else:
            print('no record found')

    def retrieve(self,id):
        query='select * from donor where id=%s'
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            return record
        else:
            print('no record found')

    def update(self,id,name,bloodgroup,phone,city,last_donation):
        query='update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s'
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def delete(self,id):
        query='delete from donor where id=%s'
        data=(id,)
        self.c.execute(query,data)
        if self.c.rowcount>0:
            return True
        else:
            return False

