#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *wrap_method_call(PyObject *self, PyObject *args) {
    PyObject *method, *instance, *method_args = NULL, *result = NULL;

    // Expect at least instance & method; optionally arguments
    if (!PyArg_UnpackTuple(args, "wrap_method_call", 2, 3, &instance, &method, &method_args)) {
        return NULL;
    }

    // Call __invariant__() before execution
    PyObject *invariant_method = PyObject_GetAttrString(instance, "__invariant__");
    if (invariant_method && PyCallable_Check(invariant_method)) {
        PyObject *res = PyObject_CallObject(invariant_method, NULL);
        if (!res) {
            Py_XDECREF(invariant_method);
            return NULL;  // Propagate exception correctly
        }
        Py_DECREF(res);
    }
    Py_XDECREF(invariant_method);

    // Call the actual method with arguments (if provided)
    if (method_args) {
        result = PyObject_CallObject(method, method_args);
    } else {
        result = PyObject_CallObject(method, NULL);
    }

    if (!result) {
        return NULL;  // If the method raised an exception, propagate it
    }

    // Call __invariant__() after execution
    invariant_method = PyObject_GetAttrString(instance, "__invariant__");
    if (invariant_method && PyCallable_Check(invariant_method)) {
        PyObject *res = PyObject_CallObject(invariant_method, NULL);
        if (!res) {
            Py_XDECREF(invariant_method);
            Py_DECREF(result);
            return NULL;  // Ensure exceptions propagate
        }
        Py_DECREF(res);
    }
    Py_XDECREF(invariant_method);

    return result;
}


static PyMethodDef InvariantMethods[] = {
    {"wrap_method_call", (PyCFunction)wrap_method_call, METH_VARARGS, "Wraps a method call with invariant checks"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef invariantmodule = {
    PyModuleDef_HEAD_INIT,
    "invariant_python",
    NULL,
    -1,
    InvariantMethods
};

PyMODINIT_FUNC PyInit_invariant_python(void) {
    return PyModule_Create(&invariantmodule);
}
