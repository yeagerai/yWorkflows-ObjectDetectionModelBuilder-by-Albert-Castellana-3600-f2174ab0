
import pytest
from pydantic import ValidationError
from typing import List, Dict, Union
from fastapi import HTTPException

from app import ObjectDetectionModelBuilder, ObjectDetectionModelBuilderIn, ObjectDetectionModelBuilderOut

# Mocked input data and expected output data for multiple test scenarios
test_data = [
    (
        ObjectDetectionModelBuilderIn(
            annotation_format="coco",
            deployment_type="cloud",
            image_labels=[
                {"category": "dog", "bbox": [114, 60, 281, 205], "score": 0.89},
                {"category": "cat", "bbox": [52, 110, 146, 267], "score": 0.79},
            ],
            model_architecture="ssd",
            model_framework="tensorflow",
            uploaded_images=["mocked_image_1", "mocked_image_2"],
        ),
        ObjectDetectionModelBuilderOut(
            deployed_url="https://example.com/deployed-model",
            deployment_status="success",
            trained_model_path="/path/to/trained/model/file",
        ),
    ),
    # Additional test scenarios and edge cases can be added here
]

@pytest.mark.parametrize("input_data, expected_output", test_data)
async def test_transform(input_data, expected_output):
    # Instantiate the ObjectDetectionModelBuilder class
    object_detection_model_builder = ObjectDetectionModelBuilder()

    # Define a "callbacks" parameter:
    # In this example, we will set it as None since no callbacks are used.
    # Replace "None" with a mocked callback object if callbacks are used in the component.
    callbacks = None

    try:
        # Call the transform() method with mocked input data
        result = await object_detection_model_builder.transform(input_data, callbacks)

        # Assert the output matches the expected output data
        assert result == expected_output
    except Exception as e:
        assert isinstance(e, HTTPException)
        assert e.status_code == 400
        assert e.detail == "Invalid input data."

# Optional: Add tests for error handling and edge case scenarios
