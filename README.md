# Hi, I'm Assaf

I like building things that think. I created [GPT Researcher](https://github.com/assafelovic/gpt-researcher), co-founded [Tavily](https://tavily.com), which [Nebius acquired](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform) in 2026, and now I'm building [Ora](https://ora.ai) to make the web usable by AI agents.

You can find me at [assafe.com](https://assafe.com), on [X](https://x.com/assaf_elovic) and on [LinkedIn](https://www.linkedin.com/in/assafe).

## Featured repositories

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/assafelovic/gpt-researcher"><b>assafelovic/gpt-researcher</b></a><br/>
<sub>An autonomous agent that researches any topic across the web or your own documents and writes a detailed report with citations, using any LLM.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
</td>
<td width="50%" valign="top">
<a href="https://github.com/ora/ax"><b>ora/ax</b></a><br/>
<sub>Score any site's agent readiness from your terminal or CI. The open source command line tool for Ora.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/ora/ax?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript"/>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/assafelovic/gptr-mcp"><b>assafelovic/gptr-mcp</b></a><br/>
<sub>An MCP server that gives Claude, Cursor and other MCP clients deep research, quick search and report writing tools.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/assafelovic/gptr-mcp?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
</td>
<td width="50%" valign="top">
<a href="https://github.com/tavily-ai/tavily-python"><b>tavily-ai/tavily-python</b></a><br/>
<sub>The official Python SDK for Tavily's search, extract, crawl, map and research APIs.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/tavily-ai/tavily-python?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/assafelovic/skyll"><b>assafelovic/skyll</b></a><br/>
<sub>Helps agents like OpenClaw find and learn new skills on their own.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/assafelovic/skyll?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
</td>
<td width="50%" valign="top">
<a href="https://github.com/assafelovic/tovana"><b>assafelovic/tovana</b></a><br/>
<sub>A memory layer that helps AI agents give personal, context aware answers.</sub><br/><br/>
<img src="https://img.shields.io/github/stars/assafelovic/tovana?style=flat&logo=github&label=stars" alt="GitHub stars"/>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
</td>
</tr>
</table>

## What I'm building now

Most of my work has been about making machines useful to people. [Ora](https://ora.ai) flips that around: it checks how well AI agents can find, read and use a website, and we share what we learn in the open. The code is at [github.com/ora](https://github.com/ora).

- **[ax](https://github.com/ora/ax)** scores any site's agent readiness from your terminal or CI ([docs](https://ora.ai/docs#cli)).
- **[webmcp](https://github.com/ora/webmcp)** is a plugin for Claude Code, Codex and Cursor that adds [WebMCP](https://github.com/webmachinelearning/webmcp) tools to your site and checks that they work.
- **[research](https://github.com/ora/research)** has the datasets and scripts behind our agent readiness research.

## GPT Researcher

I started [GPT Researcher](https://github.com/assafelovic/gpt-researcher) in 2023 as the first open source deep research agent. You give it a question, it plans the research, reads dozens of sources in parallel and writes a report with citations. The community has kept improving it every week since.

To try it, start with the [quickstart](https://docs.gptr.dev/docs/gpt-researcher/getting-started/introduction) or install it from [PyPI](https://pypi.org/project/gpt-researcher). You can also connect it to your own agent with the [MCP server](https://docs.gptr.dev/docs/gpt-researcher/mcp-server/getting-started). Everything else is on [gptr.dev](https://gptr.dev) and [docs.gptr.dev](https://docs.gptr.dev), and you're welcome to say hi on [Discord](https://discord.gg/QgZXvJAccX).

## Cited in research

Carnegie Mellon's [DeepResearchGym](https://arxiv.org/abs/2505.19253) (May 2025) tested deep research systems on 1,000 complex questions. GPT Researcher came first, ahead of Perplexity, OpenAI, OpenDeepSearch and Hugging Face.

| Metric | GPT Researcher |
| --- | --- |
| Citation precision | 85.36% |
| Citation recall | 90.82% |
| Report clarity | 83.70% |
| Report insightfulness | 78.01% |
| Key point recall | 64.67% |

It also shows up in these papers:

1. [Deep Research Comparator: A Platform For Fine-grained Human Annotations of Deep Research Agents](https://arxiv.org/abs/2507.05495), Chandrahasan et al., July 2025
2. [Deep Researcher with Test-Time Diffusion](https://arxiv.org/abs/2507.16075), Han et al., Google, July 2025
3. [HLTCOE at LiveRAG: GPT-Researcher using ColBERT retrieval](https://arxiv.org/abs/2506.22356), Duh et al., Johns Hopkins HLTCOE, June 2025
4. [Chain of Ideas: Revolutionizing Research in Novel Idea Development with LLM Agents](https://arxiv.org/abs/2410.13185), Li et al., October 2024
5. [Providing domain knowledge for process mining with ReWOO-based agents](https://www.genai4pm2024.info/papers/ICPM_2024_paper_171.pdf), Vogt, van der Putten and Reijers, GenAI4PM at ICPM 2024
6. [BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science](https://arxiv.org/abs/2407.00466), Lin et al., July 2024
7. [LLM4DESIGN: An Automated Multi-Modal System for Architectural and Environmental Design](https://arxiv.org/abs/2407.12025), Chen et al., July 2024
8. [Differential Privacy of Cross-Attention with Provable Guarantee](https://arxiv.org/abs/2407.14717), Gu et al., July 2024
9. [Exploring Large Language Model based Intelligent Agents: Definitions, Methods, and Prospects](https://arxiv.org/abs/2401.03428), Cheng et al., January 2024
