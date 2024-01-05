import ast
import configparser
import pathlib


def cleanup_files(dest_dir: str) -> None:
    """Removes the copied files & directory from UC Volumes

    Args:
        dest_dir (str): Destination location.
            For UC Volumes it takes the form /Volumes/<my_catalog>/<my_schema>/<my_volume>/<path>/<to>/<directory>
            For further information see https://docs.databricks.com/en/files/index.html
    """
    dbutils.fs.rm(dest_dir, recurse=True)


def upload_dir() -> None:
    """Copy a directory using dbutils.
    For this use case it is used as a convenient way to copy files located in the fixtures directory of this repo to UC Volumes.
    When using the Databricks extension for vsCode, files are synchronized to the user's Workspace & can then be copied to Volumes.
    """
    # Read "upload_files_config.ini" & parse configs
    upload_files_config_path = pathlib.Path(__file__).parent / "upload_files_config.ini"
    upload_files_config = configparser.ConfigParser()
    upload_files_config.read(upload_files_config_path)
    file_cleanup = ast.literal_eval(upload_files_config["options"]["file_cleanup"])
    source_dir = (
        pathlib.Path(__file__).parents[2]
        / "fixtures"
        / "raw_data"
        / "sample_eve_data"
        / "csv_files"
    )
    other_source_dir = pathlib.Path(__file__).parents[2] / "fixtures" / "schema_data"
    dest_dir = ast.literal_eval(upload_files_config["paths"]["destination"])
    other_dest_dir = ast.literal_eval(upload_files_config["paths"]["destination"])

    # Removes copied files IF "file_cleanup" is set to True in "upload_files_config.ini"
    if file_cleanup == True:
        cleanup_files(dest_dir)

    # Copies files from Workspace directory to Volumes
    else:
        dbutils.fs.cp(f"file:{source_dir}", dest_dir, recurse=True)
        dbutils.fs.cp(f"file:{other_source_dir}", other_dest_dir, recurse=True)


if __name__ == "__main__":
    upload_dir()
