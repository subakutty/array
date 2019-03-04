import datetime
def currentTime():
  print()
  today = datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-%Hh/%Mm')
  print(today)
