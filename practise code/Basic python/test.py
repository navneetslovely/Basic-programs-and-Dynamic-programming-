class A:
        
    def say(self):
        self.__say()
    
    def __say(self):
        print("A")
        

class B(A):

    def __say(self):
        print("B")


a = A()
b = B()

a.say()
b.say()