import time
def fun(n):
    time.sleep(0.01)
    print(n)
    try:
        fun(n+1)
    except:
        print("error:",n)
fun(1)