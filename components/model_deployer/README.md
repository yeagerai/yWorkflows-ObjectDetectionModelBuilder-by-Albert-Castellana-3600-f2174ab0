markdown
# Component Name

ModelDeployer

# Description

The ModelDeployer component deploys a machine learning model on the specified cloud platform and exposes a REST API for real-time object detection.

# Input and Output Models

**ModelDeployerInputDict:**
- `exported_model_path` (str): Path to the exported machine learning model to be deployed.

**ModelDeployerOutputDict:**
- `api_url` (str): URL of the exposed REST API for real-time object detection.

These models use Pydantic for data validation and serialization.

# Parameters

- `cloud_platform` (str): The cloud platform to deploy the model on. Supported platforms are "AWS" and "GCP". Defined in the component configuration file.

# Transform Function

1. Load the platform-specific implementation based on the value of `self.cloud_platform`.
2. Initialize the `DeployModel` class with the `args.exported_model_path`.
3. Call the `deploy()` method on the `model_deployer` instance to deploy the model on the chosen platform.
4. Initialize the `ExposeAPI` class.
5. Call the `expose()` method on the `api_exposer` instance to expose the REST API for real-time object detection.
6. Create the `ModelDeployerOutputDict` instance with the `api_url` and return it.

# External Dependencies

This component depends on the following external libraries:

- `os`
- `yaml`
- `dotenv`
- `fastapi`
- `pydantic`

# API Calls

The component calls the following external APIs:

- Platform-specific APIs (AWS or GCP) for deploying the machine learning model and exposing the REST API.

# Error Handling

The component handles errors by raising a ValueError exception with a descriptive error message when an invalid `cloud_platform` value is specified.

# Examples

