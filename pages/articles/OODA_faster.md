# The Companies That OODA Faster

There is a very soothing executive fantasy about AI. Buy the copilots. Run the pilots. Form the steering committee. Measure “productivity uplift.” Roll the tools out department by department. Let the organization absorb the future in neat, tasteful increments.

That fantasy is dying.

The real divide in 2026 is not between companies that “have AI” and companies that do not. It is between companies that move through reality faster than their rivals and companies that are still trapped in the old rhythm of reports, meetings, handoffs, approvals, and the ceremonial forwarding of PDFs. The decisive advantage is OODA velocity: observe, orient, decide, act. John Boyd’s point was simple and nasty. The side cycling through the loop faster does not just move sooner. It leaves the opponent reacting to a world that no longer exists ([USNI Proceedings][1]).

That is what agentic AI changes.

Look at the recent cadence out of Anthropic. In February 2026 it moved from Claude Opus 4.6 to Sonnet 4.6, then into broader enterprise workflow expansion through Cowork and plugins, plus deeper computer-use capability through its Vercept acquisition, all in a matter of weeks ([Anthropic Newsroom][2]; [Cowork and Plugins][3]). Reuters reported the market’s answer in cold blood: major software and services stocks got hit as investors absorbed what faster, more capable AI could do to legacy software economics ([Reuters][4]).

This was not just a story about model quality. It was a story about loop speed.

Most companies still use AI like a power tool. Helpful, local, impressive in demos. But a company that merely bolts AI onto existing workflows stays slow in all the old places. It still notices problems late. It still orients through fragmented human meetings. It still decides after delay. It still acts through ticket queues and managerial ceremony.

An agentic company does something else. It turns the whole enterprise into a tighter organism.

Observe becomes always-on sensing. Agents ingest product telemetry, customer complaints, repo activity, pipeline changes, vendor signals, policy updates.

Orient becomes structured synthesis. Anthropic’s own engineering guidance gets at the heart of it: the real challenge is not prompt engineering but context engineering, assembling the right memory, tools, and state for the task at hand ([Effective Context Engineering][5]).

Decide becomes ranked options instead of blank-page deliberation.

Act becomes execution. Code gets written. Tests run. documents drafted. Workflows updated. Humans still matter, but they are no longer spending their best hours reconstructing context from scratch.

Picture two companies facing the same churn problem. The first notices it in a monthly review, commissions analysis, debates causes, aligns next steps, and begins implementation several weeks later. The second sees the signal as it emerges, correlates support transcripts with product behavior, generates fixes, tees up the best option for approval, and ships a controlled change that afternoon.

Same market. Same model access. Different species of company.

The practical question, of course, is how a large organization does this without collapsing into chaos. The answer is not one more chatbot. It is a system.

First, you need orchestration: Bedrock Agents, Azure AI Foundry, something that can coordinate models, tools, and actions at enterprise scale ([Amazon Bedrock Agents][6]; [Microsoft Foundry][7]). Second, you need retrieval across the real company, not just clever prompting: data connectors, grounded access, permissions, actual institutional visibility ([Amazon Bedrock Knowledge Bases][8]). Third, you start with narrow use cases, but build them so they can spread.

Then comes the real moat: the Company Context Bank.

Without a durable memory layer, enterprise AI is just a string of expensive amnesias. The Context Bank is a living, versioned, queryable memory system: company strategy at the top, function workflows beneath that, team norms below that, individual preferences below that still. Stored in plain files. Versioned in Git. Retrieved in slices. An agent working on a release does not need the whole company stuffed into its prompt. It needs the relevant security policy, the engineering workflow, the team’s norms, and the task owner’s standing preferences. Progressive disclosure exists for exactly this reason: bring in the right layer at the right time, not the whole attic at once ([Progressive Disclosure][9]).

This is the shift. AI is no longer just software you use. It is becoming infrastructure you circulate through.

And that creates a harsh new corporate divide. On one side: firms with AI tools in tabs. On the other: firms with agentic flow in their veins and institutional memory in their bones. Boyd’s old law still rules. The side that cycles faster wins.

The question is whether your company will be the one disorienting the market, or the one staring at it, slightly dazed, while the world changes shape again.

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
