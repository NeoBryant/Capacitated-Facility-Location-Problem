# coding: utf-8
import os 

# 算法实现
def greedy_algorithm2(N, M, CAPACITY, OPEN_COST, DEMAND, ASSIGNMENT_COST):
    '''贪心策略2
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
    assignment_cost_of_facility = [0 for i in range(N)] # 每个设备的被分配的开销
    facility_of_customer = [0 for i in range(M)] # 每个设备被分配的客户
    residual_capacity = CAPACITY.copy() # 所有设备的剩余容量
    facilities_isopen = [0 for i in range(N)] # 设备是否被开启，1:open, 2: close

    # 遍历所有用户
    for customer in range(M):
        # 可选择的设备下标列表，已经排序好，从低到高[(i,v),...]
        opt_facilities = sorted(enumerate(ASSIGNMENT_COST[customer]), key=lambda x:x[1])
        open_facility = None 
        close_facility = None
        final_facility = None
        for facility, cost in opt_facilities: # 得到最小分配成本的，已开启的和未开启的设备
            if open_facility != None and close_facility != None: 
                break
            if residual_capacity[facility] >= DEMAND[customer]:
                if facilities_isopen[facility] == 1:
                    if open_facility == None: 
                        open_facility = facility
                else: 
                    if close_facility == None:
                        close_facility = facility
        
        # 若只有已开启的
        if open_facility != None and close_facility == None:
            final_facility = open_facility
        # 若只有未开启的
        elif open_facility == None and close_facility != None:
            final_facility = close_facility
            facilities_isopen[final_facility] = 1  # 更新
        # 若两种都存在，则选择总成本最低的一种     
        else:       
            if OPEN_COST[close_facility]+ASSIGNMENT_COST[customer][close_facility] >= ASSIGNMENT_COST[customer][open_facility]:
                final_facility = open_facility
            else:
                final_facility = close_facility
                facilities_isopen[final_facility] = 1  # 更新
        
        # 更新
        assignment_cost_of_facility[final_facility] += ASSIGNMENT_COST[customer][final_facility] # 设备分配成本
        residual_capacity[final_facility] -= DEMAND[customer] # 更新设备剩余容量
        facility_of_customer[customer] = final_facility

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