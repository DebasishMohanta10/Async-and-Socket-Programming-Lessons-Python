import time

def calculate_sum_of_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i**2
    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    start_time = time.time()
    for i in range(5):
        calculate_sum_of_squares(i)
    
    for i in range(6):
        sleep_a_little(i)

    end_time = time.time()

    print(end_time - start_time)

if __name__ == "__main__":
    main()

