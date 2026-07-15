variable "project_id" {
  type = string
}

variable "application_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "location" {
  type = string
}

variable "role" {
  type = string
}

variable "bucket_required" {
  type = bool
}

variable "bigquery_required" {
  type = bool
}

variable "service_account_required" {
  type = bool
}