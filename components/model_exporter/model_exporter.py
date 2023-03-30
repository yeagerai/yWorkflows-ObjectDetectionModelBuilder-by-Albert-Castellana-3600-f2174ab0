
import os

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class ModelExporterInputDict(BaseModel):
    trained_model_path: str


class ModelExporterOutputDict(BaseModel):
    exported_model_path: str


class ModelExporter(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.output_format: str = yaml_data["parameters"]["output_format"]
        self.output_path: str = yaml_data["parameters"]["output_path"]

    def transform(
        self, args: ModelExporterInputDict
    ) -> ModelExporterOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Load the trained object detection model from the input path
        trained_model = self.load_trained_model(args.trained_model_path)

        # Convert the model to the specified output_format
        converted_model = self.convert_model(trained_model, self.output_format)

        # Save the converted model at the specified output_path
        exported_model_path = self.save_model(converted_model, self.output_path)

        # Return the exported model path as output
        return ModelExporterOutputDict(exported_model_path=exported_model_path)

    def load_trained_model(self, trained_model_path: str):
        # Implement loading the trained object detection model
        pass

    def convert_model(self, trained_model, output_format: str):
        # Implement converting the model to the specified output_format
        pass

    def save_model(self, converted_model, output_path: str) -> str:
        # Implement saving the converted model at the specified output_path
        pass


load_dotenv()
model_exporter_app = FastAPI()


@model_exporter_app.post("/transform/")
async def transform(
    args: ModelExporterInputDict,
) -> ModelExporterOutputDict:
    model_exporter = ModelExporter()
    return model_exporter.transform(args)

