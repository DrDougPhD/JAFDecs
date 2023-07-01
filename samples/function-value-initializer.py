
import json
import pathlib
import random
from pprint import pprint
import string
import time

from jafdecs import initialize, utilities

random.seed(0)


def naive_function(path: pathlib.Path):
    # This code is somewhat complicated in that it initializes an asset before using it, unless the asset already exists.
    if not path.exists():
        print(f'File at {path} does not exist, so we will generate it before calling the actual function that needs it')
        generated_value = {}
        n = 18
        for i in range(10):
            key = randomstring(n=n)
            value = randomstring(n=n)
            generated_value[key] = value

        print('Sleeping to simulate a hard-to-compute function.')
        time.sleep(2)
        with path.open('w') as file:
            json.dump(generated_value, file)

    print(f'File at {path} now exists, so we can get its data.')
    with path.open() as file:
        value = json.load(file)
    
    pprint(value)


def priming_function(path: pathlib.Path):
    print(f'File at {path} does not exist, so we will generate it before calling the actual function that needs it')
    generated_value = {}
    n = 18
    for i in range(10):
        key = randomstring(n=n)
        value = randomstring(n=n)
        generated_value[key] = value

    print('Sleeping to simulate a hard-to-compute function.')
    time.sleep(2)
    with path.open('w') as file:
        json.dump(generated_value, file)


# NOTE: the names of the function parameters for both the priming function, the condition function, and the primed function must match!
@initialize.by(func=priming_function, condition=utilities.filenotfound)
def actual_function(path: pathlib.Path):
    print(f'File at {path} now exists, so we can get its data.')
    with path.open() as file:
        value = json.load(file)
    
    pprint(value)


def randomstring(n: int):
    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=n
        )
    )


def main():
    path = pathlib.Path(__file__).with_suffix('.json')

    # Delete the file if it exists.
    if path.exists():
        path.unlink()

    actual_function(path=path)

    print('Do it again, but this time to the file exists and the initializer does not need to be called.')
    actual_function(path=path)


if __name__ == '__main__':
    main()
