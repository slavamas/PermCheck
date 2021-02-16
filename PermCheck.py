def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print(
            "{:s} function took {:.3f} ms".format(f.__name__, (time2 - time1) * 1000.0)
        )
        return ret
    return wrap
######
@timing
def solution(A):
    As = set(range(1,len(A)+1))
    maxA = max(A)
    maxAs = max(As)
    D = abs(maxAs - maxA)
    idealA=set(A)
    if (D == 0) and (sum(idealA) - sum(A)) == 0:
        D = 1
        return D
    else:
        D = 0
        return D
#solution2 function took 0.010 ms
# 1
