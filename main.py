from BI import EyeshieldMgr
import time

if __name__ == '__main__':
    mgr = EyeshieldMgr.EyeShieldMgr()
    mgr.start()
    time.sleep(60*3)
    mgr.stop()