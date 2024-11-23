# HackSphere
HackSphere is a dockerized app whose purpose is to create the interface for a pentest lab.

## Installation
Install Docker on Ubuntu 22.04:

```bash
# Install the latest version docker
curl -s https://get.docker.com/ | sh

# Run docker service
systemctl start docker
```
Build and run on Linux/macOS:
```bash
# Clone repo
git clone https://github.com/usg-ishimura/hack-sphere.git

# Change directory to cloned repo
cd hack-sphere

# Build from Dockerfile
docker build --tag hack-sphere .

# Run the container
docker run --network=host -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 hack-sphere
