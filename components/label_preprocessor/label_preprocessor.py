
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from core.abstract_component import AbstractComponent
import yaml
import os
from dotenv import load_dotenv

# Define input and output data models
class Label(BaseModel):
    pass  # Replace this with your actual Label structure

class Annotation(BaseModel):
    pass  # Replace this with your actual Annotation structure

class ImageLabelInputDict(BaseModel):
    image_labels: List[Label]

class PreprocessedLabelOutputDict(BaseModel):
    preprocessed_labels: List[Annotation]

# Define the component class
class LabelPreprocessor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            config_data = yaml.safe_load(file)
        self.annotation_format = config_data["parameters"]["annotation_format"]

    def convert_to_coco(self, label: Label) -> Annotation:
        # Implement your conversion method for COCO format
        pass

    def convert_to_pascal_voc(self, label: Label) -> Annotation:
        # Implement your conversion method for Pascal VOC format
        pass

    def transform(self, args: ImageLabelInputDict) -> PreprocessedLabelOutputDict:
        preprocessed_labels = []

        if self.annotation_format == "COCO":
            conversion_method = self.convert_to_coco
        elif self.annotation_format == "Pascal VOC":
            conversion_method = self.convert_to_pascal_voc
        else:
            raise ValueError(f"Unsupported annotation format: {self.annotation_format}")

        for label in args.image_labels:
            preprocessed_label = conversion_method(label)
            preprocessed_labels.append(preprocessed_label)

        return PreprocessedLabelOutputDict(preprocessed_labels=preprocessed_labels)

# Load environment variables
load_dotenv()
label_preprocessor_app = FastAPI()

# Define the FastAPI "/transform/" endpoint
@label_preprocessor_app.post("/transform/")
async def transform(
    args: ImageLabelInputDict,
) -> PreprocessedLabelOutputDict:
    label_preprocessor = LabelPreprocessor()
    return label_preprocessor.transform(args)

