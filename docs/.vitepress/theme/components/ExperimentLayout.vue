<template>
  <!-- 继承 VitePress 默认导航栏，保证顶部菜单不丢失 -->
  <div class="exp-container">

    <!-- 1. 头部档案卡片：永远存在 -->
    <header class="exp-header glass-box">
      <div class="exp-badge" v-if="frontmatter.tag">{{ frontmatter.tag }}</div>
      <h1>{{ frontmatter.title || '未命名实验档案' }}</h1>
      <p class="exp-summary" v-if="frontmatter.summary">{{ frontmatter.summary }}</p>
    </header>

    <!-- 2. 核心指标栏：只有当你在 md 里写了 metrics 列表时才显示，不写就彻底隐去！ -->
    <section class="exp-metrics glass-box" v-if="frontmatter.metrics && frontmatter.metrics.length">
      <div class="metric-item" v-for="(item, index) in frontmatter.metrics" :key="index">
        <span class="metric-label">{{ item.label }}</span>
        <span class="metric-value">{{ item.value }}</span>
      </div>
    </section>

    <!-- 3. 架构演进对比框：只有当你填了 old_arch 或 new_arch 时才出现 -->
    <section class="exp-arch-grid" v-if="frontmatter.old_arch || frontmatter.new_arch">
      <div class="arch-card glass-box old" v-if="frontmatter.old_arch">
        <h3>⚠️ 历史脚本痛点</h3>
        <p>{{ frontmatter.old_arch }}</p>
      </div>
      <div class="arch-card glass-box new" v-if="frontmatter.new_arch">
        <h3>⚡ 重构架构方案</h3>
        <p>{{ frontmatter.new_arch }}</p>
      </div>
    </section>

    <!-- 4. 正文插槽：<Content /> 是 VitePress 内置魔法标签，你的 Markdown 正文会自动灌进这里 -->
    <main class="exp-content glass-box vp-doc">
      <Content />
    </main>

  </div>
</template>

<script setup>
import { useData } from 'vitepress'
// 提取当前 Markdown 文件顶部的 Frontmatter 数据字典
const { frontmatter } = useData()
</script>

<style scoped>
.exp-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* 统一的动漫毛玻璃方框基类 */
.glass-box {
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 12px;
  padding: 1.5rem 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.exp-badge {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  background: rgba(244, 63, 94, 0.2);
  color: #fb7185;
  border: 1px solid #f43f5e;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: bold;
  margin-bottom: 0.8rem;
}

.exp-header h1 {
  margin: 0;
  font-size: 2rem;
  color: #f8fafc;
}

.exp-summary {
  color: #94a3b8;
  margin-top: 0.5rem;
}

.exp-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.metric-item {
  display: flex;
  flex-direction: column;
}

.metric-label { font-size: 0.85rem; color: #94a3b8; }
.metric-value { font-size: 1.4rem; font-weight: bold; color: #38bdf8; }

.exp-arch-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.arch-card h3 { margin-top: 0; font-size: 1.1rem; }
.arch-card.old { border-color: rgba(245, 158, 11, 0.3); }
.arch-card.new { border-color: rgba(16, 185, 129, 0.3); }
</style>