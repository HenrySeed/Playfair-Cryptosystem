class Playfair():
    '''
    Sets up a playfair cipher based on key supplied, used to encrypt and 
    decrypt.
    '''
    
    def __init__(self, text):
        '''Builds cipher so that it can be used to encrypt and decrypt text.'''
        
        self.text = text
        self.alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', \
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
                      'x', 'y', 'z']
                 
        combo = list(self.text)
        combo += self.alpha
        cipher = []
        
        for char in combo:
            if char not in cipher and char in self.alpha:
                cipher.append(char)
            else:
                pass
        
        cipher = [cipher[:5], cipher[5:10], cipher[10:15], cipher[15:20],\
                  cipher[20:25]] 
        
        self.cipher = cipher
    
    
    def __str__(self):
        '''Returns the cipher in grid form.'''
        
        cipher = '\n'
                
        for line in self.cipher:
            for char in line:
                cipher += (char + ' ')
            cipher += '\n'
            
        return cipher[:-1] + '\n'
    
    
    def row(self, char):
        '''Finds the row for a character in the cipher grid.'''
        
        position = 0
        counter = 0
        for line in self.cipher:
            if char in line:
                position = counter
            counter += 1
            
        return position
    
    
    def col(self, char):
        '''Finds the column for a character in the cipher grid.'''
        
        position = 0
        for line in self.cipher:
            counter = 0
            for letter in line:
                if char == letter:
                    position = counter
                counter += 1
            
        return position
    
    
def encrypt(key, message):
    '''Encrypts a message Using a playfair cipher using a given key'''
    
    cipher = Playfair(key)
    prev_char = message[0]
    mess = prev_char
    
    for char in message[1:]:
        if char == prev_char:
            mess += ('q')
        mess += (char)
        prev_char = char
            
    if len(mess) % 2 != 0:
        mess += 'q'
    
    mess = [mess[i:i+2] for i in range(0, len(mess), 2)]
    ciphertext = ''
    
    for pair in mess:
        final_pair = ''
        
        if cipher.row(pair[0]) == cipher.row(pair[1]):
            for i in pair:
                if cipher.col(i) == 4:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][0]
                    
                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][cipher.col(i) + 1]
                    
            ciphertext += final_pair + ' '
            
        elif cipher.col(pair[0]) == cipher.col(pair[1]):
            for i in pair:
                if cipher.row(i) == 4:
                    final_pair += cipher.cipher[0][cipher.col(i)]
                    
                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row + 1][cipher.col(i)]
                    
            ciphertext += final_pair + ' '
        
        else:
            first = [cipher.row(pair[0]), cipher.col(pair[0])]
            second = [cipher.row(pair[1]), cipher.col(pair[1])]
            
            final_pair = cipher.cipher[first[0]][second[1]]\
                + cipher.cipher[second[0]][first[1]]
            
            ciphertext += final_pair + ' '
        
    return ciphertext[:-1]


def decrypt(key, text):
    '''Decrypts a message Using a playfair cipher using a given key'''
    
    cipher = Playfair(key)
    plaintext = ''

    if type(text) == str:
        text = text.split(' ')
    
    for pair in text:
        final_pair = ''
        if cipher.row(pair[0]) == cipher.row(pair[1]):
            
            for i in pair:
                if cipher.col(i) == 0:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][4]
                    
                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row][cipher.col(i) - 1]
                    
            plaintext += final_pair
            
        elif cipher.col(pair[0]) == cipher.col(pair[1]):
            for i in pair:
                if cipher.row(i) == 0:
                    final_pair += cipher.cipher[4][cipher.col(i)]
                    
                else:
                    row = cipher.row(i)
                    final_pair += cipher.cipher[row - 1][cipher.col(i)]
                    
            plaintext += final_pair
        
        else:
            first = [cipher.row(pair[0]), cipher.col(pair[0])]
            second = [cipher.row(pair[1]), cipher.col(pair[1])]
            
            final_pair = cipher.cipher[first[0]][second[1]]\
                + cipher.cipher[second[0]][first[1]]
            
            plaintext += final_pair
            
        if plaintext[-1] == 'q':
            plaintext = plaintext[:-1]
            
        counter = 0
        final = ''
        
        for i in plaintext:
            if i == 'q' and plaintext[counter - 1] == plaintext[counter + 1]:
                pass
            else:
                final += i
            counter += 1
                
    return final