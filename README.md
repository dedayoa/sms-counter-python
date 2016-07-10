# sms-counter-python
SMS Character Counter
=============================

Character counter for SMS messages.

##Usage

```python
from sms_counter import SMSCounter

smsmsg = SMSCounter();
smsmsg.count('ǂ some-string-to-be-counted ');
```

returns
```
<class 'dict'>
{
    'length': 28,
    'per_message': 70,
    'remaining': 42,
    'messages': 1,
    'encoding': 'UTF16'
}
```


###Mentions

* Original idea : [danxexe/sms-counter](https://github.com/danxexe/sms-counter)
* Next Original : [wobblecode/sms-counter-php](https://github.com/wobblecode/sms-counter-php/)

## License

sms-counter-python is released under the [MIT License](LICENSE.txt).

