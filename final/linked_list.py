
def create_node(value):
    """
    Створює новий вузол зі значенням value.
    """
    return {'value': value, 'next': None}

def append(head, value):
    """
    Додає новий вузол зі значенням value до кінця списку.
    """
    new_node = create_node(value)
    if not head:
        return new_node
    current = head
    while current['next']:
        current = current['next']
    current['next'] = new_node
    return head

def print_list(head):
    """
    Виводить значення всіх вузлів у списку.
    """
    current = head
    while current:
        print(current['value'], end=" -> ")
        current = current['next']
    print("None")

def reverse(head):
    """
    Реверсує (перевертає) список, змінюючи посилання між вузлами.
    """
    prev = None
    current = head
    while current:
        next_node = current['next']
        current['next'] = prev
        prev = current
        current = next_node
    return prev

def sorted_insert(head, new_node):
    """
    Вставляє новий вузол у відсортований список на правильну позицію.
    """
    if not head or head['value'] >= new_node['value']:
        new_node['next'] = head
        return new_node
    current = head
    while current['next'] and current['next']['value'] < new_node['value']:
        current = current['next']
    new_node['next'] = current['next']
    current['next'] = new_node
    return head

def insertion_sort(head):
    """
    Сортує список методом вставки.
    """
    sorted_head = None
    current = head
    while current:
        next_node = current['next']
        current['next'] = None
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head

def merge_sorted_lists(list1, list2):
    """
    Об'єднує два відсортовані однозв'язні списки в один відсортований список.
    """
    dummy = create_node(0)
    tail = dummy
    while list1 and list2:
        if list1['value'] < list2['value']:
            tail['next'] = list1
            list1 = list1['next']
        else:
            tail['next'] = list2
            list2 = list2['next']
        tail = tail['next']
    if list1:
        tail['next'] = list1
    if list2:
        tail['next'] = list2
    return dummy['next']
