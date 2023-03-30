
# ObjectDetectionModelBuilder

This is a workflow for building and deploying an object detection model. It takes in annotation_format, deployment_type, image_labels, model_architecture, model_framework, and uploaded_images inputs. The process includes creating training data, building the model using the specified architecture and framework, training the model on the image labels, and deploying the model to the specified deployment type. Finally, it outputs the deployed URL, deployment status, and trained model path.


## Initial generation prompt
description: "IOs - InputModel:\n  annotation_format: str\n  deployment_type: str\n\
  \  image_labels: List[Dict[str, Union[float, List[float]]]]\n  model_architecture:\
  \ str\n  model_framework: str\n  uploaded_images: List[bytes]\nOutputModel:\n  deployed_url:\
  \ str\n  deployment_status: str\n  trained_model_path: str\n"
name: ObjectDetectionModelBuilder


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        