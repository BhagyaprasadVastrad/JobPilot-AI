from services.job_provider import JobProvider
from models.job import Job


class GreenhouseProvider(JobProvider):

    def search_jobs(self):

        print("Searching Greenhouse...")

        jobs = [

            Job(
                title="Data Analyst",
                company="Example Company",
                location="Remote",
                apply_url="https://boards.greenhouse.io"
            ),

            Job(
                title="Power BI Developer",
                company="ABC Ltd",
                location="London",
                apply_url="https://boards.greenhouse.io"
            )

        ]

        return jobs