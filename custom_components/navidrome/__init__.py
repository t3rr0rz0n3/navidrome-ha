from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_URL, CONF_USERNAME, CONF_PASSWORD
from .api import NavidromeAPI
from .coordinator import NavidromeCoordinator


async def async_setup(hass: HomeAssistant, config: dict):
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})

    api = NavidromeAPI(
        entry.data[CONF_URL],
        entry.data[CONF_USERNAME],
        entry.data[CONF_PASSWORD],
    )

    coordinator = NavidromeCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    async def start_scan_service(call):
        await hass.async_add_executor_job(api.start_scan)

        # refrescar datos tras lanzar scan
        await coordinator.async_request_refresh()

    hass.services.async_register(
        DOMAIN,
        "start_scan",
        start_scan_service
    )

    await hass.config_entries.async_forward_entry_setups(
        entry, ["media_player", "sensor", "button"]
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, ["media_player", "sensor"]
    )

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok