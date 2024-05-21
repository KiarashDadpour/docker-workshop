# Docker Workshop Installation Guide

#### Welcome to the Docker workshop
#### This guide will help you set up your environment to participate in the workshop. 
#### Please follow the steps below:


## Prerequisites

Before you begin, ensure that you have administrative access to your Linux distribution.

## Step 1: Install Docker

### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"


```

### Cent OS:
```bash
sudo yum install -y docker-ce docker-ce-cli containerd.io
```

### Fedora:
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io
```
