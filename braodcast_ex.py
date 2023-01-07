import numpy as np

a = np.random.randn(5) # randn = 평균0 표준편차1의 가우시안 분포 
print(a)
print(a.shape) # (5,) 의 형태. 즉, rank가 1인 array이고 행과 열의 구분 x
print(a.T) # print(a.transpose()) 를 취해도 같은 형태
print(np.dot(a, a.T)) # 벡터간의 곱이지만 python에서는 행렬이 아닌 실수값이 나옴. 따라서 rank가 1인 행렬을 신경망 연산에 사용하지 않는걸 추천

######

a = np.random.rand(5,1) # 한 줄짜리 벡터라도 반드시 행 또는 열을 지정해줄것!!
print(a) # 5x1의 열 벡터로 지정
print(a.shape)
print(a.T) # 전치가 행 벡터로 달라짐
print(np.dot(a, a.T)) # 벡터의 외적이 제대로 표시
print(np.dot(a.T, a))