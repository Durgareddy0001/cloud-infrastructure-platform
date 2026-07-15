output "assigned_role" {
  value = google_project_iam_member.service_account_role.role
}

output "member" {
  value = google_project_iam_member.service_account_role.member
}