from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        NavidromeStartScanButton(coordinator)
    ])

class NavidromeStartScanButton(CoordinatorEntity, ButtonEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_has_entity_name = True
        self._attr_translation_key = "start_scan"
        self._attr_unique_id = "navidrome_start_scan"
        self._attr_icon = "mdi:database-refresh"

    @property
    def device_info(self):
        return {
            "identifiers": {("navidrome", "server")},
            "name": "Navidrome",
            "manufacturer": "Navidrome",
            "model": "Music Server",
        }

    @property
    def available(self):
        scan = self.coordinator.data.get("scan_status", {})
        return not scan.get("scanning", False)

    async def async_press(self):
        await self.hass.async_add_executor_job(
            self.coordinator.api.start_scan
        )

        await self.coordinator.async_request_refresh()