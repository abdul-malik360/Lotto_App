mylist = [1, 34, 5, 23, 21, 11]
mylist2 = [32, 21, 12, 34, 41, 2, 34]
mylist.sort()
mylist2.sort()
newlist=[]
for x in mylist:
    if x in mylist2:
        newlist.append(x)
print(newlist)



         # for i in self.gen_numbs.get():
         #    if i in self.numb_ent1.get():
         #        self.same_numb.append(i)
         #        self.same_ans.set(self.same_numb)

 # y = 0
 #        for i in range(0, 6):
 #            if self.first_numbs[i] == self.gene_numb[i]:
 #                y += 1
 #                self.same_numb.append(i)
 #            self.same_ans.set(self.same_numb)
