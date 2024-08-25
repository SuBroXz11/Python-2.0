# average_heights= [180, 124, 165, 173, 189, 169, 146]
# avg=sum(average_heights)/len(average_heights)
# print(avg)


average_heights = [180, 124, 165, 173, 189, 169, 146]

total_sum = 0
for height in average_heights:
    total_sum += height
avg = total_sum / len(average_heights)
print(round(avg))
