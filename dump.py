import threading
import playsound


def my_threaded_func():
    print("Now playing: Ai no Sukima-Rock Cover.mp3...")
    playsound.playsound('Ai no Sukima-Rock Cover.mp3')
    print("Done")


for i in range(10):
    thread = threading.Thread(target=my_threaded_func)
    thread.start()
    thread.join()
h = input()
print(h, " mundo")
