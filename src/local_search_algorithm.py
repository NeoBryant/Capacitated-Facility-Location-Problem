import os 
import random

# 全局变量
n = 0 # 设备数量
m = 0 # 客户数量
capacity = [] # 设备容量
open_cost = [] # 开启成本
demand = [] # 客户需求
assignment_cost = [] # 分配成本

# 计算总成本
def getSumCost(customer_of_facility):
    sum_cost = 0 # 总成本
    sum_open_cost = 0 # 设备启动成本
    sum_assignment_cost = 0 # 分配成本
    for i in range(len(customer_of_facility)): # i为设备
        # 开启成本 
        if len(customer_of_facility[i]) > 0:
            sum_open_cost += open_cost[i]
        # 分配成本
        for j in customer_of_facility[i]: # j为客户
            sum_assignment_cost += assignment_cost[j][i]

    sum_cost = sum_open_cost + sum_assignment_cost
    return sum_cost


# 判断解的合法性
def isValid(customer_of_facility):
    for i in range(len(customer_of_facility)): # 对于每个设备被分配的用户
        residual_capacity = capacity[i] # 剩余容量
        for j in customer_of_facility[i]:
            residual_capacity -= demand[j]
        if residual_capacity < 0:
            return False
    
    return True

# 获得随机初始解
def getInit():
    customers = [i for i in range(m)]
    random.shuffle(customers) # 随机生成客户顺序
    facilities = [i for i in range(n)]
    random.shuffle(facilities) # 随机生成设备顺序
    
    customer_of_facility = [[] for i in range(n)] # 每个设备被分配的客户
    residual_capacity = capacity.copy() # 设备剩余容量

    # 分配客户
    for i in customers: # i为客户下标
        for j in facilities:
            if residual_capacity[j] >= demand[i]:
                customer_of_facility[j].append(i)
                residual_capacity[j] -= demand[i]
                break
    
    return customer_of_facility

# 获得邻域的解
def getNeighbor(customer_of_facility):
    # 随机选出两个设备
    facility_1 = random.randint(0, len(customer_of_facility)-1) 
    facility_2 = random.randint(0, len(customer_of_facility)-1) 
    while facility_1 == facility_2: # 两个工厂不同
        facility_2 = random.randint(0, len(customer_of_facility)-1) 

    new_customer_of_facility = customer_of_facility.copy() # 每个设备被分配的客户
    # 获取随机选出的两个工厂的客户
    customers = new_customer_of_facility[facility_1] + new_customer_of_facility[facility_2] 
    new_customer_of_facility[facility_1] = [] # 清空
    new_customer_of_facility[facility_2] = [] # 清空

    # 统计剩余容量
    residual_capacity = capacity.copy() # 设备剩余容量
    for i in range(len(customer_of_facility)):
        for j in customer_of_facility[i]:
            residual_capacity[i] -= demand[j]
    
    # 重新分配
    for i in customers: # 按best fit重新分配
        opt_facilities = sorted(enumerate(assignment_cost[i]), key=lambda x:x[1]) # 该客户的分配成本升序list
        for facility, cost in opt_facilities:
            if residual_capacity[facility] >= demand[i]:
                residual_capacity[facility] -= demand[i] # 更新剩余容量
                new_customer_of_facility[facility].append(i)
                break

    return new_customer_of_facility

# 算法实现
def local_search_algorithm(N, M, CAPACITY, OPEN_COST, DEMAND, ASSIGNMENT_COST):
    '''局部搜索算法
    params
    --------
    设备数(int)，客户数(int)，每个设备的容量(list)，每个设备的开启成本(lsit)，
    每个客户的需求(list)，每个客户对应每个设备的分配成本(list[list])

    returns
    --------
    sum_cost(int): 总成本
    facilities_isopen(list): 设备的开启情况
    customers_of_facility(list[list]): 每个设备被分配的客户下标/编号
    '''
    # 初始化
    global n, m, capacity, open_cost, demand, assignment_cost
    n = N
    m = M
    capacity = CAPACITY.copy()
    open_cost = OPEN_COST.copy()
    demand = DEMAND.copy()
    assignment_cost = ASSIGNMENT_COST.copy()
    
    facility_of_customer = [0 for i in range(M)] # 每个客户被分配的设备
    customer_of_facility = [[] for i in range(N)] # 每个设备被分配的客户
    # residual_capacity = CAPACITY.copy() # 所有设备的剩余容量
    facilities_isopen = [0 for i in range(N)] # 设备是否被开启，1:open, 2: close
    iter_num = 10000 # 迭代次数

    customer_of_facility = getInit() # 获取初始解
    
    for i in range(iter_num): #迭代寻找局部最优解 
        # 复制
        temp = [[customer_of_facility[i][j] for j in range(len(customer_of_facility[i]))] for i in range(N)]
    
        new_customer_of_facility = getNeighbor(temp)
        # 判断是否为更优解
        if isValid(new_customer_of_facility):
            if getSumCost(new_customer_of_facility.copy()) < getSumCost(customer_of_facility.copy()): # 更新更优解
                customer_of_facility = new_customer_of_facility.copy() 

    # 计算分配情况
    for i in range(len(customer_of_facility)):
        for j in customer_of_facility[i]:
            facility_of_customer[j] = i
        if len(customer_of_facility[i]) > 0:
            facilities_isopen[i] = 1

    return getSumCost(customer_of_facility), facilities_isopen, facility_of_customer


