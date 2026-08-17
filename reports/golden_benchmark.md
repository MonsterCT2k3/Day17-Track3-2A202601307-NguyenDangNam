# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1478.7 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 3406.4 | 869 | 0.0% |  |
| G09 | long_term | PASS | 2051.6 | 1418 | 0.0% |  |
| G12 | semantic | PASS | 404.6 | 418 | 8.9% |  |
| G14 | semantic | PASS | 400.5 | 270 | 30.2% |  |
| G15 | semantic | PASS | 407.7 | 270 | 41.2% |  |
| G19 | mixed | PASS | 2248.9 | 581 | 0.0% |  |
| G03 | long_term | PASS | 2064.9 | 1393 | 0.0% |  |
| G04 | long_term | PASS | 1825.3 | 1406 | 0.0% |  |
| G05 | long_term | PASS | 1840.4 | 1394 | 0.0% |  |
| G10 | episodic | PASS | 406.0 | 470 | 0.0% |  |
| G11 | episodic | PASS | 407.2 | 468 | 0.0% |  |
| G13 | semantic | PASS | 404.1 | 416 | 26.4% |  |
| G16 | mixed | PASS | 2657.3 | 581 | 0.0% |  |
| G18 | mixed | PASS | 1022.3 | 500 | 11.5% |  |
| G20 | mixed | PASS | 3070.7 | 831 | 0.0% |  |
| G06 | long_term | PASS | 2051.6 | 1405 | 0.0% |  |
| G07 | long_term | PASS | 2456.0 | 1402 | 0.0% |  |
| G17 | mixed | PASS | 2448.2 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan's main project is LOTUS-88, focusing on backend development using Java and Spring Boot.  Lan prefers Java and Spring Boot for backend development and does not use Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant):`

### G09 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped m`

### G14 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's main project is LOTUS-88, focusing on backend development using Java and Spring Boot.  Lan prefers Java and Spring Boot for backend development and does not use Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 04:52:53     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend `

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G10 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScr`

### G11 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScr`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and `

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user w`

### G18 - mixed

`<EPISODIC> EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Minh dang lam kiem ke lai mo hinh cac`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user w`

### G06 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G07 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user wants short e`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27 and preference for Python remains for this project. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this specific project. The user is working on debugging async HTTP requests for ORCHID-27, specifically addressing connection churn by reusing the aiohttp ClientSession and setting concurrency to 20. The user needs to complete a benchmark report, open loop LAB-REPORT-1600, before Friday at 16:00. The user requested checks on the connection pool, client lifecycle, and concurrency.  The user prefers Python and dislikes Java. When explaining code, the user w`
