#static_class_method_concept.py

class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner): # Descriptor Protocol
        return self.func

    def __call__(self, *args, **kwargs): # Python 3.10
        return self.func(*args, **kwargs)


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func.__get__(owner, type(owner))  # Binding the {func} to other Python Instance via Descriptor
