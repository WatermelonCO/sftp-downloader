import argparse
import csv

import pysftp


def main():
    # Define command line arguments
    parser = argparse.ArgumentParser(
        description='Download files from an SFTP server based on a CSV file.')
    parser.add_argument('csv_file', type=str, help='path to the CSV file')
    parser.add_argument('remote_path',
                        type=str,
                        help='remote path to the files on the SFTP server')
    parser.add_argument('local_path',
                        type=str,
                        help='local path to save the downloaded files')
    parser.add_argument('--hostname',
                        type=str,
                        default='sftp.example.com',
                        help='SFTP server hostname')
    parser.add_argument('--username',
                        type=str,
                        default='username',
                        help='SFTP server username')
    parser.add_argument('--private_key',
                        type=str,
                        help='path to the private key file')

    # Parse command line arguments
    args = parser.parse_args()

    # Connect to SFTP server
    with pysftp.Connection(args.hostname,
                           username=args.username,
                           private_key=args.private_key) as sftp:
        # Open CSV file
        with open(args.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Get filename from CSV row
                filename = row['filename']

                # Download file
                sftp.get(args.remote_path + '/' + filename,
                         args.local_path + '/' + filename)


if __name__ == '__main__':
    main()
