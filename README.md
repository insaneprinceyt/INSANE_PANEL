# INSANE_PANEL

Branding-only customization of the [Pterodactyl Panel](https://github.com/pterodactyl/panel).

**Status:** Project setup and branding script are committed. The full upstream source is **not yet imported**. This is not a deployable build.

## Target
- Pterodactyl Panel stable v1.15.2
- Visible name: **INSANE_PANEL**
- Original UI, features, server API, and Wings integration remain unchanged
- Keep original upstream LICENSE and copyright notices

## Import upstream source
On a Linux development machine:
```bash
git clone https://github.com/insaneprinceyt/INSANE_PANEL.git
cd INSANE_PANEL
git clone --branch v1.15.2 --depth 1 https://github.com/pterodactyl/panel.git /tmp/insane-panel-upstream
rsync -a --exclude=.git --exclude=.github /tmp/insane-panel-upstream/ ./
python3 tools/brand.py
git add .
git commit -m "Import Pterodactyl v1.15.2 and apply INSANE_PANEL branding"
git push origin main
```

This script changes only certain literal frontend labels. Additional labels may need review. To configure a deployed Panel's Laravel application name, set `APP_NAME="INSANE_PANEL"` in its private `.env` file (never commit that file). Frontend changes require a build using the official instructions: https://docs.pterodactyl.io/v1/guides/customization/panel

Do not publish secrets, `.env`, private SSH keys, or credentials.

## Upstream and license
Original project copyright and license must be retained. Wings remains the separately deployed official daemon: https://github.com/pterodactyl/wings
