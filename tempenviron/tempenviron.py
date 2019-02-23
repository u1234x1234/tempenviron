import contextlib
import os


class IllegalArgumentError(ValueError):
    pass


@contextlib.contextmanager
def updated_environ(dict_env={}, **kwargs_env):
    if not isinstance(dict_env, dict):
        raise IllegalArgumentError('env must be dictionary')

    dict_env.update(kwargs_env)
    to_delete = [k for k, v in dict_env.items() if v is None]
    dict_env = {k: v for k, v in dict_env.items() if v is not None}

    # Save original
    original_environ = dict(os.environ)

    try:
        os.environ.update(dict_env)
        [os.environ.pop(k) for k in to_delete]
        yield
    except TypeError as e:
        raise IllegalArgumentError(e)
    finally:
        # Return original
        os.environ.clear()
        os.environ.update(original_environ)
