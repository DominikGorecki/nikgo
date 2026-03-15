# The Wrong Kind of Smart

# The Most Expensive Model in the Room

## Six pixels of whitespace

A software engineer opens an agentic coding tool, leaves the strongest model selected by default, and asks it to add a little more space between a form label and an input field.

That is the scene. Not a thorny migration. Not a production incident. Not a grand demonstration of machine intelligence. A few pixels of whitespace.

And yet there it is: premium reasoning, meter running, the digital equivalent of hiring a neurosurgeon to trim a hedge.

The issue is not the few extra cents. The issue is the missing decision rule. The engineer is not really choosing a model. The engineer is inheriting a mood. Strongest must be safest. Most expensive must be best. Better to overbuy intelligence than come up short.

That instinct is understandable. It is also too crude for the world software teams are entering. Model choice is becoming an operational decision, not a personal quirk. Once that happens, the question changes. The real question is not which model looks smartest in isolation. It is which model choice minimizes the total cost of getting the work done.

## The wrong kind of smart

The usual debate around coding models swings between two shallow instincts. One says use the best model you can afford. The other says squeeze cost wherever you can. Both miss the real economics of software work.

A model call has a visible price. That part is easy. It shows up on a dashboard. It can be multiplied, budgeted, and argued over in a meeting.

But the model call is not the whole event. A weak first pass can trigger retries, repair, failed tests, human cleanup, delayed merges, and subtle distortions that become tomorrow’s tech debt. The cheap answer can turn out expensive. The premium answer can turn out cheap. What matters is not the sticker price of cognition. What matters is the total expected cost of completion.

That is the shift recent economic-evaluation papers are trying to force into view. *Economic Evaluation of LLMs* argues that models should be judged in economic terms, not just by benchmark quality or raw token cost, and explicitly prices the consequences of error, latency, and abstention in dollars ([1]). *Cost-of-Pass* makes a related move, asking what it actually costs to obtain a correct result rather than merely a cheap attempt ([2]).

The broad lesson is simple enough to state and still strangely rare in practice: the cheapest token is not always the cheapest decision.

## Tokens are not the whole bill

People hear “economic framing” and assume the point is penny-pinching. It is not. The point is to count the whole loop.

The bill includes retries. It includes repair. It includes verification. It includes the human attention required to notice that the model has produced something polished, plausible, and wrong in a way that is annoying rather than dramatic. It includes the extra time a branch stays open because the first pass was close enough to tempt you, but not correct enough to ship.

One recent paper on agentic software engineering makes this concrete. Studying ChatDev traces across 30 software-development tasks, the authors found that token use was dominated not by the first draft, but by iterative review and verification. Code review consumed the largest share of tokens, which is exactly what you would expect in a world where generation is cheap and consequence is not ([3]).

That matters because it punctures a comforting fantasy. The fantasy is that cost lives in the dramatic moment when the machine writes the code. In practice, much of the cost lives in the tail: rereading, reprompting, testing, patching, reviewing, and cleaning up after almost-right output.

Software work is not a single call. It is a loop.

## A better map of the work

To reason about that loop, teams need a better way to describe the work itself.

The usual labels are too mushy. Small task. Big task. Easy. Hard. These categories blur things that should be separated. A task can be tiny in surface area and still cognitively nasty. A task can touch many files and still be conceptually simple.

A useful way to split the problem comes from the white paper behind this article, *AI Tokenomics for Software Engineering: A Practical Economic Model for Iterative Model Routing* ([5]). It decomposes software work into two dimensions: context complexity and output scope.

In plain English, that means two different questions. First, how hard is the task to understand? Second, how much actual change does the task require?

That distinction does real work. A three-line fix can be high complexity and low scope if it requires tracing state across a large system. A broad migration can be low complexity and high scope if the reasoning is simple and the changes are repetitive. The whitespace tweak from the opening scene is genuinely low on both. A new feature that touches business logic, persistence, UI states, and tests is high on both.

Once you see work that way, model choice stops looking like an IQ contest. It becomes a classification problem.

## The tiny tweak and the serious feature

Take the tiny tweak first. The label is too close to the input. The desired change is obvious. Verification is cheap. Failure is visible. If the model does something silly, the engineer can notice and fix it quickly. This is the kind of task where premium reasoning can be pure theater. It may work beautifully, but so might something much cheaper.

Now take the serious feature. A new workflow threads through several abstractions, touches API behavior, updates tests, and introduces enough complexity that a plausible-looking solution can be dangerous. Here the economics change. A bad first pass can create rework, confuse reviewers, and leave behind ugly architecture that someone else later has to unwind.

That does not prove “always use the strongest model.” It proves something more interesting: there are different regimes. In some, a mid-tier model plus cheap repair wins. In others, paying more upfront is rational because failure is expensive.

The whole point is to learn which regime you are in.

## A hypothetical ledger

Consider a deliberately hypothetical comparison.

Task A is the UI spacing tweak. A premium model costs more and succeeds more often. A mid-tier model costs less and misses a bit more often. But failure is cheap. Verification takes seconds. Repair is trivial. Over many tasks of this kind, the cheaper model can easily be the better economic choice.

Task B is a feature touching persistence, permissions, and a user-facing workflow. The premium model again costs more. But now failure means more model calls, more human review, retesting, and a higher chance of shipping a bad abstraction. In that setting, the cheaper upfront choice can become the expensive one.

These numbers will vary by team, workflow, and toolchain. That is the point. The answer depends on the interaction between direct model cost, probability of success, and the cost of failure. Teams need experimentation, not slogans.

## What today’s habits become tomorrow’s systems

This matters for a reason larger than prompt thrift.

Software teams are moving toward agentic systems that will plan, generate, verify, repair, and escalate across the whole idea-to-shipping loop. When that happens, model routing stops being a personal habit and becomes infrastructure. Someone, or something, will decide which model handles which task, when to retry, when to escalate, and when to stop.

If teams do not understand the economics of these choices now, they will build future routers on superstition. The superstition may take two opposite forms. One is prestige: always send hard work to the strongest model because nobody gets fired for buying premium cognition. The other is austerity: always start cheap because token dashboards are visible and engineering drag is harder to price. Both are bad foundations for automated orchestration.

There is already a research lineage for more disciplined routing. *FrugalGPT* showed early that adaptive selection and cascades could cut cost sharply while preserving performance on some tasks ([4]). The white paper behind this article extends that logic into software engineering by treating routing as an iterative economic problem, not a one-shot query problem ([5]).

That is the real shift underway. We are moving from taste-based prompting to policy-based orchestration.

## The operating model

The immediate lesson is not to impose a rigid playbook. It is to become more observant.

Thoughtful teams should experiment with model choice by task type. They should notice where weaker models create cheap, acceptable misses and where they create expensive downstream chaos. They should distinguish task difficulty from task size. They should treat verification cost as part of the task, not as an afterthought. They should stop treating the strongest default as neutral.

Defaults are never neutral. They are philosophy wearing sweatpants.

If the default model is always the most expensive, that tells you something. If the only metric anyone watches is token spend, that tells you something too. In both cases, the team is admitting that it does not yet know how to think economically about machine intelligence in software work.

That is normal. It should not remain normal for long.

The next generation of software teams will not be separated simply by who has access to the strongest models. Access commoditizes. Pricing shifts. Brand hierarchies wobble. What lasts is operating logic. The teams that matter will be the ones that learn how to route intelligence with discipline, because today’s model defaults are tomorrow’s orchestration layer.

## Read the full technical white paper this is based on

For the formal version of this argument, including the decomposition of work into context complexity and output scope, the pricing of failure, and the move from one-step routing to iterative rerouting, see ([5]).

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
