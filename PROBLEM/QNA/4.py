# 4. Fibonacci Series (First N Terms)

def fibonacci(num):
    if num<0:
        return "Invalid input"
    elif num ==0:
        return 0
    elif num==1:
        return 1

    return fibonacci(num-1)+fibonacci(num-2)

# time: O(2^n)

num=3
print(fibonacci(num))
