from tabulate import tabulate

def shortest_duration_first(jobs_hours):
    # Calculate the duration of each job and store it along with the start and end times and index
    jobs = [(job[0], job[1], job[1] - job[0], i) for i, job in enumerate(jobs_hours)]
    
    # Sort jobs by duration
    jobs.sort(key=lambda x: x[2])
    
    # Initialize the result list
    result = []
    
    # Iterate through the sorted jobs and select non-overlapping jobs
    for job in jobs:
        if not result or all(job[0] >= selected_job[1] or job[1] <= selected_job[0] for selected_job in result):
            result.append(job)
    
    # Extract the start and end times of the selected jobs
    selected_jobs = [(job[0], job[1]) for job in result]
    
    return selected_jobs

if __name__ == "__main__":
    jobs_hours = [(1, 4), (4, 8), (3, 5), (9, 10)]
    
    selected_jobs = shortest_duration_first(jobs_hours)
    selected_jobs.sort(key=lambda x: x[0])
    print("Selected jobs (start time, end time):", selected_jobs)