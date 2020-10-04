class UnionFind:
    def __init__(self,size):
        if size>0:
            self.union = [i for i in range(size)]
            self.size = [1]*size
            self.numberOfComponents = size

    def find(self,p):
        root = p
        while self.union[root]!=root:
            root = self.union[root]

        #path-compression
        while p!=root:
            _next = self.union[p]
            self.union[p] = root
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
            self.union[b] = a
            self.size[a]+=self.size[b]
        else:
            self.union[a] = b
            self.size[b]+=self.size[a]
        self.numberOfComponents-=1