import random

def subtractionGenerator(name):
    with open(f".\Jiahong'sMaths\{name}.txt", "w") as f:
        all_numbers = {}
        counter = 0
        for i in range(4, 19):
            all_numbers[i] = []
            for j in range(2, 10):
                all_numbers[i].append(j)
                counter += 1

        for i in range(4, 19):
            for j in range(2,10):
                if (i-j)/10 >= 1 or (i-j) < 2:
                    all_numbers[i].remove(j)
                    counter -= 1

        for i in range(0, counter):
            first_num = random.randint(4, 18)
            second_num = random.randint(2, 9)
            while len(all_numbers[first_num]) == 0:
                first_num = random.randint(4, 18)
            else:
                while second_num not in all_numbers[first_num]:
                    second_num = random.randint(2, 9)
                else:
                    all_numbers[first_num].remove(second_num)
                    f.write(str(first_num) + " - " + str(second_num) + " =\n")
    f.close()