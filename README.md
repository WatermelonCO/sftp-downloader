# sftp-downloader

sftp-downloader is a command line tool for downloading files from an SFTP server based on a CSV file. The tool is implemented in Python using the pysftp library and includes command line arguments for the CSV file path, the remote path to the files on the SFTP server, and the local path to save the downloaded files.

## Installation

To install sftp-downloader, you first need to have Python 3 and pip installed on your system. Then, you can install the tool by running the following command:

pip install sftp-downloader


This will install sftp-downloader along with all of its dependencies.

## Usage

Once you have installed sftp-downloader, you can use it to download files from an SFTP server based on a CSV file. The CSV file should have the following format:



filename,track_title,duration,bpm,artist,album,genre,subgenre,timeofday
file1.mp3,Track 1,3:30,120,Artist 1,Album 1,Pop,Rock,Morning
file2.mp3,Track 2,4:15,140,Artist 2,Album 2,Electronic,House,Evening
file3.mp3,Track 3,2:45,100,Artist 3,Album 3,Rock,Indie,Morning


To download the files, run the following command:

sftp_downloader --csv /path/to/csv/file.csv --remote /path/to/remote/files --local /path/to/local/folder


This will connect to the SFTP server and download the files specified in the CSV file to the local folder.

The following command line arguments are available:

- `--csv`: the path to the CSV file that contains the list of files to download (required)
- `--remote`: the remote path to the files on the SFTP server (required)
- `--local`: the local path to save the downloaded files (required)
- `--host`: the hostname or IP address of the SFTP server (default: localhost)
- `--port`: the port number of the SFTP server (default: 22)
- `--username`: the username for the SFTP server (default: anonymous)
- `--keyfile`: the path to the private key file for the SFTP server (default: None)
- `--local-mode`: if set, it will copy files instead of connecting to sftp.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
