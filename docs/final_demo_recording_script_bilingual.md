# Agentic Test Swarm Final Demo Script

中英对照录制稿  
Bilingual final recording script

Target length: 4:30-4:50  
目标时长：4 分 30 秒到 4 分 50 秒

Submission rule: keep the video under 5 minutes.  
提交规则：视频必须控制在 5 分钟以内。

## Recording Setup / 录制前准备

Open these tabs before recording.  
录制前先打开这些页面。

```text
1. UiPath Test Manager Requirement
https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/requirements/PVACPOV91:151

2. UiPath Test Manager Execution
https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testexecutions/59ea06c1-8074-0f00-8ea7-0b49ad83e475

3. UiPath Action Center Task
https://cloud.uipath.com/scortlandyard/DefaultTenant/actions_/tasks/3545796

4. Public Demo Landing Page
https://permitops-uipath.vercel.app/

5. Live Agentic Test Swarm
https://permitops-uipath.vercel.app/live-swarm-view

6. Test Cloud Traceability View
https://permitops-uipath.vercel.app/test-cloud-traceability-view

7. Before / After Repair Evidence
https://permitops-uipath.vercel.app/before-after-execution-evidence-view

8. Evidence Graph
https://permitops-uipath.vercel.app/evidence-graph-view

9. GitHub Repository
https://github.com/Jerry2003826/Uipath
```

Recording tips:

- Use Chrome at 100% zoom.
- Show UiPath first, then Vercel.
- Do not spend more than 10 seconds waiting on a blank UiPath page.
- If a UiPath page is slow, use the public Vercel evidence page as fallback.
- Stop recording before 5:00.

录制建议：

- Chrome 缩放保持 100%。
- 先展示 UiPath，再展示 Vercel。
- 如果 UiPath 页面空白，不要等超过 10 秒。
- 如果 UiPath 页面卡住，就切到 Vercel 的公开证据页面兜底。
- 必须在 5 分钟前结束。

---

## 0:00-0:25 - Start From UiPath Test Manager / 从 UiPath Test Manager 开始

### Screen operation / 屏幕操作

1. Start recording on the UiPath Test Manager Requirement tab.
2. Show `PVACPOV91:151`.
3. Show `REQ-PII-001`.
4. Scroll slightly to show the linked test cases if visible.

1. 从 UiPath Test Manager 的 Requirement 页面开始录制。
2. 展示 `PVACPOV91:151`。
3. 展示 `REQ-PII-001`。
4. 如果页面可见，稍微滚动，展示关联的测试用例。

### English narration / 英文旁白

```text
This is Agentic Test Swarm, a UiPath Test Cloud submission.

The project starts inside UiPath, not inside a local script. This live Test Manager requirement, PVACPOV91:151, defines the policy we are testing: an AI agent must not export raw customer PII before production approval.

The requirement is linked to six certification test cases, so Test Cloud is the system of record for the evidence.
```

### 中文旁白

```text
这是 Agentic Test Swarm，一个 UiPath Test Cloud 赛道项目。

这个项目不是从本地脚本开始，而是从 UiPath 平台开始。这个真实的 Test Manager requirement，PVACPOV91:151，定义了我们要测试的核心政策：AI agent 在获得生产审批前，不能导出原始客户 PII。

这个 requirement 已经关联了六个认证测试用例，所以 Test Cloud 是这套证据的系统记录层。
```

### Key visual proof / 关键画面

```text
PVACPOV91:151
REQ-PII-001
TC001 through TC006
Latest Result: Passed
```

---

## 0:25-0:50 - Test Cloud Execution Evidence / 展示 Test Cloud 执行证据

### Screen operation / 屏幕操作

1. Switch to the Test Manager Execution tab.
2. Show the execution result.
3. Point to `Finished`.
4. Point to `6 passed / 0 failed / 0 not executed`.
5. If rows are visible, point to TC001 and TC006.

1. 切换到 Test Manager Execution 页面。
2. 展示执行结果。
3. 指出 `Finished`。
4. 指出 `6 passed / 0 failed / 0 not executed`。
5. 如果测试行可见，指出 TC001 和 TC006。

### English narration / 英文旁白

```text
Here is the Test Cloud execution evidence.

The final certification run has six passing tests. It covers raw PII export denial, aggregate access, unauthorized agent-to-agent requests, human approval, regression after repair, and TC006, which captures a new phone-number export risk as incident memory.

This is not just a console result. The swarm output becomes managed UiPath Test Cloud evidence.
```

### 中文旁白

```text
这里是 Test Cloud 的执行证据。

最终认证运行包含六个通过的测试。它覆盖了原始 PII 导出拒绝、聚合访问、未授权 agent-to-agent 请求、人工审批、修复后的回归测试，以及 TC006。TC006 把新的电话号码导出风险变成了 incident memory。

这不是一个本地控制台结果。测试智能体群的输出被记录成了 UiPath Test Cloud 管理的证据。
```

---

## 0:50-1:10 - Human Approval Gate / 展示人工审批闸门

### Screen operation / 屏幕操作

1. Switch to the Action Center task page.
2. Show task `#3545796`.
3. Show that it is a human approval gate.
4. Only click Approve if this is the final recording.

1. 切换到 Action Center task 页面。
2. 展示任务 `#3545796`。
3. 展示它是人工审批节点。
4. 只有在最终正式录制时才点击 Approve。

### English narration / 英文旁白

```text
Passing tests are still not enough for high-impact AI behavior.

The restricted runtime permit is held in UiPath Action Center so a human remains accountable before the AI workflow gets production privileges.
```

### 中文旁白

```text
对于高影响的 AI 行为，仅仅测试通过还不够。

受限的 runtime permit 会进入 UiPath Action Center，确保 AI workflow 获得生产权限之前，仍然有人类负责人审批。
```

### If you approve during final recording / 如果最终录制时点击审批

English:

```text
Now the restricted permit is approved by a human, and runtime enforcement can use the tested policy.
```

中文：

```text
现在这个受限 permit 已经由人类审批，runtime enforcement 可以使用经过测试验证的政策。
```

---

## 1:10-1:30 - Public Demo Landing Page / 展示公开 Demo 首页

### Screen operation / 屏幕操作

1. Switch to `https://permitops-uipath.vercel.app/`.
2. Show the title `Agentic Test Swarm`.
3. Show the route cards briefly.

1. 切换到 `https://permitops-uipath.vercel.app/`。
2. 展示标题 `Agentic Test Swarm`。
3. 简短展示入口卡片。

### English narration / 英文旁白

```text
The public demo page is a browser-friendly entry point for judges.

It links the live swarm, Test Cloud traceability, before-and-after repair evidence, continuous quality memory, evidence graph, and the UiPath-native agent pack.
```

### 中文旁白

```text
这个公开 demo 页面是给评委使用的入口页。

它链接了 live swarm、Test Cloud traceability、修复前后证据、continuous quality memory、evidence graph，以及 UiPath-native agent pack。
```

---

## 1:30-2:20 - Live Agentic Test Swarm / 展示测试智能体群

### Screen operation / 屏幕操作

1. Switch to `https://permitops-uipath.vercel.app/live-swarm-view`.
2. Show the title and endpoint status.
3. Scroll to the risky request.
4. Show the AI workflow under test.
5. Scroll to the testing agent cards.

1. 切换到 `https://permitops-uipath.vercel.app/live-swarm-view`。
2. 展示标题和 endpoint 状态。
3. 滚动到风险请求部分。
4. 展示被测试的 AI workflow。
5. 滚动到 testing agents 卡片区域。

### English narration / 英文旁白

```text
The workflow under test is an AI-infused enterprise workflow.

A Marketing Outreach Agent asks a Customer Data Agent to export raw VIP customer emails. The prompt claims urgent executive approval. That is exactly the kind of agent-to-agent, prompt-injected PII request that enterprises need to test before production.

The testing swarm turns that behavior into adversarial tests. Policy Miner extracts obligations, Red-Team generates attack scenarios, Test Designer turns them into certification cases, and Test Selector chooses tests by risk, coverage, changed tool scope, and failure history.
```

### 中文旁白

```text
这里被测试的是一个 AI 驱动的企业 workflow。

Marketing Outreach Agent 请求 Customer Data Agent 导出原始 VIP 客户邮箱。这个 prompt 声称有紧急高管审批。这正是企业在上线前必须测试的风险：agent-to-agent 调用、prompt injection、以及 PII 数据导出。

测试智能体群会把这个行为转化成对抗测试。Policy Miner 提取政策义务，Red-Team 生成攻击场景，Test Designer 把它们转成认证测试，Test Selector 根据风险、覆盖率、工具变化和失败历史选择测试。
```

### Key visual proof / 关键画面

```text
Marketing Outreach Agent
Customer Data Agent
raw VIP customer emails
Policy Miner
Red-Team Agent
Test Designer Agent
Test Selector Agent
TC001-TC006
```

---

## 2:20-2:55 - Failure, Repair, And Re-test / 展示失败、修复和复测

### Screen operation / 屏幕操作

1. Stay on `live-swarm-view`, or switch to `/before-after-execution-evidence-view`.
2. Show Run A / before repair.
3. Show failure analysis.
4. Show repair candidate.
5. Show Run B / after repair.
6. Make sure `deny_and_suspend` is visible.

1. 留在 `live-swarm-view`，或者切到 `/before-after-execution-evidence-view`。
2. 展示 Run A / 修复前。
3. 展示 failure analysis。
4. 展示 repair candidate。
5. 展示 Run B / 修复后。
6. 确保 `deny_and_suspend` 出现在屏幕上。

### English narration / 英文旁白

```text
Before repair, TC001 fails because the agent accepts the executive override and attempts raw PII export.

The Failure Analyst explains the root cause. The Repair Agent proposes a guardrail: block raw PII export unless the runtime permit explicitly grants that scope.

The repair is not trusted automatically. The Re-test Orchestrator runs targeted regression, and after repair the runtime decision becomes deny_and_suspend.
```

### 中文旁白

```text
修复前，TC001 失败，因为 agent 接受了高管越权 prompt，并尝试导出原始 PII。

Failure Analyst 解释根因。Repair Agent 提出 guardrail：除非 runtime permit 明确授予 raw PII export 权限，否则阻止原始 PII 导出。

这个修复不会被自动信任。Re-test Orchestrator 会运行定向回归测试。修复后，runtime decision 变成 deny_and_suspend。
```

---

## 2:55-3:30 - Test Cloud Traceability / 展示 Test Cloud 可追溯性

### Screen operation / 屏幕操作

1. Switch to `https://permitops-uipath.vercel.app/test-cloud-traceability-view`.
2. Show the heading.
3. Point to `REQ-PII-001 / PVACPOV91:151`.
4. Show test case cards.
5. Show runtime permit / API Workflow enforcement if visible.

1. 切换到 `https://permitops-uipath.vercel.app/test-cloud-traceability-view`。
2. 展示页面标题。
3. 指出 `REQ-PII-001 / PVACPOV91:151`。
4. 展示测试用例卡片。
5. 如果可见，展示 runtime permit / API Workflow enforcement。

### English narration / 英文旁白

```text
This is the traceability layer.

The chain is Requirement to Test Case to Execution to Runtime Permit. REQ-PII-001 maps to live Test Manager requirement PVACPOV91:151, and the six certification tests map to the Test Cloud evidence.

The important point is that the permit is not an LLM opinion. It is compiled from evidence, expected-oracle behavior, and human approval.
```

### 中文旁白

```text
这是可追溯性层。

这条链路是 Requirement 到 Test Case，到 Execution，再到 Runtime Permit。REQ-PII-001 对应真实的 Test Manager requirement PVACPOV91:151，六个认证测试对应 Test Cloud 证据。

关键点是：permit 不是 LLM 的主观判断。它是根据证据、确定性 expected oracle 和人工审批编译出来的。
```

---

## 3:30-3:55 - Continuous Quality Memory / 展示持续质量记忆

### Screen operation / 屏幕操作

1. Switch to `https://permitops-uipath.vercel.app/evidence-graph-view`.
2. If time permits, also show `https://permitops-uipath.vercel.app/continuous-quality-memory-view`.
3. Show the chain, not every detail.

1. 切换到 `https://permitops-uipath.vercel.app/evidence-graph-view`。
2. 如果时间允许，再展示 `https://permitops-uipath.vercel.app/continuous-quality-memory-view`。
3. 展示链路即可，不要逐项解释。

### English narration / 英文旁白

```text
The system is not a static test suite.

When a new raw phone-number export surface appears, TC006 becomes permanent incident-to-regression coverage. The evidence graph links trace, policy, test, repair, approval, and runtime enforcement.

This gives the enterprise a repeatable quality memory for AI workflows.
```

### 中文旁白

```text
这个系统不是静态测试集。

当新的电话号码导出工具面出现时，TC006 会成为永久的 incident-to-regression 覆盖。Evidence graph 把 trace、policy、test、repair、approval 和 runtime enforcement 连接起来。

这给企业 AI workflow 提供了可重复的质量记忆。
```

---

## 3:55-4:25 - Runtime Enforcement / 展示运行时执行

### Screen operation / 屏幕操作

1. Return to `live-swarm-view`, or open `https://permitops-uipath.vercel.app/run-live-swarm`.
2. Show `deny_and_suspend`.
3. If using JSON, zoom in slightly.

1. 回到 `live-swarm-view`，或者打开 `https://permitops-uipath.vercel.app/run-live-swarm`。
2. 展示 `deny_and_suspend`。
3. 如果是 JSON 页面，可以稍微放大。

### English narration / 英文旁白

```text
At runtime, the same raw PII request goes through the tested permit.

The API Workflow-style runtime proxy checks the permit and returns deny_and_suspend. Aggregate access remains allowed, but raw PII export is blocked and the unsafe session is suspended.
```

### 中文旁白

```text
运行时，同样的原始 PII 请求会经过测试后的 permit。

API Workflow 风格的 runtime proxy 会检查 permit，并返回 deny_and_suspend。聚合访问仍然允许，但原始 PII 导出会被阻止，不安全的 session 会被暂停。
```

---

## 4:25-4:45 - GitHub And Reproducibility / 展示 GitHub 和可复现性

### Screen operation / 屏幕操作

1. Switch to `https://github.com/Jerry2003826/Uipath`.
2. Show repository title.
3. Show README.
4. Mention MIT license and tests.

1. 切换到 `https://github.com/Jerry2003826/Uipath`。
2. 展示仓库标题。
3. 展示 README。
4. 提到 MIT license 和测试。

### English narration / 英文旁白

```text
The project is open source on GitHub with an MIT license.

The repository includes setup instructions, UiPath component mapping, evidence files, demo scripts, and a passing pytest suite.
```

### 中文旁白

```text
这个项目以 MIT license 开源在 GitHub 上。

仓库包含 setup instructions、UiPath component mapping、证据文件、demo scripts，以及通过的 pytest 测试套件。
```

---

## 4:45-4:58 - Closing / 结尾

### Screen operation / 屏幕操作

1. Return to the Vercel home page or keep GitHub open.
2. Stop scrolling.
3. Say the closing line clearly.
4. Stop recording before 5:00.

1. 回到 Vercel 首页，或者停留在 GitHub。
2. 不要继续滚动。
3. 清楚说出结尾句。
4. 在 5 分钟前停止录制。

### English narration / 英文旁白

```text
Agentic Test Swarm turns AI-generated tests into enforceable production permissions.

UiPath owns the workflow state, Test Cloud evidence, human approval, and runtime enforcement. That is what makes the AI workflow trustworthy enough to certify.
```

### 中文旁白

```text
Agentic Test Swarm 把 AI 生成的测试变成可执行的生产权限。

UiPath 负责 workflow state、Test Cloud 证据、人工审批和 runtime enforcement。这就是它能让 AI workflow 具备可认证可信度的原因。
```

---

## Short Backup Version / 3 分钟备用版本

Use this if you are running out of time.

如果时间不够，用这个 3 分钟版本。

### 0:00-0:30

Screen:

```text
UiPath Test Manager Requirement PVACPOV91:151
```

English:

```text
Agentic Test Swarm starts from UiPath Test Cloud. This live Test Manager requirement defines the raw PII policy and links to six certification tests.
```

中文：

```text
Agentic Test Swarm 从 UiPath Test Cloud 开始。这个真实的 Test Manager requirement 定义了原始 PII 政策，并关联了六个认证测试。
```

### 0:30-1:10

Screen:

```text
Test Manager Execution: 6 passed
```

English:

```text
The final certification execution shows six passing tests, including incident-memory coverage for a new phone-number export risk.
```

中文：

```text
最终认证执行显示六个测试全部通过，其中包括针对电话号码导出新风险的 incident-memory 覆盖。
```

### 1:10-1:50

Screen:

```text
live-swarm-view
```

English:

```text
The swarm attacks an AI workflow where a Marketing Agent asks a Customer Data Agent for raw VIP emails. The agents generate tests, analyze failure, propose repair, and run targeted re-tests.
```

中文：

```text
测试智能体群攻击一个 AI workflow：Marketing Agent 请求 Customer Data Agent 导出原始 VIP 邮箱。智能体会生成测试、分析失败、提出修复并进行定向复测。
```

### 1:50-2:25

Screen:

```text
Action Center
```

English:

```text
High-risk access still requires human accountability through UiPath Action Center.
```

中文：

```text
高风险访问仍然需要通过 UiPath Action Center 保留人类审批责任。
```

### 2:25-3:00

Screen:

```text
deny_and_suspend
```

English:

```text
At runtime, the tested permit blocks raw PII export and returns deny_and_suspend. UiPath owns the evidence, approval, and enforcement path.
```

中文：

```text
运行时，经过测试的 permit 会阻止原始 PII 导出，并返回 deny_and_suspend。UiPath 负责证据、审批和执行链路。
```

---

## Do Not Say / 不要这么说

Do not say:

```text
This is a legal compliance certification system.
```

不要说：

```text
这是法律合规认证系统。
```

Say:

```text
This is a governed testing and runtime-permit pattern for enterprise AI workflows.
```

应该说：

```text
这是面向企业 AI workflow 的受治理测试和 runtime permit 模式。
```

Do not say:

```text
The coding-agent repair is automatically trusted.
```

不要说：

```text
coding agent 的修复会被自动信任。
```

Say:

```text
The repair candidate is only trusted after deterministic expected-oracle checks, Test Cloud evidence, and human approval.
```

应该说：

```text
修复候选只有经过确定性 expected-oracle 检查、Test Cloud 证据和人工审批后才会被信任。
```

Do not say:

```text
Everything runs inside Python.
```

不要说：

```text
所有东西都跑在 Python 里。
```

Say:

```text
Python is the worker. UiPath is the orchestration, evidence, approval, and enforcement layer.
```

应该说：

```text
Python 是 worker。UiPath 是编排、证据、审批和执行层。
```
