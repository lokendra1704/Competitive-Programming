class ClassicSegmentTree:
    def __init__(self, arr, fn=lambda x,y:x+y):
        'Builds Segment Tree using the aggregator function fn'
        self.fn = fn
        self.arr = arr
        self.n = len(arr)
        self.tree = [0]*(2*self.n)
        self.build_rec(0,self.n-1)

    def __repr__(self):
        return str(self.tree)
    
    def build_rec(self,l,r,id=1):
        'Build Tree using Recursion'
        if l==r:
            self.tree[id] = self.arr[l]
        else:
            mid = (l+r)//2
            self.build_rec(l,mid,2*id)
            self.build_rec(mid+1,r,2*id+1)
            self.tree[id] = self.fn(self.tree[2*id], self.tree[2*id+1])

    def build(self):
        'Build Tree using Iteration'
        n = self.n
        self.tree[n:2*n +1] = self.arr[:]
        for i in range(n-1,0,-1):
            self.tree[i] = self.fn(self.tree[2*i], self.tree[2*i+1])

    def update(self,pos,val):
        pos+=self.n
        self.tree[pos]=val
        while pos>0:
            l = pos
            r = pos
            if pos%2==0:
                r+=1
            else:
                l-=1
            self.tree[pos//2] = self.fn(self.tree[l], self.tree[r])
            pos//=2

    def query(self,l,r):
        l+=self.n
        r+=self.n
        total = 0
        while l<=r:
            #Check if l is right child of its parent. If so, its parent will contain sum of redundant leafs.
            if l%2==1:
                total+=self.tree[l]
                l+=1
            #Check if r is left child of its parent. If so, its parent will contain sum of redundant leafs.
            if r%2==0:
                total+=self.tree[r]
                r-=1
            l//=2
            r//=2
        return total
    

arr = [2,4,5,7]
tree = ClassicSegmentTree(arr)
print(tree)
print(tree.query(0,3))
tree.update(0,3)
print(tree)
print(tree.query(0,3))