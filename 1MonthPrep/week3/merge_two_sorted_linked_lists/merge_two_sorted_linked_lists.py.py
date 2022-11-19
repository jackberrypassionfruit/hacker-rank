def mergeLists(head1, head2):
    head = head1
    head1_tmp = head1.next
    head2_tmp = head2.next
    while head2.data <= head1.data:
        head2.next = head
        head = head2
        head2 = head2_tmp
        print(f'head.data: {head.data}, head2.data: {head2.data}')
        
        
    while head1.next and head2:
        head1_tmp = head1.next
        head2_tmp = head2.next
        
        print(f'head1.next.data: {head1.next.data}, head2.data: {head2.data}')
        if not head1.next:
            head1.next = head2
        elif head2.data <= head1.next.data:
            head2.next = head1.next
            head1.next = head2
            head2 = head2_tmp
        else:
            head1 = head1.next
            
    if head2:
        head1.next = head2
    
    return head

#  2 4 6 8
# 1 3 5 7 9


# 1 2 3
#  3 4
 
# 4 5 6
#  1 2 10