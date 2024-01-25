
def lower_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low < high:
        mid = int((low+high)/2)
        if nums[mid] < target:
            low = mid+1
        else:  # >=
            high = mid
            #pos = high
    if nums[low] >= target:
        pos = low
    return pos



def upper_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low < high:
        mid = int((low+high)/2)
        if nums[mid] <= target:
            low = mid+1
        else:  # >
            high = mid
            pos = high
    if nums[low] > target:
        pos = low
    return pos


cnt = 0
st = [1, 55550]
ed = [55549]
weight = [0.0, 0.0]


with open("E://LAB-209//YY1//bioinformatics//genetic_map_chr1_combined_b37//genetic_map_chr1_combined_b37.txt") as file_in:
    for line in file_in:
        cnt += 1
        if cnt < 3: 
            continue
        
        line = line[0:-1] 
        data = line.split(" ") 

        ed.append(int(data[0]) - 1) 
        st.append(int(data[0])) 
        weight.append(float(data[1])) 

  
ed.append(249243664)  #edit depending on the last peak end positon
cnt = 0
ans_list = []
with open("E://LAB-209//YY1//PAPER//bioinformatics-HR//data-set//recombination rate vs peak distance +-5000//YY1//chr1.txt") as file_query:
    for line in file_query:
        data = line.split("\t") 
        # print(data)
        cnt += 1
        part = data[0]
        if int(part[3:]) != 1: 
            break
        for u in range(5000,-5001,-1):
            x = (int(data[1])+int(data[2]))/2-u 
            
            l = lower_bound(ed, x)
      

            
            ans = weight[l]
            ans_list.append(ans)
            ans_list.append('\t')
        ans_list.append('\n')

    print(ans_list)

ans_len = len(ans_list) 
f = open("ans.txt", "w")
for i in range(0, ans_len):
    f.write(str(ans_list[i]))
    
f.close()
