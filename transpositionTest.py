#transposition cipher test
import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
	random.seed(42) #set the random "seed" to a static value

	for i in range(20):#run 20 tests
		#generate random messages to test
		#the message will have a random length
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)

		#convert the message string to a list to shuffle it.
		message = list(message)
		random.shuffle(message)
		message = ''.join(message) #convert list to string

		print('Test #%s: "%s..."' % (i+1,message[:50]))

		#check all possible keys for each message.
		for key in range(1,len (message)):
			encrypted = transpositionEncrypt.encryptMessage(key, message)
			decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

			#if the decryption doesn't match the original message, display
			#an error message and quit.
			if message != decrypted:
				print('Mismatch with key %s and message %s.' %(key, message))
				print(decrypted)
				sys.exit()

	print('Transposition cipher test passed.')

if __name__ == '__main__':
	main()
