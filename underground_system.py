datas = [[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],
         [2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
operations = ["checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]

customer_info = {}
avg_time = {}

for data, op in zip(datas, operations):
    #print(avg_time)
    #print(data, op)

    if op == "checkIn":
        customer_info[data[0]] = [data[1], data[2]]  # add the customer_info 
        if data[0] in avg_time.keys():
            avg_time[data[1]] = []     # add a key as in avg_time we hold the start-station as a key
    if op == "checkOut":
        start_station = customer_info[data[0]][0]
        end_station = data[1]
        start_time = customer_info[data[0]][1]
        end_time = data[2]
        # adding the time taken by this customer to avg-time
        avg_time[start_station].append([end_station, end_time - start_time])
        del customer_info[data[0]]

    if op == "getAverageTime":
        start_station = data[0]
        end_station = data[1]
        count = 0
        sum_time = 0
        
        for values in avg_time[start_station]:
            if values[0] == end_station:
                sum_time +=values[1]
                count +=1
        print(start_station, end_station, sum_time/count, sep='||')
        



