# this module is used to store objects permanently in disk
# using shelve module

import shelve

from miRNA_OOP import Mirna

# initial several Mirna instances
let7a = Mirna('human let7a',20,100)
let7b = Mirna('human let7b',20,100)
print(let7a.get_species())

# store these instances in files
db = shelve.open('miRNA_OOP_shelve_db')
db['let7a'] = let7a
db['let7b'] = let7b
db.close()

# load from shelved objects
# no need to import miRNA_OOP
db = shelve.open('miRNA_OOP_shelve_db')
for key in db.keys():
	print(db[key].get_species())
	print(db[key].target)

db.close()
