#!/usr/bin/env python3

# Constants
_UNITS_MAP = {
    "binary": {
        "units": ["B", "KiB", "MiB", "GiB", "TiB", "PiB"],
        "verbose": [
            "Bytes",
            "Kibibytes",
            "Mebibytes",
            "Gibibytes",
            "Tebibytes",
            "Pebibytes",
        ],
    },
    "decimal": {
        "units": ["B", "KB", "MB", "GB", "TB", "PB"],
        "verbose": [
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Petabytes",
        ],
    },
    "si": {
        "units": ["B", "kB", "MB", "GB", "TB", "PB"],
        "verbose": [
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Petabytes",
        ],
    },
    "unix": {
        "units": ["B", "K", "M", "G", "T", "P"]
    },
}


def _determine_units(
    binary: bool,
    si_units: bool,
    verbose: bool,
    uppercase_units: bool,
    unix_style: bool,
) -> list:
    """
    Determine the unit list based on the given options.
    """
    if unix_style:
        units = _UNITS_MAP["unix"]["units"]
    else:
        unit_type = "binary" if binary else "si" if si_units else "decimal"
        units = (_UNITS_MAP[unit_type]["verbose"]
                 if verbose else _UNITS_MAP[unit_type]["units"])

    if not uppercase_units and not si_units and not unix_style:
        units = [unit.lower() for unit in units]

    return units


def _format_size_with_precision(
    size: float,
    unit: str,
    precision: int,
    strip_trailing_zeros: bool,
    suffix: str,
) -> str:
    """
    Format the size with the specified precision, and optionally strip trailing zeros.
    """
    formatted_size = f"{size:.{precision}f} {unit}{suffix}"
    if strip_trailing_zeros:
        formatted_size = formatted_size.rstrip("0").rstrip(".")
    return formatted_size


def format_size(
    size: int,
    binary: bool = False,
    precision: int = 1,
    suffix: str = "",
    strip_trailing_zeros: bool = False,
    si_units: bool = False,
    uppercase_units: bool = True,
    verbose: bool = False,
    unix_style: bool = False,
) -> str:
    """
    Convert a file size to a human-readable format.

    Parameters:
    size (int): The file size in bytes.
    binary (bool): If True, use binary (base-1024) units (KiB, MiB, etc.). If False, use decimal (base-1000) units (KB, MB, etc.).
    precision (int): The number of decimal places to include in the formatted size.
    suffix (str): A suffix to append to the formatted size string.
    strip_trailing_zeros (bool): If True, strip trailing zeros from the formatted size.
    si_units (bool): If True, use SI units (kB, MB, etc.) which are also base-1000 but with different symbols.
    uppercase_units (bool): If True, use uppercase unit symbols (KB, MB). If False, use lowercase (kb, mb).
    verbose (bool): If True, use verbose unit names (Bytes, Kilobytes, etc.).
    unix_style (bool): If True, use single-letter Unix-style unit names (B, K, M, G, T, P).

    Returns:
    str: The human-readable format of the file size.

    Raises:
    ValueError: If size or precision is negative.
    """
    if size < 0:
        raise ValueError("Negative size not allowed")
    if precision < 0:
        raise ValueError("Precision cannot be negative")

    units = _determine_units(binary, si_units, verbose, uppercase_units,
                             unix_style)
    factor = 1024 if binary else 1000

    for unit in units:
        if size < factor:
            return _format_size_with_precision(size, unit, precision,
                                               strip_trailing_zeros, suffix)
        size /= factor

    return _format_size_with_precision(size, units[-1], precision,
                                       strip_trailing_zeros, suffix)
