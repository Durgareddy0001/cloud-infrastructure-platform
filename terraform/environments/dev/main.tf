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

module "gke" {
  source = "../../modules/gke"

  project_id       = var.project_id
  application_name = var.application_name
  environment      = var.environment
  location         = var.location
}

module "node_pool" {

  source = "../../modules/node_pool"

  project_id       = var.project_id
  location         = var.location
  application_name = var.application_name
  environment      = var.environment

  cluster_name = module.gke.cluster_name
}

module "namespace" {

  source = "../../modules/namespace"

  application_name = var.application_name
  environment      = var.environment

  depends_on = [
    module.gke,
    module.node_pool
  ]
}