# cloud-infrastructure-platform
Cloud Infrastructure Self Service Portal using Terraform, GCP, Kubernetes and GitOps


# Cloud Infrastructure Self-Service Portal

## Objective

Automate cloud infrastructure provisioning using:

- Next.js
- FastAPI
- Terraform
- GCP
- Kubernetes
- GitHub Actions
- OPA Policies
- Jira Integration

## Architecture

Developer
|
Jira Ticket
|
FastAPI
|
Terraform
|
GCP Resources


UUID means Universally Unique Identifier


We built a Cloud Infrastructure Self-Service Platform to automate infrastructure provisioning. Instead of developers manually raising tickets and waiting for DevOps teams, they can submit infrastructure requests through a portal or Jira. The request is received by a FastAPI backend, which validates and stores the request. Based on the request details, the platform generates Terraform configurations and creates a GitHub Pull Request. The PR goes through CI/CD validation, including Terraform validation, planning, and OPA security policy checks. If all checks pass, the changes are approved and Terraform provisions the required GCP resources like GKE namespaces, Cloud Storage buckets, BigQuery datasets, and IAM service accounts. Once provisioning is completed, the platform updates the request status and sends the details back to the dashboard and Jira ticket.


1. High Performance

FastAPI is built on:

Starlette (web framework)
Pydantic (data validation)
ASGI (asynchronous server interface)


------------------------
SQLAlchemy

Python ORM.

Instead of writing SQL:

INSERT INTO infrastructure_requests
VALUES(...)

we write Python:

request = InfrastructureRequestModel(...)
db.add(request)
---------------------------------------------------

Responsibilities become clear:

API → Receives HTTP requests
Service → Business logic
Repository → Database operations only
Terraform → Infrastructure provisioning
GitHub → PR creation
Jira → Ticket updates

------------------------------------------------------
   .env
                      │
                      ▼
          app/core/settings.py
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
   main.py      database.py      future modules
      │               │               │
      ▼               ▼               ▼
  FastAPI        PostgreSQL      Jira/GitHub/GCP

  -----------------------------------------------------


  Cloud Infrastructure Self-Service Platform
Final Goal

Build an enterprise-grade Internal Developer Platform where a developer can raise a Jira request and the platform automatically provisions cloud infrastructure.

Final workflow:

Developer
    │
    ▼
Raise Jira Ticket
    │
    ▼
Portal Fetches Ticket Details
    │
    ▼
Portal Dashboard
    │
    ▼
Developer Clicks Approve/Create
    │
    ▼
Backend Validation
    │
    ▼
Create GitHub Branch
    │
    ▼
Generate Terraform Code
    │
    ▼
Create Pull Request
    │
    ▼
OPA Policy Validation
    │
    ▼
Merge PR
    │
    ▼
GitHub Actions
    │
    ▼
Terraform Apply
    │
    ▼
GCP Resources Created
    │
    ▼
Update Jira Comments
    │
    ▼
Dashboard Status Updated
Final Architecture
                    Next.js Frontend
                           │
                           ▼
                   FastAPI Backend
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     PostgreSQL        GitHub API      Jira API
          │                │                │
          ▼                ▼                ▼
      Request DB       Pull Requests    Comments
                           │
                           ▼
                      GitHub Actions
                           │
                           ▼
                     Terraform Apply
                           │
                           ▼
                           GCP
          ┌─────────────────────────────────────────┐
          │ Namespace │ Bucket │ IAM │ GKE │ BQ │ SA │
          └─────────────────────────────────────────┘
                           │
                           ▼
                    Cloud Monitoring
                           │
                           ▼
                     Dashboard Status
Technology Stack
Layer	Technology
Frontend	Next.js + TypeScript + Tailwind CSS
Backend	FastAPI
Database	PostgreSQL
ORM	SQLAlchemy
Cloud	Google Cloud Platform
IaC	Terraform
Container	Docker
Kubernetes	GKE
CI/CD	GitHub Actions
SCM	GitHub
Ticketing	Jira
Policy Engine	OPA
AI	Gemini
Monitoring	Cloud Logging + Cloud Monitoring
Sprint Plan
Sprint 0 ✅ Infrastructure & Development Setup

Completed:

✅ Git
✅ GitHub Repository
✅ VS Code
✅ Python
✅ Node.js
✅ Docker
✅ Terraform
✅ GCloud CLI
✅ Kubectl
✅ Helm
✅ Virtual Environment
✅ Folder Structure
Sprint 1 (Current Sprint)
Backend Foundation

Completed:

✅ FastAPI
✅ Health API
✅ API Router
✅ Versioning
✅ Request Schema
✅ Response Schema
✅ Service Layer
✅ PostgreSQL (Docker)
✅ Environment Variables
✅ Pydantic Settings
✅ SQLAlchemy Setup
✅ Database Model
✅ Table Creation

Remaining:

Repository Layer
Save Request into PostgreSQL
Get Request by ID
Get All Requests
Update Status
Delete Request
Exception Handling
Logging
Unit Tests
Sprint 2
Frontend

We'll build:

Dashboard
Sidebar
Header
Infrastructure Request Form
Request History
Request Details
Status Page

Frontend will call FastAPI.

Sprint 3
Terraform Integration

Instead of hardcoded data:

Request

↓

Generate Terraform Variables

↓

Terraform Init

↓

Terraform Plan

↓

Terraform Apply

Resources we'll support initially:

GKE Namespace
Cloud Storage Bucket
Service Account
IAM Bindings
BigQuery Dataset
Sprint 4
GitHub Automation

Workflow:

Request

↓

Generate Terraform Files

↓

Create Branch

↓

Commit

↓

Create Pull Request

↓

Dashboard Updated
Sprint 5
Jira Integration

Workflow:

Developer raises Jira Ticket

↓

Portal fetches details

↓

Populate Request Form

↓

Developer submits

↓

Jira comments updated

↓

Status synchronized
Sprint 6
GitHub Actions

Workflow:

PR Merged

↓

GitHub Actions Triggered

↓

Terraform Apply

↓

Provision Resources

↓

Update Database

↓

Update Jira
Sprint 7
OPA Policy Validation

Examples:

CPU <= 8
Memory <= 32Gi
Bucket Naming Rules
Namespace Naming Rules
Environment Restrictions

If validation fails:

PR blocked
Sprint 8
Approval Workflow

Deletion workflow:

Developer

↓

Delete Request

↓

SecOps Approval Required

↓

Approve

↓

Terraform Destroy

↓

Jira Updated
Sprint 9
Monitoring

Dashboard will show:

Total Requests
Pending
Running
Success
Failed
Approval Pending

We'll also add filtering by environment, application, and date.

Sprint 10
AI Assistant (Gemini)

Examples:

Recommend CPU and memory based on application type.
Detect unusual infrastructure requests.
Explain Terraform errors.
Suggest cost optimizations.
Final GCP Resources

Our platform will be able to provision:

Resource	Status
GKE Namespace	✅
Cloud Storage Bucket	✅
BigQuery Dataset	✅
Service Account	✅
IAM Roles	✅
Workload Identity	✅
Kubernetes Deployment	✅
Kubernetes Service	✅
ConfigMaps	✅
Secrets	✅
Ingress	✅
HPA	✅
Cloud Logging	✅
Cloud Monitoring	✅


----------------------------------------------------------

For this project, we'll focus on application infrastructure, not platform infrastructure.

Application infrastructure (our project):

✅ GKE Namespace
✅ Kubernetes Deployment
✅ Storage Bucket
✅ BigQuery Dataset
✅ Service Account
✅ IAM
✅ Artifact Registry
✅ Secret Manager
✅ Workload Identity

