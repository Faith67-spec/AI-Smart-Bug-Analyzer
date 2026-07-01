# Knowledge Base Data Model

## BugRecord Schema

| Field | Description |
|-------|-------------|
| id | Unique defect ID |
| title | Bug title |
| description | Bug description |
| logs | Error logs |
| stack_trace | Stack traces |
| severity | Severity level |
| priority | Priority |
| component | System module |
| resolution | Previous fix |
| source_dataset | Mozilla/Apache/Eclipse |
| embedding | Vector representation |

---

## Example Record

```json
{
"id":"MOZ_1001",

"title":"NullPointerException during login",

"description":"Application crashes on login",

"severity":"Critical",

"priority":"P1",

"component":"Authentication",

"resolution":"Initialize object before access",

"source_dataset":"Mozilla"

}