import pytest
from jafdecs import worm


@worm.onproperties
class DecoratedClassWithClassmethod:
    """This is a sample docstring."""
    @classmethod
    def sample_class_method(cls):
        return cls()
    
    @property
    def sample_property(self):
        return 1


def test_decorated_class_is_not_function():
    assert str(type(DecoratedClassWithClassmethod)) != "<class 'function'>", (
        'Decoration forces decorated class to be a function type.'
    )


def test_decorated_class_is_a_type():
    assert str(type(DecoratedClassWithClassmethod)) == "<class 'type'>", (
        'Decoration does not result in class being a Type.'
    )


def test_decorated_class_is_expected_name():
    assert DecoratedClassWithClassmethod.__name__ == 'DecoratedClassWithClassmethod', (
        'Class name is overwritten.'
    )


def test_docstring_carried_over():
    assert DecoratedClassWithClassmethod.__doc__ == 'This is a sample docstring.', (
        'Class docstring is not the same.'
    )


def test_calling_class_method():
    try:
        instance = DecoratedClassWithClassmethod.sample_class_method()
    
    except Exception as e:
        pytest.fail(f'Could not execute classmethod: {e}')
    
    else:
        assert type(instance) is DecoratedClassWithClassmethod, (
            'Instance type is not the original class.'
        )
        assert isinstance(instance, DecoratedClassWithClassmethod), (
            'isinstance() is not functioning properly.'
        )
