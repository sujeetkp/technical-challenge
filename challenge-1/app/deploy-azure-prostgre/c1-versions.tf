terraform {
  required_version = "~>1.2.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.10.0"
    }
    random = {
      source = "hashicorp/random"
      version = "3.3.1"
    }
  }
  backend "azurerm" {}
}

provider "azurerm" {
  features {}
}

provider "random" {
  # Configuration options
}

# Random String
resource "random_string" "random" {
  length           = 7
  special          = false
}