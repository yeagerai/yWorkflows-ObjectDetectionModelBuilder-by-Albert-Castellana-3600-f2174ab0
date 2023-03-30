markdown
# Component Name

ImagePreprocessor

## Description

The ImagePreprocessor component is a building block of a Yeager Workflow designed to pre-process a list of images uploaded by users. It resizes the images, normalizes their pixel values, and converts them to a consistent format specified in the component configuration.

## Input and Output Models

### ImagePreprocessorInput

`ImagePreprocessorInput` is a Pydantic BaseModel that consists of just one field:

- `uploaded_images`: A list of PIL.Image objects, which represent the images uploaded by users.

### ImagePreprocessorOutput

`ImagePreprocessorOutput` is another Pydantic BaseModel that contains one field:

- `preprocessed_images`: A list of PIL.Image objects, representing the pre-processed images after the transform() method has been applied.

## Parameters

The component takes three parameters from its YAML configuration file:

- `target_size` (Tuple[int, int]): The target dimensions (width, height) that the input images should be resized to.
- `normalization_factor` (float): A factor used to normalize the pixel values in the images, typically between 0 and 1.
- `consistent_format` (str): The format that all input images should be converted to, specified as a string (e.g., "RGB").

## Transform Function

The `transform()` method of the ImagePreprocessor component takes an `ImagePreprocessorInput` object as its input and returns an `ImagePreprocessorOutput` object. The method processes each uploaded image in the following way:

1. Convert the image to the specified `consistent_format` using the `convert()` method of the PIL.Image class.
2. Resize the image to the `target_size` using the `resize()` method of the PIL.Image class.
3. Normalize the pixel values in the image by dividing them by the `normalization_factor` using the `point()` method of the PIL.Image class.

After processing all uploaded images, the method returns a new `ImagePreprocessorOutput` object containing the pre-processed images.

## External Dependencies

The component depends on the following external libraries:

- `os`: Used to interact with the operating system, such as reading the component configuration file.
- `typing`: Provides type hints for Python, such as the Tuple and List generic types.
- `fastapi`: A modern, high-performance web framework for building APIs with Python.
- `pydantic`: Provides data validation and parsing by creating Python data classes.
- `yaml`: A library used to parse and work with YAML files.
- `PIL.Image` (from Pillow library): Provides a wide range of image processing functions.

## API Calls

The component does not make any external API calls.

## Error Handling

The component does not explicitly handle errors, but any exceptions raised by the PIL.Image class or Pydantic model validation will be propagated back to the caller.

## Examples

To use the ImagePreprocessor component in a Yeager Workflow, you need to create a YAML configuration file with the required parameters first:

