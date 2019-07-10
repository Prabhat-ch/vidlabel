from pathlib import Path

import boto3
import click

@click.option('--profile', default=None, help='Use aws profile name from CLI')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucketname')
@click.command()
def upload_file(profile, pathname, bucketname):
    "upload <pathname> to <bucketname>"

    session_cfg = {}

    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucketname)
    path = Path(pathname).expanduser().resolve()

    bucket.upload_file(str(path), str(path.name))

    return


if __name__=='__main__':
    upload_file()
