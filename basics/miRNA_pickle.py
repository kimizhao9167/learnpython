# use pickle module to save the miRNA database in a binary file in disk

# import the initial data
import miRNA_initial

# import the pickle module
import pickle

# open a binary file for writing
dbfile = open('miRNA_initial','wb')

# dump the database into the file
pickle.dump(miRNA,dbfile)

# close the file
dbfile.close()

# exit() to test whether we can load this database from files in disk
import pickle
dbfile = open('miRNA_initial','rb')
miRNA_2 = pickle.load(dbfile)
print(miRNA_2['let7c']['target'])
dbfile.close()

