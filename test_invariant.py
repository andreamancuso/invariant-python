from invariant_python import InvariantMeta

class MyClass(metaclass=InvariantMeta):
    def __invariant__(self):
        print("Checking invariant...")

    def foo(self):
        return 42


# Create an instance of MyClass
my_instance = MyClass()

# Call the foo method
result = my_instance.foo()
print(f"Result of foo(): {result}")