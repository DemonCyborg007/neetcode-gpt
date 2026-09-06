import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        ans=[]
        for i in range(len(z)):
            ans.append(round(1/(1+(math.e)**(-z[i])),5))
        return ans

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        ans=[]
        for i in range(len(z)):
            if z[i]<=0: ans.append(0.0)
            else: ans.append(z[i])
        return ans
