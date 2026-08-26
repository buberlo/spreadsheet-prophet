"""Entry point for the Spreadsheet Prophet web application."""

from __future__ import annotations

import logging
import os
from typing import Tuple

from spreadsheet_prophet import __version__
from spreadsheet_prophet.web import create_app

logger = logging.getLogger("spreadsheet_prophet.app")


def _log_level() -> int:
    """Return the configured logging level for the application."""
    level_name = os.environ.get("SPREADSHEET_PROPHET_LOG_LEVEL", "INFO").upper()
    return getattr(logging, level_name, logging.INFO)


def _server_settings() -> Tuple[str, int, bool]:
    """Return host, port, and debug settings for the development server."""
    host = os.environ.get("SPREADSHEET_PROPHET_HOST", "127.0.0.1")
    port = int(os.environ.get("SPREADSHEET_PROPHET_PORT", "5000"))
    debug = os.environ.get("SPREADSHEET_PROPHET_DEBUG", "0") == "1"
    return host, port, debug


def main() -> None:
    """Create and run the Spreadsheet Prophet Flask application."""
    logging.basicConfig(
        level=_log_level(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    app = create_app()
    host, port, debug = _server_settings()

    logger.info(
        "Starting Spreadsheet Prophet %s on http://%s:%s",
        __version__,
        host,
        port,
    )
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()