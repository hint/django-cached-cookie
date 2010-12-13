Not ready for production yet!

Goals:

1. Easy storing of a cookie:

>>> import cached_cookie
>>> data = {'lorem': 'ipsum dolor sit amet'}
>>> cached_cookie.set(request, key, data)

2. Easy retrieval of the cookie:

>>> import cached_cookie
>>> data = cached_cookie.get(request, key)
>>> data
{'lorem': 'ipsum dolor sit amet'}

Things to have in mind:
* http://uts.cc.utexas.edu/~rmyers/pycookie/ already exists - maybe it offers a better implementation after all?
* proper exception handling? guessing if a Django ORM object (therefore built in serialization)?