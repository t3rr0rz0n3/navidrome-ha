from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from datetime import datetime

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        NavidromeScanStatusSensor(coordinator),
        NavidromeLastScanSensor(coordinator),
        NavidromeTotalGenresSensor(coordinator),
        NavidromeTotalArtistsSensor(coordinator),
        NavidromeTotalSongsSensor(coordinator)
    ])


class BaseNavidromeSensor(CoordinatorEntity, SensorEntity):
    @property
    def device_info(self):
        system = self.coordinator.data.get("system", {})

        return {
            "identifiers": {("navidrome", "server")},
            "name": "Navidrome",
            "manufacturer": "Navidrome",
            "model": "Music Server",
            "sw_version": system.get("version"),
            "configuration_url": self.coordinator.api.base_url,
        }


class NavidromeScanStatusSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "scan_status"
        self._attr_unique_id = "navidrome_scan_status"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return "unknown"

        scan = data.get("scan_status")

        if not scan:
            return "unknown"

        return "scanning" if scan.get("scanning") else "idle"


class NavidromeLastScanSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "last_scan"
        self._attr_unique_id = "navidrome_last_scan"
        self._attr_device_class = "timestamp"
        self._attr_state_class = "measurement"
        
    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return None

        scan = data.get("scan_status")

        if not scan:
            return None

        last_scan = scan.get("lastScan")

        if not last_scan:
            return None

        return datetime.fromisoformat(last_scan.replace("Z", "+00:00"))

class NavidromeTotalGenresSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "total_genres"
        self._attr_unique_id = "navidrome_total_genres"
        self._attr_icon = "mdi:music"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return 0

        genres = data.get("genres", [])

        return len(genres)

class NavidromeTotalArtistsSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "total_artists"
        self._attr_unique_id = "navidrome_total_artists"
        self._attr_icon = "mdi:account-music"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return 0

        indexes = data.get("artists", [])

        total = 0

        for index in indexes:
            total += len(index.get("artist", []))

        return total

class NavidromeTotalSongsSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "total_songs"
        self._attr_unique_id = "navidrome_total_songs"
        self._attr_icon = "mdi:music"
        #self._attr_native_unit_of_measurement = "songs"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return 0

        genres = data.get("genres", [])

        total = sum(g.get("songCount", 0) for g in genres)

        return total

class NavidromeTotalPlaylistsSensor(BaseNavidromeSensor):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "total_playlists"
        self._attr_unique_id = "navidrome_total_playlists"
        self._attr_icon = "mdi:playlist-music"

    @property
    def state(self):
        data = self.coordinator.data

        if not data:
            return 0

        playlists = data.get("playlists", [])

        return len(playlists)