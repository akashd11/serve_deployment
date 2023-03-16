import time


class MyRun:

    def __int__(self):
        pass

    def run(self):
        start = time.time()
        time.sleep(2)
        print("Ran for {}".format(time.time() - start))
        return {"OK"}
