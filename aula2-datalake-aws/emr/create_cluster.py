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

def emr_create_cluster():
    print('Criando Cluster...')
    cluster_id = client.run_job_flow(
        Name='puc-minas-127012818163',
        ServiceRole='EmrDefaultRole',
        JobFlowRole='EmrEc2DefaultRole',
        VisibleToAllUsers=True,
        StepConcurrencyLevel=2,
        LogUri='s3://puc-minas-emr-config/emr-logs',
        ReleaseLabel='emr-6.5.0',
        Instances={
            'InstanceGroups': [
                {
                    'Name': 'Master nodes',
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 1,
                },
                {
                    'Name': 'Worker nodes',
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'CORE',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 3,
                }
            ],
            'Ec2KeyName': 'EmrKey',
            'KeepJobFlowAliveWhenNoSteps': True,
            'TerminationProtected': False,
            'Ec2SubnetId': 'subnet-2684dd6a'
        },
        Applications=[
            {'Name': 'Spark'},
            {'Name': 'Hadoop'},
            {'Name': 'Hive'},
            {'Name':'JupyterEnterpriseGateway'},
            {'Name':'Livy'}
            ],
        Configurations=[
            {
            "Classification": "spark-env",
            "Properties": {},
            "Configurations": [{
                "Classification": "export",
                "Properties": {
                    "PYSPARK_PYTHON": "/usr/bin/python3",
                    "PYSPARK_DRIVER_PYTHON": "/usr/bin/python3"
                }
            }]
        },
            {
                "Classification": "spark-hive-site",
                "Properties": {
                    "hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
                }
            },
            {
                "Classification": "spark-defaults",
                "Properties": {
                    "spark.submit.deployMode": "cluster",
                    "spark.speculation": "false",
                    "spark.sql.adaptive.enabled": "true",
                    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
                    "spark.driver.extraJavaOptions": 
                      "-XX:+UseG1GC -XX:+UnlockDiagnosticVMOptions -XX:+G1SummarizeConcMark -XX:InitiatingHeapOccupancyPercent=35 -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:OnOutOfMemoryError='kill -9 %p'",
                      "spark.storage.level": "MEMORY_AND_DISK_SER",
                      "spark.rdd.compress": "true",
                      "spark.shuffle.compress": "true",
                      "spark.shuffle.spill.compress": "true"
                }
            },
            {
                "Classification": "spark",
                "Properties": {
                    "maximizeResourceAllocation": "true"
                }
            },
            {
              "Classification": "emrfs-site",
              "Properties": {
                "fs.s3.maxConnections": "1000",
            }
            }
        ],
         AutoTerminationPolicy={
            'IdleTimeout': 3600
        }
    )
    return cluster_id["JobFlowId"]      


emr_create_cluster()


