# AdapTabPrompt 新最终四件套独立复审

- 审计日期：2026-09-04（Asia/Shanghai）
- 审计对象：`AdapTabPrompt_ICCEIC2026_Final_Anonymous.docx/.pdf` 与 `AdapTabPrompt_ICCEIC2026_Final_Author_Copy.docx/.pdf`
- 最终结论：**PASS。** 旧候选的两个阻断项均已修复：Table IV 四格已逐字回滚到权威稿；第 6 页参考文献已真实分布到左右两栏。未发现新裁切、重叠、断表、缺字、蓝色、批注、修订或身份泄漏。

## 1. 文件完整性与页面

| 文件 | SHA-256 | 结果 |
|---|---|---|
| `AdapTabPrompt_ICCEIC2026_Final_Anonymous.docx` | `62B4C92B5AF928AB830EDDC2408D9A726B42EEC9E11A8A1514041FE23D30AAD8` | OOXML CRC 通过；Word 新导出为 6 页 |
| `AdapTabPrompt_ICCEIC2026_Final_Anonymous.pdf` | `DBA2CC54B4FEFCB5E66B69DE21744C8C4CBC9C2EA4A30CC114C24B0FCEC82DA0` | 可读、未加密、6 页 |
| `AdapTabPrompt_ICCEIC2026_Final_Author_Copy.docx` | `AB879CA1EB654406255AFC233E33F572620F2ADC2CCFEC2E8CA9E67DBB7354BB` | OOXML CRC 通过；Word 新导出为 6 页 |
| `AdapTabPrompt_ICCEIC2026_Final_Author_Copy.pdf` | `B64A7D728193BC88BF5C3D3DDADB57C6D9E162DF8B848025066CB03ED81B95EF` | 可读、未加密、6 页 |

- 四个结果均可打开。
- 两份 PDF 的 6 页全部为 `612 x 792 pt`、旋转 0，即 US Letter 纵向；不超过 8 页。
- DOCX 节尺寸为 `12240 x 15840 dxa`，正文为 IEEE 风格双栏；Table II 通过单栏跨栏节呈现，再恢复双栏。

## 2. 冻结数据与四张表

- 重新运行冻结证据校验后：18 episodes、72 ordered method rows、0 failure rows。
- Main-Tree：18/18 行完全相同；overall `+0.0000000`。
- Main-NoSem：`+0.0009668`；累计 gate/rescue `1/50`。
- Main-Perm：`-0.0005258`；累计 gate/rescue `2/100`。
- Main 累计 gate/rescue：`0/0`。
- 注册决策表：10 个条件，5 PASS、5 FAIL；最终 `NO_GO`。
- Table I、II、III、IV 均与冻结/权威内容逐格相同。
- Table IV 第二列四个权威句已全部恢复，旧版的语义改写不再存在。

## 3. 参考文献与正文引用

- 15 条参考文献编号连续 `[1]` 至 `[15]`。
- 去除纯版式 column-break 空段后，15 条参考文献文本与权威稿逐条、逐字相同。
- 正文实际引用集合为 `[1]` 至 `[15]`，每条均有正文引用，无越界或缺号。
- 第 6 页人工复审确认：左栏为 `[1]-[8]`，右栏为 `[9]-[15]`；两栏都有内容，顺序连续，没有裁切、相互覆盖或断裂条目。

## 4. 匿名性、作者信息和清洁度

- 匿名版正文、页眉页脚、OOXML story parts、核心属性和 PDF 文本中均未发现 `Lin Zhanyi`、`Hong Kong Metropolitan University` 或作者邮箱；核心属性为 `Anonymous`，标题页为 `Anonymous Authors`。
- 作者版保留 `Lin Zhanyi`、`Hong Kong Metropolitan University` 和 `lzzzy20041125@outlook.com`；DOCX/PDF 身份一致。
- 两份 DOCX 均为：批注部件 0、批注锚点 0、修订节点 0、highlight 0、`rsid*` 0、自定义属性部件 0、非灰度 story-text 颜色 0。
- 未发现外部编辑指令或查重报告残留；筛查的编辑标记均为 0 命中。
- 两份 PDF 共 12 页逐像素检查：每页非灰度像素 0，全文、表格和流程图均为黑白灰。

## 5. 逐页视觉复审

- 两份最终 PDF 各 6 页均以 200 dpi 重新渲染，并逐页人工查看。
- 两份最终 DOCX 均通过 Microsoft Word 隐藏模式重新导出为临时 PDF，再各自渲染 6 页。
- 候选 PDF 与对应 DOCX 新导出结果逐页 PNG 哈希 12/12 完全相同，因此四件套版面一一对应。
- 所有页面均未发现：文字/表格裁切、对象重叠、表格断裂、页外溢出、缺字、空白整页、异常页眉页脚或彩色残留。
- 第 6 页参考文献双栏平衡修复有效。第 5 页在正文结束后仍有正常的末节余白，参考文献从独立第 6 页开始；不造成内容缺失或版面错误。

## 6. 验收结论

新最终四件套满足本轮要求，可作为交付候选：匿名版用于匿名审稿场景；作者版仅作为实名备份或会后版本。审计状态从旧候选的 `BLOCKED` 更新为 **PASS**。
