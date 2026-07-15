"use client";

import { FormEvent, useEffect, useMemo, useState } from "react";

type RequestStatus = "PENDING" | "IN_PROGRESS" | "COMPLETED" | "FAILED" | "CANCELLED";

type InfrastructureRequest = {
  request_id: string;
  application_name: string;
  environment: string;
  region: string;
  namespace: string;
  cpu: string;
  memory: string;
  node_pool: string;
  storage_bucket?: string | null;
  bigquery_dataset?: string | null;
  service_account?: string | null;
  status: RequestStatus;
};

type RequestForm = Omit<InfrastructureRequest, "request_id" | "status">;

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000/api/v1";
const statuses: RequestStatus[] = ["PENDING", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"];
const initialForm: RequestForm = {
  application_name: "", environment: "dev", region: "asia-south1", namespace: "",
  cpu: "1", memory: "2Gi", node_pool: "default-pool", storage_bucket: "",
  bigquery_dataset: "", service_account: "",
};

function estimateTokenUsage(request: InfrastructureRequest) {
  const payload = [
    request.application_name,
    request.environment,
    request.region,
    request.namespace,
    request.cpu,
    request.memory,
    request.node_pool,
    request.storage_bucket ?? "",
    request.bigquery_dataset ?? "",
    request.service_account ?? "",
  ].join(" ");

  const charCount = payload.trim().length;
  return Math.max(80, Math.round(charCount / 4));
}

function formatTokenCount(value: number) {
  if (value >= 1000) {
    return `${(value / 1000).toFixed(1)}k`;
  }
  return `${value}`;
}

export default function Home() {
  const [requests, setRequests] = useState<InfrastructureRequest[]>([]);
  const [form, setForm] = useState<RequestForm>(initialForm);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const summary = useMemo(() => ({
    total: requests.length,
    pending: requests.filter((item) => item.status === "PENDING").length,
    progress: requests.filter((item) => item.status === "IN_PROGRESS").length,
    completed: requests.filter((item) => item.status === "COMPLETED").length,
    tokens: requests.reduce((total, item) => total + estimateTokenUsage(item), 0),
  }), [requests]);

  async function loadRequests() {
    try {
      const response = await fetch(`${API_URL}/requests`);
      if (!response.ok) throw new Error("Unable to load infrastructure requests.");
      setRequests(await response.json());
      setError("");
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Unable to load requests.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    const requestTimer = window.setTimeout(() => { void loadRequests(); }, 0);
    return () => window.clearTimeout(requestTimer);
  }, []);

  function updateForm(field: keyof RequestForm, value: string) {
    setForm((current) => ({ ...current, [field]: value }));
  }

  async function createRequest(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setSubmitting(true); setMessage(""); setError("");
    try {
      const response = await fetch(`${API_URL}/requests`, {
        method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form),
      });
      if (!response.ok) throw new Error("Unable to create the infrastructure request.");
      setForm(initialForm); setMessage("Infrastructure request created successfully.");
      await loadRequests();
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Unable to create request.");
    } finally { setSubmitting(false); }
  }

  async function updateStatus(requestId: string, status: RequestStatus) {
    const response = await fetch(`${API_URL}/requests/${requestId}/status`, {
      method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ status }),
    });
    if (!response.ok) { setError("Unable to update request status."); return; }
    await loadRequests();
  }

  async function deleteRequest(requestId: string) {
    if (!window.confirm("Delete this infrastructure request?")) return;
    const response = await fetch(`${API_URL}/requests/${requestId}`, { method: "DELETE" });
    if (!response.ok) { setError("Unable to delete request."); return; }
    setMessage("Infrastructure request deleted.");
    await loadRequests();
  }

  return (
    <div className="portal-shell">
      <aside className="sidebar">
        <div className="brand"><span>CP</span> Lakshman Cloud Platform</div>
        <nav><a className="active" href="#dashboard">Dashboard</a><a href="#new-request">New request</a><a href="#request-history">Request history</a></nav>
        <p className="sidebar-note">Sprint 2<br />Self-service portal</p>
      </aside>
      <main className="content" id="dashboard">
        <header>
          <div><p className="eyebrow">INTERNAL DEVELOPER PLATFORM</p><h1>Infrastructure requests</h1><p className="subtle">Create and track application infrastructure from one place.</p></div>
          <button className="secondary" onClick={() => { setLoading(true); void loadRequests(); }}>Refresh</button>
        </header>
        <section className="summary-grid">
          <article><p>Total requests</p><strong>{summary.total}</strong></article>
          <article><p>Pending</p><strong>{summary.pending}</strong></article>
          <article><p>In progress</p><strong>{summary.progress}</strong></article>
          <article><p>Completed</p><strong>{summary.completed}</strong></article>
          <article><p>Estimated tokens</p><strong>{formatTokenCount(summary.tokens)}</strong></article>
        </section>
        {message && <p className="notice success">{message}</p>}
        {error && <p className="notice error">{error}</p>}
        <section className="card" id="new-request">
          <h2>Create infrastructure request</h2><p className="subtle">Define the application resources you need.</p>
          <form onSubmit={createRequest} className="request-form">
            <label>Application name<input required value={form.application_name} onChange={(event) => updateForm("application_name", event.target.value)} placeholder="payments" /></label>
            <label>Environment<select value={form.environment} onChange={(event) => updateForm("environment", event.target.value)}><option>dev</option><option>test</option><option>staging</option><option>prod</option></select></label>
            <label>Region<input required value={form.region} onChange={(event) => updateForm("region", event.target.value)} /></label>
            <label>Namespace<input required value={form.namespace} onChange={(event) => updateForm("namespace", event.target.value)} placeholder="payments-dev" /></label>
            <label>CPU<input required value={form.cpu} onChange={(event) => updateForm("cpu", event.target.value)} /></label>
            <label>Memory<input required value={form.memory} onChange={(event) => updateForm("memory", event.target.value)} /></label>
            <label>Node pool<input required value={form.node_pool} onChange={(event) => updateForm("node_pool", event.target.value)} /></label>
            <label>Storage bucket <em>(optional)</em><input value={form.storage_bucket ?? ""} onChange={(event) => updateForm("storage_bucket", event.target.value)} /></label>
            <label>BigQuery dataset <em>(optional)</em><input value={form.bigquery_dataset ?? ""} onChange={(event) => updateForm("bigquery_dataset", event.target.value)} /></label>
            <label>Service account <em>(optional)</em><input value={form.service_account ?? ""} onChange={(event) => updateForm("service_account", event.target.value)} /></label>
            <button className="primary" disabled={submitting}>{submitting ? "Creating..." : "Create request"}</button>
          </form>
        </section>
        <section className="card" id="request-history">
          <h2>Request history</h2><p className="subtle">Current requests stored in the platform.</p>
          {loading ? <p className="subtle">Loading requests...</p> : requests.length === 0 ? <p className="subtle">No requests yet. Create your first request above.</p> : (
            <div className="table-wrap"><table><thead><tr><th>Application</th><th>Environment</th><th>Resources</th><th>Tokens</th><th>Status</th><th>Actions</th></tr></thead><tbody>
              {requests.map((request) => <tr key={request.request_id}>
                <td><strong>{request.application_name}</strong><small>{request.namespace}</small></td>
                <td>{request.environment}<small>{request.region}</small></td>
                <td>{request.cpu} CPU · {request.memory}<small>{request.node_pool}</small></td>
                <td><strong>{formatTokenCount(estimateTokenUsage(request))}</strong><small>estimated</small></td>
                <td><span className={`status ${request.status.toLowerCase()}`}>{request.status.replace("_", " ")}</span></td>
                <td><select aria-label={`Status for ${request.application_name}`} value={request.status} onChange={(event) => void updateStatus(request.request_id, event.target.value as RequestStatus)}>{statuses.map((status) => <option key={status}>{status}</option>)}</select><button className="delete" onClick={() => void deleteRequest(request.request_id)}>Delete</button></td>
              </tr>)}
            </tbody></table></div>
          )}
        </section>
      </main>
    </div>
  );
}
