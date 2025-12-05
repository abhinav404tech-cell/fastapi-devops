import React, { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000";

export default function App() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [created, setCreated] = useState(null);
  const [id, setId] = useState("");
  const [fetched, setFetched] = useState(null);
  const [err, setErr] = useState(null);

  async function createUser(e) {
    e.preventDefault();
    setErr(null);
    setCreated(null);
    try {
      const res = await fetch(`${API_BASE}/users`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || JSON.stringify(data));
      setCreated(data);
      setUsername("");
      setEmail("");
    } catch (e) {
      setErr(String(e));
    }
  }

  async function getUser(e) {
    e.preventDefault();
    setErr(null);
    setFetched(null);
    try {
      const res = await fetch(`${API_BASE}/users/${encodeURIComponent(id)}`);
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || JSON.stringify(data));
      setFetched(data);
    } catch (e) {
      setErr(String(e));
    }
  }

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", maxWidth: 720, margin: "2rem auto" }}>
      <h1>FastAPI Minimal Frontend</h1>
      <p>API base: <code>{API_BASE}</code></p>

      <section style={{ marginBottom: 24 }}>
        <h3>Create user</h3>
        <form onSubmit={createUser}>
          <input placeholder="username" value={username} onChange={e => setUsername(e.target.value)} required />
          {" "}
          <input placeholder="email" value={email} onChange={e => setEmail(e.target.value)} required />
          {" "}
          <button type="submit">Create</button>
        </form>
        {created && <pre style={{ background: "#f6f8fa", padding: 8 }}>{JSON.stringify(created, null, 2)}</pre>}
      </section>

      <section style={{ marginBottom: 24 }}>
        <h3>Get user</h3>
        <form onSubmit={getUser}>
          <input placeholder="id (e.g. 1)" value={id} onChange={e => setId(e.target.value)} required />
          {" "}
          <button type="submit">Get</button>
        </form>
        {fetched && <pre style={{ background: "#f6f8fa", padding: 8 }}>{JSON.stringify(fetched, null, 2)}</pre>}
      </section>

      {err && <div style={{ color: "crimson" }}>Error: {err}</div>}
    </div>
  );
}
