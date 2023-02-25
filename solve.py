from pulp import *

def ini():
    f = open('data.txt')
    line = f.readline().strip()  # 读取第一行
    txt = []
    txt.append(line)
    while line:  # 直到读取完文件
        line = f.readline().strip()  # 读取一行文件，包括换行符
        txt.append(line)
    f.close()# 关闭文件
    txt.pop()
    #print(txt)
    return txt
def s():
    # 定义问题
    prob = LpProblem("MyProblem", LpMaximize)
    # 定义变量
    x = [LpVariable("x{}".format(wh), cat=LpBinary) for wh in range(n)]
    # 定义目标函数
    for t in range(arr_two[0]):
        prob += x[t] * arr_two[t]
    # 定义约束条件
    prob += x[0] + x[1] <= 1
    prob += x[2] + x[3] + x[4] <= 2
    prob += x[5] + x[6] + x[7] + x[8] + x[9] <= 3

    # 求解问题
    prob.solve()

    # 输出结果
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Objective =", value(prob.objective))
def create_model(c, A, b):
    prob = LpProblem('01 Integer Programming', LpMaximize)
    n = len(c)
    x = [LpVariable('x%d' % i, lowBound=0, upBound=1, cat=LpInteger) for i in range(n)]
    prob += lpDot(c, x)
    for i in range(len(A)):
        prob += lpDot(A[i], x) <= b[i]
    return prob


if __name__ == '__main__':
    arr = ini()
    i = 0
    while i < len(arr):
        n = int(arr[i])
        i += 1
        arr_two = []
        B = []
        for k in range(n+1):
            zhong = []
            for ind , j in enumerate(arr[i].split()):
                if (k != 0) and (ind == len(arr[i].split()) - 1):
                    B.append(int(j))
                    break
                zhong.append(int(j))
            arr_two.append(zhong)
            i += 1
        C = arr_two.pop(0)
        ####求解
        print(arr_two)
        print(B)
        print(C)

        # 创建0-1整数规划模型，并求解
        prob = create_model(C, arr_two, B)
        status = prob.solve()
        if status != 1:
            print('Infeasible or unbounded problem')
            continue

        # 打印解
        print('Optimal value:', value(prob.objective))
        for v in prob.variables():
            print(v.name, '=', v.varValue)