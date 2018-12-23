# coding: utf-8
import os 

# 算法实现
def greedy_algorithm(N, M, CAPACITY, OPEN_COST, DEMAND, ASSIGNMENT_COST):
    '''贪心策略2
    params
    --------
    设备数(int)，客户数(int)，每个设备的容量(list)，每个设备的开启成本(lsit)，
    每个客户的需求(list)，每个客户对应每个设备的分配成本(list[list])

    returns
    --------
    sum_cost(int): 总成本
    facilities_isopen(list): 设备的开启情况
    facility_of_customer(list): 每个客户对应的设备
    '''
    # 初始化
    assignment_cost_of_facility = [0 for i in range(N)] # 每个设备的被分配的开销
    facility_of_customer = [0 for i in range(M)] # 每个设备被分配的客户
    residual_capacity = CAPACITY.copy() # 所有设备的剩余容量
    facilities_isopen = [0 for i in range(N)] # 设备是否被开启，1:open, 2: close

    # 遍历所有用户
    for customer in range(M):
        # 获取可选择的最低分配成本的设备

        # 可选择的设备下标列表，已经排序好，从低到高[(i,v),...]
        opt_facilities = sorted(enumerate(ASSIGNMENT_COST[customer]), key=lambda x:x[1])
        for facility, cost in opt_facilities: # 设备下标，设备分配成本
            if residual_capacity[facility] >= DEMAND[customer]: # 若设备剩余容量够，则匹配
                assignment_cost_of_facility[facility] += cost # 记录设备被分配的客户的分配成本
                residual_capacity[facility] -= DEMAND[customer] # 更新设备剩余容量
                #facility_of_customer[facility].append(customer) # 更新每个设备被分配的客户
                facility_of_customer[customer] = facility
                if facilities_isopen[facility] == 0: 
                    facilities_isopen[facility] = 1 
                break
            else:
                pass

    # 统计总成本
    sum_cost = 0
    for facility in range(N):
        # 开启成本 
        sum_open_cost = facilities_isopen[facility] * OPEN_COST[facility]
        # 分配成本
        sum_assignment_cost = assignment_cost_of_facility[facility]
        # 总成本
        sum_cost += sum_open_cost + sum_assignment_cost
        
    return sum_cost, facilities_isopen, facility_of_customer