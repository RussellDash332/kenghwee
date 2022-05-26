import time, random
from clrprint import *

clrprint('Logging IP address and user account information...', clr='r')
time.sleep(1)
for _ in range(3):
    time.sleep(0.7)
    print('.')
clrprint('Log completed.', clr='g')
time.sleep(1)
clrprint('Submitting plagiarism report to admins...', clr='r')
time.sleep(0.5)
for _ in range(3):
    time.sleep(1)
    print('.')
clrprint('Report submitted successfully.', clr='g')
clrprint('This incident has been reported to the teaching staff.', clr='g')
if random.random() < 0.2:
    print()
    clrprint('Have a nice day :)', clr='y')