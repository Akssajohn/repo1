class MyClass:
  n=0
  def __init__(self):
    MyClass.n = MyClass.n+1
    
  @staticmethod
  def noObjects():
    print('Number of intsances created:', MyClass.n)
  obj1 = MyClass()
  obj2 = MyClass()
  obj3 = MyClass()
  MyClass.noObjects()
