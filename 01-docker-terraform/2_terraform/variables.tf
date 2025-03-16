variable "credentials" {
  description = "GCP Credentials"
  default     = "keys/srvc_acct_kys.json"
}

variable "project" {
  description = "Project"
  default     = "storied-imprint-447506-j9"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Location"
  default     = "US"
}

variable "bq_dataset" {
  description = "My BigQuery dataset"
  default     = "my_demo_bq_dataset"
}

variable "gcp_bucket_name" {
  description = "GCP Storage Name"
  default     = "storied-imprint-447506-j9-terra-bucket"
}

variable "gcp_storage_class" {
  description = "GCP Bucket Storage Class"
  default     = "STANDARD"
}