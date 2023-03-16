import threading
import time


def adder():
    i = 0
    while True:
        print(f"In adder, i={i}", flush=True)
        time.sleep(1)
        i = i + 1
        if i == 6:
            break


def logger():
    while True:
        print("In logger", flush=True)
        time.sleep(1.5)


if __name__ == "__main__":
    print("In main", flush=True)


    adder = threading.Thread(
        target=adder,
        args=(),
        name='adder_thread',
        daemon=True)

    logger = threading.Thread(
        target=logger,
        args=(),
        name='logger_thread',
        daemon=True)

    
    threads = [adder, logger]
    for t in threads:
        print(f"starting {t.name}", flush=True)
        t.start()

    while True:
        for t in threads:
            if not t.is_alive():
                print(f"Thread {t.name} has died, exiting ...", flush=True)
                quit()

print("done", flush=True)