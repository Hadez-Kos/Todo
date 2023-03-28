import os

if __name__ == '__main__':
    try:
        os.system("python manage.py runserver")
    except KeyboardInterrupt as k:
        print("Stopped program")
