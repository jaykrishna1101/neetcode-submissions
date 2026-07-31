class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print("asd")

        rl, m = 0, len(matrix) - 1
        if m != -1:
            cl = 0
            n = len(matrix[0]) - 1
        else:
            return False
        
        # for i in range(m):
        #     if target >= matrix[i][0] and target <= matrix[i][n-1]:
        while m >= rl:
            # print("df")
            rmid = rl + (m - rl) // 2

            if matrix[rmid][0] <= target and matrix[rmid][n] >= target:
                # print("1")
                while n >= cl:
                    cmid = cl + (n - cl) // 2

                    if matrix[rmid][cmid] == target:
                        return True
                    elif matrix[rmid][cmid] > target:
                        n = cmid - 1
                    else:
                        cl = cmid + 1
                    
            elif matrix[rmid][0] > target:
                # print("2")
                m = rmid - 1
            else:
                # print("3")
                rl = rmid + 1
        return False
