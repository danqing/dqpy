import unittest

from dq import cache


class TestCache(unittest.TestCase):

    def test_cache_none(self):
        redis = cache._redis
        cache._redis = None

        def key_func():
            return ''

        @cache.cache(key_func=key_func)
        def some_func():
            return 'hello'

        assert some_func() == 'hello'

        cache._redis = redis

        @cache.cache()
        def some_func_2():
            return 'hello2'

        assert some_func_2() == 'hello2'

    def test_cache_fresh(self):
        value = 0

        def key_func(fresh=False):
            return 'cache-fresh-key'

        @cache.cache(key_func=key_func)
        def some_func(fresh=False):
            nonlocal value
            value += 1
            return value

        assert some_func(fresh=True) == 1
        assert some_func() == 1
        assert some_func(fresh=True) == 2
