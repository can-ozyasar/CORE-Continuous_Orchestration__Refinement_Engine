# CORE (Continuous Orchestration & Refinement Engine) 🏭🤖

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-00a393.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean_Architecture-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ed.svg)

CORE, "Çalışsın yeter" mantığına savaş açan, **Çoklu-Ajan Çapraz Denetim (Multi-Agent Cross-Critique)** mimarisine sahip otonom bir yazılım üretim fabrikasıdır.

Sistem, yapay zekanın kendi ürettiği koddaki hatalara karşı körleşmesi (Model Bias / Degeneration-of-Thought) problemini, deterministik bir State Machine (LangGraph) ve farklı ağırlıklara sahip iki ayrı LLM (Gemini & DeepSeek) kullanarak çözer.

## 🌟 Mimari Vizyon ve Özellikler

* **Tavizsiz Clean Architecture:** Sistem katmanları (Domain, Application, Infrastructure, Presentation) birbirinden tamamen izole edilmiştir.
* **Deterministik Orkestrasyon (LangGraph):** Ajanların yönlendirilmesi (routing) maliyetli ve kararsız LLM'lere bırakılmaz; %100 kod tabanlı iş kurallarıyla yönetilir.
* **Multi-Model FinOps:** * 🧠 **Yaratıcı (Generator) Ajan:** `Gemini 2.5 Flash` (Hızlı kod üretimi ve geniş bağlam için).
  * ⚖️ **Yargıç (Judge) Ajan:** `DeepSeek Coder` (Acımasız akıl yürütme ve SOLID/Clean Architecture denetimi için).
* **Tip Güvenli İletişim (CIR):** Ajanlar serbest metinle değil, `Pydantic V2` ile doğrulanmış JSON veri transfer nesneleri (DTO) üzerinden konuşur.
* **Güvenli Konteynerizasyon:** Multi-stage build ve yetkisiz (non-root) kullanıcı ile Enterprise standartlarında Dockerize edilmiştir.

## 🚀 Hızlı Başlangıç (Quick Start)

### 1. Gereksinimler
* Docker ve Docker Compose
* Google Gemini API Key
* DeepSeek API Key

### 2. Kurulum
Projeyi klonlayın ve konfigürasyon dosyasını oluşturun:

