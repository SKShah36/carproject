# car_project
## Installation
First, install the car_project following:
- [NodeJS](https://nodejs.org/en/) (v4.x.x recommended)
- [MongoDB](https://www.mongodb.com/)
- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)
- For more information [click here](https://webgme.readthedocs.io/en/latest/getting_started/dependencies.html)
- In order to create your own repository [Follow steps](https://webgme.readthedocs.io/en/latest/getting_started/creating_a_repository.html)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using car_project!

## Metamodel
The metadel consists of definitions for configuring a car. It provides the user their own model of a car.

## Plugin1
A simple plugin 'Cost Calculator' provides configuration and estimates the cost of service based on how you have configured the car. 

## Plugin2

This plugin generates:
1. tree.json which has json data of the entire model traversed in it.
2. meta.json which consists of entire meta data of the meta nodes.

## How to run
If you are building your deployment from scratch, having installed the dependencies mentioned above, follow the steps:
1. Navigate to http://localhost:<port_number>. By default, it is 8088 so you can type in http://localhost:8888 in the address bar, if you haven't configured any changes.
2. If you want to see how a new project is created, Go to Create New. Otherwise, our deployment already has Car_project as the project. If you choose to launch it, then skip step 3.
3. Import the .webgmex file that is provided with the project.
4. You have your car configuration metamodel ready.
### Building a car model
5. In order to check out the Examples, in the Visualizer pane on the left, navigate to Composition selector.
6. Double click Car_repository. There is a BMW-3-Series and Toyota-RAV example already checked in.
7. In order to create another example, inside the 'Car_respository' drag a Car object from Decorated Part list, on your left.
8. You can rename the example to your choice by double-clicking on it.
9. Now navigate inside the <New_Example>. 
10. You will find car elements from the same Decorated Part list on your left. Drag and drop elements. Make connections and controls by dragging arrows from the elements.

### Running plugin1

11. On the top left side, click on the 'play' button. It will list out all the plugins that can be currently executed for a state machine. Currently, it is Cost Calculator Plugin. Click on it.
12.1. Make sure, if you are using your own deployment and the webgmex file for this project then you have config.plugin.allowServerExecution = true; line added to config/config.default.js from the root of your repository.
12.2. Run the plugin. This should generate an artifact by <Car_name>.py
13. Open the file. It provides details about the car and provides an estimation for a designed configuration.

To checkout the plugin code from the root of your repository, navigate to src/plugins/CostCalculator/CostCalculator. Open __init__.py

### Running plugin2

1. Follow the same instructions as for plugin 1 but instead navigate to the root of the model and run the plugin from there.
2. From there find the play button and run the 'extractdata' plugin.
3. It should generate urls to two artifacts: tree.json and meta.json.

To checkout the plugin code from the root of your repository, navigate to src/plugins/extractdata/extractdata. Open __init__.py
