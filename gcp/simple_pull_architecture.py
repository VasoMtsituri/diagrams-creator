from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Composer, Dataproc
from diagrams.gcp.compute import Functions
from diagrams.gcp.storage import GCS

with Diagram("Simple ETL pipeline Architecture in GCP", show=True):
    with Cluster("GCP"):
        with Cluster("Composer Environment"):
            composer = Composer("Cloud Composer")
            storage = GCS("Cloud Storage")
            processing = Dataproc("Dataproc Serverless")
            data_warehouse = BigQuery("BigQuery")
            function = Functions("Cloud Function")
            storage >> function >> processing >> data_warehouse