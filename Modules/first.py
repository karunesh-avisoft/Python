import sys
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  # 2000