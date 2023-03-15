import logging

import pysftp

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Set the hostname, port number, and username for the SFTP server
hostname = 'cdn.watermelonco.es'
port = 2222
username = 'pillow'

# Set the path to your private key file in .pem format

pem_file = '/Users/luke/Downloads/pillow-key.pem'

# create connection object
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(host=hostname,
                       username=username,
                       private_key=pem_file,
                       cnopts=cnopts) as sftp:
    # Test the connection by listing the root directory
    print(sftp.listdir())