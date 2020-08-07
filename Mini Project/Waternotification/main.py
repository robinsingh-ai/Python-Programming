import time
from plyer import notification

if __name__ == "__main__":
        while True:
            notification.notify(

                title = "Please Drink 1 Glass Of Water ",
                message = " To lead a healthy life we should drink 3-4 Litres of  water everyday to make our body fit",
                app_icon= r"C:\Users\Robin Singh\PycharmProjects\untitled\venv\Sorting\Projects\Waternotification\icon.ico",
                timeout = 10

            )

            time.sleep(60*60*2)

    