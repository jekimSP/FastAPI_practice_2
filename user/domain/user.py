from dataclasses import dataclass
from datetime import datetime

@dataclass
#도메인 객체를 다루기 쉽게 하기 위해 Python에서 제공되는 dataclass 선언
class User:
    id: str
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime