seconds = int(input("Enter amount of seconds to convert: "))

hours = (seconds // 3600) #Get quotitient
minutes = (seconds % 3600)// 60 #Get the remainder after ours and get it's quotitient
seconds = (seconds % 3600) % 60 #Get the reminder after minutes
print("Time is in hours: " + str(hours) + ", minutes: " + str(minutes) + ", seconds: " + str(seconds))