## Weekly Plan vs Progress Report - 2024-09-09

### Review of Last Week's Progress

| Task | Description | Why | Planned Status | Actual Status |
| --- | --- | --- | --- | --- |
| Makemore tutorials | building the makemore neural network | So i can advance my understanding of low level tensor operations from scratch and not within special and closed up software, and to advance my understanding of how state of the art transformers are being used for sequence to sequence problems so im not just lopsided in classification | finish | finished |
| keras offical textbook | Reading francis challoits' - the founder and ceo of keras the high level API for tensorflow - Keras comprehensive textbook, a frameowork to simplify and democratise deep learning | So i can gain practical skills as well as massively advance my understnading of deep learning to not just accumulate knowledge, but accrue the tools to actually build neural networks myself | finish the book by sunday | book finished |
| Scene Classifier | building our neural network for scene classification, and obtaining suitable metrics to subsume into our repo | so that we may overcome are obstacle of insuffcient scene detection capabilties, and have a model that truly works | Enter planned status: to have trained the new model this week and obtain 70%> | 85% model achieved on sunday |
| 85% model achieved on sunday | SAM2 and Florence2 pipeline for image annotation and object + person blurring | have a tool that we can use to label fast quantities of data by finetuning on these large base models that allow us to reconcile otherwise unlabelled sets to supervised deep learning appoaches, and also demo our ability to blur brands or highlight salient people | to overcome the annotation predicament + demo practical use cases  | have the model as close to being ready to perform inference as possible for the practical tasks, and to label a small set with florences phrase grounding and sam2's segmentation |
| OpenCV Project3 course2: radiology AI model | classify from three classes: healthy, Covid and pneumonia lungs to help detect and classify illness from medical images | To implement the first practical example of a classifer model for real world use cases in the course so that one may learn the practical steps neccessary to take data all the way to deploying a model | to have completed this by sunday | code completed and above the neccessary 95% val acc to recieve full marks, but video explanation still yet to be filmed |

### Plan for This Week

| Task | Description | Why | Planned Status |
| --- | --- | --- | --- |
| Add scene classifier to the codebase | reconstruct the scene classifier service to incorporate my new model for scene classifcation and remove the clunky multistage approach used previously | So that we may produce our first high accuracy component of our product locally | to Have my model fully integrated into the codebase |
| SAM2 + florence | build the autolabelling tool + demo on brand and face blurring with both working proerply together  | so that we may build a automatic labelling service in the codebase to massively speed up production of models and potentially free us to actually make some that otherwsie we couldnt | Get a high accuracy demo using the two working locally, and then work with john to figure out how we get this local |
| Finish the remaining material of course2 in opencv, only to be left with the final project  | Finish my computer vision learning materials for advanced computer vision from scratch |  So that i take care of neccessary learning for my profession | To have course2 finished bar the final project at the end |

### Notes and Comments

- Last week was very productive - i hope to find time if things are smooth to continue other non explicit tasks such as broad research that helps me understand how to advance my intelligence and stay up to date with state of the art techniques of interest to us as a team
