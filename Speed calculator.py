distance=float(input("Enter the distance in meters: "))
#prompt the user for time in hours, minutes and seconds 
hours=int(input("Enter the time taken (hours):"))
minutes=int(input("enter the time taken (minutes):"))
second=int(input("Enter the time taken (seconds):"))
#calculate total time in second
total_seconds =(hours *3600)+(minutes*60)+ (second)
#calculate speed in meters per second
speed_mps =distance /total_seconds
#calculate speed in kilometers per hour
speed_kph=(distance/1000)/(total_seconds/3600)
#calculate speed in miles per hour
speed_mph=(distance /1609.34)/(total_seconds/3600)
#Display the speed
print("speed: ")
print("meters per second:",speed_mps)
print("kilometers per hour:",speed_kph)
print("miles per hour :",speed_mph)