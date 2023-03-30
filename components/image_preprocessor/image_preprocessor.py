
import os
from typing import List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel
import yaml
from PIL import Image

from core.abstract_component import AbstractComponent


class ImagePreprocessorInput(BaseModel):
    uploaded_images: List[Image.Image]


class ImagePreprocessorOutput(BaseModel):
    preprocessed_images: List[Image.Image]


class ImagePreprocessor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.target_size: Tuple[int, int] = yaml_data["parameters"]["target_size"]
        self.normalization_factor: float = yaml_data["parameters"]["normalization_factor"]
        self.consistent_format: str = yaml_data["parameters"]["consistent_format"]

    def transform(
        self, args: ImagePreprocessorInput
    ) -> ImagePreprocessorOutput:
        preprocessed_images = []
        for image in args.uploaded_images:
            image = image.convert(self.consistent_format.upper())
            image = image.resize(self.target_size)
            image = image.point(lambda p: p / self.normalization_factor)
            preprocessed_images.append(image)

        return ImagePreprocessorOutput(preprocessed_images=preprocessed_images)


gen_img_preprocessor_app = FastAPI()


@gen_img_preprocessor_app.post("/transform/")
async def transform(
    args: ImagePreprocessorInput,
) -> ImagePreprocessorOutput:
    img_preprocessor = ImagePreprocessor()
    return img_preprocessor.transform(args)

