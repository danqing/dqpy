import logging

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
        cls._instance = i
        return i
    except Exception:
        error(logger, 'Unable to connect to cache Redis', None)
        cls._attempted = True
        return None


_redis = _init_redis()
