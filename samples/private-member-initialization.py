from dankdecorators import privatemember


@privatemember.saveproperties(prefix='_')
class TestExample:
    @property
    def sample_property(self):
        print('Initializing...')
        return 5


example = TestExample()
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)
print(example.sample_property)


# @privatemember.saveproperties
# class TestExample2:
#     @property
#     def sample_property(self):
#         print('Initializing...')
#         return 1


# example = TestExample2()
# print(example.sample_property)
# print(example.sample_property)
# print(example.sample_property)
# print(example.sample_property)
# print(example.sample_property)