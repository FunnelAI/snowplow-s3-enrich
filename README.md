# snowplow-s3-enrich
Lambda script that enriches Snowplow event data and puts it back to S3

For the process described in Bostata blog - https://bostata.com/client-side-instrumentation-for-under-one-dollar/

Snowplow - https://github.com/snowplow/snowplow
Enrichment process: https://github.com/snowplow/snowplow/wiki/Setting-up-Enrich

This solution is an experimental alternative to EmrEtlRunner

A bit more about the background and the approach in blog post at https://www.ownyourbusinessdata.net/enrich-snowplow-data-with-aws-lambda-function/

## Compress to upload to lamvda

`ls | egrep -v "test.py|.env|.git|.vscode|README.md"|zip -9 -@ snowplow_s3_enrich.zip -r`

you can add more files to ignore for compression to that egrep of course.