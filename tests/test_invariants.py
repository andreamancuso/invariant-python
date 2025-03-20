import unittest
from invariant_python import InvariantMeta

class MyClass(metaclass=InvariantMeta):
    def __invariant__(self):
        print("Checking invariant...")

    def foo(self):
        return 42

class TestInvariants(unittest.TestCase):
    def test_foo(self):
        obj = MyClass()
        val = obj.foo()
        self.assertEqual(val, 42)

if __name__ == "__main__":
    unittest.main()
