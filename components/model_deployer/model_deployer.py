
import os

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent

# Define Input and Output Data Models
class ModelDeployerInputDict(BaseModel):
    exported_model_path: str


class ModelDeployerOutputDict(BaseModel):
    api_url: str


class ModelDeployer(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.cloud_platform: str = yaml_data["parameters"]["cloud_platform"]

    def transform(
        self, args: ModelDeployerInputDict
    ) -> ModelDeployerOutputDict:

        print(f"Executing the transform of the {type(self).__name__} component...")

        # Load Platform-specific implementation
        if self.cloud_platform.upper() == "AWS":
            from deployment_aws import DeployModel, ExposeAPI
        elif self.cloud_platform.upper() == "GCP":
            from deployment_gcp import DeployModel, ExposeAPI
        else:
            raise ValueError("Invalid cloud_platform specified.")

        # Deploy the model on the chosen platform
        model_deployer = DeployModel(args.exported_model_path)
        model_deployer.deploy()

        # Expose the REST API for real-time object detection
        api_exposer = ExposeAPI()
        api_url = api_exposer.expose()

        out = ModelDeployerOutputDict(api_url=api_url)
        return out


load_dotenv()
model_deployer_app = FastAPI()


@model_deployer_app.post("/transform/")
async def transform(
    args: ModelDeployerInputDict,
) -> ModelDeployerOutputDict:
    model_deployer = ModelDeployer()
    return model_deployer.transform(args)
