from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.application import Application
from app.schemas.application import ApplicationCreate


async def create_application(db: AsyncSession, user_id: UUID, body: ApplicationCreate) -> Application:
    app_row = Application(
        user_id=user_id,
        company=body.company,
        role=body.role,
        status=body.status,
        applied_date=body.applied_date,
    )
    db.add(app_row)
    await db.commit()
    await db.refresh(app_row)
    return app_row


async def list_applications(
    db: AsyncSession,
    user_id: UUID,
    status: Optional[str] = None,
    company: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> list[Application]:
    stmt = select(Application).where(Application.user_id == user_id)

    if status:
        stmt = stmt.where(Application.status == status)
    if company:
        stmt = stmt.where(Application.company.ilike(f"%{company}%"))

    stmt = stmt.order_by(Application.updated_at.desc()).limit(limit).offset(offset)
    result = await db.execute(stmt)
    return list(result.scalars().all())
