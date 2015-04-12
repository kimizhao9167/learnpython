# jump into OOP in python, finally OOP!

# define a Mirna class: data + methods 
class Mirna:
	def __init__(self,name,length,target = 0):
	# initialize an instance of this class
	# define default values of target to zero
	# similar to R
		self.name = name
		self.length = length
		self.target = target

	# define other methods
	# get species from name
	def get_species(self,sep=' '):
		return(self.name.split(sep=sep)[0])

	# get normalized target
	def normal_tar(self):
		return(self.target/self.length)
	
	def __str__(self):
		return '%s is a class of %s' % (self.name,self.__class__.__name__)

# one important property of OOP: inheritance
class Sirna(Mirna):
	# Sirna is inherited from miRNA, add concentration
	def add_conc(self,conc):
		self.conc=conc
	
	def normal_tar(self):
		return(self.target/self.length+10)

# if run this module as main program, then exec following
# instead, if it's imported, then __name__ is not __main__
if __name__ == '__main__':
	let7a = Mirna('human=>let7a',22,200) #let7a belongs to the class Mirna
	let7b = Mirna('human let7b',20,400)
	
	# print the values of let7b, get the values of a class by "."
	# very similar to R language
	# notice the difference from dict: dict[key]
	print(let7a.name)
	let7a.target*=0.1
	print(let7a.target)

	# use the methods of a class by instance.method(...)
	print(let7a.get_species(sep='=>'))
	# alternatively: class.method(instance,...)
	print(Mirna.get_species(let7a,sep='=>'))
	print(let7b.get_species(sep=' '))
	print(let7b.normal_tar())
	
	sirna=Sirna('mouse sirna1',25)
	# Sirna inherited Mirna's methods
	print(sirna.get_species())
	# Sirna has polymorphism: different normal_tar method
	print(sirna.normal_tar())
	# Sirna has its specific method
	sirna.add_conc(conc=1.5)
	print(sirna.name,sirna.target,sirna.conc)
	
	# print an object directly, which is ugly
	print(let7a)
	# print behavior could be defined in class by __str__
