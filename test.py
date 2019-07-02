subject1 = float(input("请输入第一科分数:"))
subject2 = float(input("请输入第二科分数:"))
subject3 = float(input("请输入第三科分数:"))
score = []
dic={9.0:'优秀',8.0:'良好'}
score.append(subject1)
score.append(subject2)
score.append(subject3)
score.sort()
if score[1]//10 in dic:
    print(dic[score[1]//10])
else:
    print("差")