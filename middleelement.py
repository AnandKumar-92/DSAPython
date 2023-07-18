class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):
        head = A
        node = ListNode(B)
        if C == 0:
            node.next = A
            return node
        count = 1
        while A.next is not None:
            if C != count:
                A = A.next
                count += 1
            else:
                break

        node.next = A.next
        A.next = node
        return head

    def middleelement(self, A):
        fast, slow = A, A
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return print(slow.val)



nodelinked=ListNode(93)
nodelinked=Solution().solve(nodelinked,28,0)
nodelinked=Solution().solve(nodelinked,36,0)
nodelinked=Solution().solve(nodelinked,26,0)
nodelinked=Solution().solve(nodelinked,98,0)
nodelinked=Solution().solve(nodelinked,42,0)
nodelinked=Solution().solve(nodelinked,14,0)
head=nodelinked
nodelinked=Solution().middleelement(head)

