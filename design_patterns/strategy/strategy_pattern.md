# Strategy Pattern

Used When

1. Children need to override the Parent Functionality.
2. Children need to share same functionality among cousins / same level classes.
3. Create strategy and inject them.
4. Strategies can be re-used. Each child has a Strategy.



```python
from strategy.offroad_vehicle import OffRoadVehicle
from strategy.normal_vehicle import NormalVehicle

v = OffRoadVehicle()
v2 = NormalVehicle()
v.drive_strategy.drive()
v2.drive_strategy.drive()

```
# Use Cases

Various algorithms for implementation same thing.
Share the algorithm with other classes.

