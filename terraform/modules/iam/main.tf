resource "google_project_iam_member" "service_account_role" {
  project = var.project_id
  role    = var.role
  member  = "serviceAccount:${var.service_account_email}"
}