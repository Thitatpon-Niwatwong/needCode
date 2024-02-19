class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Helper function to create a linked list from a list of values


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example usage
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(values)
    print("Original linked list:")
    print_linked_list(linked_list)

    solution = Solution()
    reversed_list = solution.reverseList(linked_list)

    print("Reversed linked list:")
    print_linked_list(reversed_list)
