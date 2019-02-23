import os
import pytest

from tempenviron import updated_environ, IllegalArgumentError


def test_kwarg_addition():
    value = 'u.1234.x.1234'

    with updated_environ(RANDOM_ENVIRONMENT_VARIABLE=value):
        assert os.environ['RANDOM_ENVIRONMENT_VARIABLE'] == value

    assert 'RANDOM_ENVIRONMENT_VARIABLE' not in os.environ


def test_kwarg_update():
    os.environ['variable'] = 'original_value'

    with updated_environ(variable='new_value'):
        assert os.environ['variable'] == 'new_value'

    assert os.environ['variable'] == 'original_value'


def test_kwarg_multiple():
    with updated_environ(variable1='val1', variable2='val2'):
        assert os.environ['variable1'] == 'val1'
        assert os.environ['variable2'] == 'val2'

    assert 'variable1' not in os.environ
    assert 'variable2' not in os.environ


def test_dict_update():
    os.environ['variable'] = 'original_value'

    with updated_environ({'variable': 'new_value'}):
        assert os.environ['variable'] == 'new_value'

    assert os.environ['variable'] == 'original_value'


def test_dict_multiple():

    with updated_environ({'var1': 'val1', 'var2': 'val2'}):
        assert os.environ['var1'] == 'val1'
        assert os.environ['var2'] == 'val2'

    assert 'var1' not in os.environ
    assert 'var2' not in os.environ


def test_not_dict_exception():

    with pytest.raises(IllegalArgumentError):
        with updated_environ('String'):
            pass


def test_mixed_args():

    with updated_environ({'var1': 'val1', 'var3': 'val3'}, var2='val2', var3='val4'):
        assert os.environ['var1'] == 'val1'
        assert os.environ['var2'] == 'val2'
        assert os.environ['var3'] == 'val4'  # replaced with kwarg

    assert 'var1' not in os.environ
    assert 'var2' not in os.environ
    assert 'var3' not in os.environ


def test_deletion():    
    os.environ['var1'] = 'val1'
    os.environ['var2'] = 'val2'
    os.environ['var3'] = 'val3'

    with updated_environ({'var1': None, 'var3': 'val3'}, var2=None, var3=None):
        assert 'var1' not in os.environ
        assert 'var2' not in os.environ
        assert 'var3' not in os.environ # replaced with kwarg

    os.environ['var1'] == 'val1'
    os.environ['var2'] == 'val2'
    os.environ['var3'] == 'val3'


def test_invalid_args_type():

    class MyClass:
        pass

    with pytest.raises(IllegalArgumentError):
        with updated_environ({'1': MyClass}):
            pass
