
# ImagePreprocessor

Resize and normalize input images according to the selected object detection model requirements, and also convert different input formats (png, jpeg) to a consistent format.

## Initial generation prompt
description: Resize and normalize input images according to the selected object detection
  model requirements, and also convert different input formats (png, jpeg) to a consistent
  format.
inputs_from_other_nodes:
- uploaded_images
name: ImagePreprocessor


## Transformer breakdown
- For each image in uploaded_images - Convert the image format to the consistent_format - Resize the image to target_size - Normalize the image using normalization_factor - Add the preprocessed image to the preprocessed_images list
- return preprocessed_images

## Parameters
[{'default_value': '(300, 300)', 'description': 'Target size for resizing the input images (width, height) in pixels.', 'name': 'target_size', 'type': 'Tuple[int, int]'}, {'default_value': 255.0, 'description': 'Normalization factor used for dividing pixel values to scale between 0 and 1.', 'name': 'normalization_factor', 'type': 'float'}, {'default_value': 'jpeg', 'description': 'The consistent format to convert all input images to (e.g. "png", "jpeg").', 'name': 'consistent_format', 'type': 'str'}]

        