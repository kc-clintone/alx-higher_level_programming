#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This function prints information on bytes.
 * @p: A python Object.
 * Return: Nada.
 */
void print_python_bytes(PyObject *p)
{
long int lim, mag, index;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
mag = ((PyVarObject *)(p))->ob_size;
str = ((PyBytesObject *)p)->ob_sval;
printf("  size: %ld\n", mag);
printf("  trying string: %s\n", str);
if (mag >= 10)
lim = 10;
else
lim = mag + 1;
printf("  first %ld bytes:", lim);
for (index = 0; index < lim; index++)
if (str[index] >= 0)
printf(" %02x", str[index]);
else
printf(" %02x", 256 + str[index]);
printf("\n");}

/**
 * print_python_list - This function prints information on lists.
 * @p: A python Object.
 * Return: Nada.
 */
void print_python_list(PyObject *p)
{
long int index, mag;
PyListObject *list;
PyObject *obj;

mag = ((PyVarObject *)(p))->ob_size;
list = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", mag);
printf("[*] Allocated = %ld\n", list->allocated);
for (index = 0; index < mag; index++)
{
obj = ((PyListObject *)p)->ob_item[index];
printf("Element %ld: %s\n", index, ((obj)->ob_type)->tp_name);
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}
