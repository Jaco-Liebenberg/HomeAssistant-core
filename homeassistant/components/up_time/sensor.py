"""Platform for uptime sensor integration."""
from homeassistant.helpers.entity import Entity
from datetime import datetime

STARTUP_TIME = datetime.now()

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([UptimeSensor(), StartupTime()])

class StartupTime(Entity):
    """Startup Time Sensor Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = STARTUP_TIME


    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Startup Time'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return None

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = STARTUP_TIME

class UptimeSensor(Entity):
    """Uptime Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = datetime.now() - STARTUP_TIME


    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Uptime'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return None

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = datetime.now() - STARTUP_TIME