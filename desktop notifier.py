from plyer import notification
import time
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Taking rest is crutial for human beings because it allows our bodies and minds to recharge and rejuvenate.",
            # icon = "rest.png",
            timeout = 10
        )
        time.sleep(1360)
    
