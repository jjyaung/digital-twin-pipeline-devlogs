---
title: 168 days digital twin USD Pipeline Challenge Dashboard
layout: default
---

# 🚀 168-Day Pipeline Challenge Dashboard

> **專案使命：** 每日 1.5 小時精準投入，從 Blender 基礎建模出發，貫穿 OpenUSD/Omniverse 工業級管線整合，最終落地至 Unity 數位孿生即時渲染。

---

## 📊 整體挑戰進度 (Progress Overview)

| 指標 (Metric) | 數值 / 狀態 | 說明 |
| :--- | :--- | :--- |
| **啟動日期** | 2026-09-07 | 正式計算 Day 1 |
| **預計結案** | 2027-02-21 | 累積 252 小時工程實作 |
| **目前進度** | **Day 001 / 168** | 進度率：`0.6%` |
| **目前階段** | Phase 1: Blender 建模 | 專注工業資產規格化與拓撲 |
| **履歷投遞倒數** | 84 天 (約 2026-12 初) | 第一波試水溫窗口 |

---

## 🗺️ 三階段待辦藍圖 (Roadmap & Backlog)

=== "Phase 1: Blender 工業資產與基礎 (Day 1 - 56)"
    - [x] **Milestone 0: 專案基礎建設** (GitHub Repo、MkDocs CI/CD、日誌架構初始化)
    - [ ] **Sprint 1.1 (Day 1-14): 介面與硬表面建模核心**
        - [ ] 工業標準單位與樞軸點（Pivot Point）規範建立
        - [ ] 非破壞性建模工作流 (Modifiers Stack)
    - [ ] **Sprint 1.2 (Day 15-28): UV 展開與 PBR 材質管線**
        - [ ] UDIM 多象限 UV 規劃
        - [ ] 工業設備金屬/粗糙度材質節點庫封裝
    - [ ] **Sprint 1.3 (Day 29-42): Python 自動化初探**
        - [ ] 撰寫 `bpy` 批次重新命名與階層清理腳本
        - [ ] 自動化檢查無效幾何體 (Non-manifold geometry check)
    - [ ] **Sprint 1.4 (Day 43-56): 資產規格化驗證**
        - [ ] 建立第一個工業機械臂/設備展示資產
        - [ ] Phase 1 成果總結技術報告

=== "Phase 2: OpenUSD 與 Omniverse 管線核心 (Day 57 - 112)"
    - [ ] **Sprint 2.1 (Day 57-70): OpenUSD 基礎架構解析**
        - [ ] `usda` 文字層級結構解構 (Prims, Attributes, Relationships)
        - [ ] 圖層組合機制 (SubLayers, References, Payloads, Variants)
    - [ ] **Sprint 2.2 (Day 71-84): Blender to USD 自動化轉換**
        - [ ] 撰寫 Python 腳本自訂 USD 匯出參數 (Schema, Custom Attributes)
        - [ ] 使用 `usdview` 檢驗舞台（Stage）與快取效率
    - [ ] **Sprint 2.3 (Day 85-98): NVIDIA Omniverse 整合與認證準備**
        - [ ] Nucleus 伺服器即時協同資產上傳
        - [ ] 準備 NVIDIA NCP-OUSD 認證重點知識庫 *(準備啟動第一波履歷投遞)*
    - [ ] **Sprint 2.4 (Day 99-112): 數位孿生資料綁定**
        - [ ] 將外部感測器資料 (JSON/CSV) 藉由 Python 綁定至 USD Prim 屬性

=== "Phase 3: Unity 引擎拋轉與端到端展示 (Day 113 - 168)"
    - [ ] **Sprint 3.1 (Day 113-126): USD for Unity 套件整合**
        - [ ] Unity USD Package 匯入與材質對齊 (HDRP/URP)
        - [ ] 幾何快取 (Point Cache) 動畫拋轉驗證
    - [ ] **Sprint 3.2 (Day 127-140): 即時互動與系統最佳化**
        - [ ] 設備狀態監控 UI 設計 (體現 Google UX 架構)
        - [ ] 繪製調用 (Draw Calls) 與 GPU 效能壓測分析
    - [ ] **Sprint 3.3 (Day 141-154): 作品集統整與 Demo 錄製**
        - [ ] 錄製端到端管線流程展示影片 *(啟動海外遠端與 Tier-1 投遞)*
        - [ ] 整理架構圖與 GitHub Open Source 專案說明書
    - [ ] **Sprint 3.4 (Day 155-168): 總結與模擬面試覆盤**
        - [ ] 168 天工程日誌結案報告
        - [ ] 整理常見 Pipeline TD / USD Engineer 技術面試題解庫

---

## 📝 每日開發日誌速查 (Dev Log Index)

> 提示：點擊標題即可跳轉至該日誌的詳細架構、程式碼與除錯覆盤記錄。

| 天數 (Day) | 日期 | 核心主題 (Feature / Topic) | 關鍵技術標籤 | 狀態 | 產出連結 |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **Day 001** | 2026-09-07 | 挑戰啟動與基礎架構驗證 | `Setup`, `CI/CD`, `MkDocs` | ✅ 已完成 | [[Day-001]] |
| **Day 002** | 2026-09-08 | 工業零件基準拓撲與單位規範 | `Blender`, `Modeling`, `Standard` | ⏳ 進行中 | [[Day-002]] |
| **Day 003** | 2026-09-09 | 倒角修改器與非破壞工作流 | `Blender`, `Modifiers` | 📅 待執行 | [[Day-003]] |
| **Day 004** | 2026-09-10 | 工業軸心點與裝配階層拆解 | `Blender`, `Hierarchy` | 📅 待執行 | [[Day-004]] |
| *...* | *...* | *（每日持續滾動新增）* | *...* | *...* | *...* |

---
```dataview
TABLE date AS "日期", tags AS "技術標籤", status AS "狀態"
FROM #daily-log
SORT file.name ASC
```

---

## ⚡ 快捷跳轉 (Quick Links)
* 📖 [技術資產庫 (Python 自動化腳本庫)](assets/scripts.md)
* 🏗️ [OpenUSD 拓撲架構圖解庫](assets/usd-architecture.md)
* 💼 [關於作者 / LinkedIn 履歷對照](about.md)