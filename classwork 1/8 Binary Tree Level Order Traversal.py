class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        index = 0
        result = []
        while index < len(queue):
            level = []
            level_size = len(queue) - index
            for _ in range(level_size):
                node = queue[index]
                index += 1
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result