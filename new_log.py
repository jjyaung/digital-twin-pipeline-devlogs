#!/usr/bin/env python3
import datetime
import os
import sys
import subprocess

START_DATE = datetime.date(2026, 9, 7)
TOTAL_DAYS = 168
LOG_DIR = os.path.expanduser("~/digital-twin-pipeline-devlogs/logs")

# 這裡先放前幾天的資料作為範例，你可以隨時擴充
TASKS = {
    1: (1, "Blender 4.5 Interface & Viewport Navigation", "https://www.youtube.com/watch?v=ILqOWe3zAbk", "Viewport Navigation, Orthographic/Perspective"),
    2: (1, "Edit Mode Core Shortcuts & Geometry Tools", "Grant Abbitt Blender 4 Edit mode Extrude Inset Loop Cut", "Extrude, Inset, Loop Cut"),
    3: (1, "Industrial Control Box Hard Surface Modeling", "Blender 4 hard surface modeling beginner box chassis", "Box Modeling, Bevel 2-Segments"),
}

def get_day_info(target_date):
    return (target_date - START_DATE).days + 1

def generate_devlog(day_num=None):
    today = datetime.date.today()
    if day_num is None:
        day_num = get_day_info(today)
    
    if day_num < 1 or day_num > TOTAL_DAYS:
        print(f"[Notice] Day {day_num} is out of the 168-day scope. Defaulting to Day 1.")
        day_num = 1 if day_num < 1 else TOTAL_DAYS

    week_num = (day_num - 1) // 7 + 1
    
    title, link, terms = TASKS.get(day_num, (week_num, f"Digital Twin Pipeline Implementation (Day {day_num})", "https://developer.nvidia.com/openusd", "OpenUSD, Python pxr, Unity 6"))[1:]
    
    cur_date_str = (START_DATE + datetime.timedelta(days=day_num - 1)).strftime("%Y-%m-%d")
    filename = f"Day_{day_num:03d}_{cur_date_str}.md"
    filepath = os.path.join(LOG_DIR, filename)

    if not os.path.exists(filepath):
        template = f"""---
title: "Day {day_num:03d} | {title}"
date: {cur_date_str}
week: {week_num}
day: {day_num}
tags: [DigitalTwin, Blender, OpenUSD, Unity, DevLog]
status: In Progress
---

# Day {day_num:03d}: {title}

- **Date:** {cur_date_str} (Week {week_num})
- **Core Terms:** `{terms}`
- **Reference/Tutorial:** `{link}`
- **Hardware Budget:** Quadro T2000 4GB (Target VRAM < 1.5GB for local tasks)

---

## 1. Task Checklist
- [ ] Complete technical tutorials and take API/Shortcut notes.
- [ ] Implement core functionality (Topology / OpenUSD Hierarchy / C# Scripting).
- [ ] Validate VRAM and performance overhead via `nvidia-smi` or Unity Profiler.
- [ ] Capture screenshots or record a brief demonstration GIF.

---

## 2. Implementation Details

### Key Operations & Code Snippets:
```python
# Insert pxr Python or Unity C# code here