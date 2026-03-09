---
layout:     property
title:      "participation_type"
schemas:    [loan]
---

# participation_type

---

```bash
├── agent_non_snc
├── agent_snc
├── none
├── participant_non_snc
└── participant_snc
```

Indicate if the credit facility is participated or syndicated among other financial institutions and if it is part of the Shared National Credit Program. Refer to https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q for more information.

### agent_non_snc

The reporting institution is acting as an agent in a syndication or participation arrangement, but the loan does not meet the definition of a Shared National Credit (SNC). The institution is responsible for administering the loan on behalf of the syndicate.

### agent_snc

The reporting institution is acting as an agent in a Shared National Credit (SNC) arrangement. The institution is responsible for administering the loan on behalf of the syndicate and the loan meets the SNC criteria.

### none

The loan is not part of any participation or syndication arrangement. It is held entirely by the reporting institution.

### participant_non_snc

The reporting institution is a participant in a syndication or participation arrangement, but the loan does not meet the definition of a Shared National Credit (SNC). The institution holds a portion of the loan but is not the agent.

### participant_snc

The reporting institution is a participant in a Shared National Credit (SNC) arrangement. The institution holds a portion of the loan that meets the SNC criteria but is not the agent.