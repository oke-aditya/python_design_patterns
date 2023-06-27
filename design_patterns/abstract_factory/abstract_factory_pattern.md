# Abstract factory pattern

This is used when we need Factory of Factory.

Think of creating multiple factory level objects in one class.

Higher abstraction than factory pattern.

```python
from abstract_factory.vehicle_factory import VehicleFactory
car = VehicleFactory.get_vehicle_factory("normal").get_vehicle("car")
car.speed()

rocket = VehicleFactory.get_vehicle_factory("luxury").get_vehicle("rocket")
rocket.speed()

```
