"""
Arc Vigil — Neural network training stability monitor.
Detect instability before your loss curve shows anything.
Attribute the failing module. Intervene automatically.

Usage:
    from arc_vigil import BendexMonitor, BendexConfig, BendexIntervention
"""

from arc_vigil.monitor import BendexMonitor, BendexConfig
from arc_vigil.intervention import BendexIntervention

__version__ = "1.0.0"
__all__ = ["BendexMonitor", "BendexConfig", "BendexIntervention"]
