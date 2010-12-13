from django.conf import settings
from django.core.cache import cache
import hashlib
import json 

# it must be possible to be called as HASH_METHOD(str_to_hash).hexdigest()
# (will work with all algos from hashlib)
HASH_METHOD = getattr(settings, 'CACHED_COOKIE_HASH_METHOD', hashlib.sha1)

def get(request, key):
    """Retrives COOKIE named key from cache.
    
    If not possible to retrieve, will (silently) return None.
    """
    proxy_digest = request.COOKIES.get(key, None)
    if not proxy_digest:
        return None
    else:
        value = cache.get('cached_cookie__' + proxy_digest)
        return value 

def set(response, key, value, **kwargs):
    """Store value to COOKIE named key.
    
    response must be a Django response object because of the way cookies work 
    key must be a valid COOKIE key
    """
    serialized_value = json.dumps(value)
    proxy_digest = HASH_METHOD(serialized_value).hexdigest()
    timeout = kwargs.get('max_age', None)   
    if timeout:
        cache.set('cached_cookie__' + proxy_digest, value, timeout)
    else:
        cache.set('cached_cookie__' + proxy_digest, value)
    response.set_cookie(key, proxy_digest, **kwargs)
    return response