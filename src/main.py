# coding: utf-8
import os
import time
from load_data import load_data
from greedy_algorithm import greedy_algorithm
from greedy_algorithm2 import greedy_algorithm2
from local_search_algorithm import local_search_algorithm

if __name__ == "__main__":
    for i in range(1,72): # 贪心策略
        # print("\n对于数据集p" + str(i))
        # 计算
        n, m, capacity, open_cost, demand, assignment_cost = load_data(i)
        start_time = time.time() # 计算起始时间
        sum_cost, facilities_isopen, facility_of_customer = local_search_algorithm(n, m, capacity, open_cost, demand, assignment_cost)
        end_time = time.time() # 计算结束时间

        # 结果表
        #print('| p'+str(i),'|', sum_cost, '|', round(end_time-start_time, 6), '|')
        # 打印细节
        '''print("总成本(Result):", sum_cost)
        print("设备状态:", ' '.join([str(j) for j in facilities_isopen]))
        print("计算时间(s):", round(end_time-start_time, 6))
        print("设备对应的客户分配情况:", ' '.join([str(j) for j in facility_of_customer]))'''
        print("------------------p"+str(i))
        print(sum_cost)
        print(' '.join([str(j) for j in facilities_isopen]))
        print(' '.join([str(j) for j in facility_of_customer]))

        
    #print("71个数据样本总计算时间为:", round(end_time - start_time, 2), "s")
    
    # 计算
    '''n, m, capacity, open_cost, demand, assignment_cost = load_data(1)
    start_time = time.time() # 计算起始时间
    sum_cost, facilities_isopen, facility_of_customer = local_search_algorithm(n, m, capacity, open_cost, demand, assignment_cost)
    end_time = time.time() # 计算结束时间

    # 打印结果
    print("总成本(Result):", sum_cost)
    print("设备状态:", ' '.join([str(j) for j in facilities_isopen]))
    print("计算时间(s):", round(end_time-start_time, 6))
    print("设备对应的客户分配情况:", ' '.join([str(j) for j in facility_of_customer]))
    '''

    '''
    print()
    Sum = 0
    for i in range(len(facility_of_customer)): # i：顾客，facility_of_customer[i：设备，
        print(facility_of_customer[i], ":", i, "-->", assignment_cost[i][facility_of_customer[i]]) # 设备: 顾客
        Sum += assignment_cost[i][facility_of_customer[i]]
    Sum += sum(open_cost)
    print("sum=", Sum)'''