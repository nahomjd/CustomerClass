from customer import customerList

cl = customerList()



d = {'fname':'Testguy','lname':'test',\
'email':'a@a.com','passwrod':'123','subscribe':'1'}
#cl.add(d)

cl.set('fname','fna')
cl.set('lname','ttt')
cl.set('subscribed','uuu')
cl.add()
#cl.verifyNew()
cl.insert()



#cl.data[0]['email'] = 'b@b.com' should use a method for this


#cl.verifyNew()


