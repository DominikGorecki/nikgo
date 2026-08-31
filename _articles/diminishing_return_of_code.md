---
layout: article
title: "The Diminishing Returns of Code"
description: "AI coding tools can create far more code without producing proportional gains in releases, customer usage, revenue, or economic value."
permalink: /pages/articles/diminishing_return_of_code.html
date: 2026-08-28
date_modified: 2026-08-28
last_modified_at: 2026-08-28
author: dominik-gorecki
content_id: diminishing-returns-of-code
category: agentic-engineering
topics:
  - software-development
  - ai-agents
  - organizational-systems
tags:
  - developer-productivity
  - ai-coding
  - software-economics
  - product-strategy
image:
  path: /pages/articles/images/01__diminishing_return_of_code.webp
  width: 800
  height: 450
  alt: "A torrent of code narrowing through successive gates into a small stream of realized value"
featured: false
article_type: essay
primary_question: "Why does a large increase in AI-assisted coding produce much smaller gains in releases, usage, and economic value?"
evidence_type: "Author economic analysis supported by cited software-engineering, product, and market research."
key_limitation: "The article synthesizes emerging aggregate evidence and does not establish a universal conversion rate from code to economic value."
related:
  - 90-percent-problem-agentic-delivery
  - vibe-coding-trap
  - wrong-kind-of-smart-model-routing
redirect_from: []
published: true
---

*Why 180% more coding becomes 30% more releases—and, so far, no detectable increase in usage.*

In 2026, three researchers examined the public histories of more than 100,000 GitHub developers to see what changed as the developers adopted progressively more capable AI coding tools.

The first number looked magnificent. Once autocomplete, synchronous agents, and autonomous agents were combined, coding activity measured through commits increased by roughly **180%**.

Then the researchers followed that productivity miracle up the corporate staircase.

The same developers worked on about **50% more projects**, but shipped only **30% more releases**. Across four major software marketplaces, the supply of new applications increased while early aggregate usage remained flat or declined. For synchronous coding agents alone, the collapse was even more theatrical: a greater-than-sevenfold increase in lines of code became a 65% increase in pull requests and a 20% increase in releases ([Mert Demirer, Leon Musolff, and Liyuan Yang][1]).

None of this means AI coding tools do nothing. A 30% increase in releases would be extraordinary for almost any workplace technology. The steam engine did not arrive with a pull-request dashboard.

It does show something more interesting:

> **The economic value of additional code diminishes as it moves through the business.**

The machine wrote much more code. More software made it out the door, but nowhere near proportionally. The market barely noticed.

AI had not failed. It had encountered the rest of the system.

## Code was never the product

The software industry has spent decades treating the activity of engineering as if it were the output of the business.

Commits are counted. Pull requests are counted. Tickets are counted. Story points are estimated with the serene confidence of medieval astronomers measuring the distance to heaven.

Customers, however, do not buy commits.

They buy some outcome produced by software:

* less work,
* less risk,
* more money,
* more entertainment,
* faster communication,
* better decisions,
* access to other people,
* or the ability to do something that was previously impossible.

Code is an intermediate good. It is one input in a long production chain:

**Code → Shipped capabilities → Customer value and engagement → Revenue → Economic value**

Every arrow is a conversion, and every conversion loses something.

Some code never survives review. Some reviewed code never ships. Some shipped features are barely discovered. Others are tried once, politely ignored, and left to spend eternity beneath the “More” menu. A heavily used feature may generate no additional revenue; new revenue may bring so much infrastructure, support, acquisition, and maintenance cost that profit quietly slips out the back door.

This is why “AI can produce three times as much code” is not equivalent to “AI can produce three times as much business.”

It is like announcing that a restaurant has tripled the speed at which it chops onions. Wonderful! The dining room still has forty seats.

## Why companies do not employ infinite programmers

Before AI, every software company had already settled on some rough equilibrium of engineering capacity.

Not a perfect equilibrium. Companies overhire, underhire, panic-hire, perform ceremonial layoffs, and occasionally reorganize the same people into a new shape in the hope that geometry will improve revenue.

Still, beneath the noise, there is a real economic boundary.

A company benefits from adding engineering capacity while the expected marginal value of that capacity exceeds its fully loaded cost. In the simplified textbook version, firms hire until the marginal revenue produced by another worker approaches the marginal cost of employing that worker ([OpenStax][2]).

For an engineer, that cost is not merely salary and benefits. It also includes:

* recruitment and onboarding,
* management,
* coordination,
* infrastructure,
* review capacity,
* organizational communication,
* additional technical complexity,
* and the opportunity cost of deciding what the engineer should do.

Ronald Coase’s theory of the firm begins from a related observation: organizations exist because coordination through markets is costly, but coordination inside a company is not free either. As a firm expands, the work of organizing it becomes another cost ([R. H. Coase][3]).

The first few engineers at a software startup may create the entire product. The next group may establish payments, mobile applications, analytics, security, and operational reliability. The hundredth engineer may unlock an enterprise market.

The thousandth may add a fourth way to configure notification preferences for regional administrators in Portugal.

That final feature might be useful. Portugal is a real place. Regional administrators have feelings. But the expected value of that project is unlikely to equal the value of building the original product.

Companies generally attempt their most promising known opportunities first. As their engineering capacity expands, they move progressively farther down the project list:

1. Build the thing customers desperately need.
2. Build the thing customers strongly want.
3. Build the thing a valuable segment requested.
4. Build the thing that might improve retention by half a percentage point.
5. Build the thing someone mentioned during a quarterly planning workshop and nobody had the social courage to remove.

There, in the planning spreadsheet between item four and item five, is diminishing marginal return in its natural habitat.

## AI changes the price of code, not the demand for value

AI introduces a supply shock by reducing the cost of producing candidate software changes. Work that once required days may require hours. Projects that were too expensive become affordable. Experiments that would never have passed a cost-benefit review suddenly clear the bar.

There is good evidence that this first-order productivity gain is real. Three randomized field experiments at Microsoft, Accenture, and an anonymous Fortune 100 company, covering 4,867 developers, found that access to an AI coding assistant increased completed tasks by about 26% overall. Less experienced developers adopted the tool more heavily and experienced greater gains ([Kevin Zheyuan Cui and colleagues][4]).

The effect is not universal. A much smaller randomized study by METR found that sixteen experienced open-source developers working in mature repositories took 19% longer when allowed to use early-2025 AI tools. The developers nevertheless believed AI had made them faster. The study was narrow, and METR explicitly warned against generalizing it to all software work. Still, it demonstrates that productivity depends on the developer, repository, task, and amount of context the tool must reconstruct ([Joel Becker and colleagues][5]).

We need not resolve that debate to see the larger effect. Take the optimistic case and assume AI sharply reduces implementation costs.

The company can now afford to build more.

But the newly affordable projects are not random draws from the same pool as the old ones. They are disproportionately the projects that failed the previous economic threshold: too narrow, uncertain, expensive, difficult to maintain, or simply less important than the work already approved.

Lowering the cost of implementation therefore does two things at once:

* it increases the total number of worthwhile projects;
* it reduces the expected value of the marginal project.

These are not contradictory.

A company can create more total value while receiving less value from each additional unit of software.

Diminishing returns does not mean **no returns**. It means the next scoop is less nutritious than the last.

## The first tollbooth: code becomes features

The first major loss occurs between writing code and shipping a capability.

AI-generated code must still be:

**understood → reviewed → integrated → tested → secured → deployed → operated**

Speed up the first stage and the rest become painfully visible.

This is the organizational version of Amdahl’s law. In computing, the maximum improvement to a system is constrained by the portion that remains unimproved. Make one component infinitely fast and the rest of the system becomes infinitely irritating ([Gene Amdahl][6]).

Software organizations are more flexible than processors. They can redesign workflows, add automation, change architecture, and reassign people. The near-term logic is still the same: if coding becomes three times faster while review and integration remain unchanged, the company has not created three times the throughput.

It has created a queue.

Michael Kremer’s O-ring model offers another useful lens. In a process made of complementary tasks, failure or weakness in one stage can sharply reduce the value created by excellence elsewhere ([Michael Kremer][7]). Software is full of these complements. Brilliant code that cannot be safely integrated is not partially valuable. It is waiting.

That is what the large GitHub study appears to capture. AI sharply increased activity at the bottom of the production hierarchy, but the gains contracted as changes moved through pull requests, projects, and releases. The researchers concluded that the binding constraint was migrating toward the human-intensive stages of review, integration, testing, and release ([Mert Demirer, Leon Musolff, and Liyuan Yang][1]).

AI may therefore make individual programmers locally more productive while making the surrounding system more congested. Ten agents can produce code astonishingly quickly; the organization can still understand only so much of what it now owns.

![Generated code piling up at human review and delivery checkpoints](./images/02__diminishing_return_of_code.webp)

## Code is an output—and an inventory

There is another problem with treating code production as ordinary productivity: code does not disappear after it is produced.

It remains.

Every additional capability may need to be maintained, tested, secured, documented, monitored, supported, upgraded, migrated, and eventually removed. Code is today’s output and an invoice sent to the future.

This makes software different from many other generated artifacts. An unused marketing draft can be discarded. An unused line of production code may sit inside a critical system for twelve years, quietly waiting for the exact combination of inputs that turns it into an incident.

A large Google study covering more than 1,200 projects and 7,200 developer survey responses found that greater architectural complexity was associated with more code being devoted to bug fixing rather than feature development ([Yuanfang Cai and colleagues][8]). Separate Google research found that improvements in perceived code quality tended to precede improvements in developer productivity, rather than productivity improvements reliably producing better code quality afterward ([Lan Cheng and colleagues][9]).

The implication is unpleasant but simple:

> **More code can reduce the future productivity of the people responsible for it.**

At first, the marginal value of code is positive and enormous. Later, the marginal line creates less customer value while adding roughly the same maintenance obligations. Eventually, the curve can cross zero: the new capability creates less value than the complexity, support, security, and coordination burden it introduces.

The marginal return is no longer merely diminishing. It is negative.

This is why developer-productivity researchers have repeatedly warned against using a single activity measure as productivity. The SPACE framework treats developer productivity as multidimensional, encompassing performance, satisfaction, activity, communication, and flow. Lines changed and commits created tell us that something happened. They do not tell us whether the thing was good ([Nicole Forsgren and colleagues][10]).

A developer who deletes 20,000 unnecessary lines may create more enterprise value than an agent that generates 200,000 new ones. The diff will look less impressive. The company will be healthier.

## The second tollbooth: features become engagement

Suppose the code survives.

It is reviewed, tested, released, and proudly announced in a Slack channel with seventeen celebration emojis. Now it must become customer value.

The earliest features of a product usually address broad, intense demand. A navigation application gives directions. A payment system transfers money. A communication product lets people communicate. Later features tend to address narrower segments, rarer circumstances, or smaller inconveniences.

This does not make them useless. Mature products often derive enormous value from serving edge cases, satisfying regulatory requirements, improving accessibility, or completing a bundle required by enterprise customers.

But under ordinary prioritization, the highest-value opportunities are used up first. The hundredth feature is more likely than the first to serve a smaller group, solve a weaker problem, or compete with functionality already present.

Then comes feature fatigue.

Research by Debora Thompson, Rebecca Hamilton, and Roland Rust found that consumers often prefer feature-rich products before using them because the features signal capability. After using them, usability matters more. The result is that consumers can select products whose complexity ultimately reduces satisfaction and customer lifetime value. The researchers’ model implied an optimal number of features—not an everlasting ascent toward a settings menu with its own municipal government ([Debora Thompson, Rebecca Hamilton, and Roland Rust][11]).

Real software releases often fail to produce visible customer effects. A study of 26,339 Google Play releases found that only 33% caused a statistically significant change in user ratings. Even that figure includes changes in either direction; statistically detectable does not necessarily mean delightful ([William Martin, Federica Sarro, and Mark Harman][12]).

Ratings are not a complete measure of value. Some releases reduce infrastructure costs, address security flaws, satisfy legal requirements, or improve outcomes too subtle to appear in app-store reviews.

Still, the finding punctures a comforting management fiction:

> Shipping a feature does not mean the customer received value.

Once a product becomes sufficiently complex, adding functionality can reduce engagement by making the core product harder to understand.

The new feature must now compete for:

* interface space,
* user attention,
* documentation,
* onboarding time,
* conceptual simplicity,
* and the customer’s limited willingness to learn how your company has chosen to organize buttons.

When implementation was expensive, cost imposed a crude form of discipline. Many questionable features died because nobody could justify the engineering effort. As implementation approaches abundance, that restraint disappears.

The organization must learn to say no on purpose.

## The third tollbooth: engagement becomes revenue

Even meaningful engagement is not money.

Consider a fixed-price subscription product. A customer who uses the application twice as much may pay exactly the same monthly fee. The additional engagement might improve retention or create an upgrade opportunity. It might instead double the company’s compute and support costs.

For an advertising business, greater engagement can create more inventory—but only until additional advertisements degrade the experience, reduce consumption, or push users toward paid subscriptions or the exit.

For a marketplace, browsing matters only insofar as it produces transactions.

For a usage-priced product, consumption may convert more directly into revenue, but customers still have budgets, alternatives, and declining incremental needs.

The relationship depends on the business model and the customer’s position on the demand curve. There is no universal exchange rate between minutes and dollars.

Research on social-media brand engagement found exactly this kind of nonlinear relationship. Greater engagement volume remained positively associated with brand attachment, attitudes, and purchase intentions, but the incremental benefit declined at higher levels. Variety of engagement helped, but simply maximizing the quantity of likes, comments, and posts ran into diminishing returns ([Tobias Schaefers and colleagues][13]).

A large Pandora experiment provides a more concrete view of the monetization problem. Researchers varied advertising load for more than seven million users over eighteen months. The changes affected listening, advertising revenue, and subscription behaviour differently, and on different timelines. Personalizing ad allocation increased subscription profits by 7% without reducing advertising profits—evidence that value came from allocating engagement and monetization intelligently, not simply maximizing either one ([Ali Goli, David Reiley, and Hongkai Zhang][14]).

Engagement is not the economic endpoint. It is another intermediate good. Revenue is not the endpoint either; the final destination is some measure of economic value such as contribution profit, cash flow, customer lifetime value, strategic advantage, or enterprise value.

A product can produce more usage and more revenue while destroying money with tremendous energy.

## One small function

The argument requires very little mathematics. One nested function will do:

$$
\text{Economic Value}
=
V(R(E(F(C))))
$$

Where:

* \(C\) is code,
* \(F\) is shipped functionality,
* \(E\) is customer engagement or value,
* \(R\) is revenue,
* and \(V\) is economic value after costs.

Each stage transforms the output of the previous one. A large gain at the beginning must survive every subsequent conversion. If additional code produces fewer incremental capabilities, additional capabilities produce less incremental engagement, and additional engagement produces less incremental revenue, the losses compound.

Every stage gets a veto.

Then the company must subtract the carrying cost of the code it added: maintenance, incidents, infrastructure, support, security, and the friction imposed on future changes.

This is why a 180% increase at the bottom of the chain can become 30% near the middle and disappear into statistical silence at the top.

The arithmetic is less calculus than plumbing. Value leaks.

## Cheap production creates a glut

Software is not the only market showing this pattern.

Between 2022 and late 2025, monthly book releases roughly tripled as large language models spread. Average usage and quality indicators—including ratings received, sales rankings, and average star ratings—deteriorated. AI-containing books were used less, and by 2025 they represented more than half of new releases in the researchers’ sample.

Yet the result was not purely negative. The number of modestly used books increased, suggesting some long-tail benefit. The researchers estimated that AI books created additional consumer surplus, but only modestly relative to the explosion in supply ([Imke Reimers and Joel Waldfogel][15]).

It is almost a laboratory model of the coming software economy:

* production becomes cheap;
* supply explodes;
* average usage declines;
* some previously uneconomic niches become viable;
* total value increases much less than total output.

There are more artifacts, more experiments, and more obscure needs served.

There is also more sludge.

The same pattern appears in the software-marketplace data. New applications increased, including a near doubling of monthly new iOS apps between early 2025 and April 2026. But early engagement with each monthly cohort was flat or declining across the marketplaces studied, and a larger share of new applications failed to reach even a modest audience ([Mert Demirer, Leon Musolff, and Liyuan Yang][1]).

When the cost of creation falls, production expands. Customer attention does not automatically expand with it.

AI can produce another thousand applications before lunch. It cannot manufacture another thousand mornings in which customers are eager to learn them.

![Abundant software artifacts overwhelming a marketplace with limited customer attention](./images/03__diminishing_return_of_code.webp)

## Diminishing returns are not destiny

There is a strong objection to this argument: perhaps the current attenuation is temporary.

General-purpose technologies rarely produce their full economic effect immediately. Firms must reorganize, retrain workers, change processes, create complementary infrastructure, and invent new business models. Erik Brynjolfsson, Daniel Rock, and Chad Syverson describe this as a productivity J-curve: early investments in a transformative technology may be poorly measured, or may initially consume resources, before their benefits appear in conventional productivity statistics ([Erik Brynjolfsson, Daniel Rock, and Chad Syverson][16]).

AI coding may follow this pattern.

Today, AI accelerates generation while humans remain responsible for most review, integration, testing, release, product selection, and customer discovery. Tomorrow, AI may accelerate those stages too.

Code-review agents may reduce verification costs. Test agents may improve coverage. Deployment agents may lower release friction. Product agents may identify demand. Support agents may reduce the cost of owning another feature. Better architecture and smaller modules may allow changes to move independently.

There is already evidence that downstream automation can improve the broader system. A study of more than 4,500 GitHub repositories and 280,000 issues estimated that GitHub Actions accelerated issue resolution by 10.1%, saving an average of 4.3 days per issue. The measured speed gains did not come with a detected reduction in project quality, and different forms of automation proved useful for maintenance and new development ([Ao Huang, Ni Huang, and Yili Hong][17]).

This does not refute the diminishing-returns argument. It clarifies it.

The conversion rates are not permanently fixed. Companies can improve them, but doing so requires investment across the production chain.

Buying an AI coding assistant is not the same thing as redesigning software production.

The first produces more code.

The second may produce more value.

## The bottleneck moves

AI does not abolish scarcity. It relocates it.

When code is expensive, implementation capacity determines what gets built.

When code becomes cheap, the scarce resources become:

* deciding what deserves to exist;
* understanding how a change fits the system;
* verifying correctness;
* preserving architectural coherence;
* limiting product complexity;
* earning customer attention;
* distributing the product;
* and converting customer value into sustainable economics.

This changes what an excellent software organization looks like. The winning company will not necessarily have the fastest code generator; every company will have fast code generators.

The advantage will lie in what happens along the conversion chain:

**How reliably does an idea become a coherent release?**

**How often does a release change customer behaviour?**

**How often does that behaviour create durable economic value?**

**How much complexity is added along the way?**

An engineering organization that generates twice as much code and twice as much review work may be less productive than one that generates 20% more code, rejects half of it, ships a smaller product, and produces a measurable improvement in retention.

A commit count cannot tell these organizations apart.

A token counter will confidently recommend the wrong one.

## What companies should measure instead

Code activity still has diagnostic value. A sudden decline in commits may reveal blocked work. Pull-request volume may illuminate flow. Cycle time may expose a review constraint. The mistake is promoting these measures from signals into goals.

Companies adopting AI should measure the conversion between stages:

1. **Ideas to approved work:** How much work begins with evidence of a real customer or operational problem?
2. **Approved work to release:** How much waiting, review, rework, and coordination is required?
3. **Release to adoption:** Do intended users find and use the capability?
4. **Adoption to customer outcome:** Did the feature solve the problem it was supposed to solve?
5. **Customer outcome to economics:** Did it improve retention, expansion, margin, or another strategic objective?
6. **New code to carrying cost:** How much maintenance, support, complexity, and risk did the change introduce?

The central productivity metric is not code per engineer. It is closer to:

> **Validated economic value per unit of organizational effort.**

That is irritatingly difficult to measure. Reality has shown a disappointing lack of respect for dashboards.

But the fact that the correct measurement is difficult does not make an incorrect measurement useful.

![A decision-maker pruning many possible software paths into a few valuable choices](./images/04__diminishing_return_of_code.webp)

## The age of conscious restraint

AI will make experimentation dramatically cheaper. It will allow small teams to serve narrow markets, automate neglected workflows, replace awful internal spreadsheets, and build products that could never have supported a traditional engineering budget. That is real progress.

It will also remove the economic friction that once killed mediocre ideas before they entered production.

The result will be an unprecedented abundance of software—and a sharp decline in the marginal value of merely producing more of it. The old software company was constrained by implementation. The new one will be constrained by judgment.

Its central question will no longer be:

> Can we build this?

It will be:

> Should this exist? Will anybody care? Is it worth owning forever? And what are we refusing to build instead?

AI can make code nearly free.

It cannot make customer problems, attention, trust, product coherence, or willingness to pay equally abundant.

The winners will not be the companies that produce the most software. They will be the companies that convert software into value with the least waste—and have the discipline to stop when the next line of code is worth less than the silence it replaces.

> **When code becomes abundant, judgment becomes scarce.**

---

## References

* [Mert Demirer, Leon Musolff, and Liyuan Yang. “Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools.” NBER Working Paper 35275.][1]
* [OpenStax. “14.1 The Theory of Labor Markets.” *Principles of Economics 3e*.][2]
* [R. H. Coase. “The Nature of the Firm.” *Economica*.][3]
* [Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, and Tobias Salz. “The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers.” *Management Science*.][4]
* [Joel Becker, Nate Rush, Beth Barnes, and David Rein. “Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.” METR.][5]
* [Gene M. Amdahl. “Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities.”][6]
* [Michael Kremer. “The O-Ring Theory of Economic Development.” *The Quarterly Journal of Economics*.][7]
* [Yuanfang Cai et al. “Understanding Architectural Complexity, Maintenance Burden, and Developer Sentiment—A Large-Scale Study.”][8]
* [Lan Cheng et al. “What Improves Developer Productivity at Google? Code Quality.”][9]
* [Nicole Forsgren et al. “The SPACE of Developer Productivity: There’s More to It Than You Think.” *ACM Queue*.][10]
* [Debora Viana Thompson, Rebecca W. Hamilton, and Roland T. Rust. “Feature Fatigue: When Product Capabilities Become Too Much of a Good Thing.” *Journal of Marketing Research*.][11]
* [William Martin, Federica Sarro, and Mark Harman. “Causal Impact Analysis for App Releases in Google Play.”][12]
* [Tobias Schaefers, Tomas Falk, Ashish Kumar, and Julia Schamari. “More of the Same? Effects of Volume and Variety of Social Media Brand Engagement Behavior.” *Journal of Business Research*.][13]
* [Ali Goli, David H. Reiley, and Hongkai Zhang. “Personalizing Ad Load to Optimize Subscription and Ad Revenues: Product Strategies Constructed from Experiments on Pandora.” *Marketing Science*.][14]
* [Imke Reimers and Joel Waldfogel. “AI and the Quantity and Usage of Creative Products: Have LLMs Boosted Creation of Valuable Books?” NBER Working Paper 34777.][15]
* [Erik Brynjolfsson, Daniel Rock, and Chad Syverson. “The Productivity J-Curve: How Intangibles Complement General Purpose Technologies.” *American Economic Journal: Macroeconomics*.][16]
* [Ao Huang, Ni Huang, and Yili Hong. “Workflow Automation in Open-Source Software Development: Accelerating Innovation Through Mechanization and Orchestration.” *Information Systems Research*.][17]

[1]: https://www.nber.org/papers/w35275
[2]: https://openstax.org/books/principles-economics-3e/pages/14-1-the-theory-of-labor-markets
[3]: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1468-0335.1937.tb00002.x
[4]: https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535
[5]: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[6]: https://dl.acm.org/doi/10.1145/1465482.1465560
[7]: https://academic.oup.com/qje/article-abstract/108/3/551/1881767
[8]: https://research.google/pubs/understanding-architectural-complexity-maintenance-burden-and-developer-sentiment-a-large-scale-study/
[9]: https://research.google/pubs/what-improves-developer-productivity-at-google-code-quality/
[10]: https://queue.acm.org/detail.cfm?id=3454124
[11]: https://journals.sagepub.com/doi/10.1509/jmkr.2005.42.4.431
[12]: https://dl.acm.org/doi/10.1145/2950290.2950320
[13]: https://www.sciencedirect.com/science/article/abs/pii/S014829632100446X
[14]: https://pubsonline.informs.org/doi/10.1287/mksc.2022.0357
[15]: https://www.nber.org/papers/w34777
[16]: https://www.aeaweb.org/articles?id=10.1257/mac.20180386
[17]: https://pubsonline.informs.org/doi/10.1287/isre.2024.1551
