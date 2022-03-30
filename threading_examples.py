import threading
import time

def func(wait):
	print("ran")
	time.sleep(wait)
	print("done")

x = threading.Thread(target=func, args=(2,))

x.start()
print(threading.active_count())