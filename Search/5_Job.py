def find_min_time(jobs, k):
    jobs.sort(reverse=True)
    n = len(jobs)

    left, right = max(jobs), sum(jobs)

    def can_assign_jobs(mid):
        workloads = [0] * k
        stack = [(0, workloads)]

        while stack:
            idx, workloads = stack.pop()

            if idx == n:
                return True  

            curr_job = jobs[idx]
            seen = set()

            for i in range(k):
                if workloads[i] + curr_job <= mid:
                    if workloads[i] in seen:
                        continue
                    seen.add(workloads[i])


                    new_workloads = workloads.copy()
                    new_workloads[i] += curr_job

                    stack.append((idx + 1, new_workloads))


                    if workloads[i] == 0:
                        break
        return False


    while left < right:
        mid = (left + right) // 2
        if can_assign_jobs(mid):
            right = mid
        else:
            left = mid + 1

    return left

input_data = input("Enter jobs and number of workers : ")
jobs_str, k_str = input_data.strip().split('/')
jobs = list(map(int, jobs_str.strip().split()))
k = int(k_str.strip())

min_time = find_min_time(jobs, k)
print(f"Minimum time to complete jobs with {k} workers is {min_time}")
