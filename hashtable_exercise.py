# with open("nyc_weather.csv") as file:
#     file.readline()
#     items = file.readlines()
# 
# dates = []
# temperatures = []
# data = {}
# for item in items:
#     date, temperature = item.strip().split(',')
#     data[date] = int(temperature) 
#     dates.append(date)
#     temperatures.append(int(temperature))
# 
# print("Average temperature first week of January:", round(sum(temperatures[:7])/7, 1))
# print("Maximum temperature in the first ten days of January:", round(max(temperatures[:10]), 1))
# print("The temperature on Jan 9:", data["Jan 9"])
# print("The temperature on Jan 4:", data["Jan 4"])
# 
# with open("poem.txt") as file:
#     text = file.read()
# 
# for x in ['\n', ',', '.']:
#     text = text.replace(x, ' ')
# text = text.strip().split(' ')
# 
# vocabulary = {word: 0 for word in text}
# 
# for word in text:
#     vocabulary[word] += 1

