#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: Pointer head of the linked list.
 * @number: Number to insert.
 * Return: 0 on fail, otherwise pointer to new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *nd = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (nd == NULL || nd->n >= number)
{
new->next = nd;
*head = new;
return (new);
}
while (nd && nd->next && nd->next->n < number)
nd = nd->next;
new->next = nd>next;
nd->next = new;
return (new);
}

