import matplotlib.pyplot as plt
import scipy.special as sps

import numpy as np

# shape, scale = 2., 1.  # mean=4, std=2*sqrt(2)
# s = np.random.gamma(shape, scale, 1000)
#
# print(s)
#
# count, bins, ignored = plt.hist(s, 50, density=True)
# y = bins**(shape-1)*(np.exp(-bins/scale) /
#                      (sps.gamma(shape)*scale**shape))
#
# res = np.random.dirichlet(np.ones(300), size=1)[0]
#
# # plt.plot(bins, y, linewidth=2, color='r')
# plt.plot(res)
# plt.show()

# rand_array = np.random.rand(1, 300)[0]
# print(rand_array)
# print(sum(rand_array))
# rand_array = (rand_array / (rand_array.mean()))/len(rand_array)
# print(rand_array)
# print(sum(rand_array))

array = np.arange(300)[::-1]
array = (array / (array.mean()))/len(array)

print(array)
print(sum(array))
# normed_array = (rand_array / (rand_array.mean()))/len(rand_array)

