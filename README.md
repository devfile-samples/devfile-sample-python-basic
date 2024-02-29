# Creating an application with a Python code sample

**Note:** The Python code sample version `2.0.0` uses the **8080** HTTP port.

Before you begin creating an application with this `devfile` code sample, it's helpful to understand the relationship between the `devfile` and `Dockerfile` and how they contribute to your build. You can find these files at the following URLs:

- [Sample Python `devfile.yaml`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/v2.0.0/devfile.yaml)
- [Sample Python `Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/v2.0.0/docker/Dockerfile)
- [Parent Python `devfile.yaml`](https://github.com/devfile/registry/blob/main/stacks/python/3.0.0/devfile.yaml)

This code sample has a parent devfile where it inherits most of the components and commands. The devfile contained in this repository is responsible for overwriting pieces of the parent devfile.

1. The parent `devfile.yaml` file has an [`build` component](https://github.com/devfile/registry/blob/main/stacks/python/3.0.0/devfile.yaml#L39-L45) that points to your `Dockerfile`.
2. The [`docker/Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/v2.0.0/docker/Dockerfile) contains the instructions you need to build the code sample as a container image.
3. The `devfile.yaml` [`deploy` component](https://github.com/devfile-samples/devfile-sample-python-basic/blob/v2.0.0/devfile.yaml#L25-L37) overwrites the parent `deploy` and points to a `deploy.yaml` file that contains instructions for deploying the built container image.
4. The parent `devfile.yaml` [`deploy` command](https://github.com/devfile/registry/blob/main/stacks/python/3.0.0/devfile.yaml#L82-L89) completes the [outerloop](https://devfile.io/docs/2.2.0/innerloop-vs-outerloop) deployment phase by pointing to the `build` and `deploy` components to create your application.

### Additional resources

- For more information about Python, see [Python](https://www.python.org/).
- For more information about devfiles, see [Devfile.io](https://devfile.io/).
- For more information about Dockerfiles, see [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).
