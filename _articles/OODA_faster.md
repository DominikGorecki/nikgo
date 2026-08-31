---
layout: article
title: "The Companies That OODA Faster"
description: "Competitive advantage comes from OODA velocity: continuously observing, orienting, deciding, and acting through governed agents and durable organizational context rather than isolated copilots."
permalink: /pages/articles/OODA_faster.html
date: 2026-03-27
date_modified: 2026-07-17
last_modified_at: 2026-07-17
author: dominik-gorecki
content_id: companies-that-ooda-faster
category: agentic-engineering
topics:
  - ai-agents
  - organizational-systems
  - software-development
tags:
  - ooda-loop
  - agentic-enterprise
  - context-engineering
  - organizational-memory
image:
  path: /pages/articles/images/OODA_faster_01.webp
  width: 800
  height: 450
  alt: "Companies competing by completing the OODA loop faster"
featured: true
feature_group: general
feature_order: 9
article_type: blog-post
primary_question: "How can organizations make better decisions faster when AI changes the pace of engineering work?"
evidence_type: "Author analysis using the OODA-loop metaphor and cited management and technology sources."
key_limitation: "The article does not establish a causal estimate for AI's effect on organizational performance."
related:
  - 90-percent-problem-agentic-delivery
  - office-agents-semantic-layers
  - market-for-portable-minds
redirect_from: []
published: true
---

The standard corporate AI rollout is reassuringly familiar: buy some copilots, run a few pilots, appoint a steering committee, measure the “productivity uplift,” and expand department by department. It is a sensible way to control risk. It may also be far too slow for what is happening.

In 2026, the useful distinction is not between companies that have AI and companies that do not. Nearly everyone has access to similar tools. The more consequential difference is how quickly a company notices a change, understands it, makes a decision, and follows through. That is OODA velocity: observe, orient, decide, act. John Boyd’s insight was that cycling through this loop faster does more than save time. It can leave an opponent responding to conditions that have already changed ([USNI Proceedings][1]).

Agentic AI matters because it can shorten each part of that loop, not merely help an individual employee finish a task faster.

Anthropic’s release cadence offers a recent example. In February 2026 it moved from Claude Opus 4.6 to Sonnet 4.6, expanded enterprise workflows through Cowork and plugins, and added computer-use capability through its Vercept acquisition, all within weeks ([Anthropic Newsroom][2]; [Cowork and Plugins][3]). Reuters reported a selloff in major software and services stocks as investors reconsidered the economics of legacy software businesses ([Reuters][4]). The individual announcements mattered, but so did the speed at which capabilities were accumulating.

Most companies still use AI as a local power tool. That can make an employee faster without making the organization much faster at all. Problems are still noticed late, context is reconstructed across meetings, decisions wait for several approvals, and action disappears into ticket queues.

An agentic operating model connects those stages instead of optimizing them one at a time.

Observation becomes continuous. Agents can monitor product telemetry, customer complaints, repository activity, pipeline changes, vendor signals, and policy updates.

![Fast OODA Loop](./images/OODA_faster_02.webp)

Orientation becomes structured synthesis. Anthropic’s engineering guidance calls this context engineering: assembling the memory, tools, and state a task actually requires ([Effective Context Engineering][5]). Decisions can begin with ranked options and explicit tradeoffs instead of a blank page. Action can include writing code, running tests, drafting documents, and updating workflows. Humans still make the consequential calls, but they spend less time rebuilding the background needed to make them.

Consider two companies facing the same churn problem. One notices it in a monthly review, commissions an analysis, debates the causes, agrees on next steps, and begins implementation several weeks later. The other catches the signal as it emerges, connects support transcripts with product behavior, prepares possible fixes, sends the strongest option for approval, and ships a controlled change that afternoon. The advantage does not come from exclusive access to a model. It comes from the way the company is organized around it.

The practical problem is doing this without creating chaos. Another chatbot will not solve it. Companies need orchestration that can coordinate models, tools, and actions at enterprise scale, whether through Bedrock Agents, Azure AI Foundry, or a comparable system ([Amazon Bedrock Agents][6]; [Microsoft Foundry][7]). They also need governed retrieval across real company information: data connectors, grounded access, and permissions, not just better prompts ([Amazon Bedrock Knowledge Bases][8]). The first use cases should be narrow, but their foundations should be reusable.

The most durable part of that foundation is what I call a Company Context Bank.

![Company Context Bank](./images/OODA_faster_03.webp)

Without durable memory, each AI workflow starts by rediscovering the company. A Context Bank would be a living, versioned, queryable memory system: company strategy at the top, functional workflows beneath it, then team norms and individual preferences. It could live in plain files, be versioned in Git, and be retrieved in small, relevant slices. An agent preparing a release does not need the entire company in its prompt. It needs the applicable security policy, engineering workflow, team conventions, and task owner’s standing preferences. Progressive disclosure is the discipline of supplying those layers when they become relevant ([Progressive Disclosure][9]).

At that point, AI is no longer a tool sitting in a browser tab. It becomes part of how information and work move through the company.

This creates a less dramatic but more useful dividing line. Some firms will give employees AI tools while preserving the same slow operating system. Others will build institutional memory and connect observation to action. Boyd’s principle still applies: the organization that completes the loop faster has the advantage. The question for executives is whether their AI program is improving that loop or merely adding a faster tool to one step inside it.

## References

* [USNI Proceedings][1]
* [Anthropic Newsroom][2]
* [Cowork and Plugins][3]
* [Reuters][4]
* [Effective Context Engineering][5]
* [Amazon Bedrock Agents][6]
* [Microsoft Foundry][7]
* [Amazon Bedrock Knowledge Bases][8]
* [Progressive Disclosure][9]

[1]: https://www.usni.org/magazines/proceedings/2020/june/warfighting-demands-better-decisions
[2]: https://www.anthropic.com/news
[3]: https://claude.com/blog/cowork-plugins-across-enterprise
[4]: https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/
[5]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[6]: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
[7]: https://learn.microsoft.com/en-us/azure/foundry/
[8]: https://aws.amazon.com/bedrock/knowledge-bases/
[9]: https://docs.claude-mem.ai/progressive-disclosure
