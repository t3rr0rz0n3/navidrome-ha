[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/t3rr0rz0n3/navidrome-ha.svg)](https://github.com/t3rr0rz0n3/navidrome-ha/releases)
![GitHub stars](https://img.shields.io/github/stars/t3rr0rz0n3/navidrome-ha?style=for-the-badge)

# Navidrome Home Assistant Integration

A custom Home Assistant integration to connect your Navidrome server using the Subsonic API.

This integration provides real-time information about your music server, including currently playing tracks, library statistics, and server status.

## 🌍 Languages

- English (this file)
- [Español](docs/README.es.md)
- [Català](docs/README.ca.md)

Want to translate this integration into your language? Check the [translation guide](docs/translate.md)

---

## 📦 Installation (via HACS)

1. Open HACS in Home Assistant
2. Go to **Integrations**
3. Click the three dots → **Custom repositories**
4. Add: https://github.com/t3rr0rz0n3/navidrome-ha
5. Select category: **Integration**
6. Install the integration
7. Restart Home Assistant

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services**
2. Click **Add Integration**
3. Search for **Navidrome**
4. Enter:
   - Server URL
   - Username
   - Password

---

## ✨ Features

- Media player with Now Playing information
- Trigger library scan from Home Assistant
- Library statistics:
  - Total songs
  - Total artists
  - Total genres
- Current playback sensors:
  - Current song
  - Current artist
  - Current album
- Last library scan (with relative time)
- Multi-language support (EN, ES, CA)
- Config flow support (UI setup)

---

## 📸 Screenshots

WIP 

---

## 📄 License

GPL-3.0