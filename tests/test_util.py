import os
import unittest
from contextlib import suppress

from dq import util


class TestUtil(unittest.TestCase):

    def tearDown(self):
        with suppress(Exception):
            util.rmrf('test-files')

    def test_safe_cast(self):
        assert util.safe_cast('1', int) == 1
        assert util.safe_cast('meow', int, 2) == 2

    def test_safe_mkdirp(self):
        util.mkdirp('test-files/1/2/3')
        assert os.path.isdir('test-files/1/2/3')

    def test_safe_rmrf(self):
        util.mkdirp('test-files/1/2')
        with open('test-files/1/2/3.txt', 'w') as f:
            f.write('hello')
        assert os.path.exists('test-files/1/2/3.txt')
        util.rmrf('test-files/1/2/3.txt')
        assert not os.path.exists('test-files/1/2/3.txt')
        with open('test-files/1/2/3.txt', 'w') as f:
            f.write('hello')
        util.rmrf('test-files')
        assert not os.path.exists('test-files')
        util.rmrf('none')

    def test_traverse_error(self):
        self.assertRaises(FileNotFoundError, util.traverse, 'none', None)
        self.assertRaises(NotADirectoryError, util.traverse, 'README.md', None)

    def test_traverse(self):
        util.mkdirp('test-files/1/2')
        with open('test-files/1/2/3.txt', 'w') as f:
            f.write('hello')

        tree = {}

        def callback(path, isdir):
            assert path not in tree.keys()
            tree[path] = isdir

        util.traverse('test-files', callback)
        assert tree == {'1': True, '1/2': True, '1/2/3.txt': False}
