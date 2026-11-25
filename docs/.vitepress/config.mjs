import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({

  title: "Narrarch",
  description: "record and experience",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '首页', link: '/' },

      { text: '动漫观测站', link: '/anime/' },     // 指向 docs/anime/index.md
      { text: '学习与代码', link: '/study/' },     // 指向 docs/study/index.md
      { text: '思辨随笔', link: '/thoughts/' },    // 指向 docs/thoughts/index.md

      // 可选：带下拉菜单的快捷入口
      {
        text: '硬核专项',
        items: [
          { text: '三系天体数值模拟', link: '/nbody' },
          { text: '友人帐随笔', link: '/anime/friend' }
        ]
      }
    ],
  sidebar: {
      // 1. 只要网址以 /anime/ 开头，左侧就只显示动漫目录
      '/anime/': [
        {
          text: '动漫观测站',
          collapsed: false,
          items: [
            { text: '频道总览', link: '/anime/' },       // 指向 docs/anime/index.md
            { text: 'friend', link: '/anime/friend' }   // 指向 docs/anime/friend.md
          ]
        }
      ],

      // 2. 默认兜底目录（在首页或根目录打开时显示）
      '/': [
        {
          text: '我的笔记与实验',
          collapsed: false,
          items: [
            { text: '我的第一篇笔记', link: '/first-note' },
            { text: '三系天体模拟 (nbody)', link: '/nbody' },
            { text: '进入动漫频道 →', link: '/anime/' }
          ]
        }
      ]
    },

  socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
