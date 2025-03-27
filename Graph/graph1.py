"""邻接矩阵表示图"""

class Matrix:
    def __init__(self):
        """
            matrix    邻接矩阵
            vertex    顶点
            """
        self.vertex = []
        self.matrix = []

    def CreateMatrix(self):
        """创建无向图邻接矩阵"""
        length = int(input('请输入顶点数量: '))
        for i in range(length):
            self.matrix.append([0] * length)
        # self.matrix = [[0] * length] * length         # 错误项，
        for i in range(length):
            ver = input(f'请输入第{i + 1}个顶点值: ')
            self.vertex.append(ver)
        num = int(input('请输入边的数量'))
        for i in range(num):
            verA, verB = input(f"请输入{i + 1}条边的两个顶点: ").split()
            self.matrix[self.vertex.index(verA)][self.vertex.index(verB)] = 1
            self.matrix[self.vertex.index(verB)][self.vertex.index(verA)] = 1

    def OutPutMatrix(self):
        print(*self.matrix, sep='\n')


if __name__ == "__main__":
    graph = Matrix()
    graph.CreateMatrix()
    graph.OutPutMatrix()