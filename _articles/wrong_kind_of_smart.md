---
layout: article
title: "The Wrong Kind of Smart and the Most Expensive Model in the Room"
description: "Software teams should route model intelligence by the total expected cost of completing work, rather than treating either the strongest model or the cheapest token as the universal default."
permalink: /pages/articles/wrong_kind_of_smart.html
date: 2026-03-15
date_modified: 2026-07-17
last_modified_at: 2026-07-17
author: dominik-gorecki
content_id: wrong-kind-of-smart-model-routing
category: agentic-engineering
topics:
  - model-economics
  - software-development
  - ai-tokenomics
tags:
  - model-routing
  - llm-cost
  - software-engineering
  - ai-economics
image:
  path: /pages/articles/images/wrong_kind_of_smart_01.webp
  width: 800
  height: 320
  alt: "A costly AI model assigned to a trivial interface adjustment"
featured: false
article_type: blog-post
primary_question: "When is a more expensive model the wrong choice for a software task?"
evidence_type: "Author engineering analysis informed by cited model-economics research and a linked white paper."
key_limitation: "The routing framework is not a universal benchmark and requires task-specific evaluation."
related:
  - 90-percent-problem-agentic-delivery
  - vibe-coding-trap
  - bring-your-own-ai-leverage
  - ai-tokenomics-software-engineering
redirect_from: []
published: true
---

## Six pixels of whitespace

A software engineer opens an agentic coding tool, leaves the strongest model selected, and asks for a little more space between a form label and an input. Premium reasoning is now being billed to move the interface by six pixels. It is the digital equivalent of hiring a neurosurgeon to trim a hedge.

The few extra cents are not important by themselves. The absence of a decision rule is. The engineer has not really chosen a model; the default has carried an assumption into the work: strongest must be safest, and it is better to overbuy intelligence than risk coming up short.

That instinct is understandable, but it is too crude for the way software teams are beginning to use agents. Model choice is becoming an operational decision rather than a personal preference. The relevant question is not which model looks smartest in isolation. It is which choice minimizes the total cost of finishing the work well.

## The wrong kind of smart

Discussions about coding models often settle into two camps: use the best model you can afford, or minimize model spend wherever possible. Neither position captures the economics of software work.

A model call has a visible price. It appears on a dashboard and can be budgeted. The less visible costs arrive afterward. A weak first pass can lead to retries, failed tests, human cleanup, delayed merges, and design mistakes that become tomorrow’s technical debt. A cheap call can therefore be an expensive way to finish a task, while a premium call can occasionally be the economical choice.

Recent evaluation research makes this distinction explicit. *Economic Evaluation of LLMs* argues that model comparisons should include the consequences of error, latency, and abstention, not just benchmark scores and token prices ([1]). *Cost-of-Pass* asks what it costs to obtain a correct result rather than what it costs to make one attempt ([2]). The practical lesson is straightforward: the cheapest token does not necessarily produce the cheapest completed task.

## Tokens are not the whole bill

This is not an argument for penny-pinching. It is an argument for counting the whole loop: retries, repair, verification, and the human attention needed to catch an answer that is polished and plausible but still wrong. It also includes the extra time a branch remains open because the first pass was close enough to keep but not correct enough to ship.

One paper on agentic software engineering illustrates the point. In ChatDev traces from 30 development tasks, iterative review and verification—not the first draft—dominated token use. Code review consumed the largest share ([3]). Generation attracts attention because it is visible, but much of the real cost sits in rereading, reprompting, testing, patching, and reviewing almost-right output. Software work is a loop, not a single call.

## A better map of the work

![A better map of the work](./images/wrong_kind_of_smart_02.webp)

To reason about that loop, teams need a better way to describe the work itself.

Labels such as small, big, easy, and hard collapse distinctions that matter. A tiny change can be difficult to reason about, while a change across many files can be conceptually simple and repetitive.

A useful way to split the problem comes from the white paper behind this article, *AI Tokenomics for Software Engineering: A Practical Economic Model for Iterative Model Routing* ([5]). It decomposes software work into two dimensions: context complexity and output scope.

In plain English, it asks two questions: How hard is the task to understand, and how much needs to change?

That distinction does real work. A three-line fix can be high complexity and low scope if it requires tracing state across a large system. A broad migration can be low complexity and high scope if the reasoning is simple and the changes are repetitive. The whitespace tweak from the opening scene is genuinely low on both. A new feature that touches business logic, persistence, UI states, and tests is high on both.

Seen this way, model choice becomes a classification problem rather than an IQ contest.

## The tiny tweak and the serious feature

Take the tiny tweak first. The label is too close to the input. The desired change is obvious. Verification is cheap. Failure is visible. If the model does something silly, the engineer can notice and fix it quickly. This is the kind of task where premium reasoning can be pure theater. It may work beautifully, but so might something much cheaper.

Now take the serious feature. A new workflow threads through several abstractions, touches API behavior, updates tests, and introduces enough complexity that a plausible-looking solution can be dangerous. Here the economics change. A bad first pass can create rework, confuse reviewers, and leave behind ugly architecture that someone else later has to unwind.

This does not imply that the strongest model should always handle serious work. It means different cost regimes exist. In some, a mid-tier model plus an inexpensive repair is the better option. In others, paying more up front is rational because failure is costly. Teams need to learn which regime a task belongs to.

## A hypothetical ledger

Consider a deliberately hypothetical comparison.

Task A is the UI spacing tweak. A premium model costs more and succeeds more often. A mid-tier model costs less and misses a bit more often. But failure is cheap. Verification takes seconds. Repair is trivial. Over many tasks of this kind, the cheaper model can easily be the better economic choice.

Task B is a feature touching persistence, permissions, and a user-facing workflow. The premium model again costs more. But now failure means more model calls, more human review, retesting, and a higher chance of shipping a bad abstraction. In that setting, the cheaper upfront choice can become the expensive one.

The numbers will vary by team, workflow, and toolchain. The answer depends on direct model cost, probability of success, and the consequences of failure, so teams need their own measurements rather than a universal slogan.

## What today’s habits become tomorrow’s systems

This matters for a reason larger than prompt thrift.

Software teams are moving toward agentic systems that will plan, generate, verify, repair, and escalate across the whole idea-to-shipping loop. When that happens, model routing stops being a personal habit and becomes infrastructure. Someone, or something, will decide which model handles which task, when to retry, when to escalate, and when to stop.

If teams do not understand the economics of these choices now, they will build future routers on superstition. The superstition may take two opposite forms. One is prestige: always send hard work to the strongest model because nobody gets fired for buying premium cognition. The other is austerity: always start cheap because token dashboards are visible and engineering drag is harder to price. Both are bad foundations for automated orchestration.

There is already a research lineage for more disciplined routing. *FrugalGPT* showed early that adaptive selection and cascades could cut cost sharply while preserving performance on some tasks ([4]). The white paper behind this article extends that logic into software engineering by treating routing as an iterative economic problem, not a one-shot query problem ([5]).

The shift is from choosing models by feel to routing them by an explicit policy.

## The operating model

The immediate lesson is not to impose a rigid playbook. It is to become more observant.

![The operating model](./images/wrong_kind_of_smart_03.webp)

Thoughtful teams should experiment with model choice by task type. They should notice where weaker models create cheap, acceptable misses and where they create expensive downstream chaos. They should distinguish task difficulty from task size. They should treat verification cost as part of the task, not as an afterthought. They should stop treating the strongest default as neutral.

Defaults encode a policy even when nobody has written it down. Always selecting the most expensive model reveals one assumption; watching only token spend reveals another. In both cases, the team has yet to develop a useful economic model for AI-assisted software work.

That is normal. It should not remain normal for long.

Access to strong models will not distinguish software teams for long. Pricing will change and today’s brand hierarchy will move. Operating logic is more durable. Teams should learn to route models deliberately now, because their informal defaults will become the basis of tomorrow’s orchestration layer.

## Read the full technical white paper this is based on

For the formal version of this argument, including the decomposition of work into context complexity and output scope, the pricing of failure, and the move from one-step routing to iterative rerouting, see [the full white paper][5].

## References

1. [Economic Evaluation of LLMs][1]
2. [Cost-of-Pass: An Economic Framework for Evaluating Language Models][2]
3. [Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering][3]
4. [FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance][4]
5. [AI Tokenomics for Software Engineering: A Practical Economic Model for Iterative Model Routing][5]

[1]: https://arxiv.org/abs/2507.03834 "Economic Evaluation of LLMs"
[2]: https://arxiv.org/abs/2504.13359 "Cost-of-Pass: An Economic Framework for Evaluating Language Models"
[3]: https://arxiv.org/abs/2601.14470 "Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering"
[4]: https://arxiv.org/abs/2305.05176 "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance"
[5]: https://nikgo.com/pages/articles/SWE_LLM_Tokenomecs_V2.pdf "AI Tokenomics for Software Engineering: A Practical Economic Model for Iterative Model Routing"
