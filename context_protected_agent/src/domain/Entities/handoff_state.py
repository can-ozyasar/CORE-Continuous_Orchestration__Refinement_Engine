#Ajanlar arası iletişimde kullanılacak, geçmişi hatırlayan, katı kurallı ve state-machine uyumlu Evrensel Durum Aktarım Şeması (CIR).



from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal
from datetime import datetime, timezone

class ValidationFeedback(BaseModel):
    """Yargıç ajanın ürettiği yapılandırılmış geri bildirim."""
    is_approved: bool = Field(..., description="Kodun Clean Architecture ve projenin anayasasına uygun olup olmadığı.")
    critical_issues: List[str] = Field(default_factory=list, description="Düzeltilmesi zorunlu olan mantıksal veya mimari hatalar.")
    suggested_fixes: List[str] = Field(default_factory=list, description="Yargıç ajanın çözüm önerileri.")

class HandoffState(BaseModel):
    """Ajanlar arası iletişimde kullanılan Evrensel Durum Aktarım Şeması (CIR)."""
    
    # İş Akışı (Workflow) Verileri
    task_id: str = Field(..., description="Mevcut görevin veya iş paketinin benzersiz kimliği (UUID).")
    current_phase: Literal["GENERATION", "CRITIQUE", "REFINEMENT", "COMPLETED", "FAILED"] = Field(
        default="GENERATION", description="Çapraz denetim döngüsündeki mevcut aşama."
    )
    
    # Payload (İçerik)
    generated_code: Optional[str] = Field(None, description="Yaratıcı ajan tarafından üretilen güncel kod parçası.")
    architectural_decisions: List[str] = Field(
        default_factory=list, description="Yaratıcı ajanın kodu yazarken aldığı kararlar (PROJECT_SUMMARY.md ile hizalı)."
    )
    
    # Hafıza ve Denetim (Memory & Audit)
    feedback_history: List[ValidationFeedback] = Field(
        default_factory=list, description="Ajanların önceki iterasyonlardaki tartışma ve reddedilme geçmişi."
    )
    iteration_count: int = Field(default=0, description="Sonsuz döngüyü önlemek için maksimum tartışma sayısını takip eder.")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Durumun son güncellenme zamanı.")

    # Pydantic V2 Katı Mod Ayarı (Beklenmeyen veriyi reddeder)
    model_config = ConfigDict(extra="forbid")