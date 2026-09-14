<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,50:16213e,100:0f3460&height=170&section=header&text=Haiyan%20Qin&fontSize=44&fontColor=ffffff&fontAlignY=36&desc=From%20intelligent%20models%20to%20silicon&descAlignY=58&descSize=16" width="100%" alt="Haiyan Qin" />

**AI Infra 研究者 · 北京航空航天大学 博士研究生**

<p>
  <a href="https://qhy991.github.io/"><img src="https://img.shields.io/badge/个人主页-qhy991.github.io-0f3460?style=for-the-badge&logo=googlechrome&logoColor=white" alt="个人主页"/></a>
  <a href="https://scholar.google.com/citations?user=zzmYq9QAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google%20Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar"/></a>
  <a href="mailto:haiyanq@buaa.edu.cn"><img src="https://img.shields.io/badge/邮箱-haiyanq%40buaa.edu.cn-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="邮箱"/></a>
  <a href="https://github.com/qhy991"><img src="https://img.shields.io/github/followers/qhy991?style=for-the-badge&logo=github&label=Followers&color=181717" alt="GitHub followers"/></a>
</p>

<b>简体中文</b> · <a href="README.md">English</a>

</div>

---

## 👋 关于我

我的工作在**模型与机器的交界处**——把新出现的 AI 能力落成可执行的硬件与高效的系统。

北京航空航天大学集成电路科学与工程博士研究生（2023 至今），从模型层一路做到 GPU Kernel 与电路。

- 🔬 **研究领域** —— 面向 RTL 与电路生成的 LLM Agent · GPU Kernel 生成与优化 · 存内计算
- 📄 **论文发表** —— 共 8 篇，其中 **DAC 2025 三篇**，另有 ICAIS 2025、IEEE AICAS 2023
- 🛠️ **正在构建** —— Agent 化的 Kernel 优化工作流、编译器 × Kernel 协同进化、以证据为先的研究地图
- 🌱 **当前重点** —— Agent 驱动的算子生产：让 Kernel、编译器与评测体系互相改进
- 🤝 **欢迎合作** —— [haiyanq@buaa.edu.cn](mailto:haiyanq@buaa.edu.cn)

---

## 🧭 研究方向

<table>
<tr>
<td width="33%" valign="top">

### 🤖 AI + EDA
**硬件 Agent**

LLM 驱动的 RTL 生成、多模态电路理解与多 Agent 设计流程。

`CircuitMind` `ReasoningV` `CircuitWeave`

</td>
<td width="33%" valign="top">

### ⚡ AI 系统
**GPU Kernel**

面向真实 AI 算子的高效 CUDA/Triton Kernel 与 Agent 化优化工作流。

`MegaKernel` `量化 GEMM` `ROCm`

</td>
<td width="33%" valign="top">

### 🔋 AI 硬件
**高效芯片**

存内计算、FPGA 部署与面向边缘智能的电路优化。

`SOT-CIM` `Crossbar` `Tiny NAS`

</td>
</tr>
</table>

---

## 📚 代表论文

| 年份 | 会议/期刊 | 论文 | 链接 |
|:--|:--|:--|:--|
| 2026 | arXiv | **CircuitWeave**：面向可执行多模态 RTL 生成的拓扑—行为对齐 | [arXiv](https://arxiv.org/abs/2607.23523) |
| 2025 | ICAIS 2025 | **ReasoningV**：自适应混合推理模型驱动的高效 Verilog 代码生成 —— *Token 用量降低 75%，VerilogEval-Human pass@1 达 57.8%* | [arXiv](https://arxiv.org/abs/2504.14560) · [代码](https://github.com/BUAA-CLab/ReasoningV) |
| 2025 | arXiv | **CircuitMind**：多 Agent 协作与群体智能驱动的最优电路生成 | [arXiv](https://arxiv.org/abs/2504.14625) · [代码](https://github.com/BUAA-CLab/CircuitMind) |
| 2025 | **DAC 2025** | 面向电路设计的多 Agent 良率分析 | [DBLP](https://researchr.org/publication/QinKZKX25) |
| 2025 | **DAC 2025** | 精度感知的贝叶斯良率优化 | — |
| 2025 | **DAC 2025** | 基于 Crossbar 的多核 CIM 系统权重映射与资源调度 | — |
| 2025 | Integrated Circuits and Systems | 基于高阻 SOT 器件的存内计算宏，面向边缘 AI 推理 | [DOI](https://doi.org/10.23919/ICS.2025.3567939) |
| 2023 | IEEE AICAS 2023 | 面向嵌入式 FPGA 部署的微小神经网络搜索 | [DBLP](https://researchr.org/publication/QinZBK23) |

<div align="right"><sub>完整论文与引用数据见 <a href="https://scholar.google.com/citations?user=zzmYq9QAAAAJ&hl=en">Google Scholar</a> · <a href="https://qhy991.github.io/publications.html">个人主页</a></sub></div>

---

## 🗺️ 研究地图

对快速演进领域的系统性梳理：论文、系统与 Benchmark 集中在一处。

| 仓库 | 内容 | Stars |
|:--|:--|:--|
| [**Awesome-LLM-Circuit-Agent**](https://github.com/qhy991/Awesome-LLM-Circuit-Agent) | 基于 LLM 的 RTL 与模拟电路生成相关学术工作 | ![](https://img.shields.io/github/stars/qhy991/Awesome-LLM-Circuit-Agent?style=flat-square&label=&color=0f3460) |
| [**Awesome-LLM-Kernel-Agent**](https://github.com/qhy991/Awesome-LLM-Kernel-Agent) | 112+ 篇 LLM 驱动 GPU Kernel 生成与优化论文 | ![](https://img.shields.io/github/stars/qhy991/Awesome-LLM-Kernel-Agent?style=flat-square&label=&color=0f3460) |
| [**Awesome-MegaKernel**](https://github.com/qhy991/Awesome-MegaKernel) | 整模型 Kernel、常驻运行时与深度融合的 LLM 系统 | ![](https://img.shields.io/github/stars/qhy991/Awesome-MegaKernel?style=flat-square&label=&color=0f3460) |
| [**Awesome-Kernel-Workflows**](https://github.com/qhy991/Awesome-Kernel-Workflows) | 把专家级 Kernel 优化方法封装为可运行的 Agent 工作流 | ![](https://img.shields.io/github/stars/qhy991/Awesome-Kernel-Workflows?style=flat-square&label=&color=0f3460) |

## 🔧 系统与工具

| 仓库 | 作用 | Stars |
|:--|:--|:--|
| [**open-cake-ir**](https://github.com/qhy991/open-cake-ir) | Agent 驱动的编译器与 GPU Kernel 协同进化，含类型化 IR 与执行计划 | ![](https://img.shields.io/github/stars/qhy991/open-cake-ir?style=flat-square&label=&color=16213e) |
| [**ROCm-KernelWiki-Q**](https://github.com/qhy991/ROCm-KernelWiki-Q) | 面向 AMD ROCm / CDNA 的 Kernel 优化知识图谱 | ![](https://img.shields.io/github/stars/qhy991/ROCm-KernelWiki-Q?style=flat-square&label=&color=16213e) |
| [**gpu-infra**](https://github.com/qhy991/gpu-infra) | Agent 原生的 Kernel 评测控制、GPU 调度与证据层 | ![](https://img.shields.io/github/stars/qhy991/gpu-infra?style=flat-square&label=&color=16213e) |
| [**agent-gpu-broker**](https://github.com/qhy991/agent-gpu-broker) | 单机 GPU 队列，支持共享、独占与原子多卡调度 | ![](https://img.shields.io/github/stars/qhy991/agent-gpu-broker?style=flat-square&label=&color=16213e) |
| [**Digital-CIM**](https://github.com/qhy991/Digital-CIM) | Verilog 实现的数字存内计算设计 | ![](https://img.shields.io/github/stars/qhy991/Digital-CIM?style=flat-square&label=&color=16213e) |
| [**Scientific-Figure-Design**](https://github.com/qhy991/Scientific-Figure-Design) | 论文级科研配图工具 | ![](https://img.shields.io/github/stars/qhy991/Scientific-Figure-Design?style=flat-square&label=&color=16213e) |

---

## 🧰 技术栈

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Triton](https://img.shields.io/badge/Triton-EE4C2C?style=flat-square&logo=openai&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-1F4E79?style=flat-square&logo=v&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![SGLang](https://img.shields.io/badge/SGLang-4B32C3?style=flat-square&logo=lightning&logoColor=white)
![llama.cpp](https://img.shields.io/badge/llama.cpp-000000?style=flat-square&logo=llama&logoColor=white)
![ROCm](https://img.shields.io/badge/ROCm-ED1C24?style=flat-square&logo=amd&logoColor=white)
![TVM](https://img.shields.io/badge/TVM-4285F4?style=flat-square&logo=apache&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</div>

---

## 📊 GitHub 数据

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=qhy991&theme=buefy" width="100%" alt="profile details" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=qhy991&theme=buefy" width="49%" alt="stats" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=qhy991&theme=buefy&utcOffset=8" width="49%" alt="productive time" />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=qhy991&theme=buefy" width="100%" alt="repos per language" />

</div>

---

<div align="center">

### 一起构建 AI 系统的下一层。

欢迎与在 AI—系统—硬件这条链路上工作的研究者和建设者交流。

<a href="https://qhy991.github.io/">个人主页</a> · <a href="https://scholar.google.com/citations?user=zzmYq9QAAAAJ&hl=en">Google Scholar</a> · <a href="mailto:haiyanq@buaa.edu.cn">邮箱</a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f3460,50:16213e,100:1a1a2e&height=100&section=footer" width="100%" alt="" />

</div>
