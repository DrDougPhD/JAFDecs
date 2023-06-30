import functools
from typing import Any


def save():
    pass


def save_as():
    pass


def saveproperties(prefix: str = '_'):
    """Decorator for classes to save all properties as private members.
    
    The example below will save a member variable named `_member` to an
    instance of `SampleClass` when it is first accessed. Follow-up accesses to
    `.member` will pull from `._member` and will avoid re-computing the
    property's method.

    @privatemembers.saveproperties
    class SampleClass:
        @property
        def member(self):
            import time
            print('Sleeping...')
            time.sleep(15)
            print('This took a long time to initialize!')
            return 5
    
            
    >>> x = SampleClass()
    >>> print(x.member)
    Sleeping...
    This took a long time to initialize!
    >>> print(x.member)
    """
    
    def class_decorator(cls: type[Any]):
        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            return cls(*args, **kwargs)

        def wrapped_getter(instance: cls, member: property, private_name: str):
            if not hasattr(instance, private_name):
                value = member.fget(self=instance)
                setattr(instance, private_name, value)
            
            else:
                value = getattr(instance, private_name)

            return value

        for name, member in vars(cls).items():
            if not isinstance(member, property):
                continue

            if name.startswith('__') and name.endswith('__'):
                continue

            decorated_member = property(
                fget=functools.partial(wrapped_getter, member=member, private_name=f'{prefix}{name}'),
                fset=member.fset,
                fdel=member.fdel,
                doc=member.__doc__
            )

            # Overwrite the property to use the new method.
            setattr(cls, name, decorated_member)
        
        return wrapper

    return class_decorator
