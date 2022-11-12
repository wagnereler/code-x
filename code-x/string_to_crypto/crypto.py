# -*- coding: utf-8 -*-   
from string import ascii_letters, digits, punctuation

class CodeX:
    """ 
	This class will perform the pseudo encryption of a message using the Cezar Cipher technique.
	Warning!
	This type of cipher is not secure, use it for learning purposes only.
	"""
    def __init__(self):
        self.LETTERS = ascii_letters
        self.NUMBERS = digits
        self.SPECIAL = 'àáãâéêóôõíúçÀÁÃÂÉÊÓÕÍÚÇ'
        self.PUNCTUATION = punctuation
        self.ALL_CHARACTERS = (self.LETTERS + self.NUMBERS + self.SPECIAL + self.PUNCTUATION)

    def encrypt(self, message:str, key:int, step:int):
        """Message: String of message that will be encrypted, 
           Key: Index offset number,
           Step: Index offset number to the next character.
        """
        self.message =  message
        self.key = key
        self.step = step
        new_message = ''
        for char in self.message:
            index = self.ALL_CHARACTERS.find(char)
            if index == -1:
                new_message += char
            else:
                new_index = index - (key + step)
                new_index = new_index % len(self.ALL_CHARACTERS)
                new_message += self.ALL_CHARACTERS[new_index:new_index +1]
        return new_message
    
    def dencrypt(self, message, key, step):
        """Message: String of message that will be dencrypted, 
           Key: Index offset number,
           Step: Index offset number to the next character.
        """
        self.message =  message
        self.key = key
        self.step = step
        new_message = ''
        for char in self.message:
            index = self.ALL_CHARACTERS.find(char)
            if index == -1:
                new_message += char
            else:
                new_index = index + (key + step)
                new_index = new_index % len(self.ALL_CHARACTERS)
                new_message += self.ALL_CHARACTERS[new_index:new_index +1]
        return new_message
