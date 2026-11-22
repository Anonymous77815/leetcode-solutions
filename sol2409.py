class Solution(object):
    def countDaysTogether(self,arriveAlice, leaveAlice, arriveBob, leaveBob):

        days_in_month_numbers = {
        1: 31,  # January
        2: 28,  # February (29 in a leap year)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31,  # December
    }

        def convertToDays(date):

            month,day = map(int, date.split("-"))
            totalDays = day

            for i in range(1,month):
                totalDays += days_in_month_numbers[i]

            return totalDays


        alliceA = convertToDays(arriveAlice)
        alliceR = convertToDays(leaveAlice)
        bobA = convertToDays(arriveBob)
        bobR = convertToDays(leaveBob)

        max1 = max(alliceA,bobA)
        min1 = min(alliceR, bobR)

        if min1 < max1:
            return 0 

        return min1-max1+1