from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataproc
from diagrams.gcp.compute import Functions
from diagrams.gcp.storage import GCS

with Diagram("Simple Event-driven Architecture in GCP", show=True):
    with Cluster("GCP"):
        storage = GCS("Cloud Storage")
        processing = Dataproc("Dataproc Cluster")
        data_warehouse = BigQuery("BigQuery")
        function = Functions("Cloud Function")

        storage >> function >> processing >> data_warehouse