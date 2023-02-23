# query-me
Simple web app that returns the ip address of the requesting client or the list of ip adressess that have queried the app in the past.

&nbsp;
## Installation
### Docker 

The below script builds the docker image and runs it on the local machine.
``` sh
./run.sh
```

> :warning: **Keep in mind**: Please note that the container is set to run on the host network therefore it should only be used for development/testing purpose. The solution is also limitted to Linux OS and might not be working properly on Docker for macOS/Windows.

#### Health check
```console
curl -v 127.0.0.1:5002/api/health
```
You should get the 200 status along with
```console
{
  "status": "healthy"
}
```

&nbsp;
### Minikube

Reuse Docker daemon inside minikube cluster using
```console
eval $(minikube docker-env)
```

Build the image by running
```console
docker build -t query-me:v1 .
```

Create namespace for the application
```console
kubectl create namespace query-me
```

Move to helm chart folder and deploy application using Helm
```console
cd helm-chart/query-me
helm install query-me . -f values.yaml -n query-me
```

You should see
```console
NAME: query-me
LAST DEPLOYED: Thu Feb 23 18:28:01 2023
NAMESPACE: query-me
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

#### Health check

Check if created pod(s) are running
```console
kubectl get pods -n query-me
```

Pod(s) should be in running state as below
```
NAME                        READY   STATUS    RESTARTS   AGE
query-me-7f47c944cd-q4fl8   1/1     Running   0          93m
```

In the seperate terminal expose application NodePort by using
```console
minikube service query-me --url -n query-me
```

Use the obtained address for the health check
```console
curl -v {{ SERVICE_IP }}:5002/api/health
```

You should get the 200 status along with
```console
{
  "status": "healthy"
}
```

&nbsp;
## Usage

To get the client ip address use the following endpoint
```console
{{ SERVICE_IP }}:5002/api/myip
```

Examplary output:
```
{
  "user ip": "192.168.1.4"
}
```
&nbsp;
List of ip addresses could be obtained using following endpoint
```console
{{ SERVICE_IP }}:5002/api/iplist
```
Examplary output:
```
{
  "uptime": "0:02:30.261294",
  "users ip list": [
    "192.168.1.4",
    "192.168.1.6"
  ]
}
```
&nbsp;
## Room for improvement
- Add ingress-route for communication outside of cluster (it would be more convenient to have it exposed just after the deployment)
- Multistage Dockerfile - build and run part (potentially smaller size)








