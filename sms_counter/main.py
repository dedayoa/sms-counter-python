# -*- coding: utf8 -*-
"""
Created on Jul 10, 2016
@author: Dayo
"""
from math import ceil


class SMSCounter(object):
    GSM_7BIT = 'GSM_7BIT'
    GSM_7BIT_EX = 'GSM_7BIT_EX'
    UTF16 = 'UTF16'
    GSM_7BIT_LEN = GSM_7BIT_EX_LEN = 160
    UTF16_LEN = 70
    GSM_7BIT_LEN_MULTIPART = GSM_7BIT_EX_LEN_MULTIPART = 153
    UTF16_LEN_MULTIPART = 67

    @classmethod
    def _get_gsm_7bit_map(cls):
        gsm_7bit_map = [
            10, 12, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
            46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
            63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
            80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 95, 97, 98, 99,
            100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
            113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 161, 163, 164,
            165, 191, 196, 197, 198, 199, 201, 209, 214, 216, 220, 223, 224,
            228, 229, 230, 232, 233, 236, 241, 242, 246, 248, 249, 252, 915,
            916, 920, 923, 926, 928, 931, 934, 936, 937]
        return gsm_7bit_map

    @classmethod
    def _get_added_gsm_7bit_ex_map(cls):
        added_gsm_7bit_ex_map = [12, 91, 92, 93, 94, 123, 124, 125, 126, 8364]
        return added_gsm_7bit_ex_map

    @classmethod
    def _text_to_unicode_pointcode_list(cls, plaintext):
        textlist = []
        for stg in plaintext:
            textlist.append(ord(stg))
        return textlist

    @classmethod
    def _detect_encoding(cls, plaintext):
        rf = cls._text_to_unicode_pointcode_list(plaintext)

        non_gsm_7bit_chars = set(rf) - set(cls._get_gsm_7bit_map())
        if not non_gsm_7bit_chars:
            return cls.GSM_7BIT

        non_gsm_7bit_ex_chars = non_gsm_7bit_chars - set(cls._get_added_gsm_7bit_ex_map())
        if not non_gsm_7bit_ex_chars:
            return cls.GSM_7BIT_EX

        return cls.UTF16

    @classmethod
    def count(cls, plaintext):
        textlist = cls._text_to_unicode_pointcode_list(plaintext)

        encoding = cls._detect_encoding(plaintext)
        length = len(textlist)

        if encoding == cls.GSM_7BIT_EX:
            exchars = [c for c in textlist if c in cls._get_added_gsm_7bit_ex_map()]
            lengthexchars = len(exchars)
            length += lengthexchars

        if encoding == cls.GSM_7BIT:
            permessage = cls.GSM_7BIT_LEN
            if length > cls.GSM_7BIT_LEN:
                permessage = cls.GSM_7BIT_LEN_MULTIPART
        elif encoding == cls.GSM_7BIT_EX:
            permessage = cls.GSM_7BIT_EX_LEN
            if length > cls.GSM_7BIT_EX_LEN:
                permessage = cls.GSM_7BIT_EX_LEN_MULTIPART
        else:
            permessage = cls.UTF16_LEN
            if length > cls.UTF16_LEN:
                permessage = cls.UTF16_LEN_MULTIPART

        # Convert the dividend to fload so the division will be a float number
        # and then convert the ceil result to int
        # since python 2.7 return a float
        messages = int(ceil(length / float(permessage)))

        if length == 0:
            remaining = permessage
        else:
            remaining = (permessage * messages) - length

        returnset = {
            'encoding': encoding,
            'length': length,
            'per_message': permessage,
            'remaining': remaining,
            'messages': messages
        }

        return returnset

    @classmethod
    def truncate(cls, plaintext, limitsms):
        count = cls.count(plaintext)

        if count.messages <= limitsms:
            return plaintext

        if count.encoding == 'UTF16':
            limit = cls.UTF16_LEN

            if limitsms > 2:
                limit = cls.UTF16_LEN_MULTIPART

        if count.encoding != 'UTF16':
            limit = cls.GSM_7BIT_LEN

            if limitsms > 2:
                limit = cls.GSM_7BIT_LEN_MULTIPART

        while True:
            text = plaintext[0:limit * limitsms]
            count = cls.count(plaintext)

            limit = limit - 1

            if count.messages < limitsms:
                break

        return text
