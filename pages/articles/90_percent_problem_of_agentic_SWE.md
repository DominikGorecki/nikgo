![Coding slice beside the broader software engineering task](./images/01__90_percent_problem_of_agentic_SWE.webp)

# The 90 Percent Problem of Agentic Software Delivery

*Coding agents look revolutionary in the demo. The real transformation begins when leaders stop measuring generated code and start redesigning the journey from intent to trusted release.*

The demo always knows where to aim the light.

A cursor blinks. The agent waits. A vague instruction becomes a plan, the plan becomes code, and the code appears in clean little bursts while the room performs its ritual of belief. As the founder smiles and the VP leans forward, someone says, "Ship it," before anyone has asked what the change will need to survive once it leaves the screen.

The ticket is still half-written. The architecture exception is still waiting for someone with the scars to make the call. The tests are green with the peculiar innocence of tests that have not yet met production. Down the hall, the release meeting is already gathering itself into being.

This is the seduction at the center of agentic software delivery. It turns the most theatrical slice of engineering into a stand-in for the whole machine.

The mirage is not that code is worthless. The mirage is that code is the bottleneck. A [Microsoft Research study](https://www.microsoft.com/en-us/research/publication/today-was-a-good-day-the-daily-life-of-software-developers/) of 5,971 developer self-reports found that developers spend surprisingly little time on development, and in a related discussion, Tom Zimmermann put code-writing at [66 minutes on a bad day and 96 on a good one](https://www.microsoft.com/en-us/research/podcast/the-productive-software-engineer-with-dr-tom-zimmermann/). The life-cycle view is wider still: SEBoK's summary of SWEBoK treats construction as one phase among analysis, design, testing, operation, maintenance, and end-of-life work [SEBoK](https://sebokwiki.org/wiki/Software_Engineering_in_the_Systems_Engineering_Life_Cycle). The 10 percent framing is a provocation, not a law, but the direction matters. Optimizing the typing slice while the rest of delivery keeps waiting in the hallway is not transformation. It is a brighter bulb over the most visible station.


The tools themselves already know this. GitHub describes [Copilot's cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) as work that can move through repository understanding, branch changes, pull requests, and outcome metrics. OpenAI describes [Codex](https://openai.com/index/introducing-codex/) as useful inside configured environments, checks, terminal output, and human review. Strip away the product names and the message is plain. The frontier is no longer keystrokes. It is the route by which a change becomes understood, argued over, proven, and trusted enough to release.

## The Old Queue

In the old model, the agent completes its assignment and the change begins its second life.

It waits.

It waits in the quiet jurisdictions that never appear in the demo. The reviewer opens the diff and has to rediscover the problem from the ticket, because the agent solved the words it was given, not the situation behind them. The green test run helps, but only a little. Someone still has to decide whether the checks cover the behavior customers will touch and whether this week's release can absorb one more surprise.

![Coding as one narrow slice of the software delivery lifecycle](./images/02__90_percent_problem_of_agentic_SWE.webp)

This is how acceleration becomes congestion. A pull request appears before the owner of the neighboring service has weighed in. CI fails for a reason nobody recognizes. The reviewer, already behind, reads the diff with the particular irritation reserved for work that looks finished while still asking to be understood.

Management sees motion in branches, pull requests, generated tests, apparent progress. But the delivery system feels heavier. The agent has removed labor from the beginning of the path and deposited ambiguity further down it. That does not mean the agents are overhyped. It means the management model is underdeveloped.

## The Delivery Control Plane

The better model begins earlier than the coding prompt and ends later than the pull request.

Before an agent writes code, it should carry the obligations of a careful engineer. It should learn why the request exists, find the old incident that explains the workaround, notice the service boundary, and understand the difference between the ticket and the business need.

As the work moves forward, that context should become evidence a reviewer can use. The green check should not be a talisman. The pull request should not be a sealed box. The diff should arrive with a case for itself: the intent, the risk, the tests, the limits of those tests, and the reason the change is safe enough to consider.

Call this the delivery control plane. Not a prettier coding harness. Not a better prompt library. A delivery control plane is the layer that makes the reason for the change, the danger inside it, and the proof around it travel with the work itself.

This is where agents become genuinely interesting. Not when they impersonate junior developers, but when they help the organization carry context forward instead of forcing humans to reconstruct it again and again. The real unit of work is not the prompt. It is not the diff. It is the trusted change.


## Measure the Flow

Once the work is framed this way, the dashboard has to change.

A leader who watches lines generated or agent-created pull requests is still staring at the coding station, dazzled by its little factory whistle, while the real story is moving somewhere else. Follow one change instead. Follow it from the first ambiguous request to the moment it is safely running in production. Watch where it hesitates, which evidence has to be rediscovered, and which assumptions collapse under contact with the system.

That is where the transformation is hiding. Not in the speed of code appearing, but in the speed with which the organization can turn an ambiguous request into a change it is willing to own.

A useful measurement system would feel less like a scoreboard and more like a flight recorder. It would show where the change came from, what it claimed to solve, which systems it touched, which checks ran, and why the work was allowed to proceed. Even GitHub's agent metrics point past raw code output toward pull-request outcomes such as PRs created, merged, and time to merge ([GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)). The point is to make the queue confess what kind of work it has been forced to hide.

DORA's research has been warning in the same direction. The [2024 Accelerate State of DevOps report](https://dora.dev/report/2024) found that AI can improve individual productivity while introducing tradeoffs in delivery stability and throughput. The [2025 DORA report announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) is blunter: AI amplifies what is already there. A companion guide on the [DORA AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/from-adoption-to-impact-putting-the-dora-ai-capabilities-model-to-work) makes the operational point hard to dodge. Value stream mapping keeps local AI gains from piling work up downstream.

The lesson for leaders is simple and uncomfortable. If the system cannot carry context, AI will amplify confusion.

## The ROI Trap

This is where the economics become anticlimactic.

A coding-speed program can produce real wins and still disappoint. That sounds contradictory only if code production is assumed to be the binding constraint. Microsoft's Copilot research deserves to be taken seriously: in a contained implementation task, developers using AI assistance finished [55.8 percent faster](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/). The warning is in the clean boundary around the experiment. A contained task is not an enterprise backlog.

In real organizations, the task begins as a customer complaint that may describe the symptom rather than the cause. It becomes a ticket written by someone who knows the business pain but not the system boundary. It moves into a codebase shaped by years of urgent compromises. It reaches a pull request whose reviewer has to infer not only what changed, but why this change is the right one. Then production gets its turn to ask for proof in its own dry language.

Spend the transformation budget on the typing moment, and the spreadsheet may show productivity while the product still waits for trust. This is the ROI trap. The tool did not fail. The theory of change failed.

The better ROI conversation starts with the backlog, not the license count. Pick one customer bug and follow it through the company. The obvious fix looks small until it crosses an old service boundary and nobody remembers why that boundary is there. By the time the pull request opens, the reviewer is not waiting for more code, but she is waiting for a reason to believe the change will not break production.

## What Leaders Should Do Instead

The practical move has almost no demo-room glamour. Pick one thin slice of work and walk it until it tells the truth.

![Agents participating across the full delivery lifecycle](./images/03__90_percent_problem_of_agentic_SWE.webp)

Choose a common path: a customer bug, a small feature, a dependency upgrade, a production incident follow-up. Map the journey from intent to release. Do not ask where the agent can write code. Ask where the organization loses context. Where does the reviewer have to infer the reason for the change? Where does release approval depend on memory rather than evidence?

Those are the places to aim the agent. Not at the glamorous center of the demo, but at the connective tissue of delivery: requirements clarification, codebase discovery, test selection, pull-request explanation, risk summaries, release notes, rollback plans, and post-release learning.

A useful pilot should be boring on purpose. Start with a bug in a mature service or a dependency upgrade that looks routine until it crosses the boundary between product and infrastructure. Ask the agent to build the case before it builds the patch. The first output should not be code. It should be a brief the reviewer can challenge: what behavior seems wrong, what old decision may explain it, and what evidence would make the change safe to consider.

Then measure what the work still forces humans to reconstruct. If the reviewer has to summon the engineer who remembers the old migration, the agent has not reached the bottleneck. If QA accepts the tests only after a private explanation, the evidence is still trapped in a person. The pilot succeeds when the change leaves fewer mysteries behind.

The companies that benefit most from agentic software delivery will not be the ones that treat agents as infinite junior developers. They will be the ones that rebuild delivery so agents can participate in the whole path from intent to proof. The demo will keep aiming the light at the cursor. That is where the magic is easiest to see. But the real transformation begins after the code appears, when the organization must decide whether the change deserves to live.

That is the 90 percent problem.
