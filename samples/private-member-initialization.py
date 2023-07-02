from jafdecs import worm


@worm.onproperties(prefix='_')
class TestExample:
    @property
    def sample_property(self):
        print('Initializing within function...')
        return 1


example = TestExample()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)


@worm.onproperties
class TestExample2:
    @property
    def sample_property(self):
        print('Initializing within function ...')
        return 2


example = TestExample2()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)


@worm.onproperties
class TestExample3:
    @classmethod
    def from_stuff(cls):
        return cls()
    
    @property
    def sample_property(self):
        print('Initializing within function ...')
        return 3


example = TestExample3.from_stuff()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)