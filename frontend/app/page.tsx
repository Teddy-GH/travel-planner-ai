"use client";

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  async function send() {
    const body = {
      session_id: "user-001",
      message,
    }
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ body }),
    });

    const data = await response.json();

    setReply(data.reply);
  }

  return (
    <main className="max-w-3xl mx-auto p-10 space-y-6">
      <h1 className="text-4xl font-bold">
        Travel Planner AI
      </h1>

      <textarea
        className="w-full border rounded-lg p-4"
        rows={5}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={send}
        className="bg-blue-600 text-white px-6 py-3 rounded-lg"
      >
        Ask AI
      </button>

      <div className="border rounded-lg p-5 whitespace-pre-wrap">
        {reply}
      </div>
    </main>
  );
}