
print("Enter Time in HHMMSSAM or HHMMSSPM format")
time = input()
h=time[0:2]
m=time[2:4]
s=time[4:6]
f=time[6:8]
a=time[0:6]

if a.isnumeric():
  c="AM"
  d="PM"
  if f==c or f==d:
    pass
    if int(h)<=12 and int(m)<=60 and int(s)<=60:
      pass
      if f==c:
        print(h,':',m,':',s)
      else:
        d=int(h)+12
        print(d,':',m,':',s)
    else:
      print("enter correct values for HHMMSS")
  else:
    print("enter time in AM or PM")
else:
  print("enter numbers in HHMMSS format")