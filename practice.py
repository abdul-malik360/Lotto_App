same_number = 0
        winnings = 0
        prize = [10000000, 8584, 2384, 100.50, 20, 0, 0]
        for i in len(self.same_ans1):
            if i in self.gene_numb:
                same_number += 1
            if same_number == 6:
                winnings = prize[6]
            elif same_number == 5:
                winnings = prize[5]
            elif same_number == 4:
                winnings = prize[4]
            elif same_number == 3:
                winnings = prize[3]
            elif same_number == 2:
                winnings = prize[2]

        if len(self.first_numbs) == 6:
            user_prize = float(winnings)
            self.prize1.set(str(user_prize))
            self.lotto1.set(self.gene_numb)
            return user_prize
        # else:
        #     messagebox.showinfo("Error", "Please use all your tries first")


