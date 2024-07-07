import random

def additionGenerator():
    with open(".\Jiahong'sMaths\Addition.txt", "w") as f:
        all_numbers = {}
        counter = 0
        for i in range(2, 10):
            all_numbers[i] = []
            for j in range(2, 10):
                all_numbers[i].append(j)
                counter += 1
        
        for i in range(0, counter):
            first_num = random.randint(2, 9)
            second_num = random.randint(2, 9)
            while len(all_numbers[first_num]) == 0:
                first_num = random.randint(2, 9)
            else:
                while second_num not in all_numbers[first_num]:
                    second_num = random.randint(2, 9)
                else:
                    all_numbers[first_num].remove(second_num)
                    f.write(str(first_num) + " + " + str(second_num) + " =\n")
    f.close()