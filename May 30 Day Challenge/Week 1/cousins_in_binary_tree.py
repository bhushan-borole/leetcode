class Solution:
    def isCousins(self, root, x, y):
        arr = [[0, 0] for _ in range(101)]
        def traverse(r, depth, pv):
            if not r: return
            arr[r.val] = [depth, pv]
            traverse(r.left, depth + 1, r.val)
            traverse(r.right, depth + 1, r.val)

        traverse(root, 0, -1)
        return arr[x][0] == arr[y][0] and arr[x][1] != arr[y][1]