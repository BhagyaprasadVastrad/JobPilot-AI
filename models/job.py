from dataclasses import dataclass


@dataclass
class Job:
    title: str
    company: str
    location: str
    apply_url: str

    def __str__(self):
        return f"{self.title} | {self.company} | {self.location}"