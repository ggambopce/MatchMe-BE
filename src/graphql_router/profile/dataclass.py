from dataclasses import dataclass

@dataclass
class ProfileServiceResponse:
    temperament: str
    enneagram: str
    temperament_report: str
