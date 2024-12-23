def pipeline(stages: list[int], details: list[int]) -> list[int]:

    n = len(stages)  
    m = len(details)  
    finish_times = [0] * n
    completion_times = []

    for detail_time in details:
        current_time = detail_time
        for i in range(n):
            current_time = max(current_time, finish_times[i])
            finish_times[i] = current_time + stages[i]
            current_time = finish_times[i]

        completion_times.append(current_time)

    return completion_times

stages = list(map(int, input("stages: ").split()))
details = list(map(int, input("details: ").split()))

result = pipeline(stages, details)
print(f"{result}")
