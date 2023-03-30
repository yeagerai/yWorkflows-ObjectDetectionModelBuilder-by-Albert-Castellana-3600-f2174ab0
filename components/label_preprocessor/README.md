
# LabelPreprocessor

Convert the uploaded labels into the designated annotation format required by the selected object detection model. This component takes image_labels as input and transforms them to the required format for the selected object detection model, enabling seamless integration of label data into the training process.

## Initial generation prompt
description: Convert the uploaded labels into the designated annotation format required
  by the selected object detection model.
inputs_from_other_nodes:
- image_labels
name: LabelPreprocessor


## Transformer breakdown
- Read the value for the 'annotation_format' parameter
- Initialize the corresponding label conversion method based on the 'annotation_format' value
- Iterate through the input 'image_labels' and convert each label to the specified format using the selected conversion method
- Collect the converted labels in a new list called 'preprocessed_labels'
- Return the 'preprocessed_labels' list as output

## Parameters
[{'default_value': 'COCO', 'description': 'The designated annotation format required by the selected object detection model. Supported formats are COCO, Pascal VOC, or custom. Default is set to COCO.', 'name': 'annotation_format', 'type': 'str'}]

        