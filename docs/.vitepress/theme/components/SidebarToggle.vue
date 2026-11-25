<template>
  <!-- 仅在有侧边栏的文档页面显示，避免在 layout: page 的宽屏看板页干扰视线 -->
  <button
    v-if="hasSidebar"
    class="sidebar-toggle-btn"
    @click="toggleSidebar"
    :title="isCollapsed ? '展开侧边栏' : '收起侧边栏'"
  >
    {{ isCollapsed ? '⇥' : '⇤' }}
  </button>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useSidebar } from 'vitepress/theme'

// 获取 VitePress 内置的侧边栏状态钩子
const { hasSidebar } = useSidebar()
const isCollapsed = ref(false)

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
  // 核心状态机动作：在根节点 <html> 上切换类名
  document.documentElement.classList.toggle('sidebar-collapsed', isCollapsed.value)
}

onMounted(() => {
  // 初始化同步状态
  isCollapsed.value = document.documentElement.classList.contains('sidebar-collapsed')
})
</script>

<style scoped>
.sidebar-toggle-btn {
  position: fixed;
  bottom: 28px;
  left: 24px;
  z-index: 50;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(56, 189, 248, 0.4);
  color: #38bdf8;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.25s ease;
}

.sidebar-toggle-btn:hover {
  background: rgba(56, 189, 248, 0.2);
  transform: scale(1.05);
}

/* 手机/平板窄屏下隐藏此按钮，交给 VitePress 原生汉堡菜单接管 */
@media (max-width: 960px) {
  .sidebar-toggle-btn {
    display: none;
  }
}
</style>