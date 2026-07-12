# Lessons Learned — the expertise layer

> Cross-client patterns distilled from Setup Decision Records. The assistant consults
> this file (plus all `clients/*/decisions/SDR-*.md`) before arguing any setup option,
> and cites entries by ID (LL-001, …).
>
> **Promotion rule:** an observation becomes a lesson when it is confirmed by outcomes
> in at least two clients, OR a single outcome shows a default recommendation in the
> knowledge base was wrong. The assistant drafts entries; the consultant approves them.
> Keep entries short — one pattern, one lesson, sources.

---

## LL-001 (EXAMPLE — replace with your first real lesson)

| Field | Value |
|---|---|
| Tags | `#warehouse` `#complexity` |
| Source | SDR-003 @ client-a (reversed), SDR-011 @ client-b (held) |
| Client pattern | <50 users, single warehouse, no scanners at go-live |

**Lesson:** Activating directed put-away and pick at go-live for a client without
scanner hardware and without a dedicated warehouse manager led to floor staff working
around the system within weeks; downgrading a live location is disruptive. Starting at
"inventory pick/put-away" level and upgrading in phase 2 held up well elsewhere.

**Impact on advice:** For this client pattern, recommend the basic warehouse level even
when the client asks for "full WMS" — argue phase 2 instead. Overrides the knowledge
file's neutral stance.

---

<!-- New entries below. Next ID: LL-002 -->
