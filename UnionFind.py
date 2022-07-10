import array as ar
N=1000;
parent=[0]*N;
size=[0]*N;

def make(v):
    parent[v]=v;
    size[v]=1;

def find(v):
    if (v == parent[v]):
        return v;
    parent[v]=find(parent[v]);
    return find(parent[v]);
def Union(a,b):
    a = find(a);
    b = find(b);
    if(a!=b):
        if(size[a]<size[b]):
            a,b=b,a;
        parent[b]=a;
    size[a]+=size[b];

make(1);
make(2);
Union(1,2);
make(3);
make(4);
Union(2,4);
print("parent of 4 is:",find(4));




