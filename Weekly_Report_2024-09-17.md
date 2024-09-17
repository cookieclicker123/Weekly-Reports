## Weekly Plan vs Progress Report - 2024-09-17

### Review of Last Week's Progress

| Task | Description | Why | Planned Status | Actual Status |
| --- | --- | --- | --- | --- |
| efficientNet integration | integrating the new scene detection model into aiux | because we wanted our own model to benefit from control, specificity, and a faster higher fecundity model. Long term building in house from first principles is the only way. | complete by last sunday | completed with upgrades today, monday, with more improvements than planned. The llm is no longer being relied on, thus reducing latency and very importantly deterministic outcomes, as the geometric transform will always trigger the same class unlike llms. In addition, i have solved the num of scenes issue, producing 1 on our demo scene. |
| completing the remaining opencv material for course two: mastering computer vision. | the advanced sibling of the first course, so from first principles i can gather the knowledge needed by a computer vision engineer. | Massively aiding in my ability to produce multimodal deep learning workflows | complete the remaining material, up to the final project | completed up to project 4 |
| sam2 demo | use florence and sam2 to produce main speakers in video, and blur out abstract, changing concpets like brands | so that we may produce advanced instance segments of many objects in a given frame to not only produce a shall we say a hihgly accurate, where what and when tool, but also to overcome the annotation burden of supervised learning | to finish by last sunday | not finshed. cannot produce locally, even if using mps, would not be as accurate and take insanely long, and cannot use colab as credits have ran out, and cannot use kaggle as it only supports datasets and models. I am very close to having it working over the cloud and have it running to the last block, where it is unable to support disk space. Has been a great learning curve however allocating resource to gpu time and learning what this very practical workflow is all about. Help is required to overcome the memory issue with torch, which should be solved easily enough with your help.  |

### Plan for This Week

| Task | Description | Why | Planned Status |
| --- | --- | --- | --- |
| sam2 demo | to get the sam2 demo working over cloud for salience detection and dataset annotation | to expand the representations we model, hence enhancing all image and text based workflows we embark on | to check in with John and have this hopefully working tomorrow: Tuesday |
| efficientNetb7 places 365 model | to use the very massive variant of efficientnet, which weve already produced very promising results in and working deterministcally and accruately on our tst harness, and the correspondingly bigger borther of places205, to produce our best model yet | so we can take on more classes and gain from the nunace obtained from wider class variance, and supporting this with much larger num of images per class, and a model that can match this rich data with the greater representations it can form as opposed to efficientNetb3 | to have this working byt the end of the week, obtaining 90% validation accuracy |
| to complete project 4 opencv course | build the face mask detection model | so that i may gain even more practical experience building deep learning models, which i have gained much from  | to finish by friday |

### Notes and Comments

- sam2 demo is technically working, but i underestimated the sheer memory consumption used on inference by the large sam2 and florecne base models, and i learned the valuable lesson that compute is neccesary but not sufficient, dynamically freeing up disk space on inference is equally important. mixed precision and smaller batches shouyld fix this but we will check in as you likely have other insights. it was great top build a cloud workflow and have learned many practical new skills last week, especially in efficient use of the ram and compute
