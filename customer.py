'''
In this assignment you will create a console app which stores a list of customers.  
Each customer will have the following attributes:
fname
lname
email
password
subscribed

The app should allow the user to 
Enter new customers
Remove existing customers
Update (change) a customer's attribute
Print all customers
Save / load customer list from the file 'customers.json'
In class: create and test a class definition for a customer.
'''
#INSERT INTO `customers` ('fname', 'lname', 'email', 'password', 'subscribed') VALUES ('Testguy', 'test', 'b@b.com', '1234', 'True')
import pymysql

class customerList:
    def __init__(self):
        self.data = []
        self.tempdata = {}
        self.tn = 'customers'
        self.fnl = ['fname','lname','email','password','subscribed']
        self.conn = None
        self.errorList = []
    def connect(self):
        import config
        self.conn = pymysql.connect(host=config.DB['host'], port=config.DB['port'], user=config.DB['user']\
        ,passwd=config.DB['passwd'], db=config.DB['db'], autocommit=True) #setup our credentials
        
    def add(self):
        self.data.append(self.tempdata)
    #def add(self, item):
     #   self.data.append(item)
    def set(self,fn,val):
        if fn in self.fnl:
            self.tempdata[fn] = val
        else:
            print('Invalid field: ' + str(fn))
    def update(self,n,fn,val):
        if len(self.data) >= (n + 1) and fn in self.fnl:
            self.data[n][fn] = val
        else:
            print('Could not set value at row ' + str(n) + ' col ' + str(fn))
    def insert(self, n=0):
        columns = str(self.fnl)
        vals = ('%s, '*len(self.fnl))[:-2]
        tolkens = []
        for fieldname in self.fnl:
            tolkens.append(self.data[n][fieldname])
        columns = columns[1:-1].replace("'",'`')
        sql = 'INSERT INTO `' + self.tn + '` ' + '(' + columns + ') VALUES (' + vals + ');'
        
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print(sql)
        print(tolkens)
        cur.execute(sql,tolkens)
    def verifyNew(self, n=0):
        self.errorList = []
      
        for item in self.data[n]:
            if len(self.data[n][item]) == 0:
                st = str(item) + ' cannot be blank.'
                self.errorList.append(st)    
        if '@' not in self.data[n]['email'] or '.' not in self.data[n]['email']:
            self.errorList.append("Email input not valid, missing an '@' or '.'.")
        if self.data[n]['subscribed'] != 'True' and self.data[n]['subscribed'] != 'False':
            self.errorList.append('Subscribed needs to be True or False.')
        if len(self.data[n]['password']) <= 4:
            self.errorList.append('Password is too short, needs to be greater than 4 characters.')
        #print(self.errorList)
            
        if len(self.errorList) > 0:
            return False
        else:
            return True