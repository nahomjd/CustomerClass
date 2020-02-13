from customer import customerList

cl = customerList()
'''
d = {'fname':'Testguy','lname':'test',\
'email':'a@a.com','passwrod':'123','subscribe':'1'}
cl.add(d)
'''
cl.set('fname','')
cl.set('lname','')
cl.set('email','a@acom')
cl.set('password','12345')
cl.set('subscribed','uuu')
cl.add()
cl.add()

#cl.data[0]['email'] = 'b@b.com' should use a method for this

cl.verifyNew()