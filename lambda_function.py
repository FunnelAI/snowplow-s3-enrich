""" FunnelAI's snowplow enricher """
from enricher import enrich

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    enrich(bucket_name, file_key)
