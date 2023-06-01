import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

empDf = glueContext.create_dynamic_frame.from_catalog(
        database="ineuron-glue-catalog-db",
        table_name="s3ineuron_input_data"
        )

empDf.printSchema()

sparkEmpDf = empDf.toDF()               # Converts the dynamic glue dataframe to Spark DataFrame
sparkEmpDf.show()

df2=sparkEmpDf.select("employee_id")
df2.show()

# job = Job(glueContext)
# job.init(args['JOB_NAME'], args)
# job.commit()
