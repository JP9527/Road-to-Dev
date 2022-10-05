#BFS

# 拓扑排序(100%)
# 出现连通块的关键词(100%)
# 分层遍历(100%)
# 简单图最短路径(100%)
# 给定一个变换规则，从初始状态变到终止状态最少几步(100%)
# 时间复杂度：O(n + m)
# n 是点数, m 是边数
# 空间复杂度：O(n)

import collections

def bfs(start_node):
    # BFS 必须要用队列queue，别用栈stack！
    # distance(dict) 有两个作用，一个是记录一个点是否被丢进过队列了，避免重复访问
    # 另外一个是记录start_node 到其他所有节点的最短距离
    # 如果只求连通性的话，可以换成set 就行
    # node 做key 的时候比较的是内存地址

    queue = collections.deque([start_node])

    distance = {start_node: 0}

    # while 队列不空，不停的从队列里拿出一个点，拓展邻居节点放到队列中
    while queue:
        node = queue.popleft()
        # 如果有明确的终点可以在这里加终点的判断
        if node 是终点：
            break or return something
        
        for neighbor in node. get_neighbors():
            if neighbor in distance:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + 1
        
        # 如果需要返回所有点离起点的距离，就return hashmap
        return distance

        #如果需要返回所有连通的节点, 就return HashMap 里的所有点
        return distance.keys()

        # 如果需要返回离终点的最短距离
        return distance[end_node]




