from .base import SessionLocal
from .schemas import CompanyBase
from .models import Company

Session = SessionLocal()

def new_Company(session: Session, company: CompanyBase) -> Company:
    db_company = Company(
        name_ko = company.name_ko,
        name_en = company.name_en,
        name_ja = company.name_ja,
        name_tw = company.name_tw,
        tag_ko = company.tag_ko,
        tag_en = company.tag_en,
        tag_ja = company.tag_ja,
        tag_tw = company.tag_tw
    )
    session.add(db_company)
    session.commit()
    session.refresh(db_company)

    return db_company