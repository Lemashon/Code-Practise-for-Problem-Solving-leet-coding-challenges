'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''
def dayOfTheWeek(day, month, year):
  # If the month is January or February, consider it to be the 13th or 14th month of the previous year
  if month == 1:
    month = 13
    year -= 1
  elif month == 2:
    month = 14
    year -= 1
  
  # Calculate the day of the week using the Zeller's Congruence formula
  k = day
  m = month
  C = year // 100
  Y = year % 100
  W = (k + (13 * (m + 1)) // 5 + Y + (Y // 4) + (C // 4) - 2 * C) % 7
  
  # Return the corresponding day of the week as a string
  if W == 0:
    return "Sunday"
  elif W == 1:
    return "Monday"
  elif W == 2:
    return "Tuesday"
  elif W == 3:
    return "Wednesday"
  elif W == 4:
    return "Thursday"
  elif W == 5:
    return "Friday"
  elif W == 6:
    return "Saturday"

def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        day_of_week_map = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
        year -= month < 3
        return day_of_week_map[((year  + int(year / 4) - int(year / 100) + int(year / 400) + t[month - 1] + day) % 7)]
