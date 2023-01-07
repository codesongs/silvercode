import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
             [1.2, 104.0, 52.0, 8.0],
             [1.8, 135.0, 99.0, 0.9]])

print(A)

cal = np.sum(A, axis=0) # A.sum(axis=0)와 동일. axis=0는 가로, axis=1은 세로
print(cal)

percentage = 100 * A/cal.reshape(1,4) #reshape를 안해도 cal은 1x4 행렬이지만 확실한 표기를 위한 함수사용. reshape는 상수시간이라 효율성에 큰 영향 x
print(percentage)