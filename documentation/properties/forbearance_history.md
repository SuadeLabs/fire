---
layout:     property
title:      "forbearance_history"
schemas:    [account, loan, security]
---

# forbearance_history

---

```bash
├── x2
├── x3
└── additional
```

The **forbearance_history** field records whether an instrument's forbearance
history goes beyond a single episode, or has had a further measure granted
during an active forbearance period. This field is left blank/null where no
such history applies (i.e. the instrument has never been forborne, or has
been forborne on only one occasion with no additional measures granted
during that episode).

See also [**arrears_arrangement**]

### x2
The instrument has been granted forbearance measures at two different
points in time. This includes exposures that exited forborne status
(cured) and were subsequently granted new forbearance measures.

### x3
The instrument has been granted forbearance measures at three or more
different points in time. Map to this value for any instrument forborne
three times or more — this value does not distinguish further between
three, four, or more episodes.

### additional
Forbearance measures were granted in addition to forbearance measures
already in place, while the instrument was under probation (i.e. before
the current forbearance episode had exited/cured).

---

[**arrears_arrangement**]: https://github.com/suadelabs/fire/blob/master/documentation/properties/arrears_arrangement.md