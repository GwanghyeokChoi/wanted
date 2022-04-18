from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name_ko: Optional[str] = None
    name_en: Optional[str] = None
    name_ja: Optional[str] = None
    name_tw: Optional[str] = None
    tag_ko: Optional[str] = None
    tag_en: Optional[str] = None
    tag_ja: Optional[str] = None
    tag_tw: Optional[str] = None

class Company(CompanyBase):
    idx: int

    class Config:
        orm_mode = True