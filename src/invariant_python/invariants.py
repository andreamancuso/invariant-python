class InvariantMeta(type):
    """
    A metaclass that calls __invariant__ before/after every user-defined method.
    Skips special dunder methods like __init__, __repr__, etc.
    """

    def __new__(mcs, name, bases, namespace, **kwargs):
        # 1) Create the class normally.
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)

        # 2) Wrap all user-defined callables (skip dunders).
        for attr_name, attr_value in namespace.items():
            if (attr_name.startswith('__') and attr_name.endswith('__')):
                # Skip special methods: __init__, __dir__, etc.
                continue

            if callable(attr_value):
                wrapped = mcs._wrap_invariant(attr_value)
                setattr(cls, attr_name, wrapped)

        return cls

    @staticmethod
    def _wrap_invariant(original_method):
        """Return a function calling self.__invariant__() pre- and post-."""
        def wrapped(self, *args, **kwargs):
            # pre-check
            inv = getattr(self, '__invariant__', None)
            if callable(inv):
                inv()

            # original call
            result = original_method(self, *args, **kwargs)

            # post-check
            if callable(inv):
                inv()

            return result
        return wrapped
