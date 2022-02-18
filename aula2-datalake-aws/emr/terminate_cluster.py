import os
import time
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


client = boto3.client("emr", region_name="us-east-2",
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

def list_clusters():
    cluster_id = client.list_clusters(
        ClusterStates=['WAITING']
            )
            
    return cluster_id['Clusters'][0]['Id'] 

def terminate_emr_cluster(cid):
    res = client.terminate_job_flows(
        JobFlowIds=[cid]
    )

terminate_emr_cluster(list_clusters())


