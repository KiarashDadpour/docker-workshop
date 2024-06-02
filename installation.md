#Docker Workshop Installation Guide

#### Welcome to the Docker workshop
#### This guide will help you set up your environment to participate in the workshop. 
#### Please follow the steps below:


## Prerequisites

Before you begin, ensure that you have administrative access to your Linux distribution. 

## Step 0: Set DNS
1. Open a terminal.
2. Run the following commands:
``` bash
vi /etc/resolv.conf
```
3. Press Enter and delete all lines and paste these DNS:
```
nameserver 78.157.42.101
nameserver 78.157.42.100
```
4. Press "Esc : wq" for save resolv.conf file. 

## Step 1: Install Docker

### Ubuntu/Debian:
1. Open a terminal.
2. Run the following commands:
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Cent OS:
1. Open a terminal.
2. Run the following commands:
```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
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
docker image pull mysql:latest

```
- Nginx:
```bash
docker image pull nginx:latest

  ```
- Ubuntu:
```bash
docker image pull ubuntu:latest

  ```
- Redis:
```bash
docker image pull redis:latest

  ```

### You're all set up! Attend the workshop and enjoy learning about Docker.



