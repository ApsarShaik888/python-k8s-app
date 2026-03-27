# 🐍 Python Application on Kubernetes

## 📋 Project Overview
A simple Python application containerized with Docker and deployed on Kubernetes using ReplicaSets. This project demonstrates the complete workflow of developing, containerizing, and deploying an application on Kubernetes.

## ✨ Features
- ✅ Python application with unbuffered logging
- ✅ Docker containerization
- ✅ Kubernetes ReplicaSet deployment
- ✅ Self-healing pods
- ✅ Easy scaling with `kubectl scale`
- ✅ Real-time log monitoring

## 🛠️ Prerequisites
- Docker
- Minikube or Kubernetes cluster
- kubectl

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/ApsarShaik888/python-k8s-app.git
cd python-k8s-app
2.Build Docker image
docker build -t python-k8s-app:v4 .
3. Load image into Minikube
minikube image load python-k8s-app:v4
4. Deploy to Kubernetes
kubectl apply -f deployment.yaml
5. Check running pods
kubectl get pods
6. View application logs
kubectl logs -l app=python-app -f or kubectl logs python-k8s-app-783dg
📊 Expected Output
==================================================
 Hostname : python-app-rs-xxxxx
==================================================
1 Hello! This app is alive and running!
2 Hello! This app is alive and running!
3 Hello! This app is alive and running!
...

🧪 Testing Kubernetes Features
Scale the application
# Scale to 5 replicas
kubectl scale rs python-app-rs --replicas=5

# Check pods
kubectl get pods

Test self-healing
# Delete a pod and watch it recreate
kubectl delete pod <pod-name>
kubectl get pods -w


