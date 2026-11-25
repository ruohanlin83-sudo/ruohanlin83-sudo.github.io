import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'
import ExperimentLayout from './components/ExperimentLayout.vue'
import SidebarToggle from './components/SidebarToggle.vue'

export default {
  extends: DefaultTheme,

  // 钩子 1：结构插槽注入（用于在默认布局的特定位置“塞入”全局悬浮组件）
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // 把侧边栏折叠按钮挂到全站最底部的 layout-bottom 插槽上
      'layout-bottom': () => h(SidebarToggle)
    })
  },

  // 钩子 2：Vue 应用实例增强（你原本写好的部分，用于注册全局组件或自定义整页 layout）
  enhanceApp({ app }) {
    // 只要在 md 顶部声明 layout: experiment，就会自动套用这个整页模板
    app.component('experiment', ExperimentLayout)
  }
}