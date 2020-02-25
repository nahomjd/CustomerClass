#UI Test File
from customer import customerList
c = customerList()
#should be a for loop
for fn in c.fnl:
    var = input('Enter ' + fn + ': ')
    c.set(fn, var)
c.add()
print(c.data)
if c.verifyNew():
   c.insert()
   print(c.data) 
else:
    print(c.errorList)