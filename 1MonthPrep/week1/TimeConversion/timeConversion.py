def timeConversion(s):
  hours = s[:s.index(":")]
  print(f'hours: {hours}')
  if "PM" in s:
    s = s.rstrip("PM")
    hours = str(int(hours) + 12)
    if hours == "24":
        hours = "12"
    s = hours + s[s.index(":"):]
  else:
    s = s.rstrip("AM")
    if hours == "12":
        hours = "00"
    # hours = int(s[:s.index(":")])
    s = hours + s[s.index(":"):]
    
  return s
    
  
time = "12:05:45PM"
print(timeConversion(time))