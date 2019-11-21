# Experiment HTTPxMQTT

A simple experiment application to post some data to a remote server using both MQTT and HTTP protocols, save results to a .csv file and compare them using a Jupyter Notebook visualization with Matplotlib. 

The experiment uses both a free and open to the [public MQTT broker](http://test.mosquitto.org) and an [open HTTP REST API](http://jsonplaceholder.typicode.com).

To run the experiment you will need:
1. Python3
2. Jupyter noteebok

On the root folder run the following command on a terminal to run the experiment

`python3 setup.py install && python3 runner.py`

After that tou can run the jupyter notebook to generate the visualization.

Check out the results [here](https://github.com/lucasdiniz/mqtt-api/blob/master/ExperimentMqttHttp.ipynb)
