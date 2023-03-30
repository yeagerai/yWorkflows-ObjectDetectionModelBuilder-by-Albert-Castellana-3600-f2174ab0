
import pytest
from PIL import Image
from io import BytesIO
import numpy as np
from components.image_preprocessor import ImagePreprocessor, ImagePreprocessorInput, ImagePreprocessorOutput

# Import any other necessary libraries

# Create a function to generate a test image for mocking purposes
def generate_test_image(width, height):
    test_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    test_image = Image.fromarray(test_array, "RGB")
    return test_image

# Define test cases
test_cases = [
    # Test Case 1: Single image, default settings
    {
        "input_data": ImagePreprocessorInput(uploaded_images=[generate_test_image(100, 100)]),
        "expected_output_width": 64,
        "expected_output_height": 64,
        "expected_output_format": "RGB"
    },
    # Test Case 2: Multiple images, default settings
    {
        "input_data": ImagePreprocessorInput(uploaded_images=[
            generate_test_image(100, 100),
            generate_test_image(150, 150),
            generate_test_image(200, 200)
        ]),
        "expected_output_width": 64,
        "expected_output_height": 64,
        "expected_output_format": "RGB"
    }
    # Add more test cases, including edge cases and error scenarios, if applicable
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_case", test_cases)
def test_image_preprocessor_transform(test_case):
    # Instantiate the component
    img_preprocessor = ImagePreprocessor()

    # Call the component's transform() method with the mocked input data
    output_data: ImagePreprocessorOutput = img_preprocessor.transform(test_case["input_data"])

    # Assert that the output data matches the expected output data
    assert len(output_data.preprocessed_images) == len(test_case["input_data"].uploaded_images)

    for image in output_data.preprocessed_images:
        assert image.width == test_case["expected_output_width"]
        assert image.height == test_case["expected_output_height"]
        assert image.mode == test_case["expected_output_format"]

        # Check if image is sufficiently normalized
        image_array = np.array(image)
        assert not (image_array * img_preprocessor.normalization_factor > 255).any()

    # Include any error handling and additional checks for edge case scenarios, if applicable
