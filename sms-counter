# -*- coding: utf8 -*- 
'''
Created on Jul 10, 2016

@author: Dayo
'''
from math import ceil


class SMSCounter():
    
    GSM_7BIT = 'GSM_7BIT'
    GSM_7BIT_EX = 'GSM_7BIT_EX'
    UTF16 = 'UTF16'
    GSM_7BIT_LEN = GSM_7BIT_EX_LEN = 160
    UTF16_LEN = 70
    GSM_7BIT_LEN_MULTIPART = GSM_7BIT_EX_LEN_MULTIPART = 153
    UTF16_LEN_MULTIPART = 67

    
    def get_gsm_7bit_map(self):
        
        return(
               [64, 163, 36, 165, 232, 233, 249, 
                236, 242, 199, 92, 110, 216, 248, 
                92, 114, 197, 229, 916, 95, 934, 
                915, 923, 937, 928, 936, 931, 920, 
                926, 198, 230, 223, 201, 32, 33, 92, 
                34, 35, 164, 37, 38, 39, 40, 41, 42, 
                43, 44, 45, 46, 47, 48, 49, 50, 51, 
                52, 53, 54, 55, 56, 57, 58, 59, 60, 
                61, 62, 63, 161, 65, 66, 67, 68, 69, 
                70, 71, 72, 73, 74, 75, 76, 77, 78, 
                79, 80, 81, 82, 83, 84, 85, 86, 87, 
                88, 89, 90, 196, 214, 209, 220, 167, 
                191, 97, 98, 99, 100, 101, 102, 103, 
                104, 105, 106, 107, 108, 109, 110, 
                111, 112, 113, 114, 115, 116, 117, 
                118, 119, 120, 121, 122, 228, 246, 
                241, 252, 224]
               )
        
    def get_added_gsm_7bit_ex_map(self):
        
        return [91, 93, 124, 8364, 123, 92, 125, 126, 94]
    
    def get_gsm_7bit_ex_map(self):
        
        return(self.get_added_gsm_7bit_ex_map()+self.get_gsm_7bit_map())
    
    
    def text_to_unicode_pointcode_list(self, plaintext):
        
        textlist = []
        for stg in plaintext:
            textlist.append(ord(stg))            
        return textlist
    
    def unicode_pointcode_list_to_text(self, strlist):
        
        text = ''
        for stc in strlist:
            text.join(chr(stc))            
        return text
    
    
    def detect_encoding(self, plaintext):
        
        rf = self.text_to_unicode_pointcode_list(plaintext)

        utf16chars = set(rf).difference(set(self.get_gsm_7bit_map()))

        if len(utf16chars):
            return self.UTF16
        
        exchars = set(rf).intersection(set(self.get_added_gsm_7bit_ex_map()))

        if len(exchars):
            return self.GSM_7BIT_EX
        
        return self.GSM_7BIT
        
        
        
    
    def count(self, plaintext):
        
        textlist = self.text_to_unicode_pointcode_list(plaintext)
        
        exchars = []
        encoding = self.detect_encoding(plaintext)
        length = len(textlist)
        
        if encoding == self.GSM_7BIT_EX:
            lengthexchars = len(exchars)
            length+=lengthexchars
            
        if encoding == self.GSM_7BIT:
            permessage = self.GSM_7BIT_LEN
            if length > self.GSM_7BIT_LEN:
                permessage = self.GSM_7BIT_LEN_MULTIPART
                
        
        elif encoding == self.GSM_7BIT_EX:
            permessage = self.GSM_7BIT_EX_LEN
            if length > self.GSM_7BIT_EX_LEN:
                permessage = self.GSM_7BIT_EX_LEN_MULTIPART
                
        
        else:
            permessage = self.UTF16_LEN
            if length > self.UTF16_LEN:
                permessage = self.UTF16_LEN_MULTIPART
                
        
        messages = ceil(length/permessage)
        remaining = (permessage * messages) - length
        
        returnset = {
            'encoding' : encoding,
            'length' : length,
            'per_message' : permessage,
            'remaining' : remaining,
            'messages' : messages
                     }
        
        return returnset
    
    
    def truncate(self, plaintext, limitsms):
        
        count = self.count(plaintext)
        
        if count.mesages <= limitsms:
            return plaintext
        
        
        if count.encoding == 'UTF16':
            limit = self.UTF16_LEN
            
            if limitsms > 2:
                limit = self.UTF16_LEN_MULTIPART
                
        if count.encoding != 'UTF16':
            limit = self.GSM_7BIT_LEN
            
            if limitsms > 2:
                limit = self.GSM_7BIT_LEN_MULTIPART
    
            
        while True:
            text = plaintext[0:limit*limitsms]
            count = self.count(plaintext)
            
            limit = limit - 1
            
            if count.messages < limitsms:
                break
            
        return text
            
