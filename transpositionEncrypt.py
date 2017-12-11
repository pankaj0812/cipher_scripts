import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 25

    ciphertext = encryptMessage(myKey, myMessage)
    #print the encrypted string in ciphertext to the screen , with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')
    #pyperclip.copy(ciphertext)
    

def encryptMessage(key, message):
    #Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    #loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        #keep logging until pointer goes past the length of the message.
        while pointer < len(message):
            #place the character at pointer in message at the end of the
            #current column in the ciphertext list.
            ciphertext[col] += message[pointer]
            #move pointer over
            pointer += key
            #to test for errors:pointer += key +1

    return ''.join(ciphertext)

#if transpositionEncrypt.py is run (instead of imported as a module) call
#the main() function
if __name__ == '__main__':
	main()
