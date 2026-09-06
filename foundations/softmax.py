import numpy as np
from numpy.typing import NDArray
import math


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_z = max(z)
        new_z = [i-max_z for i in z]
        ans=[]
        for i in new_z:
            ans.append(math.e**i)
        sum_ans = sum(ans)
        new_ans = [round(i/sum_ans,4) for i in ans]
        return new_ans
