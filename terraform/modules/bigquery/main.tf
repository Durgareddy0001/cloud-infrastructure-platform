locals {
  dataset_id = "${replace(var.application_name, "-", "_")}_${var.environment}"
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = local.dataset_id
  project    = var.project_id
  location   = var.location

  delete_contents_on_destroy = false
}