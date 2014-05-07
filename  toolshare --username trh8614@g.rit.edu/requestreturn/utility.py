# Light utility file
# Thomas Heissenberger

def todatetime(time):
    return datetime.datetime.today().replace(hour=time.hour, minute=time.minute, second=time.second, 
                                             microsecond=time.microsecond, tzinfo=time.tzinfo)

def timestodelta(starttime, endtime):
    return todatetime(endtime) - todatetime(starttime)