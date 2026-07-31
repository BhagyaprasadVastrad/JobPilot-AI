from services.greenhouse import GreenhouseProvider


class SearchAgent:

    def __init__(self):

        self.provider = GreenhouseProvider()

    def start(self):

        jobs = self.provider.search_jobs()

        print()

        print(f"Found {len(jobs)} jobs")

        print()

        for job in jobs:
            print(job)