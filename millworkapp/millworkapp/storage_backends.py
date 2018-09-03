from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    ''' Config for S3 Media storage '''
    location = 'media'
    file_overwrite = False
