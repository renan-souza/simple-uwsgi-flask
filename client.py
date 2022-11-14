import os
import requests

from provlake import ProvLake
from provlake.capture import ProvWorkflow, ProvTask

SERVER_HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))
ENDPOINT = os.getenv("ENDPOINT", "retrospective-provenance")

SERVICE_URL = f"http://{SERVER_HOST}:{PORT}"
ENDPOINT_URL = f"{SERVICE_URL}/{ENDPOINT}"


def synthetic_workflow_run():
    workflow_name = "simple-workflow"

    NUMBER_OF_TASKS = 1000
    prov = ProvLake.get_persister("simple-workflow",
                                  bag_size=NUMBER_OF_TASKS+10,
                                                # This value should be fine-
                                                # tuned.
                                                # This is the amount of
                                                # requests to group
                                                # before sending to the server.
                                  should_send_to_file=False,
                                  service_url=SERVICE_URL)

    with ProvWorkflow(prov, workflow_name=workflow_name) as prov_workflow:

        for i in range(NUMBER_OF_TASKS):

            in_args = {"arg1": "val1"}
            with ProvTask(prov,
                          data_transformation_name="simple-activity",
                          prov_workflow=prov_workflow,
                          input_args=in_args) as prov_task:
                out_args = {"out-arg": "out-value"}
                prov_task.end(out_args)


def simple_server_check():
    r = requests.post(ENDPOINT_URL, data={"anything": "anything"})
    assert r.status_code == 200


if __name__ == "__main__":
    synthetic_workflow_run()

