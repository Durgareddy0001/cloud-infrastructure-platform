locals {
  cluster_name = "${var.application_name}-${var.environment}-gke"
}

resource "google_container_cluster" "gke_cluster" {
  name     = local.cluster_name
  location = var.location
  project  = var.project_id

  deletion_protection = false

  remove_default_node_pool = true
  initial_node_count       = 1
}