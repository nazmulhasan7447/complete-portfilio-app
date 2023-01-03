import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "acegroup"
AWS_S3_ENDPOINT_URL = "https://sgp1.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
     "ACL": "public-read"
}
AWS_LOCATION = "https://acegroup.sgp1.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3BotoStorage"
# STATICFILES_STORAGE = 'config.cdn.backends.StaticRootS3BotoStorage'

# DO00YBF33E66ZPYC4G4H
# scrt: dPbMHGbPdDzSXo5/JtHRRmQ37Tn/15oBdZTo9aB7t24