markdown
# Component Name: ModelExporter

## Description

The ModelExporter component is a Yeager Workflow building block designed to load a trained object detection model, convert it to a specified format, and save it to the provided output path. It inherits from the AbstractComponent base class.

## Input and Output Models

### Input Model: ModelExporterInputDict

The input model for the ModelExporter is a Pydantic BaseModel called ModelExporterInputDict, which contains the following field:

- `trained_model_path: str`: The path to the trained object detection model file.

### Output Model: ModelExporterOutputDict

The output model for the ModelExporter is a Pydantic BaseModel called ModelExporterOutputDict, which contains the following field:

- `exported_model_path: str`: The path to the exported model file after conversion.

## Parameters

The ModelExporter component uses the following parameters, which are loaded from its configuration (YAML) file:

- `output_format: str`: The desired output format for the converted model. Supported formats should be documented in the component's configuration file.
- `output_path: str`: The directory where the converted model will be saved.

## Transform Function

The `transform()` method in the ModelExporter component is implemented as follows:

1. Load the trained object detection model from the input path using `load_trained_model()`.
2. Convert the loaded model to the specified `output_format` using `convert_model()`.
3. Save the converted model to the specified `output_path` using `save_model()` and obtain the exported model path.
4. Return the exported model path as part of the `ModelExporterOutputDict`.

## External Dependencies

The ModelExporter uses the following external libraries:

- `pydantic`: For input and output data validation and serialization using BaseModel.
- `yaml`: For loading configuration parameters from the component's YAML file.
- `dotenv`: For loading environment variables.
- `fastapi`: For creating a FastAPI application instance and managing API endpoints.

## API Calls

There are no external API calls made by the ModelExporter component.

## Error Handling

There is no specific error handling implemented in the ModelExporter component. Exceptions should be caught and handled by the calling code or the parent workflow. Implementing proper error handling for tasks like loading, converting, and saving models is recommended.

## Examples

Below is an example of using the ModelExporter component within a Yeager Workflow.

1. First, create a component configuration file (e.g., `model_exporter.yaml`) with the following content:

