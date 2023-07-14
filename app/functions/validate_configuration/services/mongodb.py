template = """
apiVersion: v1
kind: Pod
metadata:
  name: mongo
  namespace: {namespace}
  labels:
    app.kubernetes.io/name: mongo
spec:
  containers:
  - name: mongo
    image: mongo:{version}
    ports:
      - containerPort: {port}
        name: mongodb-port
---
apiVersion: v1
kind: Service
metadata:
  name: mongo
  namespace: {namespace}
spec:
  selector:
    app: mongo
  ports:
    - port: {port}
      targetPort: mongodb-port
"""


def mongodb(namespace, version):
    port = 27017
    # I am using minikube. I will see what is the url a real kubernates.
    MONGODB_URI = f"mongodb://host.minikube.internal:{port}/{namespace}_db"
    env = {"MONGODB_URI": MONGODB_URI}
    return template.format(namespace=namespace, version=version, port=port), env
