class DSU:
    def __init__(self,size):
        if size>0:
            self.arr = [i for i in range(size)]
            self.size = [1]*size
            self.numberOfComponents = size

    def find(self,p):
        root = p
        while self.arr[root]!=root:
            root = self.arr[root]

        #path-compression
        while p!=root:
            _next = self.arr[p]
            self.arr[p] = root
            p = _next

        return root

    def connected(self,x,y):
        return self.find(x)==self.find(y)

    def componentSize(self,x):
        return self.size[self.find(x)]

    def components(self):
        return self.numberOfComponents

    def unify(self,x,y):
        a = self.find(x)
        b = self.find(y)
        if a==b:
            return
        if self.size[a] > self.size[b]:
            self.arr[b] = a
            self.size[a]+=self.size[b]
        else:
            self.arr[a] = b
            self.size[b]+=self.size[a]
        self.numberOfComponents-=1

#Small Notation
class DSU:
    def __init__(self,n):
        self.id = [i for i in range(n)]
    def find(self,n):
        while self.id[n]!=n:
            n = self.id[n]
        return self.id[n]
    def union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        self.id[a] = b