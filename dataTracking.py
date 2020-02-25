from customer import customerList
#SImilar to quiz
c = customerList()

#cl.add(d)

cl.set('fname','TestGuy')
cl.set('lname','ttt')
cl.set('subscribed','uuu')
cl.set('email','a@a.com')
cl.set('password','12345')
cl.add()
#cl.verifyNew()
c.data[0]['lname'] = 'newname'
cl.insert()