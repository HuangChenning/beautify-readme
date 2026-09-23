<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="beautify-readme — 将任何 GitHub README 变为简洁的主题化视觉故事">
</p>

# beautify-readme

一个 Agent 技能，将任何 GitHub README 变为简洁、主题化的视觉故事。它融合了 README 内容架构、手写 SVG、横跨 5 种渲染引擎的 14 种图表引擎、可选的 [Archify](https://github.com/tt-a1i/archify) 系统图，以及可选的动画效果 — 同时支持 GitHub 原生渲染和 Markdown Viewer 增强图表。

## 它能做什么

- **README 模式** — 重构内容故事，构建视觉系统，产出一个协调的主页。
- **资产模式** — 仅创建 SVG Hero、章节标题、图表、徽章或动画图形，不修改 README。
- **双渲染上下文** — 面向 `github.com` 的 GitHub 原生 SVG/PNG/GIF，以及面向 Markdown Viewer 扩展的代码围栏图表（PlantUML、Vega、infographic、canvas、architecture、infocard）。
- **代码统计徽章** — 用 shields.io 显示代码体积和代码行数，行数由 GitHub Actions 工作流自动更新。
- **可选 Archify 系统图** — 经校验的架构 / 工作流 / 时序 / 数据流 / 生命周期图，导出 Share Card 供 GitHub 原生嵌入。

## 图表引擎

| 需求 | 引擎 | 代码围栏 / 产出 | 上下文 |
| --- | --- | --- | --- |
| 精致运行时 / 服务架构图 | Archify | PNG/SVG Share Card | GitHub 原生 |
| CI/CD、审批、工具调用工作流 | Archify | PNG/SVG Share Card | GitHub 原生 |
| API / 缓存 / 鉴权轨迹；数据流；生命周期 | Archify | PNG/SVG Share Card | GitHub 原生 |
| 软件建模（类图、序列图、活动图、状态图） | PlantUML | ` ```plantuml ` | 两者 |
| 云架构（AWS、Azure、GCP、K8s） | PlantUML | ` ```plantuml ` | 两者 |
| 网络 / 安全 / IoT / BPMN / ArchiMate | PlantUML | ` ```plantuml ` | 两者 |
| 数据图表（柱状、折线、散点、热力图） | Vega-Lite | ` ```vega-lite ` | 两者 |
| 高级图表（雷达、词云） | Vega | ` ```vega ` | 两者 |
| KPI 仪表盘、时间线、SWOT、漏斗 | Infographic | ` ```infographic ` | Viewer |
| 概念图、知识图谱 | Canvas (JSON) | ` ```canvas ` | Viewer |
| 分层系统架构（可编辑 HTML） | Architecture | 直接 HTML | Viewer |
| 编辑风格信息卡片 | Infocard | 直接 HTML | Viewer |

在 GitHub 原生上下文中，用引擎生成图表后导出为静态 SVG 或 PNG 并嵌入图片文件。在 Markdown Viewer 上下文中，直接在 README 中编写代码围栏。Archify 为可选外部技能（`tt-a1i/archify`）；不可用时回退到 PlantUML、Architecture HTML 或手写 SVG。

## 工作流程

1. **确认模式** — README 重设计还是仅创建资产。
2. **确认渲染上下文** — GitHub 原生还是 Markdown Viewer 增强。
3. **检查仓库** — README、目录树、元数据、截图、真实输出。
4. **确认视觉实现** — 纯 SVG 还是混合 SVG + 光栅合成。
5. **提取项目故事** — 受众、价值、证据、首次操作、视觉主题。
6. **冻结视觉系统** — 色板、字体、形状、母题、构图。
7. **构建视觉层** — SVG 资产、代码围栏图表或混合合成。
8. **预览和验证** — 审计脚本、视觉检查、响应式检查。
9. **安全交付** — 先展示差异；仅在用户要求时才提交或推送。

## 技能结构

```
skills/beautify-readme/
├── SKILL.md                          # 主技能文件：工作流、模式、质量标准
├── references/
│   ├── content-architecture.md       # README 内容排序和编辑规则
│   ├── readme-canvas.md              # GitHub README 画布约束
│   ├── svg-production.md             # 手写 SVG 生产规则
│   ├── visual-direction.md           # 主题化视觉方向
│   ├── design-system.md              # 整合设计规则（色彩、字体、品味）
│   ├── project-native-hero.md        # 从项目内容设计 Hero
│   ├── hybrid-svg-production.md      # 混合 SVG + 光栅合成
│   ├── motion-production.md          # GitHub 安全的 GIF 动画
│   ├── diagram-engines.md            # 引擎目录 + 可选 Archify 分支 + 语法规则
│   └── output-verification.md        # 强制合规关卡（4 个维度）
└── scripts/
    ├── audit_readme.py               # 审计 README 图片引用和 SVG 基础
    ├── verify_readme.py              # 可编程合规检查器（4 个维度）
    └── render_motion_gif.py          # 从 SVG + 动画规格渲染 GIF
```

## 安装

### 快速安装

```bash
cp -r skills/beautify-readme ~/.qoder/skills/
```

### 手动安装

将 `skills/beautify-readme/` 目录复制到你的 Agent 技能文件夹：

| Agent | 路径 |
| --- | --- |
| Qoder | `~/.qoder/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |

## 使用方式

```
使用 $beautify-readme 围绕开发者工具主题重新设计这个仓库主页。
```

```
使用 $beautify-readme 创建一个 SVG Hero 和三个章节标题，不修改 README。
```

```
使用 $beautify-readme 给这个 README 添加一个 PlantUML 架构图和一张 Vega-Lite 基准图表。
```

```
使用 $beautify-readme 通过 Archify 添加 GitHub 原生的 How it works 图，并导出 Share Card PNG。
```

```
使用 $beautify-readme 创建一个混合 Hero：SVG 排版布局加 ImageGen 角色素材。
```

## 设计理念

- 设计应看起来属于这个项目，而非属于这个技能。
- Hero 的视觉素材来自项目本身 — 不是通用装饰。
- 真实证据出现在抽象承诺之前。
- README 应更短或更清晰，而不仅仅是更花哨。
- 移除仓库名称后，Hero 不应能被无关项目复用。
- 每个视觉模块都有明确的传达职责。
- 设计选择通过品味清单：无居中 Hero、无等宽磁贴、无纯黑、无霓虹渐变、无 AI 套话。

## 局限性

- 代码围栏图表（PlantUML、Vega、infographic、canvas、architecture、infocard）需要 Markdown Viewer 扩展 — 在 `github.com` 上会显示为原始代码，除非导出为静态图片。
- Archify 系统图需要外部技能 `tt-a1i/archify` 与 Node.js；GitHub 嵌入必须使用导出的 PNG/SVG，不能仅依赖交互式 HTML。
- GIF 动画是可选的且有大小限制；GitHub 在移动端不会自动播放 GIF。
- 该技能不生成光栅照片或插图 — 请使用 `imagegen` 技能生成，再通过混合 SVG 合成。
- 审计和验证脚本检查的是结构合规性，而非审美判断 — 仍需人工视觉审查。

## 贡献者

<p align="center">
  感谢所有参与构建这个技能的人。
</p>

<p align="center">
  <a href="https://github.com/HuangChenning/beautify-readme/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=HuangChenning/beautify-readme" alt="HuangChenning/beautify-readme 贡献者" />
  </a>
</p>

### 贡献统计

<!-- CONTRIBUTORS:START -->
| 贡献者 | 提交次数 | 新增行 | 删除行 |
| --- | ---: | ---: | ---: |
| HuangChenning | 6 | +3,909 | −51 |
<!-- CONTRIBUTORS:END -->

<sub>数据来自 <code>git shortlog</code> 与 <code>git log --shortstat</code>（不含 merge 提交）。更新本 README 时请运行 <code>python3 scripts/update_contributors.py</code> 刷新。</sub>

## 许可证

MIT
