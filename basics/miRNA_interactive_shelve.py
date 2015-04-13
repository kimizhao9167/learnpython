# interactively ask the key from input, output the attributes of the key
# database is stored by shelve

import shelve
from miRNA_OOP import Mirna

db = shelve.open('miRNA_OOP_shelve_db')
# there are two mirnas in this db: let7a and let7b
fieldnames = ['name','target','length']
MaxFieldLength = max([len(f) for f in fieldnames])

# interactively ask the key from console
# use while condition to iteratively ask for keys
while True:
	key = input('\ninput the name of miRNA or EOF to exit=> ')
	if key == 'EOF':
		break
	else:
		try:
			rec = db[key]
		except:
			# no key found, asked whether to add new record
			NewChoice = input('No such miRNA in my database! create this record? yes/no?')
			if NewChoice == 'no':
				break
			else:
				NewRec = Mirna(key,0,0)
				# initialize a new instance
				# add values
				for field in fieldnames:
					NewValue=input('input the %s => ' % field)
					setattr(NewRec,field,NewValue)
					# notice the use of setattr(instance,attr,value) and getattr(instance,attr)

				print('The following record has been added to database')
				for field in fieldnames:
					print(getattr(NewRec,field))

				# add to shelve
				db[key] = NewRec
					
		else:
			for field in fieldnames:
				print(field.center(MaxFieldLength),'=>',str(getattr(rec,field)))
				# for string object, could be formatted in printing by string.ljust(width)
				# string.rjust(width)string.center(width)

db.close()
