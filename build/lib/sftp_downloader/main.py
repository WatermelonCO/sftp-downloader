import argparse
import csv
import gettext
import os
import sys
from gettext import gettext as _

import pysftp

LOCALE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locale')
DEFAULT_LOCALE = 'en_US'

gettext.install('sftp_downloader', localedir=LOCALE_DIR)
gettext.bindtextdomain('sftp_downloader', LOCALE_DIR)
gettext.textdomain('sftp_downloader')
_ = gettext.gettext


def main():
    parser = argparse.ArgumentParser(description=_(
        "Download files from an SFTP server based on a CSV file."))
    parser.add_argument(
        "--csv",
        required=True,
        help=
        _("The path to the CSV file that contains the list of files to download."
          ),
        metavar=_("CSV_FILE"))
    parser.add_argument(
        "--remote",
        required=True,
        help=_("The remote path to the files on the SFTP server."),
        metavar=_("REMOTE_PATH"))
    parser.add_argument("--local",
                        required=True,
                        help=_("The local path to save the downloaded files."),
                        metavar=_("LOCAL_PATH"))
    parser.add_argument(
        "--host",
        default="localhost",
        help=_("The hostname or IP address of the SFTP server."),
        metavar=_("HOSTNAME"))
    parser.add_argument("--port",
                        type=int,
                        default=22,
                        help=_("The port number of the SFTP server."),
                        metavar=_("PORT_NUMBER"))
    parser.add_argument("--username",
                        default="anonymous",
                        help=_("The username for the SFTP server."),
                        metavar=_("USERNAME"))
    parser.add_argument(
        "--keyfile",
        help=_("The path to the private key file for the SFTP server."),
        metavar=_("PRIVATE_KEY_FILE"))

    # Detect user's locale and set appropriate help message language
    user_locale, _ = gettext.getlocale()
    if user_locale is None:
        user_locale = DEFAULT_LOCALE

    try:
        translator = gettext.translation('sftp_downloader', LOCALE_DIR,
                                         [user_locale])
        parser.set_defaults(_=translator.gettext)
    except FileNotFoundError as fnfe:
        print(fnfe)
        pass

    args = parser.parse_args()

    with pysftp.Connection(args.host,
                           port=args.port,
                           username=args.username,
                           private_key=args.keyfile) as sftp:
        with sftp.cd(args.remote):
            with open(args.csv) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    filename = row['filename']
                    sftp.get(filename, os.path.join(args.local, filename))


if __name__ == '__main__':
    sys.exit(main())
