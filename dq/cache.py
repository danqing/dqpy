import json
import logging
from functools import wraps

import redis

from dq.config import Config
from dq.logging import error, warning
from dq.redis import strval

logger = logging.getLogger(__name__)


def _init_redis():
    cfg = Config.get('cache')
    if not cfg:
        return None
    try:
        i = redis.StrictRedis(**cfg)
        # This will attempt to connect to Redis and throw an error if the
        # connection is invalid.
        i.info()
        return i
    except Exception:
        error(logger, 'Unable to connect to cache Redis', None)
        return None


_redis = _init_redis()


def cache(ttl=600, key_func=None):
    def memoize(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            if not _redis or not key_func:
                return func(*args, **kwargs)
            key = key_func(*args, **kwargs)
            if not kwargs.get('fresh'):
                resp = _redis.get(key)
                if resp is not None:
                    return resp
                return json.loads(resp)
            resp = func(*args, **kwargs)
            if not _redis.setex(key, ttl, strval(resp)):
                warning(logger, 'Unable to save to cache', {'key': key})
            return resp

        return decorated_func
    return memoize
