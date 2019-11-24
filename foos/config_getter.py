import config
import sys
import collections.abc

def toString(value):
    if isinstance(value, collections.abc.Iterable) and not isinstance(value, str):
        return(" ".join(map(toString, value)))
    else:
        return str(value)

if __name__ == "__main__":
    values = [toString(getattr(config, x)) for x in sys.argv[1:]]
    print(" ".join(values))
