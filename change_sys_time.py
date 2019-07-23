import sys
import datetime
import time
import ctypes

tt = time.gmtime()
today = tt.tm_mday  # save today to recover
time_tuple = (tt.tm_year,  # Year
              tt.tm_mon,  # Month
              13,  # Day
              tt.tm_hour,  # Hour
              tt.tm_min,  # Minute
              tt.tm_sec,  # Second
              0,  # Millisecond
              )


def set_to_expire_time():
    import win32api
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    win32api.SetSystemTime(
        time_tuple[0], time_tuple[1], 0, time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5], 0)


def set_to_current_time():
    import win32api
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    win32api.SetSystemTime(time_tuple[0], time_tuple[1], 0,
                           today, time_tuple[3], time_tuple[4], time_tuple[5], 0)


# set_to_expire_time()

# print("wait ...")
# time.sleep(10)

# set_to_current_time()


def changeTime(func):
    def wrapper(*args, **kwargs):
        try:
            set_to_expire_time()
            func(*args, **kwargs)
            set_to_current_time()
        except:
            print ("something wrong")
        finally:
            set_to_current_time()
    return wrapper


# @changeTime
# def do_some_thing_during_time_change():
#     print("time changed!")
#     time.sleep(3)