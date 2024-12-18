import inspect
import sys


def introspection_info(obj):
    numbers = {'type': type(obj).__name__,
               'attributes': obj.__dir__,
               'methods': dir(obj),
               'module': inspect.getmodule(obj)

               }

    return numbers


number_info = introspection_info(42)
print(number_info)
