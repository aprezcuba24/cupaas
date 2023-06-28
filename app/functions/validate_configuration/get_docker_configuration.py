import yaml

template = '''
apiVersion: v1
kind: Pod
metadata:
  name: backend
  namespace: {namespace}
  labels:
    app.kubernetes.io/name: backend-app
spec:
  containers:
  - name: backend
    image: {docker_name}
    ports:
      - containerPort: {port}
        name: backend-port
    envFrom:
      - configMapRef:
          name: backend-config-env
---
apiVersion: v1
kind: Service
metadata:
  namespace: {namespace}
  name: backend-service
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: backend-app
  ports:
  - name: backend-service-port
    protocol: TCP
    port: 80
    targetPort: backend-port
---
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: {namespace}
  name: backend-config-env
{env}
'''


def get_docker_configuration(namespace, docker_name, version, env):
    image_name = f"{docker_name}:{version}"
    port = '5000'
    env["PORT"] = port
    return template.format(
        namespace=namespace,
        docker_name=image_name,
        port=port,
        env=yaml.dump({"data": env}),
    ), image_name, port
