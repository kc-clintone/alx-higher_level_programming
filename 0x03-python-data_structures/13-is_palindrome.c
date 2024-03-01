#include "lists.h"

/**
 * reverse_listint - This function reverses a linked list.
 * @head: Pointer to first node.
 * Return: Pointer to first node in new list.
*/
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *next = NULL;
listint_t *cur = *head;

while (cur)
{
next = cur->next;
cur->next = prev;
prev = cur;
cur = next;
}
*head = prev;
}

/**
 * is_palindrome - This right here checks if a linked-list is a
 * palindrome
 * @head: A double pointer to the linked-list.
 * Return: 1 if true, 0 Otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *x = *head, *y = *head;
listint_t *tmp = *head, *dbl = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);
while (1)
{
y = y->next->next;
if (!y)
{
dbl = x->next;
break;
}
if (!y->next)
{
dbl = x->next->next;
break;
}
x = x->next;
}
reverse_listint(&dbl);
while (dbl && tmp)
{
if (tmp->n == dbl->n)
{
dbl = dbl->next;
tmp = tmp->next;
}
else
return (0);
}
if (!dbl)
return (1);
return (0);
}
