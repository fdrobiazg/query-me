# query-me
Simple web app that returns the ip address of the requesting client or the list of ip adressess thath have queried the app in the past.

&nbsp;
## Installation
### Docker 

The below script builds the docker image and runs it on the local machine.
``` sh
./run.sh
```

> :warning: **If you are using mobile browser**: Please note that the container is set to run on the host network therefore it should only be used for development/testing purpose. The solution is also limitted to Linux OS and might not be working properly on Docker for macOS/Windows.

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

Build the image by running
```console
docker build -t query-me:v1 .
```

Reuse Docker daemon inside minikube cluster using
```console
eval $(minikube docker-env)
```

Create namespace for the application
```console
kubectl create namespace query-me
```


Create application deployment using <i>deployment-query-me.yaml</i>
```console
kubectl apply -f deployment-query-me.yaml
```

Expose application by creating service
```console
kubectl expose deployment query-me --name=query-me-svc --type=NodePort --port 80 --target-port 5002
```

#### Health check

Check if created pod(s) are running
```console
kubectl get pods -n query-me
```

SSH to Minikube
```console
minikube ssh
```

Check the ip address of created NodePort
```console
kubectl get svc -n query-me
```

Use this address for the health check
```console
curl -v {{ SERVICE_IP_ADDRESS }}:5002/api/health
```

You should get the 200 status along with
```console
{
  "status": "healthy"
}
```

## Usage





