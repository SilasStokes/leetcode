import random

# implementation done based on this video:
# https://www.youtube.com/watch?v=v-1EGgaTFuw

def quick_select(lst, k):
    def __quick_select(l = 0, r = len(lst) - 1):
        ...
    
    return __quick_select()

# can I parallelize(?)
def quick_sort(nums):
    
    def __quick_sort(start, end):
        def __get_pivot():
            """
            Gets the pivot based on the median value. 
            """
            from random import randint
            a, b, c = randint(start, end), randint(start, end), randint(start, end)
            if nums[a] <= nums[b] <= nums[c]:
                return b
            elif nums[b] <= nums[a] <= nums[c]:
                return a
            else: return c

        nonlocal nums

        if start >= end: 
            return 

        # grab a pivot, first do right most
        # piv = end # update this to take a median of 3 rand values

        piv = __get_pivot()

        nums[piv], nums[end] = nums[end], nums[piv]
        piv = end

        # if pivot is not r, then swap it with r.
        gt = start # gt = greater than element
        for i in range(start, end):
            if nums[i] <= nums[piv]:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt += 1
            # do nothing if the cur val is greater than the pivot

        # then place pivot in the bisected area
        nums[gt], nums[piv] = nums[piv], nums[gt]

        
        __quick_sort(gt + 1, end)
        __quick_sort(start, gt - 1)

    __quick_sort(0, len(nums)-1)
    return nums

def main():
    dtaylor_list = [40,41,17,-22,25,55,-18,35,10,25,33,19,33,51,25]
    print(f'{dtaylor_list=}')
    quick_sort(dtaylor_list)
    print(f'{dtaylor_list=}')
    
    # rand_list = random.choices(population=range(1000),k=100)
    # print(f'{rand_list}')



if __name__ == "__main__":
    main()