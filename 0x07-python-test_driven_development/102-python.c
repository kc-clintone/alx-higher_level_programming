#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - This function prints string information
 * @p: Python object
 * Return: Returns nothing
*/

void print_python_string(PyObject *p)
{

PyObject *str, *rep;

(void)rep;
printf("[.] string object info\n");

if (strcmp(p->ob_type->tp_name, "str"))
{
printf("  [ERROR] Invalid string object\n");
return;
}
if (PyUnicode_IS_COMPACT_ASCII(p))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");
rep = PyObject_Repr(p);
str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
printf("  value: %s\n", PyBytes_AsString(str));
}
