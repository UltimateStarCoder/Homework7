from tabulate import tabulate

def shortest_duration_first(jobs):
    jobs_hours_and_duration = []
    for job in jobs:
        jobs_hours_and_duration.append((job[0], job[1], job[1] - job[0]))  # Calculate duration and store it
    jobs_hours_and_duration.sort(key=lambda x: x[2])  # Sort jobs by duration

    result = []
    result.append(jobs_hours_and_duration[0])  # Add the first job to the result
    for i in range(1, len(jobs_hours_and_duration)):
        if result[-1][1] <= jobs_hours_and_duration[i][0]:  # Check if the job can be scheduled
            result.append(jobs_hours_and_duration[i])
    return result

if __name__ == "__main__":
    jobs_hours = [(2, 3), (1, 2), (5, 8), (3, 4), (3, 5)]
    answer = shortest_duration_first(jobs_hours)
    answer1 = [(answer[i][0], answer[i][1]) for i in range(len(answer))]  # Extract start and end times
    
    print(answer1)
    print(tabulate(shortest_duration_first(jobs_hours)))  # Print the result in a tabulated format
