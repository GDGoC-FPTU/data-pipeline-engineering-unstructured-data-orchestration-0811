from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    document_id: str = Field(...)
    source_type: str = Field(...)
    author: str = Field(...)
    category: str = Field(...)
    content: str = Field(...)
    timestamp: str = Field(...)
