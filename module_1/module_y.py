"""
Formatting and reporting utilities for the parallel agent-session example.

This module is intentionally correct but lightly documented. It is designed for
the "Session B" agent task: improve docstrings in this file and update README.md,
without modifying any test files.
"""

from __future__ import annotations


def format_currency(amount: float) -> str:
    """Format a number as a US-dollar string with thousands separators.

    Negative amounts place the minus sign before the dollar sign.

    Args:
        amount: The value to format.

    Returns:
        The amount rounded to two decimal places, e.g. ``"$1,234.50"`` or
        ``"-$5.00"``.
    """
    if amount < 0:
        return f"-${abs(amount):,.2f}"
    return f"${amount:,.2f}"


def build_report_title(project_name: str, version: str) -> str:
    """Build a report title in the form ``"<project> — <version>"``.

    Leading/trailing whitespace is stripped from both parts, and internal
    whitespace in the project name is collapsed to single spaces.

    Args:
        project_name: The project name. Falls back to ``"Untitled Project"``
            if blank.
        version: The version label. Falls back to ``"draft"`` if blank.

    Returns:
        The formatted title, joined with an em dash.
    """
    clean_project = " ".join(project_name.strip().split())
    clean_version = version.strip()

    if not clean_project:
        clean_project = "Untitled Project"
    if not clean_version:
        clean_version = "draft"

    return f"{clean_project} — {clean_version}"


def mask_email(email: str) -> str:
    """Return a partially masked email address for display.

    The first and last characters of the local part are kept and the rest are
    replaced with ``*``. A one-character local part becomes ``"*"`` and a
    two-character local part keeps only its first character. The domain is
    lowercased.

    Args:
        email: The email address to mask. Surrounding whitespace is ignored.

    Returns:
        The masked address, e.g. ``"j**n@example.com"`` for
        ``"john@Example.com"``.

    Raises:
        ValueError: If ``email`` has no ``@``, or its local part or domain is
            empty.
    """
    email = email.strip()
    if "@" not in email:
        raise ValueError("email must contain @")

    local_part, domain = email.split("@", 1)
    if not local_part or not domain:
        raise ValueError("email must include a local part and domain")

    if len(local_part) == 1:
        masked_local = "*"
    elif len(local_part) == 2:
        masked_local = local_part[0] + "*"
    else:
        masked_local = local_part[0] + "*" * (len(local_part) - 2) + local_part[-1]

    return f"{masked_local}@{domain.lower()}"


def generate_summary_line(name: str, status: str, score: int) -> str:
    """Build a one-line summary in the form ``"<Name>: <status> (<score>)"``.

    Args:
        name: The display name. Whitespace is collapsed and words are
            title-cased; falls back to ``"Unknown"`` if blank.
        status: The status label. Lowercased, with underscores replaced by
            spaces (e.g. ``"IN_PROGRESS"`` becomes ``"in progress"``).
        score: The score shown in parentheses.

    Returns:
        The formatted summary line.
    """
    display_name = " ".join(name.strip().split()).title()
    display_status = status.strip().lower().replace("_", " ")

    if not display_name:
        display_name = "Unknown"

    return f"{display_name}: {display_status} ({score})"


def create_markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    """Render rows of data as a Markdown table.

    Args:
        rows: The table rows, each a mapping of column name to value. Values
            are converted with ``str()``; missing columns render as empty
            cells.
        columns: The column names, in display order. Keys in ``rows`` not
            listed here are ignored.

    Returns:
        The table as a newline-separated string with header, separator, and
        one line per row.

    Raises:
        ValueError: If ``columns`` is empty.
    """
    if not columns:
        raise ValueError("columns cannot be empty")

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"

    body_lines = []
    for row in rows:
        values = [str(row.get(column, "")) for column in columns]
        body_lines.append("| " + " | ".join(values) + " |")

    return "\n".join([header, separator, *body_lines])


def truncate_text(text: str, max_length: int = 80) -> str:
    """Collapse whitespace in ``text`` and truncate it to ``max_length``.

    If truncation is needed, trailing whitespace is removed from the cut text
    and ``"..."`` is appended, so the result never exceeds ``max_length``.

    Args:
        text: The text to shorten.
        max_length: The maximum length of the result, including the ellipsis.

    Returns:
        The whitespace-normalized text, truncated if it was too long.

    Raises:
        ValueError: If ``max_length`` is less than 4.
    """
    if max_length < 4:
        raise ValueError("max_length must be at least 4")

    clean_text = " ".join(text.strip().split())
    if len(clean_text) <= max_length:
        return clean_text

    return clean_text[: max_length - 3].rstrip() + "..."
