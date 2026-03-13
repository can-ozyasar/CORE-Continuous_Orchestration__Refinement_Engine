# Amaç: Ajanlar (Generator ve Judge) arasındaki veri aktarımını sağlayan, 
#Pydantic ile sınırları kesin çizilmiş, tip güvenli durum (State) nesnesi.





from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum

class AgentType(str, Enum):
    GENERATOR = "generator"
    JUDGE = "judge"
    SYSTEM = "system"

class CritiqueFeedback(BaseModel):
    """Judge ajanının Generator ajanına vereceği yapılandırılmış geri bildirim."""
    is_approved: bool = Field(..., description="Kodun kalite standartlarını geçip geçmediği.")
    errors: List[str] = Field(default_factory=list, description="Tespit edilen mimari veya mantıksal hatalar.")
    suggestions: List[str] = Field(default_factory=list, description="İyileştirme önerileri.")

class HandoffState(BaseModel):
    """
    LangGraph state machine üzerinde ajanlar arası gidip gelecek ana DTO (Data Transfer Object).
    Bu sınıf sistemin hafızasının o anki fotoğrafıdır.
    """
    current_task_id: str = Field(..., description="Üzerinde çalışılan iş paketinin ID'si.")
    sender: AgentType = Field(..., description="Mesajı/Kodu gönderen ajan.")
    receiver: AgentType = Field(..., description="Mesajı/Kodu alacak olan ajan.")
    
    # Payload
    source_code: Optional[str] = Field(None, description="Generator tarafından üretilen kaynak kod.")
    feedback: Optional[CritiqueFeedback] = Field(None, description="Judge tarafından üretilen eleştiri nesnesi.")
    
    # Metadata
    iteration_count: int = Field(default=0, description="Bu görev için kaçıncı düzeltme döngüsünde olduğumuz.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Ekstra bağlam veya çalışma zamanı değişkenleri.")

    class Config:
        # Pydantic'in katı modunu açıyoruz. Beklenmeyen veri gelirse sistem hata fırlatır (Fail-Fast).
        extra = "forbid"