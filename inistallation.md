# Docker Workshop Installation Guide

#### Welcome to the Docker workshop
#### This guide will help you set up your environment to participate in the workshop. 
#### Please follow the steps below:


## Prerequisites

Before you begin, ensure that you have administrative access to your Linux distribution.

## Step 1: Install Docker

### Ubuntu/Debian:
1. Open a terminal.
2. Run the following commands:
```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

```

### Cent OS:
1. Open a terminal.
2. Run the following commands:
```bash
sudo yum check-update
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce docker-ce-cli containerd.io

```

### Fedora:
1. Open a terminal.
2. Run the following commands:
```bash
sudo dnf check-update
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo=https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io

```
## Step 2: Start Docker Service
- After installation, start the Docker service using the following command:
```bash
sudo systemctl start docker
```

## Step 3: Verify Installation
- Run the following command to verify that Docker is installed correctly:
```bash
docker --version
```
## Step 4: Pull Docker Images
- MySQL:
```bash
docker pull mysql:latest

```
- Nginx:
```bash
docker pull nginx:latest

  ```
- Redis:
```bash
docker pull redis:latest

  ```

### You're all set up! Attend the workshop and enjoy learning about Docker.



