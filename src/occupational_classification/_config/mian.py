"""Provides configuration for the project.

Usage:
    ```
    from sic_soc_llm import get_config
    config = get_config()
    config.CONFIG_NAME
    ```
"""

import logging
from importlib import resources
from pathlib import Path
from typing import Optional, Union

import toml
from pyprojroot import here

logger = logging.getLogger(__name__)

_config = None


def check_file_exists(
    file_name: Optional[Union[Path, str]] = "sic_soc_llm_config.toml",
) -> Path:
    """Check if the file exists.

    If relative path provided it will look for the file in these locations:
    1. relative to the current working directory
    2. ralative to project root directory
    3. relative to user's home directory
    4. relative to the package resources

    Args:
        file_name (Path or str, optional): The name of the file to check.
            Defaults to config file name.

    Returns:
        Path: The absolute path to the file if it exists, None otherwise.
    """
    file_path = Path(file_name)
    # check whether the filepath is relative or absolute
    if file_path.is_absolute():
        return file_path if file_path.exists() else None
    # check whether the file exists in the current directory
    elif (Path.cwd() / file_path).exists():
        return Path.cwd() / file_path
    # check whether the file exists in the project root directory
    elif (Path(here()) / file_path).exists():
        return Path(here()) / file_path
    # check whether the file exists in the user's home directory
    elif (Path.home() / file_path).exists():
        return Path.home() / file_path
    # check whether the file exists in the package resources
    elif (
        resources.files("occupational_classification._config") / file_path
    ).exists():
        return resources.files("occupational_classification._config") / file_path
    elif (
        resources.files("occupational_classification.example_data") / file_path
    ).exists():
        return (
            resources.files("occupational_classification.example_data") / file_path
        )
    else:
        return None


def get_config(config_name: Optional[Union[Path, str]] = "config.toml") -> dict:
    """Fetch the configuration.

    Loads config from the filepath defined in `CONFIG_FILEPATH`.

    Args:
        config_name (Path or str, optional): The name of the config file to load.
            Defaults to relative path "config.toml" - in such case it looks for
            the config file in 1. current dir, 2. project dir, 3. user home and
            4. package resources.

    Returns:
        dict: Configuration for the system.

    Raises:
        FileNotFoundError: If the config file or required data not found.
    """
    global _config

    if _config is None:
        config_filepath = check_file_exists(config_name)

        if config_filepath is None:
            raise FileNotFoundError("Config file not found.")
        else:
            with open(config_filepath) as f:
                logger.info(f"Loading config from {config_filepath}")
                in_config = toml.load(f)
            for key, soc_data in in_config["data_source"].items():
                soc_data_path = check_file_exists(soc_data)
                if soc_data_path is None:
                    if key in ["soc_index", "soc_structure"]:
                        raise FileNotFoundError(
                            f"Required soc_data file {key}: {soc_data} not found."
                        )
                    else:
                        logger.warning(
                            f"Optional lookup file {key}: {soc_data} not found."
                        )
                else:
                    in_config["data_source"][key] = soc_data_path
            _config = in_config
            logger.debug(f"Config values: {_config}")

    return _config
