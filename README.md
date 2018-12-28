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

#### Mentions

* Original idea : [danxexe/sms-counter](https://github.com/danxexe/sms-counter)
* Next Original : [wobblecode/sms-counter-php](https://github.com/wobblecode/sms-counter-php/)

#### License
MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.
