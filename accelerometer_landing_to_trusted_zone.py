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

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-s3/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1693315552442 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-s3/customer/trusted/"], "recurse": True},
    transformation_ctx="CustomerTrusted_node1693315552442",
)

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1693315680778 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustomerTrusted_node1693315552442,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="CustomerPrivacyFilter_node1693315680778",
)

# Script generated for node Drop Fields
DropFields_node1693315932531 = ApplyMapping.apply(
    frame=CustomerPrivacyFilter_node1693315680778,
    mappings=[
        ("user", "string", "user", "string"),
        ("timeStamp", "long", "timeStamp", "long"),
        ("x", "double", "x", "float"),
        ("y", "double", "y", "float"),
        ("z", "double", "z", "float"),
    ],
    transformation_ctx="DropFields_node1693315932531",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1693315932531,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-s3/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="AccelerometerTrusted_node3",
)

job.commit()
