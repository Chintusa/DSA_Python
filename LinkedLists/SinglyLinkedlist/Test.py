from LinkedList import LinkedList
class Test:
    def test():
        l=LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        l.append(8)
        l.append(9)
        while True: 
            print("Enter you choice :")
            ch=int(input("1.Apend\n2.display\n3.size\n4.appendFirst\n5.insert\n6.delete\n7.deleteFirst\n8.remove\n9.search\n10.insert before an element\n11.insert after an element\n12.exit\n"))
            if ch==1:
                l.append(int(input("Enter the data:")))
            elif ch==2:
                l.display()
            elif ch==3 :
                print(l.get_size())
            elif ch==4 :
                l.appendFirst(int(input("Enter the data:")))
            elif ch==5 :
                l.insert(int(input("Enter the Pos :")),int(input("Enter the data :")))
            
            elif ch==6 :
                l.delete()
            elif ch==7:
                l.deleteFirst()
            elif ch==8:
                l.remove(int(input("Enter the Pos :")))
            elif ch==9:
                pos=l.search(int(input("Enter the data :")))
                if pos == -1:
                    print("Element not found!")
                else:
                    print(pos)
                
            elif ch==10:
                 l.addBefore(int(input("Enter the element :")),int(input("Enter the new Data :")))
            elif ch==11:
                 l.addAfter(int(input("Enter the element :")),int(input("Enter the new Data :")))
            elif ch==12:
                break
            else:
                print("Invalid choice!")
    test()
            
            