import logging
from functools import wraps

from dq.config import Config
from dq.logging import error

logger = logging.getLogger(__name__)


def _init_redis():
    cfg = Config.get('cache')
    if not cfg:
        return None
    try:
        i = redis.StrictRedis(**cachecfg)
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
            return func(*args, **kwargs)

        return decorated_func
    return memoize
