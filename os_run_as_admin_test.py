import os
import time

import run_as_admin

if not run_as_admin.isUserAdmin():
    run_as_admin.runAsAdmin()
else:
    os.system("changeSYStime.py")
    time.sleep(3)