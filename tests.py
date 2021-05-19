from unittest import TestCase

from sms_counter import SMSCounter


class SMSCounterTestCase(TestCase):
    """ Tests for sms counting """
    GSM_7BIT_LEN = 160
    GSM_7BIT_LEN_MULTIPART = 153
    UTF16_LEN = 70
    UTF16_LEN_MULTIPART = 67
    GSM_7BIT_CHAR_MAP = list(map(chr, SMSCounter._get_gsm_7bit_map()))
    GSM_7BIT_EX_CHAR_MAP = list(map(chr, SMSCounter._get_added_gsm_7bit_ex_map()))

    def _check_gsm_7bit_sms_length(self, counter, message, message_max_length=GSM_7BIT_LEN):
        length_error = 'Message length should be less than {} symbols'.format(message_max_length)
        self.assertLessEqual(len(message), counter.get('per_message'), length_error)

        textlist = SMSCounter._text_to_unicode_pointcode_list(message)
        exchars = [c for c in textlist if c in SMSCounter._get_added_gsm_7bit_ex_map()]

        self.assertEqual(len(message) + len(exchars), counter.get('length'))
        self.assertEqual(counter.get('messages'), 1, 'Message is not multipart')

    def test_gsm_7bit_chars(self):
        message = 'This is a message with only GSM 7-bit characters'
        counter = SMSCounter.count(message)
        self._check_gsm_7bit_sms_length(counter, message)
        self.assertEqual(counter.get('encoding'), SMSCounter.GSM_7BIT)

    def test_gsm_7bit_ex_chars(self):
        message = 'This message has the GSM 7-bit extension characters appended ' + ''.join(self.GSM_7BIT_EX_CHAR_MAP)
        counter = SMSCounter.count(message)
        self._check_gsm_7bit_sms_length(counter, message)
        self.assertEqual(counter.get('encoding'), SMSCounter.GSM_7BIT_EX)

    def test_gsm_7bit_ex_chars_count_double(self):
        message = self.GSM_7BIT_EX_CHAR_MAP[:5]
        counter = SMSCounter.count(message)
        self.assertEqual(counter.get('per_message'), self.GSM_7BIT_LEN)
        self.assertEqual(counter.get('length'), 10)
        self.assertEqual(counter.get('messages'), 1)

    def test_utf_chars(self):
        utf_message = ['£', 'ф', '±'] + self.GSM_7BIT_CHAR_MAP
        utf_message = utf_message[:self.UTF16_LEN_MULTIPART]
        counter = SMSCounter.count(utf_message)
        self.assertEqual(counter.get('encoding'), SMSCounter.UTF16)
        self.assertEqual(counter.get('length'), len(utf_message))
        self.assertEqual(counter.get('messages'), 1)

    def test_multipart_sms_gsm_7bit(self):
        message = self.GSM_7BIT_CHAR_MAP + self.GSM_7BIT_EX_CHAR_MAP
        double_message = message[:self.GSM_7BIT_LEN_MULTIPART] * 2
        counter = SMSCounter.count(double_message)
        self.assertEqual(counter.get('encoding'), SMSCounter.GSM_7BIT_EX)
        self.assertEqual(counter.get('messages'), 2, 'Message must contain 2 parts')

    def test_multipart_sms_utf(self):
        utf_message = ['£', 'ф', '±'] + self.GSM_7BIT_CHAR_MAP
        double_utf_message = utf_message[:self.UTF16_LEN_MULTIPART] * 2
        counter = SMSCounter.count(double_utf_message)
        self.assertEqual(counter.get('encoding'), SMSCounter.UTF16)
        self.assertEqual(counter.get('messages'), 2, 'Message must contain 2 parts')

if __name__ == '__main__':
    import unittest
    unittest.main()
