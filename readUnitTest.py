from customer import customerList

cl = customerList()
cl.getByID(1)
cl.data[0]['fname'] = 'Ihairy'
cl.update(0,'fname','Ihairy')
print(cl.data)