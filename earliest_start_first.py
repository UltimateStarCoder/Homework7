def earliest_start_first(jobs_hours):
    # Sort jobs by their start time
    jobs_hours.sort(key=lambda x: x[0])
    
    # Initialize the list with the first job
    job_for_day = []
    job_for_day.append(jobs_hours[0])
                
    # Iterate through the jobs and select the ones that can be scheduled
    for i in range(1, len(jobs_hours)):
        # If the current job starts after or when the last selected job ends, add it to the list
        if job_for_day[-1][1] <= jobs_hours[i][0]:
            job_for_day.append(jobs_hours[i])
    
    return job_for_day

jobs_hours = [(2, 3), (1, 2), (5, 8), (3, 4),(3, 5)]
print(earliest_start_first(jobs_hours))
