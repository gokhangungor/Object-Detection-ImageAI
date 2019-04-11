	#Image AI library is imported here
	from imageai.Prediction.Custom import model training

	#Training Model Initiated
	model_trainer = ModelTraining()
	model_trainer.setModelTypeAsResNet()
	model_trainer.setDataDirectory(Directory)
	#Training Started
	model_trainer.trainModel(num_objects=10, num_experiments=100, enhance_data=True,
	batch_size=32, show_network_summary=True)

