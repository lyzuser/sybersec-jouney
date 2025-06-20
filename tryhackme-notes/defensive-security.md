# 🛡️ Defensive Security 实战笔记

## ✅ Room: A Day in the Life of a Junior SOC Analyst

> 练习目标：模拟 SOC 环境，识别恶意 IP 并采取防御行动。

---

### 🧩 Task 1：What is Defensive Security?
- 理解防御安全侧重于威胁检测、响应与隔离
- 关键词：SOC、SIEM、DFIR、EDR

---

### 🔎 Task 2：Areas of Defensive Security
- SOC（安全运营中心）
- SIEM（安全信息与事件管理系统）
- 日志分析与告警响应

---

### 🛠️ Task 3：实战操作

#### 📌 SIEM 分析步骤：
1. 查看 SIEM 仪表盘中的警报日志
2. 定位可疑 IP：143.110.250.149
3. 使用 `ip-scanner.thm` 平台核实为恶意 IP
4. 提交 Flag：`THM{THREAT-BLOCKED}` ✅

---

### 🧠 学习总结：
- 熟悉 SIEM 警报与日志信息的解读
- 学会从 IP Reputation 数据库确认恶意源
- 提升蓝队分析实战能力，适应 SOC 初级岗位模拟

