import sys
import time

import chilkat

import change_sys_time
import run_as_admin

@change_sys_time.changeTime
def save(URL, title):
    mht = chilkat.CkMht()

    success = mht.UnlockComponent("Anything for 30-day trial")
    # print("success? {}".format(success))
    if (success != True):
        print(mht.lastErrorText())
        sys.exit()

    success = mht.GetAndSaveMHT(url, title)
    if (success != True):
        print(mht.lastErrorText())
        sys.exit()
    else:
        print("MHT Created!")


url = "http://www.bing.com"
title = "bing.mht"

if not run_as_admin.isUserAdmin():
    run_as_admin.runAsAdmin()
else:
    save(url, title)