locals {
  namespace_name = "${var.application_name}-${var.environment}"
}

resource "kubernetes_namespace_v1" "namespace" {
  metadata {
    name = local.namespace_name

    labels = {
      application = var.application_name
      environment = var.environment
      managed_by  = "terraform"
    }
  }
}