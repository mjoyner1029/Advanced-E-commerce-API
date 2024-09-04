from flask_caching import Cache

cache = Cache()

def cache_response(key, timeout):
    def decorator(f):
        @cache.cached(key_prefix=key, timeout=timeout)
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapped
    return decorator
