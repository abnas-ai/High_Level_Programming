


year = int(input("Print leap years from: "))
for year in range(2000, 2025 + 1):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # print(year, end=" ")

            print(f"{year} is a leap year")
  else:
            print(f"{year} is not a leap year")




    
# def print_leap_years(start, end):
#     for year in range(2000, 2025 + 1):
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             print(year, end=" ")

# # Example: Print leap years from 2000 to 2050
# print_leap_years(2000, 2025)
