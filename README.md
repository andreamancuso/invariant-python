# Invariant Python

**Invariant Python** is a simple library that enforces **Design by Contract (DbC)** by automatically calling `__invariant__()` before and after method execution. This helps maintain object integrity and detect state violations early.

## Features

- **Automatic invariant checks** before and after method execution  
- **Metaclass-based approach** (no decorators needed)  
- **Skips dunder methods** to avoid conflicts (`__init__`, `__repr__`, etc.)  
- **Lightweight & pure Python** (no dependencies)  

## Installation

```sh
pip install git+https://github.com/andreamancuso/invariant-python.git
```

## Usage

Simply define a class with `InvariantMeta` as the metaclass, and implement `__invariant__()`.

```python
from invariant_python import InvariantMeta

class MyClass(metaclass=InvariantMeta):
    def __invariant__(self):
        print("Checking invariants...")

    def foo(self):
        print("Inside foo")

    def bar(self, x):
        print(f"Inside bar with x={x}")

# Usage
obj = MyClass()
obj.foo()
obj.bar(42)
```

### **Output:**
```
Checking invariants...
Inside foo
Checking invariants...
Checking invariants...
Inside bar with x=42
Checking invariants...
```

## How It Works

- The `InvariantMeta` metaclass **automatically wraps** every **user-defined method** in the class.
- It calls `__invariant__()` **before and after** each method execution.
- Dunder methods (`__init__`, `__repr__`, etc.) are **not wrapped** to avoid issues.

## Customization

If you need to **exclude** certain methods from being wrapped, you can subclass `InvariantMeta`:

```python
class CustomInvariantMeta(InvariantMeta):
    def __new__(mcs, name, bases, namespace):
        # Remove specific methods from being wrapped
        namespace.pop("skip_this", None)
        return super().__new__(mcs, name, bases, namespace)

class CustomClass(metaclass=CustomInvariantMeta):
    def __invariant__(self):
        print("Checking invariants...")

    def safe_method(self):
        print("This method is wrapped")

    def skip_this(self):
        print("This method is NOT wrapped")

obj = CustomClass()
obj.safe_method()   # Calls __invariant__
obj.skip_this()     # Does NOT call __invariant__
```

## Running Tests

To run the unit tests:

```sh
python -m unittest discover tests
```

## Performance Considerations

This library is implemented in pure Python. If you require **higher performance**, a C extension version may be explored in the future.

## Contributing

Contributions are welcome!  
If you have ideas, feature requests, or bug reports, please open an issue or a pull request.

### **How to Contribute**
1. Fork the repository and clone it locally.
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -e .
   ```
3. Run tests before submitting a pull request:
   ```sh
   python -m unittest discover tests
   ```
4. Open a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to contributors and the Python community for continuous improvements and feedback.

