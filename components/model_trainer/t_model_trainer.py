
import pytest
from pydantic import BaseModel
from typing import List
from core.abstract_component import AbstractComponent
from fastapi.testclient import TestClient
from test.component.model_trainer import ModelTrainer, ModelTrainerInput, ModelTrainerOutput, Model, PreprocessedImage, ConvertedLabel

test_preprocessed_images = [
    PreprocessedImage(image=b"<image_data_1>"),
    PreprocessedImage(image=b"<image_data_2>"),
]

test_converted_labels = [
    ConvertedLabel(label="label_1"),
    ConvertedLabel(label="label_2"),
]

test_input_data = ModelTrainerInput(
    preprocessed_images=test_preprocessed_images,
    converted_labels=test_converted_labels,
    model_type="test_model",
    epochs=10,
    learning_rate=0.001,
)

test_output_data = ModelTrainerOutput(
    trained_model=Model(
        content=b"<model_binary_data_here>",
        model_type="test_model",
    ),
)

@pytest.mark.parametrize("input_data, expected_output", [
    (test_input_data, test_output_data),
    # More test cases can be added here
])
def test_model_trainer_component(input_data: ModelTrainerInput, expected_output: ModelTrainerOutput):
    model_trainer = ModelTrainer()
    output_data = model_trainer.transform(input_data)
    assert output_data == expected_output

@pytest.mark.parametrize("input_data", [
    test_input_data,
    # More test cases can be added here
])
def test_model_trainer_component_api(input_data: ModelTrainerInput):
    client = TestClient(model_trainer_app)
    response = client.post("/transform/", json=input_data.dict())
    assert response.status_code == 200
    assert response.json() == ModelTrainerOutput.parse_obj(expected_output).dict()
