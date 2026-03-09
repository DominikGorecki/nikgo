![Why Office Agents Shouldn’t Live a the Shell](./images/Why_Office_Agents_Shouldnt_Live_in_a_Shell_01.png)

# Why Office Agents Shouldn’t Live in a Shell

An executive assistant is trying to do what executive assistants do. She is sorting which messages matter, deciding which introductions are worth taking, noticing that a board member’s email should not sit unanswered until Thursday, seeing that two meetings can in fact become one, and preparing the briefing that will keep a harried Tuesday from turning into a small corporate fire. This is office work in its native form. It is made of people, promises, sensitivities, priorities, approvals, and timing.

Now picture that same work running through the mental furniture of a junior developer. Files. Folders. Connectors. Command output. Maybe a browser tab or two. Maybe some shell glue. Maybe a little `grep`-style rummaging through raw material. That is the oddity hiding in plain sight in the current agent boom. The industry’s most ambitious agents are still being asked to inhabit a machine world designed for software work first and everything else second. Anthropic describes Claude Code as a tool that reads your codebase, edits files, and runs commands, and describes Cowork as bringing those same agentic capabilities into knowledge work beyond coding ([Claude Code overview][1]; [Get started with Cowork][2]). ([Claude][1])

That made a certain sense when the frontier case for agents was writing code. It makes much less sense when the task is inbox triage, calendar negotiation, relationship filtering, approvals, or the small invisible choreography by which institutions stay upright. The problem is not merely that the interface looks technical. The problem is that the abstractions are wrong. For most knowledge work, the shell is the wrong action model, and the filesystem is the wrong memory model.

## The old desktop is sneaking into the future

The easiest way to miss this is to confuse connectivity with a real operating model. We have gotten very good at building bridges. Anthropic’s Model Context Protocol is an important one. It is an open protocol for connecting LLM applications to external data sources and tools, with explicit attention to transport, authorization, and integration ([Introducing the Model Context Protocol][4]; [MCP specification][5]). Connectors extend that idea further. Anthropic’s help docs describe connectors as a way for Claude to access apps, retrieve data, and take actions across connected services ([Use connectors to extend Claude’s capabilities][6]). ([Model Context Protocol][2])

Useful, yes. Sufficient, no.

A connector is not a theory of work. A protocol is not an ontology. If anything, the rush toward connectors has made the hidden assumption harder to see. We act as if enough pipes between the model and the tools will somehow produce a native environment for office cognition. But transport is not meaning. Access is not structure. A thousand integrations do not automatically add up to an operating system for delegated knowledge work.

You can see the distinction if you line up the layers cleanly. MCP and connectors are an access layer. Slack APIs and Microsoft Graph are vendor-specific semantic layers. They expose higher-level objects such as conversations, people, events, mail, files, and insights. Slack’s Conversations API explicitly unifies public channels, private channels, DMs, and more under one conversation model, while Microsoft Graph presents a single endpoint across Microsoft 365 data and services, including people and workplace intelligence ([Using the Conversations API][7]; [Microsoft Graph overview][12]). ([Slack Developer Docs][3])

That middle layer matters because it starts to look like the real shape of office work. It is already closer to how a human assistant thinks. The assistant is not thinking, “open file, parse buffer, execute command.” The assistant is thinking, “this thread is hot, that meeting should move, this person matters, that document is relevant because of this relationship, this reply should be drafted but not yet sent.” Those are semantic objects. Those are governed actions. Those are not shell primitives.

## The filesystem is a bad office memory

The more radical claim is not about action. It is about memory.

For decades, computing trained us to treat files and folders as the neutral substrate of serious work. That structure is so familiar it barely registers as a choice. But personal information management research has been pointing at the cracks for a long time. William Jones wrote that information fragmentation appears in several guises as a major, perhaps the major, problem of personal information management, with the information required for real tasks scattered across forms, tools, and locations ([Personal Information Management][8]). ([UW Libraries][4])

![FIles and Folders versus real work objects](./images/Why_Office_Agents_Shouldnt_Live_in_a_Shell_02.png)

Office work suffers from the same disease at institutional scale. The relevant context for a task is almost never in one place. Part of it is in email, part in chat, part in a calendar series, part in a meeting note, part in an older decision nobody wrote down cleanly, part in a senior person’s sense that “we do not escalate this kind of thing until legal sees it,” and part in the social fact that one stakeholder can be ignored for forty-eight hours while another cannot be ignored for forty-eight minutes. You can dump artifacts into folders all day long and still fail to capture the thing that actually matters.

This is why platforms have been quietly evolving away from the pure document metaphor. Slack does not merely expose messages. It exposes conversations. Its work-objects push goes further, treating files, tasks, and dashboards as contextual objects that carry discussion, edits, approvals, and sharing history with them ([Using the Conversations API][7]; [Slack Work Objects][10]). Microsoft Graph’s people and workplace intelligence APIs explicitly rank relevant people and documents based on contacts, directory information, and recent communication patterns ([People and workplace intelligence in Microsoft Graph][13]). ([Slack Developer Docs][3])

Those platforms are still incomplete, still vendor-bounded, still messy. But they are already telling us something important. The native objects of office work are not folders and shell commands. They are conversations, people, meetings, commitments, documents, approvals, and tasks, all threaded through context.

## What an agent-native office layer would actually do

Once you see the mismatch, the replacement starts to come into view. The right alternative is not “chat instead of GUI,” and it is not “a friendlier terminal.” It is a governed framework that unifies memory and action.

On the memory side, imagine a context bank that exists at three levels. Company-wide context stores policies, norms, recurring judgments, relationship maps, and strategic facts that ought not depend on one person’s memory. Function-wide context stores the local logic of finance, recruiting, sales, legal, support, whatever domain has its own exceptions and rhythms. Individual context stores personal working patterns, preferences, recurring task setups, and trusted ways of handling familiar situations. The point is not just storage. It is inspection, control, versioning, rollback, and evolution.

That idea is not as eccentric as it sounds. Research on organizational memory systems has long described these systems as supporting the acquisition, retention, storage, dissemination, and reuse of knowledge to improve decision-making and problem-solving ([Information Systems and Organizational Memory][11]). A related line of work on corporate memory argues that reusable knowledge requires access to the rich context in which that knowledge was created ([CoMem][14]). ([jistem.tecsi.org][5])

![The governed context bank](./images/Why_Office_Agents_Shouldnt_Live_in_a_Shell_03.png)

On the action side, the agent would operate through semantic calls over first-class work objects. Not “open file and scrape.” More like “find the highest-priority thread involving this customer over the last seven days,” “draft a reply in the principal’s voice but do not send,” “propose three meeting blocks that preserve the one-hour buffer before the board call,” “surface commitments that were made but not yet acknowledged,” “retrieve the last approved version of the recruiting rubric for this function,” “flag this introduction for human review because it touches a sensitive relationship.” Files might still exist. Commands might still exist. But they would be implementation details below the line, not the native language of office delegation.

That is the crucial shift. Once memory and action live in the same governed framework, the machine stops behaving like a general-purpose desktop that an agent happens to inhabit. It starts behaving like a work substrate.

## Narrower could be stronger

At first glance, this looks like a safety tax. A more constrained agent sounds like a weaker agent. In one sense, it is weaker. In another, it may be much more powerful.

A governed context bank would not just hold reference material. It could become a versioned operational memory for the firm. This is where institutional intelligence begins to accumulate in a form that is inspectable rather than folkloric. Why did this exception get approved last quarter? Which relationships require extra care? What language does the chief of staff prefer in delicate follow-ups? Which meeting prep pattern actually works for this executive? What counts as escalation in this function, and what merely counts as noise? The literature on organizational memory does not prove this exact architecture, but it strongly supports the broader premise that firms gain leverage when knowledge is retained, contextualized, and reusable rather than scattered across transient tools and private recollection ([Information Systems and Organizational Memory][11]; [CoMem][14]). ([jistem.tecsi.org][5])

There is also a quieter possibility. A semantic layer may reduce some of the pointless cognitive and token churn that today’s agents endure. That claim should be treated as a hypothesis, not a settled fact. But the intuition is straightforward. If an agent can call a high-level operation over the real object of work, it may spend less effort reconstructing intent from raw files, shell output, app chrome, and intermediate glue. You would want to benchmark that, not preach it. Still, the possibility matters because it hints that the tradeoff is not merely control versus capability. It may also be control plus compression in certain classes of work.

Most of all, a semantic layer changes what the company can actually govern. The real intellectual property of a modern firm increasingly lives not just in documents or codebases, but in the accumulated context that tells the system what matters, how judgment is applied, where exceptions live, and which actions require restraint. That is not a folder tree. That is an operating memory.

## The security case is stronger than the capability case

The cleanest argument for this model is not elegance. It is trust.

NIST defines least privilege as restricting access privileges to the minimum necessary to accomplish assigned tasks ([NIST least privilege][15]). Microsoft’s AppContainer guidance says isolation is the primary goal of the environment and that least-privilege access minimizes malicious manipulation by limiting what an application can touch ([AppContainer isolation][16]). Microsoft Graph’s permissions model makes the same lesson painfully concrete by separating delegated from app-only access and by routing broader permissions through admin consent and explicit governance ([Microsoft Graph permissions overview][17]; [Permissions and consent overview][18]). ([NIST CSRC][6])

This is what shell-native office agents get wrong. The shell is broad by default. Even when wrapped in policy, it begins from the premise that the agent can potentially do whatever the machine can do. That is not how enterprises think about sensitive office work. They think in scopes, approvals, audit trails, delegation, and rollback. They want draft-not-send, propose-not-commit, read-without-export, and approve-before-action. They want to know who authorized what, under which policy, with what visible provenance.

Current products already lean in that direction whenever they get close to real deployment. Anthropic’s Cowork asks users to choose which folders and connectors Claude can see, and its Google Workspace connectors require owners to enable them on Team and Enterprise plans before individual users authenticate ([Introducing Cowork][3]; [Use Google Workspace connectors][19]). ([support.claude.com][7])

That is not an accident. It is the market confessing what trust actually requires.

## The shell’s revenge

![The Tradeoff: governed layer versus raw shell](./images/Why_Office_Agents_Shouldnt_Live_in_a_Shell_04.png)

Now the hard part.

The shell remains seductive for one reason that matters more than all the others. It is complete. It lets the agent fall one level lower and improvise. Anthropic’s Claude Code docs make this plain. Direct shell commands, background tasks, hooks, plugins, and custom automation are not side features. They are the reason the system is so capable. When the model cannot find a semantic operation, it can still build, chain, or script its way forward ([Interactive mode][20]; [Claude Code hooks][21]). ([Claude][8])

Any semantic office layer inherits a brutal challenge from that fact. It must either anticipate enough of the world to stay useful or extend itself fast enough to stay relevant. The moment you add a plugin ecosystem to solve that problem, you reopen the attack surface you were trying to tame. Anthropic’s Desktop Extensions are a perfect little case study. They make local MCP servers dramatically easier to package and install, while simultaneously forcing enterprise controls into view through pre-installed approved extensions, blocklists, private extension directories, and the option to disable the public directory entirely ([Claude Desktop Extensions][22]). OWASP’s MCP Top 10 sharpens the warning by naming risks such as context spoofing, prompt-state manipulation, insecure memory references, and covert channel abuse in MCP-enabled systems ([OWASP MCP Top 10][23]). ([Anthropic][9])

So yes, the objection is real. A managed extension ecosystem can easily become a shell in a nicer suit. A semantic layer can lag reality. A company context bank can ossify into bureaucracy. None of that should be waved away.

But the presence of tradeoffs does not rescue the old model. It clarifies the contest. The question is not whether the shell is powerful. It plainly is. The question is whether the shell is the right primitive for delegated office work at all.

## The first agents enterprises trust will probably be narrower

This is where the article stops being a design essay and becomes a market argument.

A governed semantic layer may be less magical than open computer-use agents in the near term. It may do fewer surprising things. It may require more deliberate platform building. It may frustrate people who love the infinite adaptability of code and command lines. But it may also be the first form of agentic work that large organizations actually trust enough to deploy widely.

Look at the shape of the controls already appearing around the edges. Organization owners must enable certain connectors before users can authenticate them. Admin consent governs broad Microsoft Graph access. Enterprise controls around extensions now include approval, restriction, and private distribution ([Use connectors to extend Claude’s capabilities][6]; [Permissions and consent overview][18]; [Claude Desktop Extensions][22]). ([support.claude.com][10])

That is the tell. The industry is not moving toward unconstrained machine use for its most sensitive workflows. It is moving, however awkwardly, toward governed surfaces.

Return to the executive assistant. The real test is not whether a shell-native agent can, in principle, do more. The real test is whether a company would trust it with the quiet, continuous, politically sensitive work by which the place is actually run. If the answer is no, then the future of office agents will not belong to the most general system. It will belong to the system that can make delegated judgment legible, bounded, and reviewable without stripping it of usefulness.

That is a different contest from GUI versus chat. It is a more consequential one. The next operating system battle may not be about what humans click. It may be about what agents are allowed to mean.

## References

* [Claude Code overview][1]
* [Get started with Cowork][2]
* [Introducing Cowork][3]
* [Introducing the Model Context Protocol][4]
* [MCP specification][5]
* [Use connectors to extend Claude’s capabilities][6]
* [Using the Conversations API][7]
* [Personal Information Management][8]
* [Slack Work Objects][10]
* [Information Systems and Organizational Memory][11]
* [Microsoft Graph overview][12]
* [People and workplace intelligence in Microsoft Graph][13]
* [CoMem][14]
* [NIST least privilege][15]
* [AppContainer isolation][16]
* [Microsoft Graph permissions overview][17]
* [Permissions and consent overview][18]
* [Use Google Workspace connectors][19]
* [Interactive mode][20]
* [Claude Code hooks][21]
* [Claude Desktop Extensions][22]
* [OWASP MCP Top 10][23]

[1]: https://code.claude.com/docs/en/overview "Claude Code overview - Claude Code Docs"
[2]: https://support.claude.com/en/articles/13345190-get-started-with-cowork "Get started with Cowork | Claude Help Center"
[3]: https://claude.com/blog/cowork-research-preview "Introducing Cowork | Claude"
[4]: https://www.anthropic.com/news/model-context-protocol "Introducing the Model Context Protocol | Anthropic"
[5]: https://modelcontextprotocol.io/specification/2025-11-25 "Specification - Model Context Protocol"
[6]: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities "Use connectors to extend Claude's capabilities | Claude Help Center"
[7]: https://docs.slack.dev/apis/web-api/using-the-conversations-api/ "Using the Conversations API | Slack Developer Docs"
[8]: https://digital.lib.washington.edu/server/api/core/bitstreams/1842f30b-1e59-4637-bf46-28407323424a/content "Personal Information Management"
[10]: https://slack.com/integrations/work-objects "Work Objects: Bring Your Apps and Data into Slack | Slack"
[11]: https://jistem.tecsi.org/index.php/jistem/article/download/10.4301%252FS1807-17752015000100003/495 "Information Systems and Organizational Memory"
[12]: https://learn.microsoft.com/en-us/graph/overview "Microsoft Graph overview - Microsoft Learn"
[13]: https://learn.microsoft.com/en-us/graph/social-intel-concept-overview "People and workplace intelligence in Microsoft Graph - Microsoft Learn"
[14]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7468A6DE40C98D2BA8E48AE2FDAD6672/S0890060402163025a.pdf/comem_designing_an_interaction_experience_for_reuse_of_rich_contextual_knowledge_from_a_corporate_memory.pdf "CoMem: Designing an interaction experience for reuse of rich contextual knowledge from a corporate memory"
[15]: https://csrc.nist.gov/glossary/term/least_privilege "least privilege - NIST CSRC"
[16]: https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation "AppContainer isolation - Microsoft Learn"
[17]: https://learn.microsoft.com/en-us/graph/permissions-overview "Overview of Microsoft Graph permissions - Microsoft Learn"
[18]: https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview "Overview of permissions and consent in the Microsoft identity platform - Microsoft Learn"
[19]: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors "Use Google Workspace connectors | Claude Help Center"
[20]: https://docs.anthropic.com/en/docs/claude-code/interactive-mode "Interactive mode - Claude Code Docs"
[21]: https://docs.anthropic.com/en/docs/claude-code/hooks-guide "Automate workflows with hooks - Claude Code Docs"
[22]: https://www.anthropic.com/engineering/desktop-extensions "Claude Desktop Extensions: One-click MCP server installation for Claude Desktop | Anthropic"
[23]: https://owasp.org/www-project-mcp-top-10/ "OWASP MCP Top 10 | OWASP Foundation"
[1]: https://code.claude.com/docs/en/overview?utm_source=chatgpt.com "Claude Code overview - Claude Code Docs"
[2]: https://modelcontextprotocol.io/specification/2025-11-25?utm_source=chatgpt.com "Specification"
[3]: https://docs.slack.dev/apis/web-api/using-the-conversations-api/?utm_source=chatgpt.com "Using the Conversations API | Slack Developer Docs"
[4]: https://digital.lib.washington.edu/server/api/core/bitstreams/1842f30b-1e59-4637-bf46-28407323424a/content?utm_source=chatgpt.com "Personal Information Management"
[5]: https://jistem.tecsi.org/index.php/jistem/article/download/10.4301%252FS1807-17752015000100003/495?utm_source=chatgpt.com "INFORMATION SYSTEMS AND ORGANIZATIONAL MEMORY"
[6]: https://csrc.nist.gov/glossary/term/least_privilege?utm_source=chatgpt.com "least privilege - Glossary | CSRC"
[7]: https://support.claude.com/en/articles/13345190-get-started-with-cowork?utm_source=chatgpt.com "Get started with Cowork | Claude Help Center"
[8]: https://code.claude.com/docs/en/best-practices?utm_source=chatgpt.com "Best Practices for Claude Code"
[9]: https://www.anthropic.com/engineering/desktop-extensions?utm_source=chatgpt.com "One-click MCP server installation for Claude Desktop"
[10]: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities?utm_source=chatgpt.com "Use connectors to extend Claude's capabilities"
