#include <Python.h>

/**===prototypes===*/
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - This function prints the basic info about
 * Python byte objects.
 * @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

        fflush(stdout);

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size >= 10)
                size = 10;
        else
                size = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %ld bytes: ", size);
        for (i = 0; i < size; i++)
        {
                printf("%02hhx", bytes->ob_sval[i]);
                if (i == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}
