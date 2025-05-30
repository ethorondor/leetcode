#%%
class solutions:
    def inplace_sorting(self, arr):
        """
        Sorts the array in place using the built-in sort method.
        :param arr: List of integers to be sorted.
        :return: The sorted list.
        """
        arr.sort()
        return arr
nums = [5, 2, 9, 1, 5, 6]
sol = solutions()
print(sol.inplace_sorting(nums))  # Output: [1, 2, 5, 5, 6, 9]
# %%
