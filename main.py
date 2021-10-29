import threading
import fishing_actions as fish
import setup


def main():
    configs = setup.Setup()
    t1 = threading.Thread(target=fish.fishing_loop, args=[configs])
    t1.start()
    t2 = threading.Thread(target=fish.stop)
    t2.start()

if __name__ == "__main__":
    main()
