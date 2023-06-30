from jafdecs import worm


@worm.saveproperties(prefix='_')
class TestExample:
    @property
    def sample_property(self):
        print('Initializing within function...')
        return 5


example = TestExample()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)


@worm.saveproperties
class TestExample2:
    @property
    def sample_property(self):
        print('Initializing within function ...')
        return 1


example = TestExample2()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)