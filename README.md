# sms-counter-python
----
[![Build Status](https://travis-ci.com/uralov/sms-counter-python.svg?branch=master)](https://travis-ci.com/uralov/sms-counter-python)

**sms-counter-python** is a lib that help to count characters of SMS messages.

#### Get it now
```
$ pip install git+https://github.com/dedayoa/sms-counter-python.git#egg=sms_counter
```

#### Support
* Python 2
* Python 3

#### Requirements
sms-counter-python has no external dependencies outside of the Python standard library

#### Usage
```python
from sms_counter import SMSCounter

>>> counter = SMSCounter.count('ǂ some-string-to-be-counted ');
>>> counter
>>> {'length': 29, 'messages': 1, 'remaining': 41, 'per_message': 70, 'encoding': 'UTF16'}
```

The meaning of the `length`, `remaining` and `per_message` values returned by `SMSCounter.count()` depend on the encoding. 

For GSM_7BIT_EX encoding, `length`, `remaining` and `per_message` count the number of 7-bit characters in the message, __including__ the escape character that must precede any characters in the "extended" character set. For example, the `length` of the message '€' is 2, because it takes 2 7bit characters to encode '€' in GSM_7BIT_EX.

For UTF16 and GSM_7BIT encoding, `length`, `remaining` and `per_message` count the number of characters (since all characters have an equal bit width).

#### Mentions

* Original idea : [danxexe/sms-counter](https://github.com/danxexe/sms-counter)
* Next Original : [wobblecode/sms-counter-php](https://github.com/wobblecode/sms-counter-php/)

#### License
MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.
