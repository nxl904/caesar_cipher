
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
KEY = int(input ('How many letters do you want to move?: '))

def caesar_encrypt(plain_text): 

	cipher_text = ''
	plain_text = plain_text.upper()
	
	for c in plain_text: 
		index = ALPHABET.find(c)
		index = (index+KEY) % len(ALPHABET)
		cipher_text = cipher_text + ALPHABET[index]	
	
	return cipher_text

def caesar_decrypt(cipher_text):

	plain_text = ''
	cipher_text = cipher_text.upper()
	
	for c in cipher_text: 
		index = ALPHABET.find(c)
		index = (index-KEY) % len(ALPHABET) 
		plain_text = plain_text + ALPHABET[index]

	return plain_text 

if __name__ == '__main__': 

	m = input ("Enter word to encrypt: ")
	encrypted = caesar_encrypt(m)
	print ('Plain text: ' + caesar_decrypt(encrypted))	
	print ('Encrypted: ' + (encrypted))
	
