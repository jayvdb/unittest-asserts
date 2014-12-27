from nose.tools import assert_raises, eq_
from . import sparse_check


def test_sparse_check():
    sparse_check({'status': 'ok'},
                 {'status': 'ok', 'results': [1, 2, 3]})

    assert_raises(AssertionError,
                  sparse_check,
                  {'status': 'ok'},
                  {'status': 'error', 'results': [1, 2, 3]})
