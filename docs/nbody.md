---
layout: experiment
tag: "Py.167 物理仿真重构"
title: "三体混沌动力学：从面向过程到 Verlet 辛积分引擎"
summary: "解决长时间步进下欧拉法能量发散的问题，并将全局状态拆解为高内聚物理实体类。"
metrics:
  - label: "时间复杂度"
    value: "O(N²)"
  - label: "积分器"
    value: "Velocity Verlet"
  - label: "能量误差"
    value: "< 1e-6"
old_arch: "所有坐标、速度硬编码在全局 list 中，绘图与物理步进耦合在同一个 while 循环里。"
new_arch: "抽离 Body 数据类与 GravityEngine 计算求解器，实现相空间状态与渲染视图彻底解耦。"
---

## 数学模型与核心代码实现

这里正常写你的 Markdown 正文和 Python 代码块，它们会自动被塞进底部的 `<Content />` 毛玻璃方框里！

```python
class Body:
    pass