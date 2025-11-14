terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "student_app" {
  name = "srihas0/student-app:latest"
}

resource "docker_container" "student_container" {
  name  = "student_app"
  image = docker_image.student_app.name
  ports {
    internal = 8000
    external = 8000
  }
}