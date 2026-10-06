import boto3

# My first AWS automation - S3 bucket creator
# This is what Cloud Support Engineers use daily

def create_s3_bucket(bucket_name, region='af-south-1'):
    """Create S3 bucket in Cape Town region"""
    print(f"Creating bucket: {bucket_name} in {region}")
    # s3 = boto3.client('s3', region_name=region)
    # s3.create_bucket(Bucket=bucket_name)
    print("Bucket created successfully! (simulation - needs AWS creds)")

# My buckets
buckets = ["tumelo-cloud-backup-2026", "tumelo-website-assets"]

for bucket in buckets:
    create_s3_bucket(bucket)

print("All done - Ready for AWS!")
