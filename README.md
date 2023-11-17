# Memory-checker
The test task includes an application to monitor memory usage and send a signal when memory load is high.

You need to install dependencies by <code>pip install -r requirements.txt</code>

In <code>.env</code> file you have configuration off your app


<code>API_URL</code> - set your url where you will send alarms

<code>MEMORY_LIMIT</code> - set memory limits in MB, when system value of used RAM will be more than this value - app will send alarm.

<code>API_HOST</code> - set address where your API will be deploy

<code>API_PORT</code> - set port where your API will be deploy

After setting configuration you need to start <code>api.py</code> and api service will be deploy and you can start tracking memory by <code>main.py</code> file.
