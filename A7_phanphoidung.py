import matplotlib.pyplot as plt
import numpy as np

String=['vừa mới thay','còn tốt','vẫn dùng được','đã bị hỏng']

PI_i=[[0.2],[0.3],[0.1],[0.4]]

P=np.array([[0,0.8,0.2,0],
			[0,0.6,0.4,0],
			[0,0,0.5,0.5],
			[1,0,0,0]])

PI=np.array([0.2,0.3,0.1,0.4])

for i in range(1,51):
	PI=PI.dot(P);
	for j in range(0,len(PI_i)):
		PI_i[j].append(PI[j])
A=np.arange(51)

for k in range(0,len(String)):
	plt.plot(A, PI_i[k], label=String[k])

plt.legend(loc='best')

plt.show()