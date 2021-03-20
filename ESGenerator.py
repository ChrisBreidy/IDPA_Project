from collections import deque

class Generator:

    def __init__(self,arr,seq1,seq2):
        self.arr = arr
        self.seq1 = seq1
        self.seq2 = seq2

    def get_edit_script(self):
        edit_scpt = deque()
        edit_scripts = []
        ed = self.arr[len(self.seq1)][len(self.seq2)]
        i = len(self.seq1)
        j = len(self.seq2)

        def edit_script(i, j):

            while i > 0 and j > 0:

                if (len(edit_scpt) == self.arr[len(self.seq1)][len(self.seq2)]):
                    break

                if (self.arr[i][j - 1] == self.arr[i][j] - 1):
                    # edit_scpt.appendleft(f'Ins(B{j},{i + 1})')
                    edit_scpt.appendleft(['Ins', f'B{j},{i+1}'])
                    j = j - 1
                    edit_script(i, j)


                else:
                    if (self.arr[i - 1][j] == self.arr[i][j] - 1):
                        # edit_scpt.appendleft(f'Del(A{i})')
                        edit_scpt.appendleft(['Del', f'A{i}'])
                        i = i - 1
                        edit_script(i, j)

                    else:
                        if (self.arr[i - 1][j - 1] == self.arr[i][j]):
                            i = i - 1
                            j = j - 1
                            edit_script(i, j)

                        else:

                            if (self.arr[i - 1][j - 1] == self.arr[i][j] - 1):
                                # edit_scpt.appendleft(f'Upt(A{i},B{j})')
                                edit_scpt.appendleft(['Upt',f'A{i},B{j}'])
                                i = i - 1
                                j = j - 1
                                edit_script(i, j)

            # if(len(edit_scpt)==3):
            #     edit_scripts.append(edit_scpt)
            # else:
            #     edit_scpt.clear()

        edit_script(len(self.seq1), len(self.seq2))

        return edit_scpt

    # print_arr(Dist)
    # print(get_edit_script(Dist,A,B))