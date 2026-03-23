# Integración Navidrome para Home Assistant

Integración personalizada para Home Assistant que permite conectar con tu servidor Navidrome mediante la API Subsonic.

Proporciona información en tiempo real sobre la música que se está reproduciendo, estadísticas de la biblioteca y estado del servidor.

## 📦 Instalación (HACS)

1. Abre HACS en Home Assistant
2. Ve a **Integraciones**
3. Menú ⋮ → **Repositorios personalizados**
4. Añade: https://github.com/t3rr0rz0n3/navidrome-ha
5. Tipo: **Integration**
6. Instala la integración
7. Reinicia Home Assistant

---

## ⚙️ Configuración

1. Ajustes → Dispositivos y servicios
2. Añadir integración → Navidrome
3. Introduce:
   - URL del servidor
   - Usuario
   - Contraseña

---

## ✨ Características

- Reproductor multimedia con información en tiempo real
- Botón para escanear la biblioteca
- Estadísticas:
  - Total de canciones
  - Total de artistas
  - Total de géneros
- Sensores de reproducción:
  - Canción actual
  - Artista actual
  - Álbum actual
- Último escaneo (tiempo relativo)
- Soporte multi-idioma
- Configuración desde la interfaz (config flow)

---

## 📸 Capturas

WIP 

---

## 📄 Licencia

GPL-3.0