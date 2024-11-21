def earliest_finish_first(jobs_hours):
    # Sort jobs by their finish times
    jobs_hours.sort(key=lambda x: x[1])
    print(jobs_hours)  # Print sorted jobs for debugging
    job_for_day = []
    job_for_day.append(jobs_hours[0])  # Add the first job to the schedule
                
    for i in range(1, len(jobs_hours)):
        # If the current job starts after or when the last job in the schedule finishes
        if job_for_day[-1][1] <= jobs_hours[i][0]:
            job_for_day.append(jobs_hours[i])  # Add the current job to the schedule

    return job_for_day  # Return the list of scheduled jobs

# List of jobs with their start and finish times
jobs_hours = [(2, 4), (2, 3), (1, 4), (5, 8), (3, 4), (3, 5)]
print(jobs_hours)  # Print the original list of jobs
print(earliest_finish_first(jobs_hours))  # Print the scheduled jobs
