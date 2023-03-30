
import pytest
from pydantic import BaseModel
from typing import List
from app.component import (
    LabelPreprocessor, Label, Annotation,
    ImageLabelInputDict, PreprocessedLabelOutputDict
)


# Define mocked Label and Annotation classes for testing
class MockedLabel(Label):
    id: int
    name: str

class MockedAnnotation(Annotation):
    id: int
    label: str

# Define test cases with mocked input and expected output data
test_cases = [
    (
        # Input data
        ImageLabelInputDict(
            image_labels=[
                MockedLabel(id=1, name="car"),
                MockedLabel(id=2, name="person")
            ]
        ),
        # Expected output data
        PreprocessedLabelOutputDict(
            preprocessed_labels=[
                MockedAnnotation(id=1, label="Coco_car"),
                MockedAnnotation(id=2, label="Coco_person"),
            ],
            # Component configuration (annotation_format)
            "COCO",
        ),
    ),
    (
        # Input data
        ImageLabelInputDict(
            image_labels=[
                MockedLabel(id=3, name="dog"),
                MockedLabel(id=4, name="bicycle"),
            ]
        ),
        # Expected output data
        PreprocessedLabelOutputDict(
            preprocessed_labels=[
                MockedAnnotation(id=3, label="PascalVOC_dog"),
                MockedAnnotation(id=4, label="PascalVOC_bicycle"),
            ],
            # Component configuration (annotation_format)
            "Pascal VOC",
        ),
    ),
]


@pytest.mark.parametrize("input_data, expected_output, annotation_format", test_cases)
def test_label_preprocessor(input_data, expected_output, annotation_format):
    # Override the component's configuration by setting its 'annotation_format' property
    label_preprocessor = LabelPreprocessor()
    label_preprocessor.annotation_format = annotation_format

    # Call the component's transform() method and assert that the output matches the expected_output
    output = label_preprocessor.transform(input_data)
    assert output == expected_output

    # Add error handling and edge case scenarios, if applicable
    with pytest.raises(ValueError):
        label_preprocessor.annotation_format = "Unsupported format"
        label_preprocessor.transform(input_data)
