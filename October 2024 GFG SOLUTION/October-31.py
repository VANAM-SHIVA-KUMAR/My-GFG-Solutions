#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        temp=head
        prev=None
        if head.data>x:
            temp1=Node(x)
            temp1.next=head
            return temp1
        while temp!=None:
            if temp.data>x:
                break
            prev=temp
            temp=temp.next
        temp1=Node(x)
        prev.next=temp1
        temp1.next=temp
        return head
