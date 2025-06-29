from dataclasses import dataclass

@dataclass
class MatchProfileData:
    profile_id: int
    nickname: str
    temperament: str
    enneagram: str
    introduction: str
    gender: str
    birth_date: str
    job: str
    profile_image_url: str
    location: str
    relationship_intent: str
    temperament_report: str
    match_score: int
    match_report: str
