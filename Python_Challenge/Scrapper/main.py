# from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
# from wework import get_wework_jobs
from remote import get_remote_jobs
# from save import save_to_file

# so_jobs = get_so_jobs()
# indeed_jobs = get_indeed_jobs()

jobs = get_remote_jobs("driver")
# jobs = so_jobs + indeed_jobs
# save_to_file(jobs)


