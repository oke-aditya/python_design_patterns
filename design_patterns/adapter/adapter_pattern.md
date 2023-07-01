# Adapter Pattern

Use the Adapter class when you want to use some existing class, 
but its interface isn’t compatible with the rest of your code.

Use the pattern when you want to reuse several existing 
subclasses that lack some common functionality that can’t be added to the superclass.


Adapter changes the interface of an existing object, while Decorator enhances an 
object without changing its interface. 

In addition, Decorator supports recursive composition, which isn’t possible when you use Adapter.

Adapter provides a different interface to the wrapped object, 
Proxy provides it with the same interface, and Decorator provides it with an enhanced interface.

Bridge is usually designed up-front, letting you develop parts of an 
application independently of each other. On the other hand, Adapter is commonly 
used with an existing app to make some otherwise-incompatible classes work together nicely.

# Example

```python

from adapter.weight_machine_adapter import WeightMachineAdapter
from adapter.weight_machine import WeightMachine

wm_adapter = WeightMachineAdapter(WeightMachine())
print(wm_adapter.get_weight_machine_in_kgs())

```


# Use Cases

1. XML to JSON Parser
2. Foreign Currency Exchange 
3. Getting data which is different from what we want.
4. Weight Machine (works in pounds), Needs to work in Kgs.



