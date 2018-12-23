# coding: utf-8
import os
import pickle

#读取数据文件，并保存到pkl文件中
def init_data():
    pass


# 加载数据
def load_data(num): 
    # 读取的文件名
    dir_name = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/data"
    file_name = dir_name + "/p" + str(num)

    # 数据变量
    n = 0
    m = 0
    capacity = [] # 设备容量
    open_cost = [] # 设备成本
    demand = [] # 用户需求
    assignment_cost = [] # 分配成本

    with open(file_name, 'r') as f:
        # 读取（n、m）
        data = f.readline().strip().split() # 取出两头空字符，再以空格切分为数组
        n = int(data[0]) # n个设备
        m = int(data[1]) # m个客户

        # 读取n个（容量、开启成本）
        for i in range(n):
            data = f.readline().strip().split()
            capacity.append(int(data[0]))
            open_cost.append(int(data[-1]))

        # 读取m个客户需求
        if num != 67:
            for i in range(int(m/10)):
                data = f.readline().strip().replace('.','').split() 
                for j in range(10): # 每行10个数据
                    demand.append(int(data[j]))
        else:
            for i in range(int(m/10)):
                data = f.readline().strip().replace('.','').split() 
                for j in range(6): # 每行6个数据
                    demand.append(int(data[j]))
                data = f.readline().strip().replace('.','').split() 
                for j in range(4): # 每行6个数据
                    demand.append(int(data[j]))
        
        # 读取n*m个分配成本
        data_list = []
        if num != 67:
            for i in range(int(n*m/10)):
                data = f.readline().strip().replace('.','').split()
                data_list_int = [int(data[j]) for j in range(10)]
                data_list += data_list_int
        else:
            for i in range(int(n*m/10)):
                data = f.readline().strip().replace('.','').split()
                data_list_int = [int(data[j]) for j in range(6)]
                data_list += data_list_int
                data = f.readline().strip().replace('.','').split()
                data_list_int = [int(data[j]) for j in range(4)]
                data_list += data_list_int

        for i in range(n): # 转化为二维数组 [n][m]
            assignment_cost.append(data_list[i*m:(i+1)*m])
        # 将每个设备对应的客户的分配成本变为每个客户对应的设备的分配成本
        temp_assignment_cost = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(assignment_cost[j][i])
            temp_assignment_cost.append(temp)

        f.close() # 关闭文件

    return n, m, capacity, open_cost, demand, temp_assignment_cost

if __name__ == "__main__":
    init_data()
    #load_data(2)
    '''for i in range(1, 72):
        print("----------------p"+str(i))
        n, m, capacity, open_cost, demand, assignment_cost = load_data(i)
        print("n:", n)
        print("m:", m)
        print("capacity:", capacity)
        print("open_cost:", open_cost)
        print("demand:", demand)
        print("assignment_cost:", assignment_cost)
    '''

    '''n, m, capacity, open_cost, demand, assignment_cost = load_data(22)
    print("n:", n)
    print("m:", m)
    print("capacity:", capacity)
    print("open_cost:", open_cost)
    print("demand:", demand)
    print("assignment_cost:", assignment_cost)'''
    