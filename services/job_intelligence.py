class JobIntelligence:

    def enrich(self, job):

        score = 0

        if job.visa_sponsorship:
            score += 40

        if job.recruiter_phone:
            score += 20

        elif job.recruiter_email:
            score += 15

        if "Power BI" in job.title:
            score += 15

        if "Data Analyst" in job.title:
            score += 15

        if "Business Intelligence" in job.title:
            score += 15

        job.opportunity_score = score

        return job