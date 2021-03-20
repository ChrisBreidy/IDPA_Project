

class EditDistance:


    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.arr = 0

    def CostDel(self,x):
        return x+1

    def CostInst(self,x):
        return x+1

    def print_arr(self,arr):
        for x in arr:
            print(x)

    #Case sensitive update
    def CostUpdt(self,x,y):
        if x==y:
            return 0
        else:
            return 1

    seq1= ""
    seq2= ""

    def set_seq1(self,seq1):
        self.seq1 = seq1

    def set_seq2(self,seq2):
        self.seq2 = seq2

    def get_seq1(self):
        return self.seq1

    def get_seq2(self):
        return self.seq2

    def compute_ed(self):


        rows, cols = (len(self.seq1) + 1, len(self.seq2) + 1)
        dist = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(1, len(self.seq1) + 1):
            dist[i][0] = self.CostDel(dist[i - 1][0])

        for i in range(1, len(self.seq2) + 1):
            dist[0][i] = self.CostInst(dist[0][i - 1])

        # print_arr(Dist)

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                dist[i][j]=min((dist[i - 1][j - 1] + self.CostUpdt(self.seq1[i - 1], self.seq2[j - 1])), (self.CostInst(dist[i][j - 1])), (self.CostDel(dist[i - 1][j])))
        self.arr = dist
        return dist


    def get_ed(self):
        return self.arr[len(self.seq1)][len(self.seq2)]







