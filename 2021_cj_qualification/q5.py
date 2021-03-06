import random
MAGIC_NUMBER = 15
PERCENTAGE_THRESHOLD = 8
SMALLEST_PTS = 30

def fcn(students):
    num_questions = len(students[0])
    questions_correct = [sum([int(row[i]) for row in students]) for i in range(num_questions)]
    # print('Questions', questions_correct)
    slopes = []
    for j,s in enumerate(students):
        # print('\nStudent number: ', j, end=' ')
        total = [0 for _ in range(100)]
        correct = [0 for _ in range(100)]
        total_correct = 0
        for i, q in enumerate(s):
            if int(q) == 1:
                total[questions_correct[i]-1] += 1
                correct[questions_correct[i]-1] += 1
                total_correct += 1
            else:
                total[questions_correct[i]] += 1
        samples = []
        a = 0
        c_a = 0
        while c_a < SMALLEST_PTS:
            if total[a] < PERCENTAGE_THRESHOLD:
                a += 1
                continue
            b = a + 1
            c_b = b
            while c_b < a+SMALLEST_PTS and b < 99:
                if total[b] < PERCENTAGE_THRESHOLD:
                    b += 1
                    continue
                percentage_a = correct[a]/total[a]*100
                percentage_b = correct[b]/total[b]*100
                samples.append((percentage_a-percentage_b) / (a-b))
                b += 1
                c_b += 1
            a += 1
            c_a += 1
        over_fifty = 0
        total_count = 0
        for i,(c,t) in enumerate(zip(correct, total)):
            if t > MAGIC_NUMBER:
                total_count += 1
                p = c/t*100
                if p >= 50:
                    over_fifty += 1
                # print(int(c/t*1000)/10, end=' ')
        slope = sum(samples) / len(samples)
        if over_fifty / total_count > 0.75:
            slopes.append((slope, total_correct, over_fifty/total_count, j))
    slopes.sort()
    # print(slopes)
    # for slope, total_correct, percent, index in slopes:
    #     if percent > 0.985 and slope < 0.6:
    #         return index + 1
    # for slope, total_correct, percent, index in slopes:
    #     if percent > 0.975:
    #         return index + 1
    return slopes[0][3] + 1

t = int(input())
p = int(input())
for i in range(1, t + 1):
    students = []
    for j in range(100):
        students.append(list(input()))
    print("Case #{}: {}".format(i, fcn(students)))
