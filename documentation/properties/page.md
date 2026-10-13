---
layout:     property
title:      "page"
schemas:    [adjustment]
---

# page

---

The **page** attribute identifies the page of the report to which an adjustment relates and is a string field.

The [FIRE adjustment schema, `page` property][schema] defines this field as the report page to which the adjustment relates. It helps reviewers locate the adjustment in a rendered report alongside the row and column coordinates.

Page names can be irregular; consult the destination system for acceptable pages and page names.

[schema]: https://github.com/SuadeLabs/fire/blob/master/schemas/adjustment.json#:~:text=The%20page%20of%20the%20report%20that%20this%20adjustment%20relates%20to.
