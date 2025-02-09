from __future__ import annotations

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping

HTML_MIME_TYPE: Final = "text/html"
MARKDOWN_MIME_TYPE: Final = "text/markdown"
PDF_MIME_TYPE: Final = "application/pdf"
PLAIN_TEXT_MIME_TYPE: Final = "text/plain"
POWER_POINT_MIME_TYPE: Final = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
EXCEL_MIME_TYPE: Final = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
PLAIN_TEXT_MIME_TYPES: Final[set[str]] = {PLAIN_TEXT_MIME_TYPE, MARKDOWN_MIME_TYPE}

IMAGE_MIME_TYPES: Final[set[str]] = {
    "image/bmp",
    "image/gif",
    "image/jp2",
    "image/jpeg",
    "image/jpm",
    "image/jpx",
    "image/mj2",
    "image/pjpeg",
    "image/png",
    "image/tiff",
    "image/webp",
    "image/x-bmp",
    "image/x-ms-bmp",
    "image/x-portable-anymap",
    "image/x-portable-bitmap",
    "image/x-portable-graymap",
    "image/x-portable-pixmap",
    "image/x-tiff",
}
IMAGE_MIME_TYPE_EXT_MAP: Final[Mapping[str, str]] = {
    "image/bmp": "bmp",
    "image/x-bmp": "bmp",
    "image/x-ms-bmp": "bmp",
    "image/gif": "gif",
    "image/jpeg": "jpg",
    "image/pjpeg": "jpg",
    "image/png": "png",
    "image/tiff": "tiff",
    "image/x-tiff": "tiff",
    "image/jp2": "jp2",
    "image/jpx": "jpx",
    "image/jpm": "jpm",
    "image/mj2": "mj2",
    "image/webp": "webp",
    "image/x-portable-anymap": "pnm",
    "image/x-portable-bitmap": "pbm",
    "image/x-portable-graymap": "pgm",
    "image/x-portable-pixmap": "ppm",
}
PANDOC_SUPPORTED_MIME_TYPES: Final[set[str]] = {
    "application/csl+json",
    "application/docbook+xml",
    "application/epub+zip",
    "application/rtf",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/x-biblatex",
    "application/x-bibtex",
    "application/x-endnote+xml",
    "application/x-fictionbook+xml",
    "application/x-ipynb+json",
    "application/x-jats+xml",
    "application/x-latex",
    "application/x-opml+xml",
    "application/x-research-info-systems",
    "application/x-typst",
    "text/csv",
    "text/tab-separated-values",
    "text/troff",
    "text/x-commonmark",
    "text/x-dokuwiki",
    "text/x-gfm",
    "text/x-markdown",
    "text/x-markdown-extra",
    "text/x-mdoc",
    "text/x-multimarkdown",
    "text/x-org",
    "text/x-pod",
    "text/x-rst",
}

SUPPORTED_MIME_TYPES: Final[set[str]] = (
    PLAIN_TEXT_MIME_TYPES
    | IMAGE_MIME_TYPES
    | PANDOC_SUPPORTED_MIME_TYPES
    | {PDF_MIME_TYPE, POWER_POINT_MIME_TYPE, HTML_MIME_TYPE, EXCEL_MIME_TYPE}
)
