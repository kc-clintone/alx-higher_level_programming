#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if it is a palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1)

listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *temp;
int result = is_palindrome(&head);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}
if (fast != NULL)
slow = slow->next;

while (slow != NULL)
{
if (slow->n != prev->n)
return (0);

slow = slow->next;
prev = prev->next;
}

return (1);
}
