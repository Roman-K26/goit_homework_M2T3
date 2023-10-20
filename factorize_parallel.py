import time
from multiprocessing import Pool, cpu_count

def factorize_single(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_single, numbers)
    
    return results

if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)  # Кортеж чисел

    start_time = time.time()
    a, b, c, d = factorize_parallel(*numbers)  # Розпакування кортежу
    end_time = time.time()

    print("Паралельна версія виконана за {} секунд.".format(end_time - start_time))
    print(a)
    print(b)
    print(c)
    print(d)

