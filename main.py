import threading

def run1():
    exec(open("window1.py").read())

def run2():
    exec(open("window2.py").read())

t1 = threading.Thread(target=run1)
t2 = threading.Thread(target=run2)

t1.start()
t2.start()

t1.join()
t2.join()