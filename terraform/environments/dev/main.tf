module "bucket" {

  count = var.bucket_required ? 1 : 0

  source = "../../modules/bucket"

  project_id       = var.project_id
  application_name = var.application_name
  environment      = var.environment
  location         = var.location
}

module "bigquery" {

  count = var.bigquery_required ? 1 : 0

  source = "../../modules/bigquery"

  project_id       = var.project_id
  application_name = var.application_name
  environment      = var.environment
  location         = var.location
}

module "service_account" {

  count = var.service_account_required ? 1 : 0

  source = "../../modules/service_account"

  project_id       = var.project_id
  application_name = var.application_name
  environment      = var.environment
}

module "iam" {

  count = var.service_account_required ? 1 : 0

  source = "../../modules/iam"

  project_id            = var.project_id
  service_account_email = module.service_account[0].service_account_email
  role                  = var.role
}