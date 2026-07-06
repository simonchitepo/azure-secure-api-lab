variable "project_name" {
  description = "Short project name used for Azure resource naming."
  type        = string
  default     = "secureapi"
}

variable "location" {
  description = "Azure region for the lab."
  type        = string
  default     = "westeurope"
}

variable "container_image" {
  description = "Container image to deploy. After ACR build, use <acrLoginServer>/secure-azure-api-lab:v1."
  type        = string
  default     = "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest"
}

variable "app_port" {
  description = "Port exposed by the container."
  type        = number
  default     = 8080
}

variable "tags" {
  description = "Common Azure tags."
  type        = map(string)
  default = {
    project     = "secure-azure-api-lab"
    owner       = "simon-chitepo"
    environment = "lab"
  }
}
