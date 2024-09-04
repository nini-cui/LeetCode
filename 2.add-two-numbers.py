# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def create_linkedlist(self, lst):
        root = dummy = ListNode(0)

        for ele in lst:
            root.next = ListNode(ele)
            root = root.next
        
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l2.val == 0:
            return [0]

        l1_res = []
        l2_res = []

        l1_res.append(l1.val)
        l2_res.append(l2.val)

        while l1 or l2:
            if l1.next:
                l1_res.append(l1.next.val)
                l1 = l1.next

            if l2.next:
                l2_res.append(l2.next.val)
                l2 = l2.next

            if not l1.next and not l2.next:
                break

        l1_sum = 0
        l2_sum = 0

        for (idx, num) in enumerate(l1_res):
            l1_sum += num * int("1" + str(0) * idx)

        for (idx, num) in enumerate(l2_res):
            l2_sum += num * int("1" + str(0) * idx)

        total = l1_sum + l2_sum

        res_lst = []
        for _ in str(total):
            res_lst.append(int(_))

        return self.create_linkedlist(res_lst[::-1])
    
if __name__ == "__main__":
    solution = Solution()
    l1 = solution.create_linkedlist([9,9,9,9,9,9,9])
    l2 = solution.create_linkedlist([9,9,9,9])
    solution.addTwoNumbers(l1, l2)
        

        
            
            
                    

        
        