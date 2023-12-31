import os
from trainingModel import trainModel
from training_Validation_Insertion import train_validation



try:

    path = 'Training_Batch_Files'
    train_valObj = train_validation(path) #object initialization

    train_valObj.train_validation()#calling the training_validation function


    trainModelObj = trainModel() #object initialization
    trainModelObj.trainingModel() #training the model for the files in the table


except ValueError:

    print("Error Occurred! %s" % ValueError)

except KeyError:

    print("Error Occurred! %s" % KeyError)

except Exception as e:

    print("Error Occurred! %s" % e)
print("Training successfull!!")
