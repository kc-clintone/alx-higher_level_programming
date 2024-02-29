#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - This function prints some basic info
 *about pytohn list
 * @p: python object
*/

void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int x;
PyListObject *obj = (PyListObject *)p;
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj->allocated);
for (x = 0; x < size; x++)
printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
}
