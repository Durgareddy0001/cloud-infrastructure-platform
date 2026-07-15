locals {
  bucket_name = "${var.application_name}-${var.environment}-bucket"
}

resource "google_storage_bucket" "bucket" {
  name     = local.bucket_name
  project  = var.project_id
  location = var.location

  uniform_bucket_level_access = true
  force_destroy               = false
}