class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class LinkedList:
    def __init__(self):
        self.start=None;
    def ViewList(self):
        if self.start==None:
            print("List is empty");
        else:
            temp=self.start;
            while temp!=None:
                print(temp.data,end=" ");
                temp=temp.next;
    def DeleteFirst(self):
        if self.start==None:
            print("List is empty");
        else:
            self.start=self.start.next;

    def Insert(self,value):
        newNode=Node(value);
        if(self.start==None):
            self.start=newNode;
        else:
            temp=self.start;
            while temp.next!=None:
                temp=temp.next;
            temp.next=newNode;

def main():
    Mylist=LinkedList();
    Mylist.Insert(1);
    Mylist.Insert(2);
    Mylist.Insert(3);
    Mylist.Insert(4);

    Mylist.ViewList();
if __name__=="__main__":
    main();
