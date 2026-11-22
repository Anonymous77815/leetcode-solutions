class Solution(object):
    def countServers(self, n, logs, x, queries):

        logs.sort(key=lambda x:x[1])
        queries_sort = queries_sort = sorted(enumerate(queries), key=lambda x: x[1])

        dictLog = dict.fromkeys((item[0] for item in logs),0)
        result = [0]*len(queries_sort)

        left,right = 0, 0

        for index, q in queries_sort:

            pass