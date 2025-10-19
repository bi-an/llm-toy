# AI工程化 / RAG应用路线学习计划（6个月）

## 🧭 目标定义

🎯 半年后，你要能独立开发一个“小型企业级AI知识问答系统”（带RAG、LangChain、向量数据库、接口服务）。
并能用这个项目投理想、小鹏、智元等公司的AI应用开发 / LLM平台工程师岗位。

---

## 🧩 六个月详细学习计划（含资源与项目）

### 📘 第1–2个月：AI应用开发基础 + Python实践

**目标:** 打通从Python编程 → AI应用框架 → 基础API的完整通路。

**学习内容:**

| 模块 | 内容 | 推荐资料 |
|------|-------|----------|
| Python复习 | 类、模块、异常、文件I/O、多线程 | [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/)；B站“Python工程化课程” |
| Python工程实践 | 虚拟环境、logging、requests、FastAPI | [FastAPI官方文档](https://fastapi.tiangolo.com/zh/) |
| LLM基础 | Prompt概念、API调用（OpenAI / 通义千问 / GLM） | [OpenAI Cookbook](https://github.com/openai/openai-cookbook)；[智谱AI文档](https://open.bigmodel.cn/dev/api) |

**实践任务:**
- 调用OpenAI或通义千问API，实现一个命令行对话程序
- 用FastAPI封装成本地聊天Web服务

---

### 📗 第3个月：RAG基础与向量数据库

**目标:** 理解并实现检索增强生成（RAG）核心流程。

**学习内容:**

| 模块 | 内容 | 推荐资料 |
|------|-------|----------|
| 向量化与检索 | Embedding概念、余弦相似度、Faiss、Milvus | [Faiss文档](https://faiss.ai/)、[Milvus文档](https://milvus.io/docs/) |
| RAG原理 | 检索+生成流水线、chunking策略、Embedding更新 | [LangChain RAG教程](https://python.langchain.com/docs/use_cases/question_answering/) |
| 框架实战 | LangChain + Milvus + OpenAI/GLM | LangChain官方example项目 |

**实践任务:**
- 构建一个文档问答系统（上传PDF → 向量化 → 模型回答）
- 示例结构：
```
user upload → split & embed → store in Milvus → query → LLM answer
```

---

### 📙 第4个月：AI服务工程化

**目标:** 学会将RAG系统包装成可部署服务（企业级结构）。

**学习内容:**

| 模块 | 内容 | 推荐资料 |
|------|-------|----------|
| 后端结构 | FastAPI项目架构、RESTful接口规范 | [FastAPI高级文档](https://fastapi.tiangolo.com/advanced/) |
| 缓存与并发 | Redis缓存、异步I/O | [Redis入门](https://redis.io/docs/)；Python asyncio |
| 部署 | Docker + Nginx + gunicorn 部署 | [Docker官方教程](https://docs.docker.com/get-started/) |

**实践任务:**
- 将RAG项目封装为RESTful服务
- 提供 `/upload` `/query` API
- 前端调用返回JSON
- Docker部署

---

### 📒 第5个月：增强功能 + 企业级特性

**目标:** 让项目能对标真实公司内部AI应用。

**学习内容:**

| 模块 | 内容 | 推荐资料 |
|------|-------|----------|
| 多模态接入 | 图像/OCR支持（百度API或PaddleOCR） | [PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR) |
| Agent设计 | LangChain Agent、Tool调用、记忆机制 | [LangChain Agents](https://python.langchain.com/docs/modules/agents/) |
| 模型管理 | 模型切换（GLM / Qwen / ChatGLM2） | 各模型API文档 |
| 向量数据库优化 | 批量插入、索引重建、TopK检索优化 | Milvus/Faiss官方优化指南 |

**实践任务:**
- 实现支持文档+图像问答的系统
- 加入记忆功能
- 可切换不同LLM（ChatGPT/GLM/Qwen）
- 优化检索性能

---

### 📘 第6个月：项目打磨 + 简历包装

**目标:** 项目能在简历中作为亮点展示，便于投AI应用岗位。

**学习内容:**

| 模块 | 内容 | 推荐资料 |
|------|-------|----------|
| 简历包装 | 如何写“AI应用开发”项目描述 | 自行总结，参考GitHub README写法 |
| 项目部署 | 云端部署（腾讯云 / 阿里云 / Render） | 云厂商文档 |
| GitHub优化 | Markdown文档、美化README、架构图 | [readme.so](https://readme.so) |
| 技术补充 | LangChain表达式语言、RAG评估 | LangChain blog文章 |

**实践成果:**
- 完成「企业知识库AI问答平台」
- 发布GitHub + README + 部署Demo
- 简历描述示例：
```
设计并实现基于LangChain+Milvus+LLM的企业知识问答平台，
支持文档解析、语义检索、上下文记忆与多模态输入，
实现从文档上传到智能问答的全流程工程化闭环。
```

---

## 📦 推荐学习资源合集

| 分类 | 推荐资源 |
|------|-----------|
| Python & FastAPI | [FastAPI官方文档](https://fastapi.tiangolo.com/zh/)、B站UP主“Python工程化指南” |
| LangChain | [LangChain官方文档](https://python.langchain.com/docs/get_started/introduction) |
| 向量数据库 | [Milvus文档](https://milvus.io/docs/) / [Faiss文档](https://faiss.ai/) |
| 项目参考 | GitHub：[langchain-chatchat](https://github.com/chatchat-space/Langchain-Chatchat)、[privateGPT](https://github.com/imartinez/privateGPT) |
| LLM调用 | [OpenAI Cookbook](https://github.com/openai/openai-cookbook)、[智谱AI开放平台](https://open.bigmodel.cn/dev/api) |

---

## ✅ 阶段成果总结

| 阶段 | 核心成果 |
|--------|----------------|
| 1–2月 | 会用Python + FastAPI + 调API |
| 3月 | 理解RAG并能构建文档问答 |
| 4月 | 将RAG系统服务化 |
| 5月 | 加多模态、记忆、模型切换等功能 |
| 6月 | 项目上线 + 简历优化 + GitHub展示 |
