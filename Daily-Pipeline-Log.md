---
title: "Day {{date:DD}} - [今日技術主題]"
date: {{date:YYYY-MM-DD}}
tags:
  - daily-log
  - blender
  - openusd
  - pipeline
status: in-progress # 狀態管理：in-progress, completed, blocked
---

# Day {{date:DD}} - [今日技術主題]

## 🎯 1.5 小時精準打擊目標 (Sprint Objectives)
> **Goal:** [用一句話描述今日 1.5 小時的核心產出目標，例如：透過 Python API 自動化匯出 Blender 靜態網格體至 USD 格式]

- [ ] 任務 A：[例如：撰寫基礎 Mesh 匯出腳本]
- [ ] 任務 B：[例如：在 `usdview` 中驗證階層結構]
- [ ] 任務 C：[例如：將更新後的腳本推播至 GitHub]

---

## 🛠️ 技術實作與產出 (Execution & Output)
*(記錄您的架構設計、節點配置或核心工作流)*

### 關鍵腳本 / 結構對照
*(提示：此區塊利用 MkDocs 的 Tabbed 擴充功能，在網頁端會自動轉換為並排頁籤，而在 Obsidian 中則能直接閱讀底層結構。)*

=== "Python (Blender API)"
    ```python
    import bpy
    # 在此貼上您的自動化腳本核心片段
    ```

=== "USD Ascii"
    ```usda
    # 在此貼上對應生成的 USD 結構
    #def Xform "MyAsset"
    ```

---

## 🚧 障礙與除錯 (Roadblocks & Debugging)
*(展現技術總監/資深工程師價值的核心區塊：解決問題的能力)*

* **Symptom (現象描述)：** [例如：匯出 USD 時，特定的自訂法線資料遺失]
* **Root Cause (根本原因)：** [例如：當前使用的外掛版本未勾選 export_custom_normals 參數]
* **Solution (解決方案)：** [例如：在 Python 腳本的匯出 operator 中強制寫入 `export_custom_normals=True`]

---

## 🔗 知識拓撲與資源 (Knowledge & Resources)
* **內部關聯：** [[Pipeline-Architecture-Overview]] *(利用 Obsidian 雙向連結建立您的知識庫)*
* **外部參考：**
    * [NVIDIA Omniverse 官方文件標題](https://...)
    * [GitHub Issue 討論串](https://...)

---

## 📅 明日滾動規劃 (Next Steps)
- [ ] [填入明日 1.5 小時預計推進的下一個管線節點]