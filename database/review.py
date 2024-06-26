from dataclasses import dataclass
from datetime import date
from database.business import Business


@dataclass
class Review:
    review_id: str
    stars: float
    review_date: date
    votes_funny: int
    votes_useful: int
    votes_cool: int
    review_text: str

    business: Business
    business_id: str

    def __eq__(self, other):
        return self.review_id == other.review_id

    def __hash__(self):
        return hash(self.review_id)
