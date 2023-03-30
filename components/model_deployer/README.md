
# ModelDeployer

Deploy the exported object detection model on the chosen cloud platform, and expose a REST API for real-time object detection.

## Initial generation prompt
description: Deploy the exported object detection model on the chosen cloud platform,
  and expose a REST API for real-time object detection.
inputs_from_other_nodes:
- exported_model_path
name: ModelDeployer


## Transformer breakdown
- Set up cloud platform credentials and services based on the selected cloud_platform.
- Deploy the model from exported_model_path.
- Expose a REST API for real-time object detection.
- Return the API URL.

## Parameters
[{'default_value': 'AWS', 'description': 'The cloud platform to deploy the model on. Can be either "AWS" or "GCP".', 'name': 'cloud_platform', 'type': 'str'}]

        