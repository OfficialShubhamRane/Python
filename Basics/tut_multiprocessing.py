from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    process_a = Process(target=counter, args=(50000000,))
    process_b = Process(target=counter, args=(50000000,))

    process_a.start()
    process_b.start()

    process_a.join()
    process_b.join()

    print("finished in: ",  time.perf_counter(),  "seconds")

if __name__ == '__main__':
    main()