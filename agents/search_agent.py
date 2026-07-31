from services.job_collector import JobCollector


class SearchAgent:

    def __init__(self):
        self.collector = JobCollector()

    def start(self):

        jobs = self.collector.collect_jobs()

        print("\n==============================")
        print(f"Found {len(jobs)} jobs")
        print("==============================\n")

        for job in jobs:
            print(job)