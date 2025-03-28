class List:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def sort(self, reverse=False):
        p = self.next
        while p:
            q = p.next
            while q:
                if not reverse:
                    if p.data > q.data:
                        p.data, q.data = q.data, p.data
                else:
                    if p.data < q.data:
                        p.data, q.data = q.data, p.data
                q = q.next
            p = p.next



def ListCreate():
    """头插法创建链表"""
    head = List()
    n = int(input("请输入链表长度: "))
    for i in range(1, n + 1):
        data = int(input(f"请输入第{i}个元素: "))
        p = List(data)
        p.next = head.next
        head.next = p
    return head


def ListCreate2():
    """尾插法创建链表"""
    head = List()
    rear = head
    n = int(input("请输入链表长度: "))
    for i in range(1, n + 1):
        data = int(input(f"请输入第{i}个元素: "))
        p = List(data)
        rear.next = p
        rear = p
    return head


def ListPrint(head):
    p = head.next
    while p:
        print(p.data, end=" ")
        print('->', end=' ')
        p = p.next
    print('None')


if __name__ == "__main__":
    Head = ListCreate2()
    ListPrint(Head)
    Head.sort()
    ListPrint(Head)