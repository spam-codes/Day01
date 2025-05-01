days = 5
day=1
total_temp = 0
avg_temp =0
while(days):
    temperature = int(input(f"Temperature On Day {day} :"))
    total_temp += temperature 
    day +=1
    days -= 1

avg_temp = total_temp/5
print(f"\nThe Averag Temperature Of The Five Day Is : {avg_temp}")    
    
    