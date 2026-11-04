# INSANE_PANEL

**INSANE_PANEL** is a branding-only customization of the open-source [Pterodactyl Panel](https://github.com/pterodactyl/panel), based on the upstream **v1.15.2** source tree.

## Current status

- Full upstream Panel source has been imported into this repository.
- The initial `tools/brand.py` script was applied during import, replacing selected exact visible labels.
- The original Pterodactyl application logic, admin UI, server features, and Wings integration are retained.
- **Branding coverage is not yet fully audited, frontend build has not yet been verified, and the Panel has not been deployed.**
- Wings is a separate daemon: https://github.com/pterodactyl/wings

## Build validation

See **Actions → Validate frontend build** for CI validation. A passing frontend build does not validate a production deployment.

## Branding

To reapply the limited display-label substitution:

```bash
python3 tools/brand.py
```

Review the frontend manually for additional hard-coded branding. Do not globally replace the word "pterodactyl" in URLs, package names, API paths, database identifiers, license text, or daemon configuration: doing so can break compatibility.

Set the Laravel application name to `APP_NAME="INSANE_PANEL"` in the private deployment `.env` file. Never commit your `.env` or credentials.

## Deployment

Follow the official v1 Panel installation instructions at https://pterodactyl.io/panel/1.0/getting_started.html and Wings instructions at https://pterodactyl.io/wings/1.0/installing.html on a supported Linux host. Android PRoot is not a compatible Wings Docker host.

## Attribution

This repository is derived from Pterodactyl. Retain its original LICENSE, copyright notices, and attribution. INSANE_PANEL is a community customization, not an official Pterodactyl release.
