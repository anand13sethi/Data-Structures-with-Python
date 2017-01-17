# To check weather a given string is palindrome or not using DeQueue.


from DoublyEndedQueue import Deque


def is_palindrome(queue=Deque()):
    palin = True
    while not queue.is_empty() and queue.size != 1:
        if queue.dequeue_front() != queue.dequeue_rear():
            palin = False
    return palin
