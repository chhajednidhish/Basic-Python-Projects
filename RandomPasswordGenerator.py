""" import random
import string

def GenerateRandomPass(size):
    RandomPassword = ''.join([random.choice(string.ascii_letters + string.digits) for n in range[size]])

    return RandomPassword

password = GenerateRandomPass(7)
print(password) """

	
	
# Importing random to generate
# random string sequence
import random

# Importing string library function
import string

def rand_pass(size):
	
	# Takes random choices from
	# ascii_letters and digits
	generate_pass = ''.join([random.choice( string.ascii_letters + string.digits) for n in range(size)])
						
	return generate_pass

# Driver Code
password = 'nac'
it = 0
for i in range(it,100):
	while(password == 'nac'):
		password = rand_pass(3)
		it = it+1
		continue


print(password)
	
	
