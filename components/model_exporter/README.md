
# ModelExporter

Export the trained object detection model into a standardized format (e.g., ONNX, TensorFlow) suitable for deployment. The ModelExporter component receives the trained_model_path, converts the model to the desired format and exports it to a specified output path.

## Initial generation prompt
description: Export the trained object detection model into a standardized format
  (e.g., ONNX, TensorFlow) suitable for deployment.
inputs_from_other_nodes:
- trained_model_path
name: ModelExporter


## Transformer breakdown
- Load the trained object detection model from the input path.
- Convert the model to the specified output_format.
- Save the converted model at the specified output_path.
- Return the exported model path as output.

## Parameters
[{'default_value': 'ONNX', 'description': "The desired standardized format to which the model should be exported. It can be either 'ONNX' or 'TensorFlow'.", 'name': 'output_format', 'type': 'str'}, {'default_value': './exported_models/', 'description': 'The path where the exported model will be saved.', 'name': 'output_path', 'type': 'str'}]

        