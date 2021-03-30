from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
    default_acl = "public-read"


class PrivateRootS3BOTO3Storage(S3Boto3Storage):
    location = "private"
    default_acl = "private"
    file_overwrite = False
    # custom_domain = False
