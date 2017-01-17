# To check weather a given string is palindrome or not using DeQueue.


from DoublyEndedQueue import Deque


def is_palindrome(str):
    queue = Deque()
    for i in range(0, len(str)):
        queue.enqueue_rear(str[i])
    palin = True
    while not queue.is_empty() and queue.size != 1:
        if queue.dequeue_front() != queue.dequeue_rear():
            palin = False
    return palin
