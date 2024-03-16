from datetime import datetime

from pydantic import BaseModel


class KeyInfo(BaseModel):
    expiration: datetime
