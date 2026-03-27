# AI in the Veins: How Agentic Companies Use the OODA Loop to Leave Competitors Disoriented

The comforting boardroom story about AI goes like this: buy a few copilots, run a handful of pilots, appoint a steering committee, measure productivity gains, then slowly spread the tools across the enterprise. It is the managerial fantasy of control. It is also, by now, obsolete.

What matters in 2026 is not whether your company has access to frontier models. Plenty of companies do. What matters is whether your organization can cycle through reality faster than its rivals: see sooner, make sense sooner, decide sooner, ship sooner. In military language, whether it can move through the OODA loop faster: observe, orient, decide, act. John Boyd’s point was not that speed alone wins, but that faster, better loops leave the opponent responding to a world that has already changed ([USNI Proceedings][4]). ([usni.org][1])

That is what many executives still miss about agentic AI. They are treating it as a tool acquisition problem, when it is really an organizational velocity problem.

You could see the difference in February 2026. Anthropic moved from Claude Opus 4.6 on February 5 to Sonnet 4.6 on February 17, then to Cowork-and-plugins updates for enterprise teams on February 24, followed the next day by its Vercept acquisition to deepen computer-use capability ([Anthropic Newsroom][1]; [Claude Opus 4.6][17]; [Claude Sonnet 4.6][16]; [Cowork and Plugins][12]; [Vercept Acquisition][18]). Over roughly three weeks, the company did not merely release models. It signaled a whole direction of travel: better coding, better long-context reasoning, better computer use, more role-specific enterprise agents, more workflow reach. At the same time, Reuters reported that software and services stocks had shed about $830 billion in market value over six trading days by February 4, with the latest selloff linked to fears stirred by Anthropic’s legal tooling and accelerating AI disruption ([Reuters on Software Selloff][2]; [Reuters on Anthropic Upgrade][3]). ([Reuters][2])

That was not just a model story. It was a speed story.

## Speed Is the Strategy Now

Most executives still talk about AI in the vocabulary of capability. Which model is strongest? Which vendor is safest? Which team has the best prompts? Those questions matter, but they are not the decisive ones. The decisive question is whether the organization itself has become fast enough to exploit machine intelligence as part of its operating rhythm.

A traditional company observes the world in batches. The signal arrives through quarterly reviews, weekly dashboards, Monday meetings, handoffs, escalations, and PowerPoint decks built to survive committee life. Orientation happens in fragments. Marketing has one picture, operations another, product a third, finance a fourth. Decisions get made after synthesis meetings. Action comes later still, once tickets are written, owners assigned, dependencies sorted, approvals gathered, and the calendar eventually permits movement.

That company can own the same model access as its rival and still lose badly.

An agentic company does something else. It turns the firm into a tighter organism. Signals are ingested continuously. Emerging patterns are synthesized across functions while they are still fresh. Options are ranked before the meeting invite is even sent. Low-risk actions are executed automatically. Higher-risk ones arrive at humans already structured, evidenced, and staged for judgment. The result is not simply “doing AI.” It is compressing the distance between noticing and shipping.

This is why OODA matters more now than it did when executives mostly used it as a strategy-conference metaphor. Boyd’s loop was always about disorientation. The side moving faster does not just move first. It changes the environment faster than the other side can model it. The lagging side starts acting on stale assumptions. It thinks it is competing in the present while actually fighting the recent past ([USNI Proceedings][4]). ([usni.org][1])

In business, that is what a genuinely agentic company can now do to a slower rival. Not because it has a magical AI brain. Because its idea-to-shipping loop has become unnervingly short.

## From Four Stages to One Organism

The easiest way to understand agentic AI is to stop picturing a chatbot in a browser tab and start picturing a circulatory system.

Observe becomes an always-on sensing layer. Agents watch product telemetry, support logs, CRM changes, security events, procurement signals, repository activity, competitor announcements, and regulatory updates. Nothing waits politely for next Tuesday’s status review.

Orient becomes structured synthesis. Anthropic’s own engineering material makes a crucial distinction here: prompt engineering is no longer enough; context engineering is the real task, the ongoing curation of the right state, tools, instructions, memory, and external data for the next model step ([Effective Context Engineering][5]). Orientation, in other words, is not a human-only act anymore. It is a managed system of context assembly. ([Anthropic][3])

Decide becomes ranked choice, not blank-page deliberation. The agents do not replace judgment. They narrow the field, surface tradeoffs, attach evidence, and tee up decisions at the right level of human review. Some decisions still deserve a person. Many never deserved a committee.

Act becomes execution, not memo distribution. Code gets written, tests run, documents routed, forecasts refreshed, tickets opened, knowledge updated, vendors pinged, customers notified, staging environments prepared. The gap between “we should” and “it is done” begins to collapse.

Picture two companies facing the same problem: churn is spiking among mid-market customers because onboarding is confusing.

The first company, the familiar one, notices the pattern in a monthly review. An analyst is asked to pull the numbers. Customer success adds anecdotes. Product schedules research. Marketing disputes the framing. Engineering asks for a written proposal. Two weeks later there is alignment on the need for action. Four weeks later there is a draft plan. Six weeks later somebody starts implementing.

The second company sees the churn signal as it emerges. Agents correlate product-dropoff events with support transcripts and CRM notes. They identify three onboarding failure clusters and model likely fixes. A ranked recommendation lands with the VP of Product before lunch, along with projected impact, required copy changes, UI diffs, and a tested rollout plan. A human approves the top option. The variant ships to 15 percent of affected accounts that afternoon.

Same market. Same abstract “AI capability.” Different loop.

That is the divide that matters.

## The Four-Step Shift From AI Tools to Agentic Flow

The good news is that this is not reserved for frontier labs. The infrastructure is now widely available. The bad news is that many companies are still using it as if it were just a nicer chatbot wrapper.

The rollout model is conceptually simple.

### Start with orchestration, not chat

An enterprise needs a substrate that can coordinate models, tools, data sources, and actions. AWS says Bedrock Agents orchestrate interactions among foundation models, data sources, software applications, and conversations, while automatically invoking APIs and knowledge bases as needed ([Amazon Bedrock Agents][8]). Microsoft describes Foundry as an “AI app and agent factory” for building, governing, and operating AI apps and agents at scale ([Microsoft Foundry Docs][10]). ([AWS Documentation][4])

That matters because the leap is not from one chatbot to a better chatbot. It is from isolated conversations to orchestrated work.

### Connect the company, not just the prompt

The next requirement is comprehensive retrieval across the organization’s real data. Bedrock Knowledge Bases explicitly supports grounding agents on private enterprise data, with connectors for sources such as S3, Confluence, Salesforce, SharePoint, and web crawlers, plus support for structured sources and reranking ([Amazon Bedrock Knowledge Bases][9]). Microsoft’s Foundry IQ makes a similar pitch: one entry point for grounding agents on multiple data sources with built-in access permissions ([Azure AI Foundry][11]). ([Amazon Web Services, Inc.][5])

This is the first place many AI programs quietly fail. They try to get intelligence without plumbing. But a firm cannot become faster by asking a model to guess around the edges of inaccessible institutional knowledge. It has to let the model see, within permissions, the actual moving parts of the company.

### Launch narrow use cases, but design for reuse

This is where discipline matters. Do not begin with “AI transformation.” Begin with one painful loop: support triage, vendor review, underwriting prep, postmortem drafting, onboarding QA, contract routing, internal research, bug-fix generation. But choose the use case so that the components can generalize.

That is precisely where the market is moving. Anthropic’s enterprise messaging now emphasizes plugins and role-specific agents, not generic assistants. Its Cowork update says plugins can turn Claude into specialized agents for every role and department and be distributed through private marketplaces across the organization ([Cowork and Plugins][12]). The open-source knowledge-work-plugins repository is even more explicit: plugins tell Claude how work should be done, what tools and data to pull from, and which critical workflows and commands to expose, so teams get more consistent outcomes ([Knowledge Work Plugins Repo][13]). TechCrunch described the February push as Anthropic’s most aggressive move yet to integrate enterprise agents into everyday workplaces ([TechCrunch on Enterprise Agents][14]). ([Claude][6])

In other words, the winning path is not “one dazzling demo.” It is a set of reusable agentic patterns that can spread.

### Then build the memory layer

This is where most initiatives stall, because this is where the company has to admit something uncomfortable: the real bottleneck is not inference. It is organizational memory.

## The Company Context Bank

Call it a Company Context Bank, a memory lattice, an institutional memory layer, whatever you like. The name matters less than the function. Every enterprise that wants durable agentic flow needs a living, versioned, queryable long-term memory system that survives across sessions, teams, and time.

Without it, you do not have agentic scale. You have a series of expensive amnesias.

Anthropic’s documentation already points toward the ingredients. Its context-engineering guidance argues that context is finite and must be curated carefully because too much irrelevant state degrades performance ([Effective Context Engineering][5]). Claude-Mem’s documentation frames progressive disclosure as the cure for context pollution: show lightweight metadata first, fetch details only when needed, then read source files only for deeper dives ([Progressive Disclosure][6]). Claude Code’s memory system distinguishes among organization-level, project-level, and user-level instruction files, and notes that more specific locations take precedence while subdirectory instructions can load on demand ([Claude Code Memory][7]). ([Anthropic][3])

That combination suggests the shape of a practical enterprise memory system.

Not one giant prompt. Not one bloated wiki. Not one vector index swallowing every document in sight. A layered memory bank, stored in plain files, versioned in Git or a Git-like system, organized by scope, and retrieved dynamically according to relevance and permission.

At the top sits company-level guidance: strategy, risk posture, brand rules, operating principles, approved vendors, escalation rules, security constraints. Below that come function-level workflows: sales qualification logic, finance review standards, engineering release norms, HR process rules. Below that come team patterns: how Team X runs incident review, how Team Y writes customer summaries, what “done” means in a specific product area. Below that come individual preferences and task-specific notes.

One illustrative structure might look like this:

`/company/strategy.md`
`/company/risk/compliance.md`
`/sales/pipeline/review-rules.md`
`/engineering/platform/release-workflow.md`
`/engineering/team-x/incident-patterns.md`
`/individual/jane-doe/preferences.md`

The point is not that this exact tree is sacred. It is that the memory is hierarchical, scoped, versioned, inspectable, and retrievable in slices.

So when an engineering agent works on a deployment workflow, it does not drag in the entire company’s memory. It pulls the company-wide security policy, the engineering release standard, the relevant team workflow, and maybe the task owner’s preferences. When a finance agent prepares board materials, it retrieves the current reporting conventions, last-quarter narrative guidance, and the CFO’s standing preferences, not the front-end team’s test strategy.

That is how you avoid context bloat. You do not solve it by hoping bigger windows make discipline unnecessary. You solve it by giving the agents a memory architecture that mirrors the company’s actual structure.

And because the files are versioned, the memory becomes governable. Proposed changes can be drafted by agents, reviewed by humans, promoted upward when they prove durable, and rolled back when they do not. What was once tribal knowledge becomes a living system of record.

This is the moat most executives are not yet talking about. Not model access. Memory coherence.

## The Friction Is Real, but the Path Is Straight

The objections come fast.

This only works for AI-native companies.

No. AI-native companies feel faster because they adopted the habits earlier, not because they possess secret physics. The core pieces are already mainstream: agent orchestration in Bedrock and Foundry, enterprise grounding layers, role-specific plugin patterns, and explicit memory systems ([Amazon Bedrock Agents][8]; [Microsoft Foundry Docs][10]; [Azure AI Foundry][11]; [Cowork and Plugins][12]). ([AWS Documentation][4])

Context bloat and versioning complexity will kill it.

Only if you build the memory layer carelessly. Anthropic’s own guidance warns that context is a finite resource. Progressive disclosure exists precisely because dumping everything into the model is sloppy engineering, not sophistication ([Effective Context Engineering][5]; [Progressive Disclosure][6]). ([Anthropic][3])

It is too expensive or culturally disruptive.

Compared with what, exactly? A company that still burns senior time on context reconstruction, repetitive analysis, stale dashboards, duplicated decisions, and handoffs that exist solely because the organization cannot remember itself? Anthropic’s December 2025 survey of more than 500 technical leaders found that 57 percent of organizations were already deploying agents for multi-stage workflows, and 80 percent reported measurable economic returns from agent investments ([How Enterprises Are Building AI Agents][15]). The real question is no longer whether agentic systems can create value. It is whether leadership can reorganize work fast enough to capture it. ([Claude][7])

The cultural piece is the hardest, but also the most clarifying. A Company Context Bank forces an enterprise to articulate how it actually works, which rules are real, which are folklore, which preferences deserve promotion, and which should stay local. It turns “how we do things here” from a whisper network into infrastructure.

Imagine a VP of Engineering watching an internal agent revise a deployment workflow. The agent notices recurring rollback friction, compares recent incident notes against release procedures, proposes a tighter checklist, updates the team-level draft memory, and opens a review for promotion. Nobody had to hold a special summit to discover the pattern. Nobody had to start from zero. The organization learned in public, in version control, and in a form future agents can use.

That is what maturity starts to look like.

## The Choice Is Becoming Brutally Clear

The next few years will produce a new corporate divide.

On one side will be companies that bought AI features. They will have copilots in tabs, pilots in decks, and impressive demos in town halls. Their people will still spend too much time hunting context, rebuilding the same knowledge, waiting on handoffs, and moving through slow, human-gated loops. They will mistake AI presence for AI integration.

On the other side will be companies that rebuilt their operating rhythm around agentic flow. They will treat AI less like software you use and more like infrastructure you circulate through. They will orchestrate models, tools, memory, and human judgment as one system. They will keep a living context bank. They will retrieve the right slice of institutional memory at the right moment. They will close the gap between observation and action until competitors start looking strangely clumsy.

Boyd’s old truth has not changed. The side that cycles through the loop fastest wins. What has changed is the mechanism. In an age of agentic AI, the fastest loop belongs to the company that has put intelligence in the veins and memory in the bones.

That choice is still available.

Not for long.

## References

* [Anthropic Newsroom][1]
* [Reuters on Software Selloff][2]
* [Reuters on Anthropic Upgrade][3]
* [USNI Proceedings][4]
* [Effective Context Engineering][5]
* [Progressive Disclosure][6]
* [Claude Code Memory][7]
* [Amazon Bedrock Agents][8]
* [Amazon Bedrock Knowledge Bases][9]
* [Microsoft Foundry Docs][10]
* [Azure AI Foundry][11]
* [Cowork and Plugins][12]
* [Knowledge Work Plugins Repo][13]
* [TechCrunch on Enterprise Agents][14]
* [How Enterprises Are Building AI Agents][15]
* [Claude Sonnet 4.6][16]
* [Claude Opus 4.6][17]
* [Vercept Acquisition][18]

[1]: https://www.anthropic.com/news
[2]: https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/
[3]: https://www.reuters.com/business/retail-consumer/anthropic-releases-ai-upgrade-market-punishes-software-stocks-2026-02-05/
[4]: https://www.usni.org/magazines/proceedings/2020/june/warfighting-demands-better-decisions
[5]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[6]: https://docs.claude-mem.ai/progressive-disclosure
[7]: https://code.claude.com/docs/en/memory
[8]: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
[9]: https://aws.amazon.com/bedrock/knowledge-bases/
[10]: https://learn.microsoft.com/en-us/azure/foundry/
[11]: https://azure.microsoft.com/en-us/products/ai-foundry
[12]: https://claude.com/blog/cowork-plugins-across-enterprise
[13]: https://github.com/anthropics/knowledge-work-plugins
[14]: https://techcrunch.com/2026/02/24/anthropic-launches-new-push-for-enterprise-agents-with-plugins-for-finance-engineering-and-design/
[15]: https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026
[16]: https://www.anthropic.com/news/claude-sonnet-4-6
[17]: https://www.anthropic.com/news/claude-opus-4-6
[18]: https://www.anthropic.com/news/acquires-vercept
[1]: https://www.usni.org/magazines/proceedings/2020/june/warfighting-demands-better-decisions "Warfighting Demands Better Decisions | Proceedings - June 2020 Vol. 146/6/1,408"
[2]: https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/ "Selloff wipes out nearly $1 trillion from software and services stocks as investors debate AI's existential threat | Reuters"
[3]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents "Effective context engineering for AI agents \ Anthropic"
[4]: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html "Automate tasks in your application using AI agents - Amazon Bedrock"
[5]: https://aws.amazon.com/bedrock/knowledge-bases/ "Foundation Models for RAG - Amazon Bedrock Knowledge Bases - AWS"
[6]: https://claude.com/blog/cowork-plugins-across-enterprise "Cowork and plugins for teams across the enterprise | Claude"
[7]: https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026 "How enterprises are building AI agents in 2026 | Claude"
