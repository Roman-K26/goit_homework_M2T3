import time

def factorize(*numbers):
    results = []

    for num in numbers:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        results.append(divisors)

    return results


# Приклад використання:
numbers = [128, 255, 99999, 10651060]
start_time = time.time()
results = factorize(*numbers)
end_time = time.time()

print("Синхронна версія виконана за {} секунд.".format(end_time - start_time))
print(results)

