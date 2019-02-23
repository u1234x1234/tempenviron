[![Build Status](https://travis-ci.org/u1234x1234/temp-environ.svg?branch=master)](https://travis-ci.org/u1234x1234/temp-environ)
[![Coverage Status](https://coveralls.io/repos/github/u1234x1234/temp-environ/badge.svg?branch=master)](https://coveralls.io/github/u1234x1234/temp-environ?branch=master)

# temp_environ

`temp_environ` allows you to temporary modify your environment variables with context manager.

## Usage:
```python
from temp_environ import updated_environ


# Update with keyword arg
assert 'RANDOM_ENVIRONMENT_VARIABLE' not in os.environ

with updated_environ(RANDOM_ENVIRONMENT_VARIABLE='SOME_VALUE'):
    assert os.environ['RANDOM_ENVIRONMENT_VARIABLE'] == 'SOME_VALUE'

assert 'RANDOM_ENVIRONMENT_VARIABLE' not in os.environ


# Or pass a dictionary
with updated_environ({'var1': 'val1', 'var2': 'val2'}):
    assert os.environ['var1'] == 'val1'
    assert os.environ['var2'] == 'val2'


# Or both. In that case keywords have a higher priority
with updated_environ({'var1': 'val1', 'var2': 'val2'}, var2='val3'):
    assert os.environ['var2'] == 'val3'


# To temporary delete an environment variable, set the variable to None
os.environ['var1'] = 'val1'

with updated_environ(var1=None):
    assert 'var1' not in os.environ

assert os.environ['var1'] == 'val1'

```
