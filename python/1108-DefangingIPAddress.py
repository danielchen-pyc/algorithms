'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
'''


# My Solution (Runtime: 96.56%)
def defangIPaddr(self, address: str) -> str:
    return address.replace('.', '[.]')
