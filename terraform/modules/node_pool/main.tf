locals {
  node_pool_name = "${var.application_name}-${var.environment}-nodepool"
}

resource "google_container_node_pool" "primary_nodes" {

  name       = local.node_pool_name
  cluster    = var.cluster_name
  location   = var.location
  project    = var.project_id

  node_count = 1

  node_config {

    machine_type = "e2-standard-2"

    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}