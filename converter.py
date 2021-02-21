import datetime
def deltaTime(endTime):
    timeNow = datetime.datetime.now()

    curHour = int(timeNow.strftime('%H'))
    curMinutes = int(timeNow.strftime('%M'))
    curTimeInMin = curHour * 60 + curMinutes

    endHour = int(endTime) // 100
    endMinute = int(endTime) % 100
    endTimeInMin = endHour * 60 + endMinute

    deltaTimeInMin = endTimeInMin - curTimeInMin
    return deltaTimeInMin