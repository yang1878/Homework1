#!/usr/bin/python3
year=2021
# Your code should be below this line
if year % 100 != 0:
  if year % 4 == 0:
    print(f"True")
  else:
    print(f"False")
else:
  if year % 400 == 0:
    print(f"True")
  else:
    print(f"False")
