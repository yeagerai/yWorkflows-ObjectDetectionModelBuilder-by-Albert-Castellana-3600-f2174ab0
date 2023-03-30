
import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class PreprocessedImage(BaseModel):
    image: bytes


class ConvertedLabel(BaseModel):
    label: str


class Model(BaseModel):
    content: bytes
    model_type: str


class ModelTrainerInput(BaseModel):
    preprocessed_images: List[PreprocessedImage]
    converted_labels: List[ConvertedLabel]
    model_type: str
    epochs: int
    learning_rate: float


class ModelTrainerOutput(BaseModel):
    trained_model: Model


class ModelTrainer(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(self, args: ModelTrainerInput) -> ModelTrainerOutput:
        # Initialize the selected object detection model
        # Prepare the training dataset with preprocessed_images and converted_labels
        # Set the model training parameters (e.g., epochs, learning_rate)
        # Train the model using the prepared dataset and training parameters
        # Save the trained model in the desired format (e.g., PyTorch, TensorFlow)

        # Replace the following lines with the specific steps for training the model
        trained_model = Model(
            content=b"<model_binary_data_here>",
            model_type=args.model_type,
        )

        return ModelTrainerOutput(trained_model=trained_model)


load_dotenv()
model_trainer_app = FastAPI()


@model_trainer_app.post("/transform/")
async def transform(args: ModelTrainerInput) -> ModelTrainerOutput:
    model_trainer = ModelTrainer()
    return model_trainer.transform(args)

