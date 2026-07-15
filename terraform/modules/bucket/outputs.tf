output "bucket_name" {
  description = "Name of the created bucket"
  value       = google_storage_bucket.bucket.name
}

output "bucket_url" {
  description = "Bucket URL"
  value       = google_storage_bucket.bucket.url
}