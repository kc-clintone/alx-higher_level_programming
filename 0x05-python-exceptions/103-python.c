#include <Python.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_float - This function prints basic info about
 * Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
char *bfr = NULL;

PyFloatObject *float_obj = (PyFloatObject *)p;

fflush(stdout);
printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
bfr = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", bfr);
PyMem_Free(bfr);
}

/**
 * print_python_bytes - This funtion prints basic info
 * about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t x, y;
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
x = 10;
else
x = ((PyVarObject *)p)->ob_size + 1;
printf("  first %ld bytes: ", x);
for (y = 0; y < x; y++)
{
printf("%02hhx", bytes->ob_sval[y]);
if (y == (x - 1))
printf("\n");
else
printf(" ");
}
}

/**
 * print_python_list - This function prints basic info about
 * Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t x, y, z;
const char *type;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

x = var->ob_size;
y = list->allocated;

fflush(stdout);
printf("[*] Python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}
printf("[*] Size of the Python List = %ld\n", x);
printf("[*] Allocated = %ld\n", y);
for (z = 0; z < x; z++)
{
type = list->ob_item[z]->ob_type->tp_name;
printf("Element %ld: %s\n", z, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(list->ob_item[z]);
else if (strcmp(type, "float") == 0)
print_python_float(list->ob_item[z]);
}
}
