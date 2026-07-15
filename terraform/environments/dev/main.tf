module "bucket" {
  source = "../../modules/bucket"

  project_id  = var.project_id
  location    = var.location
  bucket_name = var.bucket_name
}

module "bigquery" {
  source = "../../modules/bigquery"

  project_id = var.project_id
  dataset_id = var.dataset_id
  location   = var.location
}