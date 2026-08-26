"""Spreadsheet Prophet package.

This package provides the core analysis, forecasting, narrative, plotting,
export, and web-application logic for Spreadsheet Prophet.
"""

__all__ = [
    "__title__",
    "__version__",
    "__version_info__",
    "__description__",
    "__author__",
    "__license__",
    "__url__",
]

__title__ = "Spreadsheet Prophet"
__version__ = "0.1.0"
__version_info__ = tuple(int(part) for part in __version__.split(".") if part.isdigit())

__description__ = (
    "Upload a CSV, infer column types, units, and anomalies, and receive a "
    "past/present/future narrative with confidence bands and a betrayal-metric flag."
)

__author__ = "Spreadsheet Prophet Team"
__license__ = "MIT"
__url__ = "https://example.com/spreadsheet-prophet"