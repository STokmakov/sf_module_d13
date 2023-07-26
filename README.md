# sf_module_d7
D7.5. Итоговое практическое задание:

установка Redis в minikube

redis-server запущен в minikube

kubectl apply -f redis-conf.yaml
kubectl apply -f redis-pod.yaml
kubectl expose deployment redis --type=NodePort (пробрасываем порт 6379 наружу через NodePort)


"# sf_module_d13" 
