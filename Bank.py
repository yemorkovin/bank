import sqlite3

class Bank:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create(self):
        self.cursor.execute('''
        create table users(
        id integer primary key autoincrement,
        login text,
        pin integer,
        balance integer
        )
        ''')
        self.cursor.execute('''
        create table balance(
        id integer primary key autoincrement,
        balance integer,
        lim integer
        )
        ''')
    def auth(self, login, pin):
        self.cursor.execute('select * from users where login=? and pin=?', (login, pin))
        self.conn.commit()
        if len(self.cursor.fetchall()) == 0:
            return False
        return True


    def balancebank(self):
        self.cursor.execute('insert into balance (balance, lim) values (?, ?)', (10000, 1000))
        self.conn.commit()



    def writeusers(self):
         for i in range(100):
            self.cursor.execute('insert into users (login, pin, balance) values (?, ?, ?)', ('user_'+str(i), 12345, 3000))
            self.conn.commit()

    def selectbalance(self):
        try:
            self.cursor.execute('select * from balance')
            self.conn.commit()
            return  self.cursor.fetchone()[1]
        except:
            return False

    def selectlimit(self):
        self.cursor.execute('select * from balance')
        self.conn.commit()
        return  self.cursor.fetchone()[2]

    def updatebalance(self, bal):
        self.cursor.execute('update balance set balance=?', (bal,))
        self.conn.commit()

    def selectbalanceuser(self, login, pin):
        self.cursor.execute('select balance from users where login=? and pin=?', (login, pin))
        self.conn.commit()
        return self.cursor.fetchone()[0]

    def updatebalanceuser(self, login, pin, balance):
        self.cursor.execute('update users set balance=? where login=? and pin=?', (balance, login, pin))
        self.conn.commit()
