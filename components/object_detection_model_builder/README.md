markdown
# Component Name

ObjectDetectionModelBuilder

# Description

The `ObjectDetectionModelBuilder` is a Yeager Workflow component designed to create and train an object detection model and deploy it. It takes in annotated images and user-defined model settings, trains the model, and deploys it to a specified platform.

# Input and Output Models

The component uses Pydantic for input and output data validation and serialization. There are two custom data models for the `ObjectDetectionModelBuilder`:

- `ObjectDetectionModelBuilderIn`: Represents the input data format.
  - annotation_format: str
  - deployment_type: str
  - image_labels: List[Dict[str, Union[float, List[float]]]]
  - model_architecture: str
  - model_framework: str
  - uploaded_images: List[bytes]

- `ObjectDetectionModelBuilderOut`: Represents the output data format.
  - deployed_url: str
  - deployment_status: str
  - trained_model_path: str

# Parameters

The `ObjectDetectionModelBuilder` class does not take any parameters in its constructor method.

# Transform Function

The `transform()` method of `ObjectDetectionModelBuilder` does the following steps:

1. Calls the `transform()` method of the parent (AbstractWorkflow) class with the input data (`args`) and callbacks, receiving a `results_dict` in return.
2. Extracts `deployed_url`, `deployment_status`, and `trained_model_path` from the `results_dict`.
3. Creates an instance of `ObjectDetectionModelBuilderOut` with the extracted values and returns it to the caller.

# External Dependencies

- typing: Provides type hints
- dotenv: Loads environment variables
- fastapi: For creating a FastAPI application
- pydantic: For creating input and output data models
- core.workflows.abstract_workflow: Provides the `AbstractWorkflow` base class

# API Calls

None

# Error Handling

The component does not implement any specific error handling logic. Errors will be propagated to the caller, and it is the caller's responsibility to catch and handle exceptions.

# Examples

Here's an example of how to use the `ObjectDetectionModelBuilder` in a Yeager Workflow:

