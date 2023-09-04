import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Trusted
CustomerTrusted_node1693320268024 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-s3/customer/trusted"], "recurse": True},
    transformation_ctx="CustomerTrusted_node1693320268024",
)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1693320269201 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-s3/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1693320269201",
)

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1693315680778 = Join.apply(
    frame1=CustomerTrusted_node1693320268024,
    frame2=AccelerometerLanding_node1693320269201,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="CustomerPrivacyFilter_node1693315680778",
)

# Script generated for node Drop Fields
DropFields_node1693315932531 = ApplyMapping.apply(
    frame=CustomerPrivacyFilter_node1693315680778,
    mappings=[
        ("serialNumber", "string", "serialNumber", "string"),
        ("shareWithPublicAsOfDate", "long", "shareWithPublicAsOfDate", "long"),
        ("birthDay", "string", "birthDay", "string"),
        ("registrationDate", "long", "registrationDate", "long"),
        ("shareWithResearchAsOfDate", "long", "shareWithResearchAsOfDate", "long"),
        ("customerName", "string", "customerName", "string"),
        ("email", "string", "email", "string"),
        ("lastUpdateDate", "long", "lastUpdateDate", "long"),
        ("phone", "string", "phone", "string"),
        ("shareWithFriendsAsOfDate", "long", "shareWithFriendsAsOfDate", "long"),
    ],
    transformation_ctx="DropFields_node1693315932531",
)

# Script generated for node Customer Curated
CustomerCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1693315932531,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://stedi-s3/customer/curated/", "partitionKeys": []},
    transformation_ctx="CustomerCurated_node3",
)

job.commit()
