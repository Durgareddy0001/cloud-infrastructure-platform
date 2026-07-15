output "dataset_id" {
  description = "BigQuery Dataset ID"
  value       = google_bigquery_dataset.dataset.dataset_id
}

output "self_link" {
  description = "BigQuery Dataset Self Link"
  value       = google_bigquery_dataset.dataset.self_link
}