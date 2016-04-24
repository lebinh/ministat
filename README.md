# ministat
Python statistics library based on the `ministat` command

```
>>> import ministat
>>> iguana = [50, 200, 150, 400, 750, 400, 150]
>>> chameleon = [150, 400, 720, 500, 930]
>>> ministat.compare_and_print(iguana, chameleon)
No difference proven at 95.0% confidence
>>> ministat.compare_and_print(iguana, chameleon, confidence_level=80)
Difference at 80.0% confidence
-240 +/- 212.215
-80% +/- 70.7384%
(Student's t, pooled s = 154.676)
```
