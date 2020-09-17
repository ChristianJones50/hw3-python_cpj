# Author: Christian Jones cpj5199@psu.edu

def digit_sum(n):
  if n > 0:
    digit = int(n % 10) # Stores the Last Digit
    n = n // 10
    return digit + digit_sum(n)
  else:
    return 0

def run():
  intMain = int(input("Enter an int: "))
  print(f"sum of digits of {intMain} is {digit_sum(intMain)}.")

if __name__ == "__main__":
  run()
