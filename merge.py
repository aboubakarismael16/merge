from heapq import heapify,heappush,heappop

class Node:
    def __init__(self,val,next_node=None):
        self.val = val
        self.next = next_node

    def __lt__(self,other):
        return self.val < other.val
    

def merge_list(lists):
    heap = list(lists)
    heapify(heap)

    ref = Node(0)
    tail = None

    while heap:
        lowest = heap[0]
        heappop(heap)
        if lowest.next:
            heappush(heap,lowest.next)

        if ref.next is None:
            ref.next = lowest
            tail = lowest
        else:
            tail.next = lowest
            tail = lowest
    return ref.next


def print_list(head):
    while head:
        print(head.val)
        head = head.next

# five = Node(5)
# four = Node(4,five)
# one = Node(1,four)

# four_2 = Node(4)
# three = Node(3,four_2)
# one_2 = Node(1,three)

# six  = Node(6)
# two = Node(2,six)

# merged = merge_list([one,one_2,two])
# print_list(merged)

# merged = merge_list([])
# print(merged)



five = Node(5)
four = Node(4,five)
one = Node(1,four)

four_2 = Node(4)
two = Node(2,four_2)
three = Node(3,two)

six = Node(6)
one_2 = Node(1,six)

merged = merge_list([one,one_2,three])
print_list(merged)

merged = merge_list([])
print(merged)
