from services.greenhouse import GreenhouseProvider


class JobCollector:

    def __init__(self):
        self.providers = [
            GreenhouseProvider()
        ]

    def collect_jobs(self):

        all_jobs = []

        for provider in self.providers:

            print(f"\nUsing {provider.__class__.__name__}")

            jobs = provider.search_jobs()

            all_jobs.extend(jobs)

        return all_jobs