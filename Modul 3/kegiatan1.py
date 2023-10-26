def konversi(week=0):
    def day(day=0):
        def hour(hour=0):
            return (week * 7 * 24 * 60) + (day * 24 * 60) + (hour * 60)
        return hour
    return day


Data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

outputData = []

for data in Data:
    data_split = data.split()
    
    week = int(data_split[0])
    day = int(data_split[2])
    hour = int(data_split[4])
    minute = int(data_split[6])
    
    konvert = konversi(week)(day)(hour) + minute
    outputData.append(konvert)
    
print("Output Data = ",outputData)
