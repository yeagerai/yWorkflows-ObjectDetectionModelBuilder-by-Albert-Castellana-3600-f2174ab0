
import typing
from typing import Dict, List, Union
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ObjectDetectionModelBuilderIn(BaseModel):
    annotation_format: str
    deployment_type: str
    image_labels: List[Dict[str, Union[float, List[float]]]]
    model_architecture: str
    model_framework: str
    uploaded_images: List[bytes]


class ObjectDetectionModelBuilderOut(BaseModel):
    deployed_url: str
    deployment_status: str
    trained_model_path: str


class ObjectDetectionModelBuilder(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ObjectDetectionModelBuilderIn, callbacks: typing.Any
    ) -> ObjectDetectionModelBuilderOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        deployed_url = results_dict[0].deployed_url
        deployment_status = results_dict[1].deployment_status
        trained_model_path = results_dict[2].trained_model_path
        out = ObjectDetectionModelBuilderOut(
            deployed_url=deployed_url,
            deployment_status=deployment_status,
            trained_model_path=trained_model_path,
        )
        return out


load_dotenv()
object_detection_model_builder_app = FastAPI()


@object_detection_model_builder_app.post("/transform/")
async def transform(
    args: ObjectDetectionModelBuilderIn,
) -> ObjectDetectionModelBuilderOut:
    object_detection_model_builder = ObjectDetectionModelBuilder()
    return await object_detection_model_builder.transform(args, callbacks=None)

