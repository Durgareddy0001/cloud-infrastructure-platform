locals {

  service_account_id = "${var.application_name}-${var.environment}-sa"

  display_name = "${title(var.application_name)} Service Account"

  description = "Service Account for ${var.application_name}"
}

resource "google_service_account" "service_account" {
  project      = var.project_id
  account_id   = local.service_account_id
  display_name = local.display_name
  description  = local.description
}