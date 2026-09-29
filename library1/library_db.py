import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='hidar',host='localhost',database='library_db')
        self.c=self.con.cursor()
        print('connection successful')


    def list(self):
        query='select * from book'
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            return record
        else:
            print('no record found')

    def create(self,title,author,price,language,pages):
        #creating new record.

        query='insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s)'
        data=(title,author,price,language,pages)
        self.c.execute(query,data)
        self.con.commit()
        print('Inserted successfully')

    def retrieve(self,id):
        query='select * from book where id=%s'
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            return record
        else:
            print('no record found')

    def delete(self,id):
        query='delete from book where id=%s'
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def update(self,id,title,author,price,language,pages):
        query='update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id=%s'
        data=(title,author,price,language,pages,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

# class_instance=BookListCreateRetrieveUpdateDelete()
# #class_instance.list()
# # #class_instance.create('ABC ','Dingan',599,'English',699)
# # class_instance.retrieve(2)
# #class_instance.delete(3)
# class_instance.update(1,'dingapuranam','dinganswami',999,'malayalam',799)