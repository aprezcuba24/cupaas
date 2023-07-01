template = """
apiVersion: v1
kind: Namespace
metadata:
  name: {name}
"""


def get_namespace(name):
    name = name.replace("/", "-")
    return template.format(name=name), name
