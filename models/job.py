from dataclasses import dataclass
from typing import Optional


@dataclass
class Job:
    title: str
    company: str
    location: str
    apply_url: str

    source: str = ""

    country: str = ""
    salary: str = ""
    experience: str = ""

    visa_sponsorship: Optional[bool] = None
    relocation: Optional[bool] = None

    recruiter_name: str = ""
    recruiter_email: str = ""
    recruiter_phone: str = ""

    posted_date: str = ""

    match_score: float = 0.0
    opportunity_score: float = 0.0

    def __str__(self):
        sponsor = (
            "Yes" if self.visa_sponsorship is True
            else "No" if self.visa_sponsorship is False
            else "Unknown"
        )

        return (
            f"{self.title} | "
            f"{self.company} | "
            f"{self.location} | "
            f"Sponsorship: {sponsor}"
        )