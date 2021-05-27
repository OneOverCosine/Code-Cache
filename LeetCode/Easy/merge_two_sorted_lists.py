# still working on this one

# # Definition for singly-liked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    remaining = None        
    count = 0
    sorted = []
    
    node_count = 0

    while l1 != None and l2 != None:
        if l1.val < l2.val:
            sorted.append(l1)
            l1 = l1.next
        else:
            sorted.append(l2)
            l2 = l2.next
        
        node_count += 1
        print(f"Node {node_count} added!")    
        
        if len(sorted) > 1:
            sorted[count].next = sorted[count + 1]
            print("Node added to previous.next")
            count += 1
            
        print("--------")
    
    if l1.next == None:
        remaining = l2
    else:
        remaining = l1
        
        
    while remaining != None:
        sorted.append(remaining)
        remaining = remaining.next
        node_count += 1
        print(f"Node {node_count} added (rem)!")
        
        if count > 1:
            sorted[count].next = sorted[count + 1]
            print("Node added to previous.next")
            count += 1

        print("--------")
    
    
    out_str = ""
    for node in sorted:
        out_str += str(node.val) + " "
        
    print(out_str)
    
    return sorted[0]

# setup the lists

list_1 = [1, 2, 4]
list_2 = [1, 3, 4]

for value in list_1:
    temp = ListNode()