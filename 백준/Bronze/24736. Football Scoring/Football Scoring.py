a=list(map(int,input().split()))
b=list(map(int,input().split()))

def s(q):
    return q[0]*6+q[1]*3+q[2]*2+q[3]+q[4]*2
print(s(a),s(b))