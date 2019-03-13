#Uma metaclasse é uma classe cujas instâncias são classes. Como uma classe "comum" define o comportamento das instâncias da classe, uma metaclasse define o comportamento das classes e suas instâncias.


class MetaSingleton(type):
    _instances={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, \
                cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()

logger2 = Logger()

print(logger1)
print(logger2)