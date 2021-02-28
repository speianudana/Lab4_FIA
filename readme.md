# Model Deployment
## Table of contents
* [Introduction](#general-info)
* [Technologies](#technologies)
* [Sources](#sources)
* [Client endpoints](#client-endpoints)

## Introduction - the project's aim

The task for the laboratory nr.4 is to deploy a machine learning model so that the clients could obtain the prediction from the deployed model. The ML model we will use is the linear regression model from the third laboratory work that had the goal to predict the price for an apartment base on  historical data about apartment complexes on the space station and their prices.
- I’ll first need to register to GitHub Student Pack, so that to be able to use for free a tool for deployment.
- Following, I’ll need to choose a platform to deploy
my model. 
- I’ll need to show how a client can obtain a
prediction from the deployed model.
- I’ll also need to illustrate a simple CI / CD process.
- I’ll need to show that a commit triggers a build and tests to run. If successful, the model should deployed and served once again.

## Technologies
* Python 3.7
* Microsoft Azure
* Flask
* Sklearn
* Panda
* Json

## Sources
* Tool for deployment: https://portal.azure.com/
* Tutorial used in this laboratory: https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e
## Client endpoints

1. For finding the path to dataset: https://lab4-fia.azurewebsites.net/
2. For finding the path to model score: https://lab4-fia.azurewebsites.net/modelScore
3. For finding the path to prediction of the price: https://lab4-fia.azurewebsites.net/predict



