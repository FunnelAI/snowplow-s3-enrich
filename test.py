""" Enricher test
"""
import os
import boto3
from enricher import enrich

S3 = boto3.client('s3',
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                  region_name=os.getenv("REGION_NAME"))

enrich('snowplow-funnel-logs',
       'E2TOTHS7895X2G.2019-09-10-21.07bd7ac8.gz',
       S3=S3)
