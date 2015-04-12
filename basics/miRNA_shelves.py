# pickle is pretty handy for small database, but for very large
# database, it will be very slow, because we need to load and dump
# a very big database in memory
# a possible solution is separate each record into different pickle
# but it's kind of complicated to write the codes
# and millions of reads will occupy large amount of avaiable inodes
# shelve solves these questions
# shelve is treated as a dict at the top level

# import shelve module
import shelve

# open a file for shelve to write  
db = shelve.open('miRNA_shelve')

# input each record, record name is used as the key of shelve dict
for key in miRNA:
	db[key] = miRNA[key] #shelve is treated like a dict

# close the shelve 
db.close()

# a file names miRNA_shelve is created in this directory, with very
# strange encoding characters

# load from shelve, update the contents, dump again
# load
db = shelve.open('miRNA_shelve')
# update
for key in db.keys(): # multiple targets by 10
	db[key]['target']*=10
	print(db[key]['target'])

#express like this, no changes is not written into the disk file
# a separate line after for loop is important
db.close()

# instead, use a intermediate step, and re-assign back to shelve
db = shelve.open('miRNA_shelve')
# update
for key in db.keys(): # multiple targets by 10
	rec = db[key]
	rec['target'] *= 10
	db[key] = rec 

db.close()

# print the new contents
db = shelve.open('miRNA_shelve')
for key in db: # multiple targets by 10
	print(db[key]['target'])

db.close()
